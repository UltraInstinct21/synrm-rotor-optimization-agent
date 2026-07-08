---
type: motorcad_troubleshooting
name: "PyMotorCAD Troubleshooting"
purpose: "Common issues and solutions for PyMotorCAD automation"
source_files: ["Troubleshooting — pymotorcad-core.md", "Motor-CAD errors — pymotorcad-core.md"]
confidence: Verified
---

# PyMotorCAD Troubleshooting

## Common Issues

### UI Not Updated When Parameter Changed

**Symptom:** Motor-CAD GUI doesn't reflect parameter changes made via automation.

**Cause:** Motor-CAD skips UI updates during scripting for speed. Changing parameters shown on the currently displayed tab causes stale display.

**Fix:** Always display the Scripting tab before changing parameters:

```python
mc.display_screen("scripting")
```

### Error Messages Interrupting Script

**Symptom:** Motor-CAD dialogues pause or break automation scripts.

**Fix:** Disable popup messages:

```python
mc.set_variable("MessageDisplayState", 2)
```

**Warning:** This also suppresses critical prompts (save, overwrite, material reconciliation). Default actions are taken automatically.

**Retrieve message history:**

```python
num_messages = 100
messages = mc.get_messages(num_messages)
mc.clear_message_log()  # Clear after reading
```

Use `num_messages = 0` to retrieve all messages in history.

### Wrong Version of Motor-CAD Launches

**Symptom:** Automation connects to an unexpected Motor-CAD version.

**Cause:** Automation launches whichever version is registered as the default.

**Fix:** Check the Motor-CAD registration form to verify which version is registered as default.

## MotorCADError Exception

All Motor-CAD execution errors raise `MotorCADError`:

```python
import ansys.motorcad.core as pymotorcad

try:
    mc.do_magnetic_calculation()
except pymotorcad.MotorCADError:
    print("Calculation failed.")
```

## Related Pages

- [[motorcad/api/motorcad-errors]] — MotorCADError API reference
- [[motorcad/api/motorcad-api]] — MotorCAD constructor
- [[motorcad/overview/motorcad-setup]] — Initial setup
