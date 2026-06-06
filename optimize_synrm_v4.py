r"""
optimize_synrm_v4.py — SynRM 45kW IE5 Rotor Barrier Optimization
=================================================================
Model: SynRM_45kW_IE5.mot (D:\SRM\Motor _CAD\ScriptFiles\SynRM_45kW_IE5.mot)

Strategy:
  Phase 1: Adaptive Latin Hypercube Sampling (ALS) — 40 candidates
           Uses proper SynRM barrier ratio constraints
    Phase 2: Adaptive coordinate-descent refinement from top-3 seeds
  Phase 3: PhaseAdvance co-optimization with best geometry
  Phase 4: Final verification + save

Key differences from v3:
  - Uses the new model with working winding (580V DC, 121A RMS)
  - Includes PhaseAdvance as optimization variable
  - Multi-objective: torque error + efficiency gap + power factor penalty
  - Proper SynRM barrier spacing ratios (not just min/max)
  - Adaptive sampling: second batch focused on promising region
  - Reads PowerFactor from Lab context if available

Target specs (from CLAUDE.md):
  Torque: 143 Nm @ 3000 RPM (±2%)
  Efficiency: >= 96% (IE5)
  Power Factor: >= 0.85
  PhaseAdvance: 45° (spec fixed, but we test 30-65°)
"""

import os, pathlib, math, time, copy, csv, random, sys, signal, ctypes, multiprocessing as mp
import ansys.motorcad.core as pymotorcad

# ── Paths ──────────────────────────────────────────────────────────────────────
MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL_FILE   = r"D:\\SRM\\Motor _CAD\\ScriptFiles\\backup_v4.mot"
RESULTS_CSV  = r"D:\SRM\Motor _CAD\ScriptFiles\optimization_results_v4.csv"
BEST_MODEL   = r"D:\SRM\Motor _CAD\ScriptFiles\best_so_far_v4.mot"
BACKUP_MODEL = r"D:\SRM\Motor _CAD\ScriptFiles\backup_v4.mot"

# ── Target specs ───────────────────────────────────────────────────────────────
TARGET_TORQUE    = 143.0    # Nm
TARGET_EFF       = 96.0     # % IE5
TARGET_PF        = 0.85     # power factor
SPEED            = 3000     # RPM
NOMINAL_PA       = 45       # degrees (spec nominal)
SOLVE_TIMEOUT_S  = 10      # per-evaluation timeout for a hung Motor-CAD solve

# ── Motor constants ────────────────────────────────────────────────────────────
SHAFT_DIA  = 80.0   # mm
ROTOR_OD   = 214.0  # mm (stator_bore - 2*airgap = 215 - 2*0.5)
N_POLES    = 4
N_BARRIERS = 3

COUPLING_SETTINGS = {
    "MagneticThermalCoupling": 2,
    "LabThermalCoupling": 0,
    "LabThermalCoupling_DutyCycle": 0,
    "LabMagneticCoupling": 0,
}

ACTIVE_MC = None
STOP_REQUESTED = False
_CTRL_HANDLER = None


def install_interrupt_handler():
    """Force Ctrl+C to stop the script even during blocked Motor-CAD calls."""
    if os.name != "nt":
        return

    ctrl_types = {0, 1, 2, 5, 6}

    global _CTRL_HANDLER

    @ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_uint)
    def handler(ctrl_type):
        if ctrl_type in ctrl_types:
            global STOP_REQUESTED
            STOP_REQUESTED = True
            sys.stderr.write("\nCtrl+C received; stopping Motor-CAD run.\n")
            sys.stderr.flush()
            os._exit(130)
        return 0

    _CTRL_HANDLER = handler
    ctypes.windll.kernel32.SetConsoleCtrlHandler(handler, True)

# ── Search ranges (12 barrier params + PhaseAdvance) ──────────────────────────
# Based on SynRM design theory + current baseline analysis
# Current: L1=99.9, L2=138.7, L3=168.0, bridges=0.8, webs=18/41/64
# Theory says: L3 should be ~0.85-0.90 * ROTOR_OD = 182-193mm
SEARCH_RANGES = {
    # Barrier diameters — key saliency drivers
    "L1_Diameter":          (94.0,  108.0),   # ~1.17-1.35 * shaft
    "L2_Diameter":          (130.0, 155.0),   # spacing ratio with L1,L3
    "L3_Diameter":          (175.0, 195.0),   # 0.82-0.91 * rotor OD (theory: 0.85-0.90)

    # Bridge thickness — thin = high saliency, but >= 0.5mm mechanical
    "L1_Bridge_Thickness":  (0.5,   2.0),     # already 0.8, keep thin
    "L2_Bridge_Thickness":  (0.5,   2.0),
    "L3_Bridge_Thickness":  (0.5,   2.0),

    # Web thickness — balance between mechanical strength and magnetic performance
    "L1_Web_Thickness":    (8.0,   28.0),    # current: 18.2
    "L2_Web_Thickness":    (25.0,  55.0),    # current: 41.2
    "L3_Web_Thickness":    (45.0,  80.0),    # current: 63.9

    # Angle offset — controls rib tip position relative to d/q axes
    "L1_Outer_Angle_Offset": (-20.0, -5.0),  # current: -7.9, -15, -15

    # Barrier end thickness
    "L1_Outer_Thickness":  (1.0,   4.0),     # current: 2.18
    "L1_Inner_Thickness":  (1.0,   4.0),     # current: 1.70
}

# PhaseAdvance search range
PA_RANGE = (30, 65)  # degrees

# ── Current baseline (from new model) ─────────────────────────────────────────
CURRENT_BASELINE = {
    "L1_Diameter":           99.91,
    "L2_Diameter":          138.70,
    "L3_Diameter":          168.00,
    "L1_Bridge_Thickness":   0.80,
    "L2_Bridge_Thickness":   0.80,
    "L3_Bridge_Thickness":   0.80,
    "L1_Web_Thickness":     18.23,
    "L2_Web_Thickness":     41.19,
    "L3_Web_Thickness":     63.94,
    "L1_Outer_Angle_Offset": -7.90,
    "L1_Outer_Thickness":    2.18,
    "L1_Inner_Thickness":    1.70,
}

# ── Motor-CAD connection ──────────────────────────────────────────────────────
def connect():
    global ACTIVE_MC
    os.environ.setdefault("MOTORCAD_INSTALL_DIR",
                          str(pathlib.Path(MOTORCAD_EXE).parent))
    mc = pymotorcad.MotorCAD(
        open_new_instance=True,
        use_blackbox_licence=True,
        keep_instance_open=False,
    )
    mc.set_variable("MessageDisplayState", 2)
    mc.load_from_file(MODEL_FILE)
    apply_coupling_settings(mc)
    # Set operating point for EMag solver
    mc.set_variable("Constant_Torque_or_Constant_Current", 0)  # 0=Constant_Torque
    mc.set_variable("Ansys_DriveType", 0)                      # 0=Current driven
    mc.set_variable("DCBusVoltage", 580.0)                     # DC bus voltage in volts
    mc.set_variable("PeakCurrent", 171.4)                      # Peak current (A)
    mc.set_variable("RMSCurrent", 121.0)                       # RMS current (A)
    ACTIVE_MC = mc
    return mc


def apply_coupling_settings(mc):
    """Apply the requested Motor-LAB and magnetic/thermal coupling settings."""
    for name, value in COUPLING_SETTINGS.items():
        mc.set_variable(name, value)

# ── Geometry constraint checker ───────────────────────────────────────────────
def check_constraints(p):
    """
    Validate barrier geometry constraints.
    Returns True if valid, raises AssertionError otherwise.
    """
    # Ordering: shaft < L1 < L2 < L3 < rotor OD
    assert p["L1_Diameter"] > SHAFT_DIA, \
        f"L1_Dia ({p['L1_Diameter']}) must be > shaft ({SHAFT_DIA})"
    assert p["L1_Diameter"] < p["L2_Diameter"], \
        f"L1_Dia ({p['L1_Diameter']}) must be < L2_Dia ({p['L2_Diameter']})"
    assert p["L2_Diameter"] < p["L3_Diameter"], \
        f"L2_Dia ({p['L2_Diameter']}) must be < L3_Dia ({p['L3_Diameter']})"
    assert p["L3_Diameter"] < ROTOR_OD, \
        f"L3_Dia ({p['L3_Diameter']}) must be < rotor OD ({ROTOR_OD})"

    # Bridge mechanical minimum
    for layer in ["L1", "L2", "L3"]:
        assert p[f"{layer}_Bridge_Thickness"] >= 0.5, \
            f"{layer}_Bridge ({p[f'{layer}_Bridge_Thickness']}) must be >= 0.5mm"

    # L3 + outer thickness must not exceed rotor OD
    assert p["L3_Diameter"] + p["L1_Outer_Thickness"] < ROTOR_OD, \
        f"L3_Dia + outer_thick ({p['L3_Diameter'] + p['L1_Outer_Thickness']}) >= rotor OD"

    # Spacing ratio: barriers should be reasonably spaced
    # (L2-L1) and (L3-L2) should not differ by more than 2x
    span_inner = p["L2_Diameter"] - p["L1_Diameter"]
    span_outer = p["L3_Diameter"] - p["L2_Diameter"]
    if span_inner > 0 and span_outer > 0:
        ratio = max(span_inner, span_outer) / min(span_inner, span_outer)
        assert ratio <= 2.5, \
            f"Barrier spacing ratio ({ratio:.1f}) too unbalanced (max 2.5)"

    # Web thickness must be positive and reasonable
    for layer in ["L1", "L2", "L3"]:
        key = f"{layer}_Web_Thickness"
        assert p[key] > 0, f"{key} must be positive"

    return True

# ── Apply barrier geometry to Motor-CAD ──────────────────────────────────────
def set_barriers(mc, p):
    """Apply barrier parameters to Motor-CAD model."""
    # Layer-specific arrays (indexed 0,1,2 for L1,L2,L3)
    mc.set_array_variable("UShape_InnerDiameter_Array", 0, p["L1_Diameter"])
    mc.set_array_variable("UShape_InnerDiameter_Array", 1, p["L2_Diameter"])
    mc.set_array_variable("UShape_InnerDiameter_Array", 2, p["L3_Diameter"])

    mc.set_array_variable("UShape_WebThickness_Array", 0, p["L1_Web_Thickness"])
    mc.set_array_variable("UShape_WebThickness_Array", 1, p["L2_Web_Thickness"])
    mc.set_array_variable("UShape_WebThickness_Array", 2, p["L3_Web_Thickness"])

    mc.set_array_variable("UShape_BridgeThickness_Array", 0, p["L1_Bridge_Thickness"])
    mc.set_array_variable("UShape_BridgeThickness_Array", 1, p["L2_Bridge_Thickness"])
    mc.set_array_variable("UShape_BridgeThickness_Array", 2, p["L3_Bridge_Thickness"])

    # Shared arrays (same value for all 3 layers)
    for idx in range(3):
        mc.set_array_variable("UShape_OuterAngleOffset_Array", idx, p["L1_Outer_Angle_Offset"])
        mc.set_array_variable("UShape_Thickness_Outer_Array", idx, p["L1_Outer_Thickness"])
        mc.set_array_variable("UShape_Thickness_Inner_Array", idx, p["L1_Inner_Thickness"])


def reload_backup(mc):
    """Reload the last saved backup model to clear accumulated solver state."""
    try:
        mc.load_from_file(BACKUP_MODEL)
    except Exception:
        pass

# ── Run EMag calculation ──────────────────────────────────────────────────────
def run_emag(mc, phase_advance=NOMINAL_PA, reload_interval=0, iteration=0):
    """
    Run EMag calculation at given phase advance.
    Returns dict with all results.
    """
    mc.show_magnetic_context()
    apply_coupling_settings(mc)
    mc.set_variable("Shaft_Speed_[RPM]", SPEED)
    mc.set_variable("PhaseAdvance", phase_advance)
    mc.set_variable("TorquePointsPerCycle", 30)
    mc.set_variable("TorqueNumberCycles", 1)
    mc.set_variable("TorqueCalculation", True)

    mc.do_magnetic_thermal_calculation()

    # Read all results BEFORE changing anything
    results = {}
    result_vars = [
        "ShaftTorque", "InputPower", "OutputPower", "MotorEfficiency",
        "PeakLineLineVoltage", "LineLineVoltage", "PhaseVoltage",
        "RMSPhaseCurrent", "StatorIronLoss_Total", "ConductorLoss",
    ]
    for var in result_vars:
        try:
            results[var] = float(mc.get_variable(var))
        except:
            results[var] = None

    # Try power factor — use the specific waveform/phasor variables
    results["WaveformPowerFactor"] = None
    results["WaveformPowerFactorAngle"] = None
    results["WaveformPowerFactor_THD"] = None
    results["PhasorPowerFactor"] = None
    results["PhasorPowerFactorAngle"] = None
    results["PowerFactor"] = None  # fallback
    pf_names = ["WaveformPowerFactor", "PhasorPowerFactor", "PowerFactor"]
    for pf_name in pf_names:
        try:
            results["PowerFactor"] = float(mc.get_variable(pf_name))
            break
        except:
            pass
    # Also read the angle and THD versions
    for var in ["WaveformPowerFactorAngle", "WaveformPowerFactor_THD", "PhasorPowerFactorAngle"]:
        try:
            results[var] = float(mc.get_variable(var))
        except:
            results[var] = None

    results["PhaseAdvance"] = phase_advance
    return results


def _evaluate_candidate_worker(result_queue, params, phase_advance):
    mc = None
    try:
        mc = connect()
        set_barriers(mc, params)
        results = run_emag(mc, phase_advance=phase_advance)
        result_queue.put((True, results, None))
    except Exception as exc:
        result_queue.put((False, None, f"{type(exc).__name__}: {exc}"))
    finally:
        if mc is not None:
            try:
                mc.quit()
            except Exception:
                pass


def run_candidate_with_timeout(params, phase_advance=NOMINAL_PA, timeout_s=SOLVE_TIMEOUT_S):
    """Evaluate one candidate in a child process so a hung solve can be killed."""
    ctx = mp.get_context("spawn")
    result_queue = ctx.Queue()
    process = ctx.Process(target=_evaluate_candidate_worker, args=(result_queue, params, phase_advance))
    process.start()
    process.join(timeout_s)

    if process.is_alive():
        process.terminate()
        process.join(5)
        if process.is_alive() and hasattr(process, "kill"):
            process.kill()
            process.join(5)
        raise TimeoutError(f"Motor-CAD solve timed out after {timeout_s}s")

    if result_queue.empty():
        raise RuntimeError("Motor-CAD worker exited without returning results")

    ok, results, error = result_queue.get()
    if not ok:
        raise RuntimeError(error)

    return results


def save_model_with_params(params, path):
    """Save a model snapshot for the supplied parameters."""
    mc = None
    try:
        mc = connect()
        set_barriers(mc, params)
        mc.save_to_file(path)
    finally:
        if mc is not None:
            try:
                mc.quit()
            except Exception:
                pass

# ── Objective function ────────────────────────────────────────────────────────
def objective(results, weight_torque=1.0, weight_eff=1.0, weight_pf=0.5):
    """
    Multi-objective score. Lower is better.
    
    Components:
    - torque_error%: how far from 143 Nm target
    - eff_gap%: how far below 96% IE5 target
    - pf_penalty: how far below 0.85 target (uses PhasorPowerFactor if available)
    """
    t   = results.get("ShaftTorque", 0) or 0
    eff = results.get("MotorEfficiency", 0) or 0
    # Use PhasorPowerFactor if available, else WaveformPowerFactor, else PowerFactor
    pf  = results.get("PhasorPowerFactor", results.get("WaveformPowerFactor", results.get("PowerFactor", 0))) or 0

    # Torque error (%)
    torque_err = abs(t - TARGET_TORQUE) / TARGET_TORQUE * 100

    # Efficiency gap (% points below target)
    eff_gap = max(0.0, TARGET_EFF - eff)

    # Power factor penalty
    pf_penalty = max(0.0, (TARGET_PF - pf) * 100) if pf > 0 else 0

    score = (weight_torque * torque_err +
             weight_eff * eff_gap +
             weight_pf * pf_penalty)

    return score, torque_err, eff_gap, pf_penalty

# ── Latin Hypercube Sampling ──────────────────────────────────────────────────
def latin_hypercube(n_samples, ranges, seed=None):
    """Generate n_samples from Latin Hypercube over given ranges."""
    if seed is not None:
        random.seed(seed)

    keys = list(ranges.keys())
    lo = [ranges[k][0] for k in keys]
    hi = [ranges[k][1] for k in keys]
    n_dims = len(keys)

    # Generate LHS matrix
    lhs = []
    for d in range(n_dims):
        samples = [lo[d] + (hi[d] - lo[d]) * (i + random.random()) / n_samples
                   for i in range(n_samples)]
        random.shuffle(samples)
        lhs.append(samples)

    # Build parameter sets
    param_sets = []
    for i in range(n_samples):
        p = {keys[d]: round(lhs[d][i], 4) for d in range(n_dims)}
        try:
            check_constraints(p)
            param_sets.append(p)
        except AssertionError:
            pass

    return param_sets

def adaptive_latin_hypercube(n_samples, best_region, scale=0.3):
    """
    Generate samples focused around a promising region.
    best_region: dict of center values
    scale: fraction of full range to use (0.3 = ±15% of range around center)
    """
    focused_ranges = {}
    for key, (lo, hi) in SEARCH_RANGES.items():
        if key in best_region:
            center = best_region[key]
            half_width = (hi - lo) * scale
            new_lo = max(lo, center - half_width)
            new_hi = min(hi, center + half_width)
            focused_ranges[key] = (new_lo, new_hi)
        else:
            focused_ranges[key] = (lo, hi)

    return latin_hypercube(n_samples, focused_ranges)

# ── Logging ────────────────────────────────────────────────────────────────────
CSV_FIELDS = [
    "iteration", "phase", "timestamp", "elapsed_s", "score",
    "torque_err%", "eff_gap%", "pf_penalty",
    "L1_Diameter", "L2_Diameter", "L3_Diameter",
    "L1_Bridge_Thickness", "L2_Bridge_Thickness", "L3_Bridge_Thickness",
    "L1_Web_Thickness", "L2_Web_Thickness", "L3_Web_Thickness",
    "L1_Outer_Angle_Offset", "L1_Outer_Thickness", "L1_Inner_Thickness",
    "PhaseAdvance",
    "ShaftTorque", "MotorEfficiency", "PowerFactor",
    "WaveformPowerFactor", "WaveformPowerFactorAngle", "WaveformPowerFactor_THD",
    "PhasorPowerFactor", "PhasorPowerFactorAngle",
    "InputPower", "OutputPower", "ConductorLoss", "StatorIronLoss_Total",
    "PeakLineLineVoltage", "LineLineVoltage", "RMSPhaseCurrent",
]

def init_csv(path):
    """Initialize CSV with headers."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()

def log_result(path, iteration, phase, params, results, elapsed, score_info):
    """Append a result row to CSV."""
    score, torque_err, eff_gap, pf_penalty = score_info
    row = {
        "iteration": iteration,
        "phase": phase,
        "timestamp": time.time(),
        "elapsed_s": round(elapsed, 1),
        "score": round(score, 4),
        "torque_err%": round(torque_err, 4),
        "eff_gap%": round(eff_gap, 4),
        "pf_penalty": round(pf_penalty, 4),
        "L1_Diameter": params.get("L1_Diameter", ""),
        "L2_Diameter": params.get("L2_Diameter", ""),
        "L3_Diameter": params.get("L3_Diameter", ""),
        "L1_Bridge_Thickness": params.get("L1_Bridge_Thickness", ""),
        "L2_Bridge_Thickness": params.get("L2_Bridge_Thickness", ""),
        "L3_Bridge_Thickness": params.get("L3_Bridge_Thickness", ""),
        "L1_Web_Thickness": params.get("L1_Web_Thickness", ""),
        "L2_Web_Thickness": params.get("L2_Web_Thickness", ""),
        "L3_Web_Thickness": params.get("L3_Web_Thickness", ""),
        "L1_Outer_Angle_Offset": params.get("L1_Outer_Angle_Offset", ""),
        "L1_Outer_Thickness": params.get("L1_Outer_Thickness", ""),
        "L1_Inner_Thickness": params.get("L1_Inner_Thickness", ""),
        "PhaseAdvance": results.get("PhaseAdvance", NOMINAL_PA),
        "ShaftTorque": results.get("ShaftTorque", ""),
        "MotorEfficiency": results.get("MotorEfficiency", ""),
        "PowerFactor": results.get("PowerFactor", ""),
        "WaveformPowerFactor": results.get("WaveformPowerFactor", ""),
        "WaveformPowerFactorAngle": results.get("WaveformPowerFactorAngle", ""),
        "WaveformPowerFactor_THD": results.get("WaveformPowerFactor_THD", ""),
        "PhasorPowerFactor": results.get("PhasorPowerFactor", ""),
        "PhasorPowerFactorAngle": results.get("PhasorPowerFactorAngle", ""),
        "InputPower": results.get("InputPower", ""),
        "OutputPower": results.get("OutputPower", ""),
        "ConductorLoss": results.get("ConductorLoss", ""),
        "StatorIronLoss_Total": results.get("StatorIronLoss_Total", ""),
        "PeakLineLineVoltage": results.get("PeakLineLineVoltage", ""),
        "LineLineVoltage": results.get("LineLineVoltage", ""),
        "RMSPhaseCurrent": results.get("RMSPhaseCurrent", ""),
    }

    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writerow(row)

# ── Print helpers ─────────────────────────────────────────────────────────────
def print_result(idx, total, params, results, score_info, elapsed):
    score, torque_err, eff_gap, pf_penalty = score_info
    t = results.get("ShaftTorque", 0)
    eff = results.get("MotorEfficiency", 0)
    pf = results.get("PowerFactor", 0) or 0
    pf_wf = results.get("WaveformPowerFactor")
    pf_ph = results.get("PhasorPowerFactor")
    pa = results.get("PhaseAdvance", NOMINAL_PA)

    pf_wf_text = f"{pf_wf:.3f}" if pf_wf is not None else "n/a"
    pf_ph_text = f"{pf_ph:.3f}" if pf_ph is not None else "n/a"
    print(f"  [{idx:>3}/{total}] PA={pa:>2}° T={t:>6.1f}Nm  E={eff:>5.2f}%  "
          f"PF={pf:.3f} (WF={pf_wf_text} PH={pf_ph_text})  err={torque_err:>5.2f}%  gap={eff_gap:>4.2f}  "
          f"score={score:>6.2f}  ({elapsed:.0f}s)")

def print_params(params, label=""):
    print(f"  {label}")
    print(f"    Diameters:  L1={params['L1_Diameter']:.1f}  "
          f"L2={params['L2_Diameter']:.1f}  L3={params['L3_Diameter']:.1f}")
    print(f"    Bridges:    L1={params['L1_Bridge_Thickness']:.1f}  "
          f"L2={params['L2_Bridge_Thickness']:.1f}  L3={params['L3_Bridge_Thickness']:.1f}")
    print(f"    Webs:       L1={params['L1_Web_Thickness']:.1f}  "
          f"L2={params['L2_Web_Thickness']:.1f}  L3={params['L3_Web_Thickness']:.1f}")
    print(f"    AngleOff={params['L1_Outer_Angle_Offset']:.1f}°  "
          f"Outer={params['L1_Outer_Thickness']:.1f}  Inner={params['L1_Inner_Thickness']:.1f}")

# ── Phase 1: Coarse sweep ────────────────────────────────────────────────────
def phase1_coarse(mc, n_samples=40, csv_path=RESULTS_CSV):
    """
    Two-batch adaptive Latin Hypercube:
    - Batch 1: 30 samples across full range
    - Batch 2: 20 samples focused on best region from Batch 1
    """
    print(f"\n{'='*70}")
    print(f"  PHASE 1 — Adaptive Latin Hypercube Sweep")
    print(f"  Batch 1: {n_samples} samples across full range")
    print(f"  Batch 2: 20 samples focused on best region")
    print(f"{'='*70}")

    all_results = []
    t_start = time.time()
    iteration = 0

    # Batch 1: Full range
    print(f"\n  --- Batch 1: Full range ({n_samples} samples) ---")
    param_sets = latin_hypercube(n_samples, SEARCH_RANGES, seed=42)
    print(f"  Generated {len(param_sets)} valid parameter sets")

    for i, params in enumerate(param_sets, start=1):
        iteration += 1
        try:
            results = run_candidate_with_timeout(params, phase_advance=NOMINAL_PA, timeout_s=SOLVE_TIMEOUT_S)
            score_info = objective(results)
            elapsed = time.time() - t_start
            log_result(csv_path, iteration, "P1-B1", params, results, elapsed, score_info)
            all_results.append((score_info[0], params, results))
            print_result(i, len(param_sets), params, results, score_info, elapsed)
        except Exception as e:
            print(f"  [{i:>3}/{len(param_sets)}] FAILED: {e}")

    if not all_results:
        print("\n  WARNING: Batch 1 produced no valid candidates; using baseline fallback")
        fallback_params = copy.deepcopy(CURRENT_BASELINE)
        try:
            results = run_candidate_with_timeout(fallback_params, phase_advance=NOMINAL_PA, timeout_s=SOLVE_TIMEOUT_S)
            score_info = objective(results)
            elapsed = time.time() - t_start
            log_result(csv_path, iteration + 1, "P1-FALLBACK", fallback_params, results, elapsed, score_info)
            all_results.append((score_info[0], fallback_params, results))
            print_result(1, 1, fallback_params, results, score_info, elapsed)
        except Exception as e:
            raise RuntimeError(f"Phase 1 fallback evaluation failed: {e}")

    # Sort and find best region
    all_results.sort(key=lambda x: x[0])
    best = all_results[0]
    print(f"\n  Batch 1 best: score={best[0]:.2f}")
    print_params(best[1], "Best params:")

    # Batch 2: Focused on best region
    print(f"\n  --- Batch 2: Focused sampling (20 samples) ---")
    focused_sets = adaptive_latin_hypercube(20, best[1], scale=0.25)
    print(f"  Generated {len(focused_sets)} valid parameter sets")

    for i, params in enumerate(focused_sets, start=1):
        iteration += 1
        try:
            results = run_candidate_with_timeout(params, phase_advance=NOMINAL_PA, timeout_s=SOLVE_TIMEOUT_S)
            score_info = objective(results)
            elapsed = time.time() - t_start
            log_result(csv_path, iteration, "P1-B2", params, results, elapsed, score_info)
            all_results.append((score_info[0], params, results))
            print_result(i, len(focused_sets), params, results, score_info, elapsed)
        except Exception as e:
            print(f"  [{i:>3}/{len(focused_sets)}] FAILED: {e}")

    # Final ranking
    all_results.sort(key=lambda x: x[0])
    top3 = all_results[:3]

    print(f"\n  Phase 1 complete in {time.time()-t_start:.0f}s")
    print(f"  Top 3 candidates:")
    for rank, (score, params, res) in enumerate(top3, 1):
        pf = res.get("PowerFactor", 0) or 0
        print(f"    #{rank}: T={res['ShaftTorque']:.1f}Nm  E={res['MotorEfficiency']:.2f}%  "
              f"PF={pf:.3f}  score={score:.2f}")
        print(f"          L1={params['L1_Diameter']:.1f}  L2={params['L2_Diameter']:.1f}  "
              f"L3={params['L3_Diameter']:.1f}")

    # Save best
    save_model_with_params(top3[0][1], BEST_MODEL)
    print(f"\n  Saved best to {BEST_MODEL}")

    return top3

# ── Phase 2: Nelder-Mead simplex refinement ─────────────────────────────────
def phase2_refine(mc, seeds, csv_path=RESULTS_CSV, max_iters=15):
    """
    Multi-start Nelder-Mead refinement from the top-3 seeds.

    Each seed initializes its own simplex around the seed point, then the
    simplex is iteratively updated using reflection, expansion, contraction,
    and shrink steps.
    """
    print(f"\n{'='*70}")
    print(f"  PHASE 2 — Nelder-Mead Simplex ({len(seeds)} seeds, max {max_iters} iters each)")
    print(f"{'='*70}")

    t_start = time.time()
    iter_counter = 1000
    best_overall_score = float("inf")
    best_overall_params = None
    best_overall_results = None

    nm_alpha = 1.0
    nm_gamma = 2.0
    nm_rho = 0.5
    nm_sigma = 0.5

    def clip_and_validate(params):
        clipped = {}
        for key, (lo, hi) in SEARCH_RANGES.items():
            clipped[key] = float(max(lo, min(hi, params[key])))
        check_constraints(clipped)
        return clipped

    def centroid(vertices, exclude_index):
        point_count = len(vertices)
        centroid_params = {}
        for key in SEARCH_RANGES:
            centroid_params[key] = sum(
                vertex[key] for idx, vertex in enumerate(vertices) if idx != exclude_index
            ) / (point_count - 1)
        return centroid_params

    def evaluate_candidate(params, phase_tag):
        nonlocal iter_counter

        try:
            valid_params = clip_and_validate(params)
        except AssertionError:
            return float("inf"), None, None, None

        try:
            results = run_candidate_with_timeout(valid_params, phase_advance=NOMINAL_PA, timeout_s=SOLVE_TIMEOUT_S)
            score_info = objective(results)
            iter_counter += 1
            elapsed = time.time() - t_start
            log_result(csv_path, iter_counter, phase_tag, valid_params, results, elapsed, score_info)
            return score_info[0], score_info, valid_params, results
        except Exception:
            return float("inf"), None, None, None

    def build_initial_simplex(seed_params):
        simplex = [copy.deepcopy(seed_params)]
        for key in SEARCH_RANGES:
            lo, hi = SEARCH_RANGES[key]
            step = max(0.1, (hi - lo) * 0.10)
            vertex = copy.deepcopy(seed_params)
            if vertex[key] + step <= hi:
                vertex[key] = vertex[key] + step
            elif vertex[key] - step >= lo:
                vertex[key] = vertex[key] - step
            else:
                vertex[key] = lo if abs(vertex[key] - lo) < abs(vertex[key] - hi) else hi
            simplex.append(vertex)
        return simplex

    for seed_idx, (seed_score, seed_params, seed_results) in enumerate(seeds):
        print(f"\n  --- Seed {seed_idx+1} (initial score={seed_score:.2f}) ---")
        simplex = build_initial_simplex(seed_params)
        simplex_data = []

        for vertex_idx, vertex in enumerate(simplex):
            score, score_info, valid_vertex, results = evaluate_candidate(vertex, f"P2-S{seed_idx}-V{vertex_idx}")
            if valid_vertex is None:
                continue
            simplex_data.append({"params": valid_vertex, "score": score, "score_info": score_info, "results": results})

        if len(simplex_data) < 2:
            print(f"    Seed {seed_idx+1}: insufficient valid simplex vertices, skipping")
            continue

        for it in range(max_iters):
            simplex_data.sort(key=lambda item: item["score"])
            best = simplex_data[0]
            worst = simplex_data[-1]
            second_worst = simplex_data[-2]

            spread = max(
                abs(simplex_data[i]["score"] - best["score"]) for i in range(1, len(simplex_data))
            )
            if spread < 1e-4:
                print(f"    Seed {seed_idx+1}: converged at iter {it} (score spread < 1e-4)")
                break

            centroid_params = centroid([item["params"] for item in simplex_data], len(simplex_data) - 1)

            reflected = {}
            for key in SEARCH_RANGES:
                reflected[key] = centroid_params[key] + nm_alpha * (centroid_params[key] - worst["params"][key])

            reflected_score, reflected_info, reflected_params, reflected_results = evaluate_candidate(
                reflected, f"P2-S{seed_idx}-R{it}"
            )

            if reflected_params is None:
                reflected_score = float("inf")

            if best["score"] <= reflected_score < second_worst["score"]:
                simplex_data[-1] = {
                    "params": reflected_params,
                    "score": reflected_score,
                    "score_info": reflected_info,
                    "results": reflected_results,
                }
                pf = reflected_results.get("PowerFactor", 0) or 0
                print(f"    [S{seed_idx}-I{it}] reflect → T={reflected_results['ShaftTorque']:.1f}Nm  "
                      f"E={reflected_results['MotorEfficiency']:.2f}%  PF={pf:.3f}  score={reflected_score:.2f}")
                continue

            if reflected_score < best["score"]:
                expanded = {}
                for key in SEARCH_RANGES:
                    expanded[key] = centroid_params[key] + nm_gamma * (reflected_params[key] - centroid_params[key])

                expanded_score, expanded_info, expanded_params, expanded_results = evaluate_candidate(
                    expanded, f"P2-S{seed_idx}-E{it}"
                )

                chosen = (expanded_score, expanded_info, expanded_params, expanded_results)
                if expanded_params is None or expanded_score >= reflected_score:
                    chosen = (reflected_score, reflected_info, reflected_params, reflected_results)

                simplex_data[-1] = {
                    "params": chosen[2],
                    "score": chosen[0],
                    "score_info": chosen[1],
                    "results": chosen[3],
                }
                pf = simplex_data[-1]["results"].get("PowerFactor", 0) or 0
                print(f"    [S{seed_idx}-I{it}] expand → T={simplex_data[-1]['results']['ShaftTorque']:.1f}Nm  "
                      f"E={simplex_data[-1]['results']['MotorEfficiency']:.2f}%  PF={pf:.3f}  score={simplex_data[-1]['score']:.2f}")
                continue

            contracted = {}
            if reflected_score < worst["score"]:
                # Outside contraction
                for key in SEARCH_RANGES:
                    contracted[key] = centroid_params[key] + nm_rho * (reflected_params[key] - centroid_params[key])
                contraction_tag = f"P2-S{seed_idx}-OC{it}"
            else:
                # Inside contraction
                for key in SEARCH_RANGES:
                    contracted[key] = centroid_params[key] - nm_rho * (centroid_params[key] - worst["params"][key])
                contraction_tag = f"P2-S{seed_idx}-IC{it}"

            contracted_score, contracted_info, contracted_params, contracted_results = evaluate_candidate(
                contracted, contraction_tag
            )

            if contracted_params is not None and contracted_score < worst["score"]:
                simplex_data[-1] = {
                    "params": contracted_params,
                    "score": contracted_score,
                    "score_info": contracted_info,
                    "results": contracted_results,
                }
                pf = contracted_results.get("PowerFactor", 0) or 0
                print(f"    [S{seed_idx}-I{it}] contract → T={contracted_results['ShaftTorque']:.1f}Nm  "
                      f"E={contracted_results['MotorEfficiency']:.2f}%  PF={pf:.3f}  score={contracted_score:.2f}")
                continue

            # Shrink the simplex toward the current best point.
            print(f"    [S{seed_idx}-I{it}] shrink simplex")
            best_params = simplex_data[0]["params"]
            new_simplex = [simplex_data[0]]
            for vertex_idx in range(1, len(simplex_data)):
                shrunk = {}
                for key in SEARCH_RANGES:
                    shrunk[key] = best_params[key] + nm_sigma * (simplex_data[vertex_idx]["params"][key] - best_params[key])

                shrunk_score, shrunk_info, shrunk_params, shrunk_results = evaluate_candidate(
                    shrunk, f"P2-S{seed_idx}-S{it}-{vertex_idx}"
                )
                if shrunk_params is None:
                    continue

                new_simplex.append({
                    "params": shrunk_params,
                    "score": shrunk_score,
                    "score_info": shrunk_info,
                    "results": shrunk_results,
                })

            if len(new_simplex) >= 2:
                simplex_data = new_simplex

        simplex_data.sort(key=lambda item: item["score"])
        seed_best = simplex_data[0]
        print(f"    Seed {seed_idx+1} final: score={seed_best['score']:.2f}")

        if seed_best["score"] < best_overall_score:
            best_overall_score = seed_best["score"]
            best_overall_params = copy.deepcopy(seed_best["params"])
            best_overall_results = seed_best["results"]

    print(f"\n  Phase 2 complete in {time.time()-t_start:.0f}s")
    print(f"  Best overall: score={best_overall_score:.2f}")
    print_params(best_overall_params, "Best params:")

    save_model_with_params(best_overall_params, BEST_MODEL)

    return best_overall_params, best_overall_results, best_overall_score

# ── Phase 3: PhaseAdvance co-optimization ────────────────────────────────────
def phase3_pa_optimize(mc, best_params, csv_path=RESULTS_CSV):
    """
    With the best geometry, sweep PhaseAdvance to find optimal operating point.
    Also try small geometry perturbations at each PA.
    """
    print(f"\n{'='*70}")
    print(f"  PHASE 3 — PhaseAdvance Co-optimization")
    print(f"{'='*70}")

    t_start = time.time()
    best_score = float("inf")
    best_pa = NOMINAL_PA
    best_results = None

    pa_values = [30, 35, 40, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65]

    for pa in pa_values:
        try:
            results = run_candidate_with_timeout(best_params, phase_advance=pa, timeout_s=SOLVE_TIMEOUT_S)
            score_info = objective(results)
            elapsed = time.time() - t_start
            log_result(csv_path, f"PA-{pa}", "P3", best_params, results, elapsed, score_info)

            pf = results.get("PowerFactor", 0) or 0
            print(f"  PA={pa:>2}°: T={results['ShaftTorque']:>6.1f}Nm  "
                  f"E={results['MotorEfficiency']:>5.2f}%  PF={pf:.3f}  "
                  f"score={score_info[0]:.2f}")

            if score_info[0] < best_score:
                best_score = score_info[0]
                best_pa = pa
                best_results = results

        except Exception as e:
            print(f"  PA={pa:>2}°: FAILED - {e}")

    print(f"\n  Best PA: {best_pa}°  score={best_score:.2f}")
    if best_results:
        pf = best_results.get("PowerFactor", 0) or 0
        print(f"  T={best_results['ShaftTorque']:.1f}Nm  "
              f"E={best_results['MotorEfficiency']:.2f}%  PF={pf:.3f}")

    return best_pa, best_results, best_score

# ── Phase 4: Final verification ──────────────────────────────────────────────
def phase4_verify(mc, best_params, best_pa):
    """Final comprehensive verification at multiple operating points."""
    print(f"\n{'='*70}")
    print(f"  PHASE 4 — Final Verification")
    print(f"{'='*70}")

    save_model_with_params(best_params, BEST_MODEL)

    print(f"\n  Saved final model to {BEST_MODEL}")

    # Verify at PA=45° (spec) and at optimal PA
    for pa in [45, best_pa]:
        print(f"\n  --- Verification at PA={pa}° ---")
        results = run_candidate_with_timeout(best_params, phase_advance=pa, timeout_s=SOLVE_TIMEOUT_S)
        score_info = objective(results)

        t = results.get("ShaftTorque", 0)
        eff = results.get("MotorEfficiency", 0)
        pf = results.get("PowerFactor", 0) or 0
        inp = results.get("InputPower", 0)
        out = results.get("OutputPower", 0)
        cond_loss = results.get("ConductorLoss", 0)
        iron_loss = results.get("StatorIronLoss_Total", 0)
        ll_rms = results.get("LineLineVoltage", 0)
        ll_peak = results.get("PeakLineLineVoltage", 0)
        irms = results.get("RMSPhaseCurrent", 0)

        torq_err_pct = abs(t - TARGET_TORQUE) / TARGET_TORQUE * 100
        eff_ok = eff >= TARGET_EFF
        pf_ok = pf >= TARGET_PF
        torq_ok = torq_err_pct <= 2.0

        print(f"  Torque:       {t:.2f} Nm  (target: {TARGET_TORQUE} ±2%)  "
              f"[{'PASS' if torq_ok else 'FAIL'}]")
        print(f"  Efficiency:   {eff:.2f}%  (target: ≥{TARGET_EFF}%)  "
              f"[{'PASS' if eff_ok else 'FAIL'}]")
        print(f"  Power Factor: {pf:.3f}  (target: ≥{TARGET_PF})  "
              f"[{'PASS' if pf_ok else 'FAIL'}]")
        print(f"  Input Power:  {inp:.1f} W")
        print(f"  Output Power: {out:.1f} W")
        print(f"  Copper Loss:  {cond_loss:.1f} W")
        print(f"  Iron Loss:    {iron_loss:.1f} W")
        print(f"  LL Voltage:   {ll_rms:.1f} V RMS  ({ll_peak:.1f} V peak)")
        print(f"  Phase Current:{irms:.1f} A RMS")

    return results

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    import argparse
    parser = argparse.ArgumentParser(description="SynRM 45kW IE5 Rotor Optimization v4")
    parser.add_argument("--phase1-only", action="store_true", help="Run Phase 1 only")
    parser.add_argument("--samples", type=int, default=40, help="Phase 1 sample count (default: 40)")
    parser.add_argument("--skip-phase2", action="store_true", help="Skip Phase 2 refinement")
    parser.add_argument("--skip-phase3", action="store_true", help="Skip Phase 3 PA optimization")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    install_interrupt_handler()

    # Initialize CSV
    init_csv(RESULTS_CSV)
    print(f"Results will be logged to: {RESULTS_CSV}")

    # Baseline check
    print(f"\n{'='*70}")
    print(f"  BASELINE — Current model at PA=45°")
    print(f"{'='*70}")
    baseline = run_candidate_with_timeout(CURRENT_BASELINE, phase_advance=45, timeout_s=SOLVE_TIMEOUT_S)
    bl_score = objective(baseline)
    bl_pf = baseline.get("PowerFactor", 0) or 0
    print(f"  Torque: {baseline['ShaftTorque']:.2f} Nm  (target: {TARGET_TORQUE})")
    print(f"  Efficiency: {baseline['MotorEfficiency']:.2f}%  (target: {TARGET_EFF}%)")
    print(f"  Power Factor: {bl_pf:.3f}  (target: {TARGET_PF})")
    print(f"  Input Power: {baseline['InputPower']:.1f} W")
    print(f"  Output Power: {baseline['OutputPower']:.1f} W")
    log_result(RESULTS_CSV, 0, "baseline", CURRENT_BASELINE, baseline, 0, bl_score)

    # Phase 1: Coarse sweep
    top3 = phase1_coarse(None, n_samples=args.samples)

    if args.phase1_only:
        print("\n  Phase 1 only mode — stopping.")
        return

    # Phase 2: Refinement
    if not args.skip_phase2:
        best_params, best_results, best_score = phase2_refine(None, top3)
    else:
        best_params = top3[0][1]
        best_results = top3[0][2]
        best_score = top3[0][0]

    # Phase 3: PA optimization
    if not args.skip_phase3:
        best_pa, pa_results, pa_score = phase3_pa_optimize(None, best_params)
    else:
        best_pa = NOMINAL_PA
        pa_results = best_results
        pa_score = best_score

    # Phase 4: Final verification
    final = phase4_verify(None, best_params, best_pa)

    # Summary
    print(f"\n{'='*70}")
    print(f"  OPTIMIZATION COMPLETE")
    print(f"{'='*70}")
    print(f"  Results CSV:  {RESULTS_CSV}")
    print(f"  Best model:   {BEST_MODEL}")
    print(f"  Best PA:      {best_pa}°")
    print(f"\n  Final barrier parameters:")
    print_params(best_params)
    print(f"\n  Baseline → Optimized (PA=45°):")
    print(f"    Torque:     {baseline['ShaftTorque']:.1f} → {best_results['ShaftTorque']:.1f} Nm")
    print(f"    Efficiency: {baseline['MotorEfficiency']:.1f} → {best_results['MotorEfficiency']:.1f}%")
    print(f"    PF:         {bl_pf:.3f} → {best_results.get('PowerFactor', 0) or 0:.3f}")
    save_model_with_params(best_params, BEST_MODEL)
    print("\nDone!")

if __name__ == "__main__":
    main()
