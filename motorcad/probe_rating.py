"""Read-only probe: rating + materials of bldc1_design.mot as stored on disk."""
import os, pathlib
import ansys.motorcad.core as pymotorcad

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
MODEL = r"D:\SRM\Agent\motorcad\bldc1_design.mot"

os.environ.setdefault("MOTORCAD_INSTALL_DIR", str(pathlib.Path(MOTORCAD_EXE).parent))
mc = pymotorcad.MotorCAD(open_new_instance=True, use_blackbox_licence=True,
                         keep_instance_open=False)
mc.set_variable("MessageDisplayState", 2)
mc.load_from_file(MODEL)

print("== RATING (as stored in file) ==")
for n in ["Pole_Number", "Slot_Number", "Shaft_Speed_[RPM]", "PeakCurrent",
          "RMSPhaseCurrent", "DCBusVoltage", "PhaseAdvance",
          "WindingLayers", "ParallelPaths", "Wdg_Definition",
          "Armature_Winding_Definition", "Slot_Fill",
          "Wire_Diameter", "Copper_Diameter", "ConductorsPerSlot",
          "ShaftTorque", "OutputPower", "InputPower",
          "PeakLineLineVoltage", "MotorEfficiency",
          "Magnet_Length", "Magnet_Thickness", "Magnet_Arc_[ED]",
          "Stator_Lam_Dia", "Stator_bore", "Stator_Lam_Length",
          "RotorDiameter", "Airgap"]:
    try:
        print(f"  {n} = {mc.get_variable(n)}")
    except Exception as e:
        print(f"  {n} = <ERR {type(e).__name__}: {e}>")

print("\n== MATERIALS ==")
for comp in ["Magnet", "Stator Lam (Back Iron)", "Rotor Lam (Back Iron)",
             "Shaft", "Wire", "Housing"]:
    try:
        print(f"  {comp}: {mc.get_component_material(comp)}")
    except Exception as e:
        print(f"  {comp}: <ERR {type(e).__name__}: {e}>")

mc.quit()
print("\nprobe done")
