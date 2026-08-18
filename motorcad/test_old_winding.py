"""
test_old_winding.py  --  Compare old (3-slot span) vs new (1-slot span) winding
==================================================================================
Loads bldc_latest_fixed.mot (correct geometry, BPMRotor=0, M250-35A),
applies the OLD 3-slot-span winding pattern from the original bldc_latest.mot,
runs EMag, prints results, and does NOT save -- so bldc_latest_fixed.mot is safe.

Old pattern (from original bldc_latest.mot probe):
  Ph1: 1->4, 4->7, 7->10, 10->1   (span=3)
  Ph2: 9->12, 12->3, 3->6, 6->9   (span=3)
  Ph3: 5->8, 8->11, 11->2, 2->5   (span=3)
"""
import os, math, pathlib

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL_FILE   = r"D:\SRM\Agent\motorcad\bldc_latest_fixed.mot"

COPPER_DIA = 0.50
WIRE_DIA   = 0.55
I_PEAK     = 8.0
DC_BUS     = 48.0
RPM        = 3000.0

# Old 3-slot-span coil table (phase, go_slot, ret_slot)
OLD_COILS = [
    (1, 1,  4), (1, 4,  7), (1, 7, 10), (1, 10,  1),
    (2, 9, 12), (2, 12, 3), (2, 3,  6), (2,  6,  9),
    (3, 5,  8), (3, 8, 11), (3, 11, 2), (3,  2,  5),
]

def s(mc, n, v):
    mc.set_variable(n, v)

def g(mc, n):
    try: return mc.get_variable(n)
    except: return None

def apply_wire(mc):
    s(mc, "Wire_Type_Stator", 0)
    s(mc, "Armature_Winding_Definition", 1)
    s(mc, "Wire_Diameter",   WIRE_DIA)
    s(mc, "Copper_Diameter", COPPER_DIA)

def apply_old_pattern(mc):
    mc.set_variable("MagneticWindingType", 2)
    mc.set_variable("MagPathType",   0)
    mc.set_variable("MagPhases",     3)
    mc.set_variable("WindingLayers", 2)
    mc.set_variable("NumberOfCoils", 4)
    coil_idx = {1: 1, 2: 1, 3: 1}
    for ph, go_s, ret_s in OLD_COILS:
        mc.set_winding_coil(ph, 1, coil_idx[ph],
                            go_s, "C", ret_s, "C", 30)
        span = abs(ret_s - go_s)
        span = min(span, 12 - span)
        print(f"  Ph{ph} Coil{coil_idx[ph]}: {go_s}->{ret_s}  span={span}")
        coil_idx[ph] += 1
    s(mc, "ParallelPaths",     1)
    s(mc, "ConductorsPerSlot", 60)

def run_and_report(mc, label):
    apply_wire(mc)
    s(mc, "PeakCurrent",          I_PEAK)
    s(mc, "RMSCurrent",           round(I_PEAK / math.sqrt(2), 4))
    s(mc, "PhaseAdvance",         0.0)
    s(mc, "CurrentAngle",         0.0)
    s(mc, "DCBusVoltage",         DC_BUS)
    s(mc, "Shaft_Speed_[RPM]",    RPM)
    s(mc, "TorqueCalculation",    True)
    s(mc, "TorquePointsPerCycle", 60)
    s(mc, "TorqueNumberCycles",   1)

    print(f"\nRunning EMag [{label}]...")
    mc.do_magnetic_calculation()

    T   = g(mc, "ShaftTorque")   or 0
    Po  = g(mc, "OutputPower")   or 0
    Pi  = g(mc, "InputPower")    or 0
    eta = (Po/Pi*100) if Pi and Pi > 0 else 0
    Vll = g(mc, "PeakLineLineVoltage") or 0
    Pcu = g(mc, "ConductorLoss") or 0
    Pfe = g(mc, "StatorIronLoss_Total") or 0
    return dict(T=T, Po=Po, Pi=Pi, eta=eta, Vll=Vll, Pcu=Pcu, Pfe=Pfe)


import time
os.environ.setdefault("MOTORCAD_INSTALL_DIR",
                      str(pathlib.Path(MOTORCAD_EXE).parent))
import ansys.motorcad.core as pymotorcad

print("Connecting to Motor-CAD (retrying up to 120 s)...")
mc = None
for attempt in range(40):
    try:
        mc = pymotorcad.MotorCAD(open_new_instance=False)
        print(f"  Connected on attempt {attempt+1}")
        break
    except Exception as e:
        print(f"  Attempt {attempt+1}: not ready ({e!s:.60}) -- retrying in 3s")
        time.sleep(3)
if mc is None:
    raise RuntimeError("Motor-CAD did not become available within 120 s")

try:
    mc.set_variable("MessageDisplayState", 2)
    mc.load_from_file(MODEL_FILE)
    mc.show_magnetic_context()
    print(f"Loaded: {g(mc,'Pole_Number')}p/{g(mc,'Slot_Number')}s  BPMRotor={g(mc,'BPMRotor')}")

    # --- Apply OLD 3-slot pattern ---
    print("\nApplying OLD winding (3-slot span, kw~0):")
    apply_old_pattern(mc)

    old = run_and_report(mc, "OLD 3-slot span")

    # --- Restore NEW 1-slot pattern ---
    print("\n\nRestoring NEW winding (1-slot span, kw=0.866):")
    NEW_COILS = [
        (1, 1,  2), (1, 4,  5), (1, 7,  8), (1, 10, 11),
        (2, 2,  3), (2, 5,  6), (2, 8,  9), (2, 11, 12),
        (3, 3,  4), (3, 6,  7), (3, 9, 10), (3, 12,  1),
    ]
    mc.set_variable("MagneticWindingType", 2)
    mc.set_variable("WindingLayers", 2)
    mc.set_variable("NumberOfCoils", 4)
    coil_idx = {1:1, 2:1, 3:1}
    for ph, go_s, ret_s in NEW_COILS:
        mc.set_winding_coil(ph, 1, coil_idx[ph], go_s, "C", ret_s, "C", 30)
        span = abs(ret_s - go_s); span = min(span, 12 - span)
        print(f"  Ph{ph} Coil{coil_idx[ph]}: {go_s}->{ret_s}  span={span}")
        coil_idx[ph] += 1
    s(mc, "ParallelPaths",     1)
    s(mc, "ConductorsPerSlot", 60)

    new = run_and_report(mc, "NEW 1-slot span")

    # --- Side-by-side comparison ---
    print("\n" + "="*62)
    print("  WINDING COMPARISON  (same geometry, same I_peak=8A)")
    print("="*62)
    print(f"  {'Parameter':<22} {'OLD (3-slot)':<18} {'NEW (1-slot)':<18}")
    print(f"  {'-'*58}")
    print(f"  {'Coil span':<22} {'3 slots (kw~0)':<18} {'1 slot (kw=0.866)':<18}")
    print(f"  {'Shaft Torque':<22} {old['T']:.4f} Nm         {new['T']:.4f} Nm")
    print(f"  {'P_out':<22} {old['Po']:.1f} W           {new['Po']:.1f} W")
    print(f"  {'Efficiency':<22} {old['eta']:.1f} %           {new['eta']:.1f} %")
    print(f"  {'V_LL,peak':<22} {old['Vll']:.1f} V           {new['Vll']:.1f} V")
    print(f"  {'P_copper':<22} {old['Pcu']:.1f} W           {new['Pcu']:.1f} W")
    print(f"  {'P_iron':<22} {old['Pfe']:.1f} W           {new['Pfe']:.1f} W")
    print("="*62)
    print(f"  Torque improvement: {new['T']/old['T']:.1f}x" if old['T'] != 0 else
          "  Old torque was zero/negative -- infinite improvement")
    print(f"  NOTE: bldc_latest_fixed.mot NOT overwritten (restored to new pattern)")
    print("="*62)

finally:
    try: mc.quit()
    except: pass
    print("Motor-CAD closed.")
