# AGENTS.md — General Motor Design Agent

> This agent is machine-general: it works with ANY machine type and rating.
> All project-specific numbers (targets, bounds, locked params, operating
> point) come from the ACTIVE PROJECT FOLDER — never from this file.
> Active project resolution: `$MOTOR_PROJECT` > `workspace/projects/active.json`
> > `workspace/specs/active.json` (legacy) > example template.
> Use `/project list` to see projects, `/project new <slug>` to create one,
> `/project use <slug>` to switch. Numbers in docs, wiki, or examples are
> illustrative only and are ALWAYS overridden by the active project's
> `spec.json`.

Read this entire file before writing any code.

---

## Project Setup

Each project lives in its own folder:

```
workspace/projects/<slug>/
├── spec.json       # targets, param bounds, constraints, locked list, operating point
├── ledger.jsonl    # scored CANDIDATE_RESULT log (append-only)
├── scratch/        # generated run scripts for this project
├── models/         # .mot files and backups (e.g. best_so_far.mot)
└── README.md       # project notes
```

A `synrm_45kw` example template ships under `workspace/specs/` for
reference. New machines start as a new project folder (`/project new`),
not by editing this file.

---

## Operating Point

Never hardcode speeds, control angles, or torque options. Read them from
the active project's `spec.json` (`operating_point`) and apply them in
every script. If a control variable name (e.g. current / voltage) is not
already verified, discover it via the parameter database first — never
invent variable names.

---

## Optimization Strategy

Motor-CAD solves are expensive (each EMag calc can take ~60–90 seconds),
so use a two-phase approach:

**Phase 1 — Coarse sweep (seeded Latin Hypercube or grid)**
- Sample ~20–50 points across the spec bounds
- Run the solver for each candidate
- Record the scored outputs (torque, power, efficiency, power factor, ...)
- Identify the top candidates from the project ledger

**Phase 2 — Local refinement**
- Start from the best Phase 1 candidate in the ledger
- Perturb each variable ±one step, keep changes that improve the scored
  objective from `score_motor_result`
- Repeat until the spec's convergence helper reports convergence

### Objective

Never hand-compute spec compliance. Call `validate_motor_params` BEFORE
every solve and `score_motor_result` AFTER every solve. The scorer owns
the objective (lower is better) and pass/fail.

### Results Logging

Every iteration must be logged immediately after the calculation — Motor-CAD
results are lost if the model is changed before reading them. Generated
scripts print one JSON line per evaluated candidate:

```
CANDIDATE_RESULT: {"params": {...}, "results": {"torque": ..., "input_power_w": ..., "speed_rpm": ..., ...}}
```

The execution wrapper auto-logs and auto-scores these lines into the
active project's `ledger.jsonl`. Resume from the ledger, not from stdout
history. Sweep sampling MUST use the seeded `src.motor.sweep` helpers so
runs are reproducible.

---

## Script Structure to Follow

```
<project scratch>/run_*.py
│
├── connect_motorcad()          — launch + load the project .mot model
├── discover_variables()        — run once at startup, print all var names
├── verify_fixed_params()       — assert spec locked params unchanged
├── set_candidate_params(params)— apply one candidate's geometry
├── check via validate_motor_params — validate before solving (no hand-rolled asserts)
├── run_emag()                  — show_magnetic_context → do_magnetic_calculation
├── read_results()              — read ALL outputs immediately after the solve
├── score via score_motor_result — computed compliance, never eyeballed
└── main()                      — orchestrate full workflow
```

---

## Motor-CAD Connection

```python
import os
import ansys.motorcad.core as pymotorcad

MOTORCAD_EXE = os.environ.get("MOTORCAD_EXE", r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe")
MODEL_FILE = ...  # the active project's .mot file (see project README / /project show)

def connect_motorcad():
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
| Load model | `mc.load_from_file(path)` |
| Close instance | `mc.quit()` |

---

## Common Result Variable Names (pre-verified, no search needed)

`ShaftTorque`, `InputPower`, `OutputPower`, `Shaft_Speed_[RPM]`,
`PhaseAdvance`, `TorquePointsPerCycle`, `TorqueNumberCycles`,
`TorqueCalculation`, `DCBusVoltage`, `PeakLineLineVoltage`,
`StatorCopperLossAC`, `StatorIronLoss_Total`, `T_[Winding_Min]`,
`T_[Winding_Max]`, `T_[Winding_Average]`.

**For any variable not in this list: search `workspace/wiki/motorcad/parameter_database` using `wiki_tool`. Never guess variable names or run trial-and-error solver loops.**

---

## Mandatory Parameter Database Search & Navigation

When writing any script, any unknown or unverified Motor-CAD parameters MUST be searched in the parameter database located at:
`workspace/wiki/motorcad/parameter_database/`

### How to Navigate `workspace/wiki/motorcad/`:
1. **Parameter Database (`workspace/wiki/motorcad/parameter_database/`)**:
   - `index.md`: Master index listing all Motor-CAD parameters across categories.
   - `categories/`: Category breakdown files (e.g., `Dimensions.md`, `Magnetics.md`, `Calc_Options.md`, `Airgap.md`, `Thermal.md`, `Winding.md`, `FEA_Settings.md`, `Mechanical.md`, `Losses_At_RPM_Ref.md`). Read a category file to discover all related parameters for a subsystem.
   - `parameters/<ParameterName>.md`: Direct detail specification files for exact parameter names, data types, read/write permissions, default values, units, and descriptions.
   - `data_types/` & `reports/`: Data types and coverage audit reports.
2. **Motor-CAD Code & API Function Reference (`workspace/wiki/motorcad/`)**:
   - `index.md`: Knowledge base index.
   - `workflow.md`: Standard Motor-CAD simulation workflow steps.
   - `parameters.md` & `result_fields.md`: Common design inputs and output result metrics.
   - **PyMotorCAD API Docs (`pymotorcad-*.md`)**:
     - `pymotorcad-getting-started.md`: Connection & initialization (`ansys.motorcad.core.MotorCAD`).
     - `pymotorcad-calculations-api.md`: Solvers & calculation methods (`do_magnetic_calculation`, `do_steady_state_analysis`, `show_magnetic_context`, etc.).
     - `pymotorcad-geometry-basic.md` / `objects.md` / `drawing.md` / `shapes.md` / `tree.md`: Geometry creation, drawing, shapes, and tree manipulation.
     - `pymotorcad-adaptive-geometry.md` & `pymotorcad-adaptive-templates-guide.md`: Adaptive template manipulation.
     - `pymotorcad-curved-flux-barriers.md` & `pymotorcad-bezier-rotor-pockets.md`: Rotor flux barrier definitions and Bezier pocket geometry.
     - `pymotorcad-emag-example.md` & `pymotorcad-thermal-example.md` & `pymotorcad-thermal-steady-state.md` & `pymotorcad-thermal-transient.md`: Full script execution examples for EMag & Thermal calculations.
     - `pymotorcad-lab-api.md` & `pymotorcad-lab-model-example.md`: Motor-LAB API functions and operating point calculations.
     - `pymotorcad-graphs-api.md` & `pymotorcad-force-extraction.md` & `pymotorcad-stress-postprocessing.md`: Post-processing graphs, forces, and stress extraction.
     - `pymotorcad-errors.md` & `pymotorcad-troubleshooting.md`: Exception handling and debugging.

---

## Anti-Hallucination Rules — CRITICAL

Motor-CAD variable names are exact internal strings. Wrong names cause silent
wrong results or exceptions with no indication of which variable failed.

### Rule 1 — Search parameter database before writing script

First check `workspace/wiki/motorcad/parameter_database/parameters/<ParameterName>.md` using `wiki_tool` or `grep`.

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

### Rule 4 — Always save before changing params

Save a backup of the current best model (in the active project's
`models/` folder) before applying the next candidate, so you can always
recover the best result found so far.

### Rule 5 — Read all results before changing any parameter

Motor-CAD results refer to the last calculation. Read everything you need
before calling `set_variable()` for the next iteration.

---

## Filesystem & Deletion Policy

- The agent has full filesystem access (absolute paths allowed). Prefer
  project-relative paths (`workspace/projects/<slug>/...`) so work stays
  inside the active project folder.
- Generated scripts may only write to the active project's `scratch/` and
  `models/` folders, `workspace/experiments/`, or explicit model backup
  paths. Destructive primitives (`shutil`, `os.remove/unlink/rmdir`,
  `subprocess`, network, `eval/exec/__import__`) are blocked in generated
  code by the safety scan.
- Deleting ANY file goes through the HITL-gated `delete_file` tool (human
  approval required every time). Never bypass it with generated code.

---

## Motor-CAD Version

Ansys Motor-CAD path is environment-specific — set `MOTORCAD_EXE`
(or use the default install path) rather than relying on a fixed version
string here.
