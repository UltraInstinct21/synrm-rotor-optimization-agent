---
type: motorcad_workflow
name: "Mechanical Force Internal Scripting"
purpose: "Internal scripting example for force/NVH calculation with operating points"
prerequisites: ["Motor-CAD", "Lab model built"]
source_files: ["Mechanical force — pymotorcad-core.md"]
confidence: Verified
---

# Mechanical Force Internal Scripting

## Purpose

Demonstrate internal scripting for force/NVH calculation using the `mechanical_forces` class with operating point setup.

## Internal Script Pattern

```python
class mechanical_forces:
    def initial(self):
        mc.set_variable("MessageDisplayState", 2)

        # Set operating points (speed and torque)
        NVH_Duty_Speed = [250, 6000, 9000]
        NVH_Duty_Torque = [40, 20, 10]
        mc.set_variable("NumLoadPoints", len(NVH_Duty_Speed))

        for i in range(len(NVH_Duty_Speed)):
            mc.set_array_variable("LoadPoint_Speed_Array", i, float(NVH_Duty_Speed[i]))
            mc.set_array_variable("LoadPoint_Torque_Array", i, float(NVH_Duty_Torque[i]))

        # Set steps per cycle (30 minimum, 90+ recommended)
        mc.set_variable("TorquePointsPerCycle", 30)

    def final(self):
        # Get natural frequencies
        freq_mode_0 = mc.get_magnetic_graph_point("NVH_NaturalFrequency", 0)
        freq_mode_8 = mc.get_magnetic_graph_point("NVH_NaturalFrequency", 8)
        mc.show_message(" Natural_Freq_Mode_0 " + str(freq_mode_0))
        mc.show_message(" Natural_Freq_Mode_8 " + str(freq_mode_8))
        mc.set_variable("MessageDisplayState", 0)
```

## Key Notes

- Requires Lab model to be built first
- For IM: use `IMSingleLoadPointsPerCycle_Rotating` instead of `TorquePointsPerCycle`
- For IM operating points: use `LoadPoint_Current_Array` and `LoadPoint_Slip_Array`

## Related Pages

- [[motorcad/workflows/force-extraction-example]] — External force extraction
- [[motorcad/workflows/force-export-ansys-motion]] — Export for Ansys Motion
- [[motorcad/api/lab-methods]] — Lab model methods
