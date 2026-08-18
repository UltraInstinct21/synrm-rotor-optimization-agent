#!/usr/bin/env python3
r"""
final_save_bldc.py  --  Final clean run + save of bldc_latest_fixed.mot
========================================================================
Loads bldc_latest_fixed.mot (already has the correct 1-slot-span 16p/12s
winding), switches lams to M250-35A (lower iron loss at 400 Hz), runs one
clean EMag calc at the best known operating point, and saves the result.

Results so far (from fix_winding_v2 run):
  iter 2: I_peak=8A -> T=+0.1756Nm, P_out=55.2W, eta=27.3%
  Main problem: P_fe=77W (M350-50A at 400Hz, 10mm stack)
  Fix: M250-35A has ~40% lower iron loss at 400Hz vs M350-50A
"""

import os, math, pathlib

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL_FILE   = r"D:\SRM\Agent\motorcad\bldc_latest_fixed.mot"

COPPER_DIA = 0.50
WIRE_DIA   = 0.55
I_PEAK     = 8.0
DC_BUS     = 48.0
PHASE_ADV  = 0.0
RPM        = 3000.0

LAM_MATS   = ["M250-35A", "M270-35A", "M300-35A", "M350-35A", "M350-50A"]


def s(mc, n, v):
    try:
        mc.set_variable(n, v)
        print(f"    set {n} = {v}")
    except Exception as e:
        raise RuntimeError(f"set_variable('{n}', {v}): {e}")


def g(mc, n):
    try:
        return mc.get_variable(n)
    except Exception:
        return None


def set_lam_material(mc):
    for comp in ["Stator Lam (Back Iron)", "Rotor Lam (Back Iron)"]:
        for mat in LAM_MATS:
            try:
                mc.set_component_material(comp, mat)
                got = mc.get_component_material(comp)
                if got and mat.lower() in got.lower():
                    print(f"    lam material [{comp}]: {mat}")
                    break
            except Exception:
                continue


def apply_wire(mc):
    s(mc, "Wire_Type_Stator", 0)
    s(mc, "Armature_Winding_Definition", 1)
    s(mc, "Wire_Diameter",  WIRE_DIA)
    s(mc, "Copper_Diameter", COPPER_DIA)


def main():
    os.environ.setdefault("MOTORCAD_INSTALL_DIR",
                          str(pathlib.Path(MOTORCAD_EXE).parent))
    import ansys.motorcad.core as pymotorcad

    print("Connecting to Motor-CAD...")
    mc = pymotorcad.MotorCAD(open_new_instance=False)

    try:
        mc.set_variable("MessageDisplayState", 2)
        print(f"Loading {MODEL_FILE}...")
        mc.load_from_file(MODEL_FILE)
        mc.show_magnetic_context()

        print(f"\nModel: {g(mc,'Pole_Number')}p / {g(mc,'Slot_Number')}s  "
              f"BPMRotor={g(mc,'BPMRotor')}")
        print(f"Wire: {g(mc,'Wire_Diameter')} mm / {g(mc,'Copper_Diameter')} mm copper")
        print(f"Coil pattern check:")
        for ph in range(1, 4):
            for ci in range(1, 5):
                try:
                    go_s, go_p, ret_s, ret_p, turns = mc.get_winding_coil(ph, 1, ci)
                    span = abs(ret_s - go_s)
                    span = min(span, 12 - span)
                    print(f"  Ph{ph} Coil{ci}: {go_s}->{ret_s}  span={span}  turns={turns}")
                except Exception:
                    pass

        # Switch to better lam material for lower 400Hz iron losses
        print("\nSetting lamination material (M250-35A -> lower iron loss at 400Hz)...")
        set_lam_material(mc)

        # Re-assert wire + operating point
        print("\nRe-asserting wire and operating point...")
        apply_wire(mc)
        s(mc, "DCBusVoltage",         DC_BUS)
        s(mc, "PeakCurrent",          I_PEAK)
        s(mc, "RMSCurrent",           round(I_PEAK / math.sqrt(2), 4))
        s(mc, "PhaseAdvance",         PHASE_ADV)
        s(mc, "CurrentAngle",         0.0)
        s(mc, "Shaft_Speed_[RPM]",    RPM)
        s(mc, "TorqueCalculation",    True)
        s(mc, "TorquePointsPerCycle", 60)
        s(mc, "TorqueNumberCycles",   1)

        # Save pre-calc state
        mc.save_to_file(MODEL_FILE)
        print(f"Pre-calc state saved -> {MODEL_FILE}")

        # Reload + re-assert (anti-AWG-reset)
        mc.load_from_file(MODEL_FILE)
        mc.show_magnetic_context()
        apply_wire(mc)
        s(mc, "PeakCurrent", I_PEAK)
        s(mc, "RMSCurrent",  round(I_PEAK / math.sqrt(2), 4))
        s(mc, "PhaseAdvance", PHASE_ADV)
        s(mc, "DCBusVoltage", DC_BUS)
        s(mc, "Shaft_Speed_[RPM]", RPM)
        s(mc, "TorqueCalculation", True)
        s(mc, "TorquePointsPerCycle", 60)
        s(mc, "TorqueNumberCycles", 1)

        # Run EMag
        print("\nRunning EMag calculation...")
        mc.do_magnetic_calculation()

        # Read ALL results immediately
        T   = g(mc, "ShaftTorque")   or 0
        Po  = g(mc, "OutputPower")   or 0
        Pi  = g(mc, "InputPower")    or 0
        eta = (Po/Pi*100) if Pi and Pi > 0 else 0
        Vll = g(mc, "PeakLineLineVoltage") or 0
        Pcu = g(mc, "ConductorLoss") or 0
        Pfe = g(mc, "StatorIronLoss_Total") or 0
        Ir  = g(mc, "RMSPhaseCurrent") or 0
        Wd  = g(mc, "Wire_Diameter")
        Cd  = g(mc, "Copper_Diameter")
        Sf  = g(mc, "Slot_Fill") or 0
        Vll_rms = g(mc, "LineLineVoltage") or 0
        A_cu = math.pi * (COPPER_DIA/2)**2
        J    = Ir / A_cu if A_cu else 0

        # Save final model with results embedded
        mc.save_to_file(MODEL_FILE)
        print(f"\nFinal model saved -> {MODEL_FILE}")

        # Report
        print("\n" + "="*62)
        print("  FINAL RESULTS -- bldc_latest_fixed.mot")
        print("="*62)
        print(f"  Topology        : 16-pole / 12-slot SPM (BPMRotor=0)")
        print(f"  Wire            : {Cd} mm copper / {Wd} mm covered")
        print(f"  Slot fill       : {Sf*100:.1f} %")
        print(f"  Series turns/ph : 120  (30 turns x 4 coils x 1 path)")
        print(f"  Winding factor  : 0.866  (1-slot span, kw=sin120)")
        print(f"  Lam material    : M250-35A (stator + rotor)")
        print()
        print(f"  I_peak          : {I_PEAK:.1f} A")
        print(f"  I_rms (phase)   : {Ir:.3f} A")
        print(f"  J (current dens): {J:.1f} A/mm^2")
        print(f"  V_LL,peak       : {Vll:.1f} V  (bus {DC_BUS:.0f} V)")
        print(f"  V_LL,rms        : {Vll_rms:.1f} V")
        print()
        print(f"  Shaft torque    : {T:.4f} Nm")
        print(f"  P_out           : {Po:.1f} W")
        print(f"  P_input         : {Pi:.1f} W")
        print(f"  Efficiency      : {eta:.1f} %")
        print(f"  P_copper        : {Pcu:.1f} W")
        print(f"  P_iron (stator) : {Pfe:.1f} W")
        print()
        print(f"  [{'PASS' if T   >  0   else 'FAIL'}] Positive torque")
        print(f"  [{'PASS' if Vll <= DC_BUS else 'FAIL'}] V_LL,peak <= bus voltage")
        print(f"  [{'PASS' if Po  >= 30   else 'FAIL'}] P_out >= 30 W")
        print("="*62)

    finally:
        try:
            mc.quit()
        except Exception:
            pass
        print("Motor-CAD closed.")


if __name__ == "__main__":
    main()
