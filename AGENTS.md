
# AGENTS.md

This file provides guidance to Codex when working with Motor-CAD automation
scripts in this repository. Read this entire file before writing any code.

---

## Project Goal

**Optimize the rotor flux barrier geometry of a 45 kW SynRM to meet the target
specification**, by iterating rotor parameters in Motor-CAD and evaluating
electromagnetic performance after each iteration.

The stator geometry is fixed and must not be changed.
Only rotor barrier parameters are optimization variables.

---

## Target Specification (Must Be Met)

| Parameter | Target | Acceptable Tolerance |
|---|---|---|
| Output Power | 45 kW | ±2% |
| Rated Torque | 143 Nm @ 3000 RPM | ±2% |
| Rated Speed | 3000 RPM | exact |
| Max Speed | 6000 RPM | must not degrade |
| Efficiency Class | IE5 | must meet or exceed |
| Electrical Control Angle | 45 deg | fixed |
| Service Factor | 1.2 | must sustain |

Power factor should be good too .85 and above
IE5 efficiency threshold at 45 kW / 4-pole / 3000 RPM is **≥ 96.0%** (IEC 60034-30-2).

---

## What Is Fixed (Do Not Touch)

### Stator (locked — already in model)

| Parameter | Variable | Value |
|---|---|---|
| Stator OD | `Stator_Lam_Dia` | 340 mm |
| Stator Bore | `Stator_bore` | 215 mm |
| Slot Number | `Slot_Number` | 48 |
| Tooth Width | `Tooth_Width` | 7.5 mm |
| Slot Depth | `Slot_Depth` | 29 mm |
| Slot Corner Radius | `Slot_Corner_Radius` | 4.7 mm |
| Tooth Tip Depth | `Tooth_Tip_Depth` | 0.6 mm |
| Slot Opening | `Slot_Opening` | 2.9 mm |
| Tooth Tip Angle | `Tooth_Tip_Angle` | 15 deg |
| Sleeve Thickness | `Sleeve_Thickness` | 0 |
| Slot Type | — | Parallel Tooth |
| Lamination Material | — | 50C250, 0.50 mm |

### Winding (locked — already in model)

| Parameter | Variable | Value |
|---|---|---|
| Wire Diameter | `WireDiameter` | 1.715 mm |
| Copper Slot Fill | `Copper_Slot_Fill` | 0.4 |
| Liner Thickness | `Liner_Thickness` | 0.25 mm |
| Conductors/Slot | — | 44 (output, not set) |
| EWdg Fill | `EWdg_Fill` | 0.3618 |
| Coil Style | — | Stranded |

### Fixed Rotor Parameters (locked)

| Parameter | Variable | Value |
|---|---|---|
| Pole Number | `Pole_Number` | 4 |
| Rotor Type | `RotorType_Str` | Interior U-Shape |
| Barrier Layers | `Barrier_Layers` | 3 |
| Airgap | `Airgap` | 0.5 mm |
| Shaft Dia | `Shaft_Dia` | 80 mm |
| Rotor Diameter [Calc] | — | 214 mm (derived) |

---

## Optimization Variables (Rotor Barriers Only)

These are the 12 parameters Codex is allowed to vary.
All other parameters must remain at their locked values.

### Current Baseline (from Motor-CAD GUI screenshot)

| Variable | Motor-CAD Name | Baseline | Search Range |
|---|---|---|---|
| L1 Diameter | `L1_Diameter` | 100 mm | 90 – 115 mm |
| L1 Bridge Thickness | `L1_Bridge_Thickness` | 4 mm | 1 – 6 mm |
| L1 Web Thickness | `L1_Web_Thickness` | 17 mm | 5 – 30 mm |
| L1 Outer Angle Offset | `L1_Outer_Angle_Offset` | -10 deg | -20 – 0 deg |
| L1 Outer Thickness | `L1_Outer_Thickness` | 4 mm | 2 – 8 mm |
| L1 Inner Thickness | `L1_Inner_Thickness` | 5 mm | 2 – 8 mm |
| L2 Diameter | `L2_Diameter` | 130 mm | 120 – 150 mm |
| L2 Bridge Thickness | `L2_Bridge_Thickness` | 5 mm | 1 – 6 mm |
| L2 Web Thickness | `L2_Web_Thickness` | 50 mm | 20 – 70 mm |
| L3 Diameter | `L3_Diameter` | 160 mm | 145 – 175 mm |
| L3 Bridge Thickness | `L3_Bridge_Thickness` | 5 mm | 1 – 6 mm |
| L3 Web Thickness | `L3_Web_Thickness` | 82 mm | 50 – 100 mm |

### Constraints Between Variables

These must hold after every parameter change or Motor-CAD will reject the geometry:

```
L1_Diameter < L2_Diameter < L3_Diameter < Rotor_Diameter (214 mm)
L1_Diameter > Shaft_Dia (80 mm)
Each Bridge_Thickness >= 1 mm  (mechanical minimum)
L3_Diameter + L3_Outer_Thickness < 214 mm
```

---

## Operating Point for All Calculations

```python
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)          # electrical control angle — fixed per spec
mc.set_variable("TorquePointsPerCycle", 30)
mc.set_variable("TorqueNumberCycles", 1)
mc.set_variable("TorqueCalculation", True)
# PeakCurrent and DCBusVoltage: discover actual variable names before setting
```

---

## Optimization Strategy

### Recommended Approach: Sequential Parameter Sweep → Gradient Refinement

Since Motor-CAD calls are expensive (each EMag calc ~60–90 seconds), use a
two-phase approach:

**Phase 1 — Coarse sweep (Latin Hypercube or grid)**
- Sample ~20–50 points across the search ranges
- Run `do_magnetic_calculation()` for each
- Record `ShaftTorque` and `Efficiency` (or `InputPower`)
- Identify the top 5 candidates

**Phase 2 — Local refinement**
- Start from best Phase 1 candidate
- Perturb each variable ±one step, keep changes that improve the objective
- Repeat until convergence (change in torque < 0.5 Nm between iterations)

### Objective Function

```python
def objective(mc, target_torque=143.0, target_efficiency_pct=96.0):
    torque     = mc.get_variable("ShaftTorque")
    input_pwr  = mc.get_variable("InputPower")
    shaft_pwr  = torque * 3000 * 2 * 3.14159 / 60   # W
    efficiency = shaft_pwr / input_pwr * 100 if input_pwr > 0 else 0

    torque_error = abs(torque - target_torque) / target_torque
    eff_penalty  = max(0, target_efficiency_pct - efficiency)

    # Lower is better
    return torque_error * 100 + eff_penalty
```

### Results Logging

Every iteration must be logged immediately after the calculation — Motor-CAD
results are lost if the model is changed before reading them.

```python
import csv, time

def log_result(csv_path, iteration, params, torque, input_power, shaft_power, efficiency):
    row = {"iteration": iteration, "timestamp": time.time(), **params,
           "ShaftTorque": torque, "InputPower": input_power,
           "ShaftPower": shaft_power, "Efficiency": efficiency}
    write_header = not os.path.exists(csv_path)
    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(row)
```

---

## Script Structure to Follow

```
optimize_rotor.py
│
├── connect_motorcad()          — launch + load SRM_1.mot
├── discover_variables()        — run once at startup, print all var names
├── verify_fixed_params()       — assert stator/winding params unchanged
├── set_rotor_barriers(params)  — apply one candidate's barrier geometry
├── check_geometry_constraints(params) — validate before sending to Motor-CAD
├── run_emag()                  — show_magnetic_context → do_magnetic_calculation
├── read_results()              — ShaftTorque, InputPower, efficiency
├── log_result()                — append to CSV immediately
├── run_sweep()                 — Phase 1: sample and evaluate N candidates
├── run_refinement()            — Phase 2: local search from best candidate
└── main()                      — orchestrate full workflow
```

---

## Motor-CAD Connection

```python
import os, pathlib
import ansys.motorcad.core as pymotorcad

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL_FILE   = r"D:\SRM\Motor _CAD\SRM_1.mot"
RESULTS_CSV  = r"D:\SRM\Motor _CAD\ScriptFiles\optimization_results.csv"

def connect_motorcad():
    os.environ.setdefault("MOTORCAD_INSTALL_DIR",
                          str(pathlib.Path(MOTORCAD_EXE).parent))
    mc = pymotorcad.MotorCAD(
        open_new_instance=True,
        use_blackbox_licence=True,
        keep_instance_open=False,
    )
    mc.set_variable("MessageDisplayState", 2)
    mc.load_from_file(MODEL_FILE)
    return mc
```

---

## Verified Method Names (from official PyMotorCAD docs)

| Task | Method |
|---|---|
| Switch to EMag | `mc.show_magnetic_context()` |
| Switch to Thermal | `mc.show_thermal_context()` |
| Show scripting tab | `mc.display_screen("Scripting")` |
| EMag calculation | `mc.do_magnetic_calculation()` |
| Thermal steady-state | `mc.do_steady_state_analysis()` |
| Coupled emag+thermal | `mc.do_magnetic_thermal_calculation()` |
| Set material | `mc.set_component_material(component, material)` |
| Save model | `mc.save_to_file(path)` |
| Load model | `mc.load_from_file(path)` |
| Discover variables | `mc.get_variable_names()` |
| Close instance | `mc.quit()` |

---

## Verified Result Variable Names

| Result | Variable |
|---|---|
| Shaft torque | `ShaftTorque` |
| Peak line-line voltage | `PeakLineLineVoltage` |
| Input power | `InputPower` |
| Stator copper loss AC | `StatorCopperLossAC` |
| Stator iron loss total | `StatorIronLoss_Total` |
| Winding temp min | `T_[Winding_Min]` |
| Winding temp max | `T_[Winding_Max]` |
| Winding temp average | `T_[Winding_Average]` |

**For any variable not in this list: call `discover_variables()` first. Never guess.**

---

## Anti-Hallucination Rules — CRITICAL

Motor-CAD variable names are exact internal strings. Wrong names cause silent
wrong results or exceptions with no indication of which variable failed.

### Rule 1 — Always discover before first use

```python
def discover_variables(mc, keyword):
    try:
        all_vars = mc.get_variable_names()
        matches = [v for v in all_vars if keyword.lower() in v.lower()]
        print(f"  '{keyword}' matches: {matches}")
        return matches
    except Exception as e:
        print(f"  discover_variables failed: {e}")
        return []

# Run at script startup after loading model:
for kw in ["torque", "efficiency", "power", "barrier", "diameter",
           "bridge", "web", "thickness", "winding", "current", "voltage"]:
    discover_variables(mc, kw)
```

### Rule 2 — Always use safe_get / safe_set wrappers

```python
def safe_get(mc, name, label=""):
    try:
        val = mc.get_variable(name)
        if label:
            print(f"  {label}: {val}")
        return val
    except Exception as e:
        raise RuntimeError(f"get_variable('{name}') failed: {e}")

def safe_set(mc, name, value):
    try:
        mc.set_variable(name, value)
    except Exception as e:
        raise RuntimeError(f"set_variable('{name}', {value}) failed: {e}")
```

### Rule 3 — Always call show_magnetic_context() before EMag methods

### Rule 4 — Always save before changing rotor params

Save a backup of the current best model before applying the next candidate,
so you can always recover the best result found so far.

```python
mc.save_to_file(r"D:\SRM\Motor _CAD\best_so_far.mot")
```

### Rule 5 — Read all results before changing any parameter

Motor-CAD results refer to the last calculation. Read everything you need
before calling `set_variable()` for the next iteration.

---

## Geometry Constraint Checker

```python
def check_geometry_constraints(params):
    shaft = 80
    rotor = 214
    assert params["L1_Diameter"] > shaft,              "L1 must be > shaft dia"
    assert params["L1_Diameter"] < params["L2_Diameter"], "L1 < L2 required"
    assert params["L2_Diameter"] < params["L3_Diameter"], "L2 < L3 required"
    assert params["L3_Diameter"] < rotor,              "L3 must be < rotor OD"
    for layer in ["L1", "L2", "L3"]:
        assert params[f"{layer}_Bridge_Thickness"] >= 1, \
            f"{layer} bridge must be >= 1 mm"
    return True
```

---

## File Paths

| Item | Path |
|---|---|
| Motor-CAD exe | `C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe` |
| Model file | `D:\SRM\Motor _CAD\SRM_1.mot` |
| Script directory | `D:\SRM\Motor _CAD\ScriptFiles\` |
| Official test script | `D:\SRM\Motor _CAD\ScriptFiles\test_motorcad.py` |
| Optimization results | `D:\SRM\Motor _CAD\ScriptFiles\optimization_results.csv` |
| Best model backup | `D:\SRM\Motor _CAD\best_so_far.mot` |

---

## Motor-CAD Version

Ansys Motor-CAD v2025.1.1 — confirmed from GUI title bar.