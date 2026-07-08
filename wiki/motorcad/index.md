---
type: motorcad_index
name: "PyMotorCAD Wiki Index"
purpose: "Master index for all PyMotorCAD documentation pages"
confidence: Verified
---

# PyMotorCAD Wiki

Documentation for [PyMotorCAD](https://motorcad.docs.pyansys.com/) (ansys.motorcad.core) — the Python API for Ansys Motor-CAD electric motor design software.

## Overview

- [[motorcad/overview/getting-started]] — Installation, pip install, first steps
- [[motorcad/overview/motorcad-setup]] — Registration, parameter names, GUI, units
- [[motorcad/overview/backwards-compatibility]] — ActiveX to PyMotorCAD migration
- [[motorcad/overview/python-virtual-environment]] — venv setup for Motor-CAD
- [[motorcad/overview/contributing-pymotorcad]] — Dev install, testing, contributions
- [[motorcad/overview/matlab-scripting]] — PyMotorCAD in MATLAB

## API Reference

### Core

- [[motorcad/api/motorcad-api]] — `MotorCAD()` constructor
- [[motorcad/api/motorcad-compatibility-api]] — `MotorCADCompatibility()` constructor
- [[motorcad/api/motorcad-errors]] — `MotorCADError` exception
- [[motorcad/api/utility-functions]] — `set_default_instance`, `set_motorcad_exe`, `set_server_ip`

### Methods

- [[motorcad/api/general-methods]] — ~40 general methods (load, save, export, variable access)
- [[motorcad/api/calculations-methods]] — 15 calculation methods
- [[motorcad/api/lab-methods]] — 18 Lab model methods
- [[motorcad/api/graphs-methods]] — 12 graph retrieval methods

### Geometry

- [[motorcad/api/geometry-methods]] — Geometry validity checks and winding coil
- [[motorcad/api/geometry-objects-functions]] — Region, Line, Arc, Coordinate, EntityList
- [[motorcad/api/geometry-shapes]] — triangular_notch, square, eq_triangle
- [[motorcad/api/geometry-tree]] — GeometryTree (v2026R1+)
- [[motorcad/api/geometry-drawing-methods]] — draw_objects, draw_objects_debug
- [[motorcad/api/geometry-fitting-methods]] — return_entity_list

### Adaptive & FEA Geometry

- [[motorcad/api/adaptive-geometry-methods]] — 17 adaptive geometry methods
- [[motorcad/api/fea-geometry-methods]] — ~30 FEA geometry methods

### Scripting

- [[motorcad/api/internal-scripting-methods]] — load_script, run_script, save_script
- [[motorcad/api/emagnetic-methods]] — E-magnetic scripting pattern

## Workflows

### Adaptive Templates

- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/workflows/material-mesh-properties]] — Custom material and mesh
- [[motorcad/workflows/custom-dxf-geometry]] — DXF import workflow

### Geometry Examples

- [[motorcad/workflows/bezier-curve-rotor-pockets]] — Bezier curves for IPM pockets
- [[motorcad/workflows/curved-rotor-flux-barriers-syncrel]] — Curved barriers for SYNCREL
- [[motorcad/workflows/triangular-rotor-notches-ipm]] — Rotor notches for NVH
- [[motorcad/workflows/triangular-stator-notches]] — Stator notches for NVH
- [[motorcad/workflows/custom-magnet-angles-spm]] — Halbach array magnet angles
- [[motorcad/workflows/converting-im-tooth-bar]] — IM parallel to tapered tooth
- [[motorcad/workflows/round-parallel-slot-bottom]] — Round slot bottom corners
- [[motorcad/workflows/setting-material-close-slot]] — Close slot with material change

### Duct Modifications

- [[motorcad/workflows/oblong-stator-ducts]] — Oblong stator ducts + thermal correction
- [[motorcad/workflows/trapezoidal-ducts]] — Trapezoidal rotor ducts

### Thermal Analysis

- [[motorcad/workflows/thermal-steady-state]] — Steady-state thermal internal scripting
- [[motorcad/workflows/thermal-transient]] — Transient thermal internal scripting
- [[motorcad/workflows/thermal-example-script]] — Full thermal analysis script

### Mechanical Analysis

- [[motorcad/workflows/mechanical-stress-example]] — Stress internal scripting
- [[motorcad/workflows/mechanical-force-example]] — Force/NVH internal scripting
- [[motorcad/workflows/stress-post-processing]] — Neuber/Glinka corrections
- [[motorcad/workflows/stress-sampling-example]] — Bridge stress sampling

### Force & NVH

- [[motorcad/workflows/force-extraction-example]] — Force extraction and 2D FFT
- [[motorcad/workflows/force-export-ansys-motion]] — UNV/ANF export for Motion

### Twin Builder Integration

- [[motorcad/workflows/emag-twin-builder-ece]] — ECE model export for PMSM
- [[motorcad/workflows/thermal-twin-builder-rom]] — Thermal ROM component export

### Other

- [[motorcad/workflows/simple-parametric-sweep]] — 2D parametric sweep example
- [[motorcad/workflows/lab-model-example]] — Lab model build and calculation
- [[motorcad/workflows/motorcad-internal-scripting-tab]] — Scripting tab guide

## Troubleshooting

- [[motorcad/troubleshooting/troubleshooting]] — Common issues and solutions

## Legacy References

- Motor specs and constraints: `AGENTS.md`
- Reference motor model: `SynRM_45kW_IE5.mot`
- Existing optimizer: `optimize_synrm_v4.py`
