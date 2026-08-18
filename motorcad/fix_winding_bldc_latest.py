#!/usr/bin/env python3
r"""
fix_winding_v2.py  --  Full winding fix for bldc_latest.mot (16p/12s)
=======================================================================
ROOT CAUSE OF ZERO TORQUE:
  For 16-pole / 12-slot:  alpha_e per slot = (16/2) * 360/12 = 240 deg/slot
  Existing 3-slot span  = 3 * 240 = 720 deg el = 2 full cycles -> net EMF = 0
  Fix: use 1-slot span  = 1 * 240 = 240 deg el -> kw = sin(120) = 0.866

CORRECT DOUBLE-LAYER 16p/12s pattern (star-of-slots, kw=0.866):
  Slot phasors (el): 1:0, 2:240, 3:120, 4:0, 5:240, 6:120, 7:0, 8:240, 9:120, 10:0, 11:240, 12:120
  Phase A (go@0 slots, ret@240 slots, 1-slot adjacent):
      Coil A1: go=1, ret=2   Coil A2: go=4, ret=5
      Coil A3: go=7, ret=8   Coil A4: go=10, ret=11
  Phase B (go@240 slots, ret@120 slots):
      Coil B1: go=2, ret=3   Coil B2: go=5, ret=6
      Coil B3: go=8, ret=9   Coil B4: go=11, ret=12
  Phase C (go@120 slots, ret@0 slots):
      Coil C1: go=3, ret=4   Coil C2: go=6, ret=7
      Coil C3: go=9, ret=10  Coil C4: go=12, ret=1

GEOMETRY FIX (for BPMRotor=0, Surface Radial SPM):
  Stator bore = 80mm, Airgap = 0.5mm, Magnet_Thickness = 2.4mm
  -> RotorDiameter (core) = 80 - 2*0.5 - 2*2.4 = 74.2mm  => set 74mm

ANALYTICAL OPERATING POINT:
  kw=0.866, N_series=120, Phi_1=7.2e-5 Wb (N30UH, Bg~0.73T, stack=10mm)
  E_ph,rms = 4.44 * 400 * 120 * 7.2e-5 * 0.866 = 13.3 V
  E_LL,peak = 13.3 * sqrt(3) * sqrt(2) = 32.6 V  << 48 V bus  ->  use 48V
  Kt = 0.127 Nm/A_rms (3-phase, SPM, id=0)
  At I_rms=3A: T=0.38Nm, P_out=120W, P_cu=3*(3^2)*0.65=17.6W  eta~77%
  At I_rms=5A: T=0.64Nm, P_out=200W, P_cu=48.8W               eta~74%

Connect to already-running Motor-CAD (open_new_instance=False).
"""

import os, sys, math, pathlib

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL_IN   = r"D:\SRM\Agent\motorcad\bldc_latest.mot"
MODEL_OUT  = r"D:\SRM\Agent\motorcad\bldc_latest_fixed.mot"

# ── Wire (fixed constraint) ──────────────────────────────────────────────────
COPPER_DIA = 0.50   # mm  bare copper (user constraint)
WIRE_DIA   = 0.55   # mm  covered  (0.5 mm + 0.025 mm enamel each side)

# ── Winding (redesigned for kw=0.866) ────────────────────────────────────────
TURNS_PER_COIL = 30         # keeps slot fill ~54%, as found in existing model
PARALLEL_PATHS = 1
N_SERIES       = TURNS_PER_COIL * 4   # 120 series turns/phase

# ── 1-slot-span double-layer coil table (Phase, go_slot, ret_slot) ───────────
# All at position 'C'. WindingLayers=2; Motor-CAD assigns the two layers.
COILS = [
    # Phase A
    (1, 1,  2), (1, 4,  5), (1, 7,  8), (1, 10, 11),
    # Phase B
    (2, 2,  3), (2, 5,  6), (2, 8,  9), (2, 11, 12),
    # Phase C
    (3, 3,  4), (3, 6,  7), (3, 9,  10), (3, 12, 1),
]
COIL_POS = "C"

# ── Operating point ──────────────────────────────────────────────────────────
DC_BUS      = 48.0   # V   matches E_LL,peak ~33V (69% utilisation, good)
I_PEAK_INIT = 4.0    # A   start: J ~ 14.4 A/mm^2  (burst mode initial guess)
PHASE_ADV   = 0.0    # deg SPM MTPA
RPM         = 3000.0
I_PEAK_MAX  = 8.0    # A   safety cap (~28.8 A/mm^2, high but short stack)
MAX_ITER    = 5

# ── Geometry fix for Surface Radial SPM ─────────────────────────────────────
ROTOR_DIAM_FIX = 74.0  # mm  lamination OD: bore(80)-2*gap(0.5)-2*mag(2.4)=74.2


def s(mc, name, val):
    try:
        mc.set_variable(name, val)
        print(f"    set {name} = {val}")
    except Exception as e:
        raise RuntimeError(f"set_variable('{name}', {val}): {e}")


def g(mc, name):
    try:
        return mc.get_variable(name)
    except Exception:
        return None


def apply_wire(mc):
    """Re-assert wire every time before an EMag calc."""
    s(mc, "Wire_Type_Stator", 0)            # direct input, NOT AWG table
    s(mc, "Armature_Winding_Definition", 1) # wire-size mode
    s(mc, "Wire_Diameter",  WIRE_DIA)
    s(mc, "Copper_Diameter", COPPER_DIA)


def set_coils(mc):
    """Apply the correct 1-slot-span 16p/12s double-layer pattern."""
    print("  Applying 1-slot-span winding pattern (kw=0.866):")
    mc.set_variable("MagneticWindingType", 2)  # custom
    mc.set_variable("MagPathType", 0)
    mc.set_variable("MagPhases", 3)
    mc.set_variable("WindingLayers", 2)
    mc.set_variable("NumberOfCoils", 4)   # 4 per phase = 12 total

    coil_idx = {1: 1, 2: 1, 3: 1}
    for ph, go_s, ret_s in COILS:
        mc.set_winding_coil(ph, 1, coil_idx[ph],
                            go_s,  COIL_POS,
                            ret_s, COIL_POS,
                            TURNS_PER_COIL)
        print(f"    Ph{ph} Coil{coil_idx[ph]}: {go_s}C -> {ret_s}C  ({TURNS_PER_COIL} turns)")
        coil_idx[ph] += 1

    s(mc, "ParallelPaths",    PARALLEL_PATHS)
    s(mc, "ConductorsPerSlot", TURNS_PER_COIL * 2)  # double-layer: 2 sides


def verify_coils(mc):
    """Read back coils and confirm 1-slot span."""
    print("\n  Winding verification:")
    all_ok = True
    for ph in range(1, 4):
        for ci in range(1, 5):
            try:
                go_s, go_p, ret_s, ret_p, turns = mc.get_winding_coil(ph, 1, ci)
                span = abs(ret_s - go_s)
                span = min(span, 12 - span)   # wrap-around
                ok = (span == 1 and turns == TURNS_PER_COIL)
                flag = "OK" if ok else "*** BAD SPAN ***"
                print(f"    Ph{ph} Coil{ci}: {go_s}{go_p}->{ret_s}{ret_p} "
                      f"turns={turns} span={span}  {flag}")
                if not ok:
                    all_ok = False
            except Exception as e:
                print(f"    Ph{ph} Coil{ci}: <ERR {e}>")
                all_ok = False
    return all_ok


def read_results(mc):
    keys = ["ShaftTorque", "OutputPower", "InputPower",
            "RMSPhaseCurrent", "PeakLineLineVoltage",
            "ConductorLoss", "StatorIronLoss_Total",
            "MotorEfficiency",
            "Wire_Diameter", "Copper_Diameter", "Slot_Fill"]
    return {k: g(mc, k) for k in keys}


def report(res, tag):
    T   = res["ShaftTorque"]   or 0
    Po  = res["OutputPower"]   or 0
    Pi  = res["InputPower"]    or 0
    eta = (Po / Pi * 100) if (Pi and Pi > 0) else 0
    Vll = res["PeakLineLineVoltage"] or 0
    Pcu = res["ConductorLoss"] or 0
    Pfe = res["StatorIronLoss_Total"] or 0
    Ir  = res["RMSPhaseCurrent"] or 0
    A_cu = math.pi * (COPPER_DIA/2)**2
    J = Ir / A_cu if A_cu else 0

    print(f"\n{'='*60}")
    print(f"  RESULTS [{tag}]")
    print(f"{'='*60}")
    print(f"  Torque      = {T:.4f} Nm")
    print(f"  P_out       = {Po:.1f} W")
    print(f"  Efficiency  = {eta:.1f} %")
    print(f"  V_LL,peak   = {Vll:.1f} V  (bus {DC_BUS:.0f} V)")
    print(f"  P_cu        = {Pcu:.1f} W   P_fe = {Pfe:.1f} W")
    print(f"  I_rms       = {Ir:.3f} A   J = {J:.1f} A/mm^2")
    print(f"  Wire        = {res['Wire_Diameter']} mm / {res['Copper_Diameter']} mm copper")
    print(f"  Slot fill   = {(res['Slot_Fill'] or 0)*100:.1f} %")
    print(f"{'='*60}")
    return T, Po, Pi, eta


def main():
    os.environ.setdefault("MOTORCAD_INSTALL_DIR",
                          str(pathlib.Path(MOTORCAD_EXE).parent))
    import ansys.motorcad.core as pymotorcad

    print("Connecting to Motor-CAD (existing instance)...")
    mc = pymotorcad.MotorCAD(open_new_instance=False)

    try:
        mc.set_variable("MessageDisplayState", 2)

        print(f"\nLoading {MODEL_IN}...")
        mc.load_from_file(MODEL_IN)
        mc.show_magnetic_context()
        print(f"  Loaded: {g(mc,'Pole_Number')}p / {g(mc,'Slot_Number')}s")

        # ── 1. Fix rotor type to Surface Radial SPM ──────────────────────────
        print("\n-- FIX 1: Rotor type -> Surface Radial SPM (BPMRotor=0) --")
        s(mc, "BPMRotor", 0)
        s(mc, "RotorDiameter", ROTOR_DIAM_FIX)  # geometry consistent with bore+airgap+mag
        print(f"  RotorDiameter set to {ROTOR_DIAM_FIX} mm "
              f"(was 78; needed: bore80-2*gap0.5-2*mag2.4=74.2)")

        # ── 2. Apply correct 1-slot-span winding ─────────────────────────────
        print("\n-- FIX 2: Winding pattern (1-slot span, kw=0.866) --")
        set_coils(mc)
        good = verify_coils(mc)
        if not good:
            print("  WARNING: some coils have wrong span -- check Motor-CAD winding editor")

        # ── 3. Wire --  0.5 mm copper enforced ───────────────────────────────
        print("\n-- FIX 3: Wire -> 0.5 mm copper (direct input mode) --")
        apply_wire(mc)

        # ── 4. Operating point ────────────────────────────────────────────────
        print("\n-- FIX 4: Operating point --")
        s(mc, "DCBusVoltage",         DC_BUS)
        s(mc, "PeakCurrent",          I_PEAK_INIT)
        s(mc, "RMSCurrent",           round(I_PEAK_INIT / math.sqrt(2), 4))
        s(mc, "PhaseAdvance",         PHASE_ADV)    # 0 deg = SPM MTPA
        s(mc, "CurrentAngle",         0.0)
        s(mc, "Shaft_Speed_[RPM]",    RPM)
        s(mc, "TorqueCalculation",    True)
        s(mc, "TorquePointsPerCycle", 60)
        s(mc, "TorqueNumberCycles",   1)

        # ── 5. Save + reload (commit wire state -- proven anti-AWG-reset trick) -
        print(f"\nSaving to {MODEL_OUT}...")
        mc.save_to_file(MODEL_OUT)

        print("Reloading to commit winding state...")
        mc.load_from_file(MODEL_OUT)
        mc.show_magnetic_context()
        apply_wire(mc)                   # re-assert after reload
        s(mc, "DCBusVoltage",         DC_BUS)
        s(mc, "PeakCurrent",          I_PEAK_INIT)
        s(mc, "RMSCurrent",           round(I_PEAK_INIT / math.sqrt(2), 4))
        s(mc, "PhaseAdvance",         PHASE_ADV)
        s(mc, "CurrentAngle",         0.0)
        s(mc, "Shaft_Speed_[RPM]",    RPM)
        s(mc, "TorqueCalculation",    True)
        s(mc, "TorquePointsPerCycle", 60)
        s(mc, "TorqueNumberCycles",   1)
        print(f"  Wire confirmed: {g(mc,'Wire_Diameter')} / {g(mc,'Copper_Diameter')} mm")

        # ── 6. EMag iteration loop ────────────────────────────────────────────
        print("\n" + "="*60)
        print("  EMag Calculations")
        print("="*60)

        I_peak = I_PEAK_INIT
        res = None
        Kt  = None     # will be measured from first run

        for it in range(1, MAX_ITER + 1):
            print(f"\nIteration {it}  (I_peak = {I_peak:.3f} A)")
            mc.save_to_file(MODEL_OUT)
            apply_wire(mc)
            s(mc, "PeakCurrent", I_peak)
            s(mc, "RMSCurrent",  round(I_peak / math.sqrt(2), 4))

            mc.do_magnetic_calculation()
            res = read_results(mc)
            T, Po, Pi, eta = report(res, f"iter {it}")

            # Measure Kt on first iter; use it to target best efficiency zone
            if it == 1:
                if T is not None and T > 0.01 and I_peak > 0:
                    Kt = T / I_peak
                    print(f"\n  Measured Kt = {Kt:.4f} Nm/A_peak")
                    # Target J ~6-8 A/mm^2 for good efficiency
                    A_cu = math.pi * (COPPER_DIA / 2) ** 2
                    J_target = 7.0   # A/mm^2
                    I_rms_target = J_target * A_cu
                    I_peak_new = min(I_PEAK_MAX, I_rms_target * math.sqrt(2))
                    print(f"  Targeting J={J_target} A/mm^2 -> "
                          f"I_rms={I_rms_target:.2f} A, I_peak={I_peak_new:.2f} A")
                    I_peak = I_peak_new
                elif T is not None and T <= 0:
                    print("\n  *** TORQUE STILL NON-POSITIVE ***")
                    print("  Winding pattern may not have applied correctly.")
                    print("  Trying with higher current anyway...")
                    I_peak = min(I_PEAK_MAX, I_peak * 2)
                else:
                    I_peak = min(I_PEAK_MAX, I_peak * 1.5)
                continue

            # Converge toward efficiency peak
            A_cu = math.pi * (COPPER_DIA / 2) ** 2
            Ir = res["RMSPhaseCurrent"] or 0
            J_now = Ir / A_cu
            if J_now > 10.0:
                # Reduce current - too high J
                I_peak = max(1.0, I_peak * 0.85)
            elif abs(I_peak - I_PEAK_MAX) / I_PEAK_MAX < 0.02:
                print("  At max current, stopping.")
                break
            else:
                # Converged
                if abs(I_peak - (res["RMSPhaseCurrent"] or 0) * math.sqrt(2)) < 0.1:
                    break

        # ── 7. Final report ───────────────────────────────────────────────────
        if res:
            T, Po, Pi, eta = report(res, "FINAL")
            Vll = res["PeakLineLineVoltage"] or 0
            A_cu = math.pi * (COPPER_DIA / 2) ** 2
            Ir = res["RMSPhaseCurrent"] or 0
            J = Ir / A_cu

            print("\n  PASS/FAIL")
            print(f"  [{'PASS' if T  > 0   else 'FAIL'}] Positive torque        {T:.3f} Nm")
            print(f"  [{'PASS' if Vll<=DC_BUS else 'FAIL'}] V_LL,peak <= bus      {Vll:.1f} / {DC_BUS:.0f} V")
            print(f"  [{'PASS' if eta>=70   else 'FAIL'}] Efficiency >= 70%      {eta:.1f} %")
            print(f"  [{'PASS' if Po >=50   else 'FAIL'}] P_out >= 50 W          {Po:.1f} W")
            print(f"  Current density J = {J:.1f} A/mm^2")
            print(f"  Wire: 0.5 mm copper confirmed: {res['Copper_Diameter']} mm")
            print(f"  Series turns/phase = {N_SERIES}")

            mc.save_to_file(MODEL_OUT)
            print(f"\n  Saved -> {MODEL_OUT}")

    finally:
        try:
            mc.quit()
        except Exception:
            pass
        print("\nMotor-CAD closed.")


if __name__ == "__main__":
    main()
