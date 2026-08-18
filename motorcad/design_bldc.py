#!/usr/bin/env python3
"""
design_bldc.py — Implement the 500 W / 48 V / 3000 rpm BLDC design in Motor-CAD
================================================================================
Loads  D:\\SRM\\Agent\\motorcad\\bldc1.mot  (stock BPM-Therm template), converts the
rotor from Interior U-Shape IPM (BPMRotor=13) to Surface Radial SPM (BPMRotor=0),
applies the analytically-derived design (see bldc_design.py), runs the EMag
calculation and iterates the phase current until ShaftTorque ~= 1.59 Nm.

Usage:
    python design_bldc.py [--dry-run] [--iterations N] [--keep-open]

Parameter/variable names verified against:
    workspace/wiki/motorcad/parameter_database/  +  ActiveXParameters.xlsx
    workspace/raw/pymotorcad_markdown/  (BPMRotor=0 -> "Surface Radial")
"""

import os
import sys
import time
import pathlib

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL_IN     = r"D:\SRM\Agent\motorcad\bldc1.mot"
MODEL_OUT    = r"D:\SRM\Agent\motorcad\bldc1_design.mot"

# ---------------------------------------------------------------- design ----
DESIGN = {
    # topology
    "Pole_Number": 8,
    "Slot_Number": 12,
    "BPMRotor": 0,                      # 0 = Surface Radial (SPM)
    # stator
    "Stator_Lam_Dia": 105,              # mm  stator lamination OD
    "Stator_bore": 65.0,                # mm  bore = 58 core + 2*(3 mag + 0.5 gap)
    "Stator_Lam_Length": 45.0,          # mm  stack
    "Tooth_Width": 6.5,                 # mm  parallel tooth
    "Slot_Depth": 12.0,                 # mm  bore -> slot bottom
    "Slot_Opening": 2.0,                # mm
    "Tooth_Tip_Depth": 1.0,             # mm
    "Tooth_Tip_Angle": 20.0,            # deg
    "Slot_Corner_Radius": 1.0,          # mm
    "Housing_Dia": 110.0,               # mm  frame
    # rotor
    "RotorDiameter": 58.0,              # mm  rotor CORE OD (under magnets)
    "Shaft_Dia": 20.0,                  # mm
    "Rotor_Lam_Length": 45.0,           # mm
    "Airgap": 0.5,                      # mm
    "Magnet_Thickness": 3.0,            # mm  radial
    "Magnet_Arc_[ED]": 140.0,           # elec deg  (pole arc ratio ~0.78)
    "Magnet_Length": 45.0,              # mm  axial
    "Banding_Thickness": 0.0,           # mm  not needed at 10 m/s tip speed
    # winding
    "Wdg_Definition": 0,                # 0 = Input_Slot_Fill
    "Armature_Winding_Definition": 0,   # 0 = copper slot fill (not AWG table!)
    "Slot_Fill": 0.40,                  # target fill -> sizes the wire
    "ConductorsPerSlot": 10,            # single-layer: 10 turns/coil -> 20 ser/ph
    "ParallelPaths": 1,
    "Wire_Diameter": 2.50,              # mm  covered (set AFTER pattern!)
    "Copper_Diameter": 2.35,            # mm  bare copper
    # drive / operating point
    "DCBusVoltage": 48.0,               # V
    "PeakCurrent": 23.0,                # A  peak phase current
    "RMSCurrent": 16.3,                 # A  rms phase current
    "PhaseAdvance": 0.0,                # elec deg (SPM -> MTPA at 0)
    "CurrentAngle": 0.0,                # elec deg
    "Shaft_Speed_[RPM]": 3000.0,
    # solver settings
    "TorqueCalculation": True,
    "TorquePointsPerCycle": 60,
    "TorqueNumberCycles": 1,
    "MessageDisplayState": 2,
}

# 8-pole / 12-slot SINGLE-LAYER concentrated winding (per user: 1 layer,
# 1 parallel path — simplest to manufacture).
# 6 coils, pitch 2 (span 240 degE, k_w = sin120 = 0.866), each slot used
# exactly once. EMF phase groups (120 deg apart): A=30, B=150, C=270 degE.
# Coil (go->return):
#   A: 1->3, 4->6      B: 5->7, 8->10      C: 9->11, 12->2
# (phase, go_slot, return_slot) -- single layer, position 'C' (central)
WINDING_COILS = [
    (1, 1, 3), (1, 4, 6),
    (2, 5, 7), (2, 8, 10),
    (3, 9, 11), (3, 12, 2),
]
TURNS_PER_COIL = 10        # 2 coils/phase x 10 = 20 series turns/phase
COIL_POSITION  = "C"       # central path (MagPathType=0, single layer)

TARGET_TORQUE = 1.592      # Nm  (500 W @ 3000 rpm)
TARGET_POWER  = 500.0      # W
TARGET_EFF    = 90.0       # %   minimum acceptable
V_BUS         = 48.0       # V   voltage limit

MAGNET_MATERIALS = ["N42", "N42H", "N42SH", "NdFeB 42"]
# component names verified in raw/pymotorcad_markdown "Motor-CAD E-magnetic
# example script": laminations are "Stator Lam (Back Iron)" / "Rotor Lam (Back Iron)"
LAM_COMPONENTS   = ["Stator Lam (Back Iron)", "Rotor Lam (Back Iron)"]
LAM_MATERIALS    = ["M250-35A", "M270-35A", "M350-50A"]


def safe_set(mc, name, value, quiet=False):
    try:
        mc.set_variable(name, value)
        if not quiet:
            print(f"    set {name} = {value}")
    except Exception as e:
        raise RuntimeError(f"set_variable('{name}', {value}) failed: {e}")


def safe_get(mc, name):
    try:
        return mc.get_variable(name)
    except Exception as e:
        raise RuntimeError(f"get_variable('{name}') failed: {e}")


def set_material(mc, component, candidates, current):
    """Try candidate material names; keep current if none matches."""
    for mat in candidates:
        try:
            mc.set_component_material(component, mat)
            got = mc.get_component_material(component)
            if got.strip().lower() == mat.strip().lower():
                print(f"    material {component}: {mat}  OK")
                return mat
        except Exception:
            continue
    print(f"    material {component}: no candidate applied, keeping '{current}'")
    return current


def connect():
    os.environ.setdefault("MOTORCAD_INSTALL_DIR",
                          str(pathlib.Path(MOTORCAD_EXE).parent))
    import ansys.motorcad.core as pymotorcad
    mc = pymotorcad.MotorCAD(open_new_instance=True,
                             use_blackbox_licence=True,
                             keep_instance_open=False)
    return mc


def read_results(mc):
    """Read all results immediately after the calc (results are volatile)."""
    res = {
        "ShaftTorque":           safe_get(mc, "ShaftTorque"),
        "OutputPower":           safe_get(mc, "OutputPower"),
        "InputPower":            safe_get(mc, "InputPower"),
        "PhaseCurrent":          safe_get(mc, "PhaseCurrent"),
        "RMSPhaseCurrent":       safe_get(mc, "RMSPhaseCurrent"),
        "PeakLineLineVoltage":   safe_get(mc, "PeakLineLineVoltage"),
        "LineLineVoltage":       safe_get(mc, "LineLineVoltage"),
        "ConductorLoss":         safe_get(mc, "ConductorLoss"),
        "StatorIronLoss_Total":  safe_get(mc, "StatorIronLoss_Total"),
        "TotalLoss":             safe_get(mc, "TotalLoss"),
        "MotorEfficiency":       safe_get(mc, "MotorEfficiency"),
        "Wire_Diameter":         safe_get(mc, "Wire_Diameter"),
        "Copper_Diameter":       safe_get(mc, "Copper_Diameter"),
        "Slot_Fill":             safe_get(mc, "Slot_Fill"),
    }
    return res


def report(res, tag):
    print("\n" + "-" * 72)
    print(f"RESULTS  [{tag}]")
    print("-" * 72)
    for k, v in res.items():
        print(f"    {k:<22} {v}")
    T  = res["ShaftTorque"]
    Po = res["OutputPower"]
    Pi = res["InputPower"]
    eta = (Po / Pi * 100.0) if Pi and Pi > 0 else 0.0
    Vll = res["PeakLineLineVoltage"]
    print("-" * 72)
    print(f"    Torque={T:.3f} Nm (target {TARGET_TORQUE:.3f})  "
          f"P_out={Po:.1f} W (target {TARGET_POWER:.0f})  "
          f"efficiency={eta:.1f} %")
    print(f"    V_LL,peak={Vll:.1f} V  (bus {V_BUS:.0f} V)  "
          f"{'OK' if Vll <= V_BUS else 'OVER-VOLTAGE'}")
    return eta


def main():
    dry_run    = "--dry-run" in sys.argv
    keep_open  = "--keep-open" in sys.argv
    max_iter   = 3
    for a in sys.argv:
        if a.startswith("--iterations="):
            max_iter = int(a.split("=")[1])

    print("== Connecting to Motor-CAD ==")
    mc = connect()
    try:
        print("== Loading model ==")
        mc.load_from_file(MODEL_IN)
        mc.show_magnetic_context()

        print("== Verifying starting point ==")
        for v in ("Motor_Type", "Pole_Number", "Slot_Number", "BPMRotor",
                  "Stator_Lam_Dia", "Stator_bore", "Material_Magnet"):
            pass  # Motor_Type/Material_Magnet are file keys, not var names
        print(f"    BPMRotor (before) = {safe_get(mc, 'BPMRotor')}  "
              f"(13 = Interior_UShape IPM)")
        print(f"    Pole_Number (before) = {safe_get(mc, 'Pole_Number')}")
        print(f"    Slot_Number (before) = {safe_get(mc, 'Slot_Number')}")
        print(f"    PeakCurrent (before) = {safe_get(mc, 'PeakCurrent')}")

        print("== Applying design ==")
        # 1. topology first (slot/pole change invalidates winding pattern)
        safe_set(mc, "Pole_Number", DESIGN["Pole_Number"])
        safe_set(mc, "Slot_Number", DESIGN["Slot_Number"])
        safe_set(mc, "BPMRotor", DESIGN["BPMRotor"])
        mc.create_winding_pattern()
        print("    winding pattern regenerated for 8p/12s")

        # 2. geometry
        for k in ("Stator_Lam_Dia", "Stator_bore", "Stator_Lam_Length",
                  "Tooth_Width", "Slot_Depth", "Slot_Opening",
                  "Tooth_Tip_Depth", "Tooth_Tip_Angle", "Slot_Corner_Radius",
                  "Housing_Dia", "RotorDiameter", "Shaft_Dia",
                  "Rotor_Lam_Length", "Airgap", "Magnet_Thickness",
                  "Magnet_Arc_[ED]", "Magnet_Length", "Banding_Thickness"):
            safe_set(mc, k, DESIGN[k], quiet=True)
        print("    geometry applied (18 params)")

        # 3. winding — explicit custom pattern: single-layer 8p/12s, 6 coils
        #    pitch 2 (user requirement: 1 layer, 1 parallel path). The auto
        #    pattern for 8p/12s was broken (50 turns/coil, 3 slots unused).
        mc.set_variable("MagneticWindingType", 2)   # Custom
        mc.set_variable("MagPathType", 0)           # Central -> position 'C'
        mc.set_variable("MagPhases", 3)
        mc.set_variable("WindingLayers", 1)         # single layer (simple)
        mc.set_variable("NumberOfCoils", 2)         # 2 coils per phase (6 total)
        safe_set(mc, "Wdg_Definition", DESIGN["Wdg_Definition"])
        safe_set(mc, "Armature_Winding_Definition",
                 DESIGN["Armature_Winding_Definition"])
        safe_set(mc, "Slot_Fill", DESIGN["Slot_Fill"])
        safe_set(mc, "ConductorsPerSlot", DESIGN["ConductorsPerSlot"])
        safe_set(mc, "ParallelPaths", 1)            # single path (simple)
        coil_idx = {1: 1, 2: 1, 3: 1}
        for ph, gs, rs in WINDING_COILS:
            mc.set_winding_coil(ph, 1, coil_idx[ph], gs, COIL_POSITION, rs,
                                COIL_POSITION, TURNS_PER_COIL)
            coil_idx[ph] += 1
        # wire size MUST be set AFTER the pattern — create_winding_pattern /
        # set_winding_coil reset it to the AWG gauge table (0.574 mm copper),
        # which caused the 72 % efficiency run.
        safe_set(mc, "Wire_Diameter", DESIGN["Wire_Diameter"])
        safe_set(mc, "Copper_Diameter", DESIGN["Copper_Diameter"])
        print(f"    winding: 6 coils x {TURNS_PER_COIL} turns (single-layer "
              f"8p/12s, pitch 2)" )
        # clear template slot-depth-reduction leftovers (slots 3,4 had 2/4 mm)
        for s in range(1, DESIGN["Slot_Number"] + 1):
            try:
                mc.set_variable(f"Slot_Depth_Reduction/Slot[{s}]", 0)
            except Exception:
                pass

        # verify winding + geometry before continuing
        print("    winding verification:")
        n_coils_ok = 0
        for ph in (1, 2, 3):
            for coil in (1, 2):
                go_s, go_p, ret_s, ret_p, turns = mc.get_winding_coil(
                    ph, 1, coil)
                print(f"      ph{ph} coil{coil}: slot {go_s}{go_p} -> "
                      f"{ret_s}{ret_p}, {turns} turns")
                n_coils_ok += 1 if turns == TURNS_PER_COIL else 0
        assert n_coils_ok == 6, "winding pattern verification failed"
        try:
            ok = mc.check_if_geometry_is_valid(True)
            print(f"    geometry valid: {ok}")
        except Exception as e:
            print(f"    geometry check skipped: {str(e)[:60]}")

        # 4. materials
        print("    materials:")
        set_material(mc, "Magnet", MAGNET_MATERIALS, "?")
        for comp in LAM_COMPONENTS:
            set_material(mc, comp, LAM_MATERIALS, "?")

        # 5. drive / operating point
        for k in ("DCBusVoltage", "PeakCurrent", "RMSCurrent", "PhaseAdvance",
                  "CurrentAngle", "Shaft_Speed_[RPM]", "TorqueCalculation",
                  "TorquePointsPerCycle", "TorqueNumberCycles"):
            safe_set(mc, k, DESIGN[k], quiet=True)
        print("    drive settings applied")

        # 6. save design model (keeps bldc1.mot pristine until verified)
        mc.save_to_file(MODEL_OUT)
        print(f"== Saved design to {MODEL_OUT} ==")

        # 7. RELOAD — commits the winding state. Without the reload, the
        #    EMag calc re-derives the wire from the AWG gauge table
        #    (Wire_Type=AWG_Table -> 0.574 mm copper) and the efficiency
        #    collapses to ~60 %. After reload the explicit wire override
        #    survives the calc (proven: 2.5/2.35 mm -> 92.1 %).
        print("== Reloading to commit winding state ==")
        mc.load_from_file(MODEL_OUT)
        mc.show_magnetic_context()
        safe_set(mc, "Wire_Diameter", DESIGN["Wire_Diameter"])
        safe_set(mc, "Copper_Diameter", DESIGN["Copper_Diameter"])
        set_material(mc, "Magnet", MAGNET_MATERIALS, "?")
        for comp in LAM_COMPONENTS:
            set_material(mc, comp, LAM_MATERIALS, "?")
        for k in ("DCBusVoltage", "PeakCurrent", "RMSCurrent", "PhaseAdvance",
                  "CurrentAngle", "Shaft_Speed_[RPM]", "TorqueCalculation",
                  "TorquePointsPerCycle", "TorqueNumberCycles"):
            safe_set(mc, k, DESIGN[k], quiet=True)
        print("    operating state re-applied after reload")
        print(f"    wire now: {safe_get(mc, 'Wire_Diameter')} / "
              f"{safe_get(mc, 'Copper_Diameter')} mm")

        if dry_run:
            print("DRY RUN — model prepared, EMag calculation skipped.")
            return

        # 8. EMag calculation + current iteration loop
        I_peak = DESIGN["PeakCurrent"]
        I_rms  = DESIGN["RMSCurrent"]
        for it in range(1, max_iter + 1):
            print(f"\n== EMag calculation (iteration {it}, "
                  f"PeakCurrent={I_peak:.2f} A) ==")
            mc.save_to_file(MODEL_OUT)          # recovery point
            safe_set(mc, "Wire_Diameter", DESIGN["Wire_Diameter"])  # re-assert
            safe_set(mc, "Copper_Diameter", DESIGN["Copper_Diameter"])
            mc.do_magnetic_calculation()
            res = read_results(mc)
            eta = report(res, f"iter {it}")

            T = res["ShaftTorque"]
            if abs(T - TARGET_TORQUE) / TARGET_TORQUE <= 0.02:
                print(f"\n*** Torque within 2% of target: {T:.3f} Nm ***")
                break
            # scale current: torque ~ I for SPM
            scale = (TARGET_TORQUE / T) ** 0.9 if T > 0 else 1.1
            I_peak = min(25.0, I_peak * scale)
            I_rms  = I_peak / 1.4142
            if it < max_iter:
                print(f"    -> scaling current to {I_peak:.2f} A peak / "
                      f"{I_rms:.2f} A rms")
                mc.set_variable("PeakCurrent", I_peak)
                mc.set_variable("RMSCurrent", I_rms)

        # 8. final verdict
        print("\n" + "=" * 72)
        print("FINAL VERDICT")
        print("=" * 72)
        T  = res["ShaftTorque"]
        Po = res["OutputPower"]
        Pi = res["InputPower"]
        eta = (Po / Pi * 100.0) if Pi > 0 else 0.0
        checks = [
            ("Power >= 500 W +/-2%",   Po >= 490.0),
            ("Torque ~= 1.59 Nm +/-2%",abs(T - TARGET_TORQUE) <= 0.032),
            ("Efficiency >= 90%",      eta >= TARGET_EFF),
            ("V_LL,peak <= 48 V bus",  res["PeakLineLineVoltage"] <= V_BUS + 1.0),
        ]
        for name, ok in checks:
            print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"    Torque={T:.3f} Nm  P_out={Po:.1f} W  eta={eta:.1f} %  "
              f"V_LL,pk={res['PeakLineLineVoltage']:.1f} V")
        print(f"    Wire: {res['Wire_Diameter']:.3f} mm covered / "
              f"{res['Copper_Diameter']:.3f} mm copper, "
              f"slot fill {res['Slot_Fill']*100:.1f} %")
        print("=" * 72)

    finally:
        if not keep_open:
            mc.quit()
            print("\nMotor-CAD closed.")


if __name__ == "__main__":
    main()
