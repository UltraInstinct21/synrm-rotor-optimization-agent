"""Read-only probe: all parameters of bldc_latest.mot as stored on disk."""
import os, pathlib
import ansys.motorcad.core as pymotorcad

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL = r"D:\SRM\Agent\motorcad\bldc_latest.mot"

os.environ.setdefault("MOTORCAD_INSTALL_DIR", str(pathlib.Path(MOTORCAD_EXE).parent))
mc = pymotorcad.MotorCAD(open_new_instance=False)
mc.set_variable("MessageDisplayState", 2)
mc.load_from_file(MODEL)
mc.show_magnetic_context()

print("== TOPOLOGY ==")
for n in ["Pole_Number", "Slot_Number", "BPMRotor", "MagneticWindingType"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== STATOR GEOMETRY ==")
for n in ["Stator_Lam_Dia", "Stator_bore", "Stator_Lam_Length",
          "Tooth_Width", "Slot_Depth", "Slot_Opening",
          "Tooth_Tip_Depth", "Tooth_Tip_Angle", "Slot_Corner_Radius", "Housing_Dia"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== ROTOR GEOMETRY ==")
for n in ["RotorDiameter", "Shaft_Dia", "Rotor_Lam_Length", "Airgap",
          "Magnet_Thickness", "Magnet_Arc_[ED]", "Magnet_Length", "Banding_Thickness"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== WINDING DEFINITION ==")
for n in ["Wdg_Definition", "Armature_Winding_Definition", "Wire_Type_Stator",
          "WindingLayers", "MagPathType", "MagPhases", "NumberOfCoils",
          "ConductorsPerSlot", "ConductorsPerSlot_Total", "ParallelPaths",
          "Slot_Fill", "Wire_Diameter", "Copper_Diameter",
          "EWdg_Fill", "Liner_Thickness", "Winding_Type"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== WINDING COIL PATTERN ==")
try:
    n_phases = int(mc.get_variable("MagPhases"))
except Exception:
    n_phases = 3
try:
    n_coils = int(mc.get_variable("NumberOfCoils"))
except Exception:
    n_coils = 4

for ph in range(1, n_phases + 1):
    for coil in range(1, n_coils + 1):
        try:
            go_s, go_p, ret_s, ret_p, turns = mc.get_winding_coil(ph, 1, coil)
            print(f"  Phase {ph}  Coil {coil}: go=slot{go_s}{go_p}  ret=slot{ret_s}{ret_p}  turns={turns}")
        except Exception as e:
            print(f"  Phase {ph}  Coil {coil}: <ERR: {e}>")

print("\n== WINDING AREA OUTPUTS ==")
for n in ["Area_Copper", "Area_Covered_Wire", "GrossSlotFillFactor",
          "NetSlotFillFactor", "Slot_Fill_(Slot_Area)", "Wire_Ins_Thickness", "EWdg_MLT"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== DRIVE / OPERATING POINT ==")
for n in ["DCBusVoltage", "PeakCurrent", "RMSCurrent", "PhaseAdvance",
          "CurrentAngle", "Shaft_Speed_[RPM]", "TorqueCalculation",
          "TorquePointsPerCycle", "TorqueNumberCycles"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== LAST SAVED EMAG RESULTS (may be stale) ==")
for n in ["ShaftTorque", "OutputPower", "InputPower",
          "PhaseCurrent", "RMSPhaseCurrent",
          "PeakLineLineVoltage", "LineLineVoltage",
          "ConductorLoss", "StatorCopperLossAC",
          "StatorIronLoss_Total", "MotorEfficiency"]:
    try: print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e: print(f"  {n} = <ERR: {e}>")

print("\n== MATERIALS ==")
for comp in ["Magnet", "Stator Lam (Back Iron)", "Rotor Lam (Back Iron)", "Shaft", "Wire", "Housing"]:
    try: print(f"  {comp}: {mc.get_component_material(comp)}")
    except Exception as e: print(f"  {comp}: <ERR: {e}>")

mc.quit()
print("\nprobe done")
