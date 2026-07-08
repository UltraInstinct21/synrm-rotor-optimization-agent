---
title: Motor Design Engineering Wiki
created: 2026-07-06
updated: 2026-07-06
type: index
---

# Motor Design Engineering Wiki

> Persistent engineering knowledge base for SynRM design, simulation, optimization, and MotorCAD automation.

## How to Use This Wiki

1. Start here to navigate
2. Follow `[[wikilinks]]` to related pages
3. Check [[log]] for recent activity
4. Raw sources live in `raw/` — never edit them

---

## Topologies

| Page | Motor Type | Status |
|------|-----------|--------|
| [[topologies/synrm]] | Synchronous Reluctance Motor | Active |
| [[topologies/pmasynrm]] | PM-Assisted SynRM | Planned |
| [[topologies/ipmsm]] | Interior PM Synchronous Motor | Planned |
| [[topologies/spm]] | Surface PM Motor | Planned |
| [[topologies/induction_motor]] | Induction Motor | Planned |
| [[topologies/srm]] | Switched Reluctance Motor | Planned |
| [[topologies/bldc]] | Brushless DC Motor | Planned |

---

## Concepts

- [[concepts/saliency_ratio]] — Ld/Lq ratio and its role in torque production
- [[concepts/reluctance_torque]] — Torque from magnetic anisotropy
- [[concepts/torque_ripple]] — Periodic torque variation and mitigation
- [[concepts/power_factor]] — PF in SynRM and improvement methods
- [[concepts/magnetic_loading]] — Airgap flux density considerations
- [[concepts/electric_loading]] — Current density and ampere-conductor distribution
- [[concepts/saturation]] — Magnetic saturation effects in rotor/stator
- [[concepts/iron_loss]] — Core loss mechanisms and models
- [[concepts/copper_loss]] — Winding loss and thermal implications
- [[concepts/dq_theory]] — d-q reference frame for SynRM analysis

---

## Equations

- [[equations/torque_synrm]] — Electromagnetic torque expression
- [[equations/d2l_sizing]] — D²L sizing equation
- [[equations/current_density]] — Current density formulation
- [[equations/saliency_ratio_eq]] — Saliency ratio definition
- [[equations/airgap_flux_density]] — Airgap flux density relations
- [[equations/carter_coefficient]] — Slot opening correction factor
- [[equations/loss_models]] — Iron and copper loss models

---

## Design Guidelines

- [[design_guidelines/stack_length]] — Stack length selection and tradeoffs
- [[design_guidelines/rotor_diameter]] — Rotor diameter considerations
- [[design_guidelines/airgap]] — Airgap selection
- [[design_guidelines/barrier_design]] — Flux barrier geometry and optimization
- [[design_guidelines/bridge_design]] — Mechanical bridge sizing
- [[design_guidelines/rib_design]] — Rib thickness and saturation
- [[design_guidelines/slot_selection]] — Slot/pole combinations
- [[design_guidelines/pole_selection]] — Pole count effects
- [[design_guidelines/current_density_limits]] — Thermal and electromagnetic limits
- [[design_guidelines/flux_density_limits]] — Saturation thresholds

---

## Heuristics

- [[heuristics/low_pf_diagnosis]] — Diagnosing and fixing low power factor
- [[heuristics/saliency_improvement]] — Practical saliency improvement strategies
- [[heuristics/torque_ripple_reduction]] — Torque ripple reduction patterns
- [[heuristics/barrier_tuning_rules]] — Barrier geometry tuning heuristics

---

## MotorCAD

- [[motorcad/overview/motorcad_overview]] — MotorCAD modules and workflow fit
- [[motorcad/api/index]] — PyMotorCAD API reference pages
- [[motorcad/variables/index]] — MotorCAD variable mappings
- [[motorcad/workflows/index]] — Operational workflow guides
- [[motorcad/outputs/index]] — Output interpretation guides
- [[motorcad/troubleshooting/index]] — Known issues and fixes

---

## Research Papers

- [[research/papers/nagarkar_optimized_rotor_synrm]] — Optimized rotor design for torque (Nagarkar 2021)
- [[research/papers/bianchi_fast_synthesis_pmasynrm]] — Fast PMaSynRM synthesis (Bianchi 2016)
- [[research/papers/aghazadeh_external_rotor_synrm]] — External rotor SynRM sizing (Aghazadeh 2019)
- [[research/papers/bridgeless_rotor_synrm]] — Bridgeless rotor for SynRM (2025)
- [[research/papers/topology_optimization_synrm]] — Topology optimization for SynRM
- [[research/papers/optimal_rotor_current_angle]] — Optimal rotor considering current angle
- [[research/papers/optimal_rotor_srm]] — Optimal rotor design for SRM
- [[research/papers/design_torque_ripple_reduction_srm]] — SRM torque ripple reduction
- [[research/papers/design_rotors_srm_analytical]] — SRM rotor analytical treatment
- [[research/papers/pmasynrm_design]] — PMaSynRM design methodology
- [[research/papers/synrm_drive_design]] — SynRM drive design (IEEE)
- [[research/papers/reliable_design_pmasynrm]] — Reliable PMaSynRM design
- [[research/papers/review_high_speed_synrm]] — High-speed SynRM rotor review
- [[research/papers/metamodel_optimization_synrm]] — Metamodel-based SynRM optimization
- [[research/papers/overview_high_efficiency_synrm]] — High-efficiency SynRM overview (Li 2023, DOI: 10.30941/CESTEMS.2023.00030)
- [[research/papers/synrm_iit_madras]] — SynRM coursework (IIT Madras)
- [[research/papers/ee6703_synrm_unit1]] — SynRM lecture notes
- [[research/papers/irset_synrm]] — IRSET SynRM paper
- [[research/papers/jamnani_icam2021]] — Jamnani IC-AM2 2021
- [[research/papers/synrm_barrier_review_2025]] — SynRM barrier design review (2025)

---

## Optimization

- [[optimization/bayesian_optimization]] — Bayesian optimization methods
- [[optimization/pso]] — Particle swarm optimization
- [[optimization/nsga2]] — Multi-objective NSGA-II
- [[optimization/doe]] — Design of experiments

---

## Projects

- [[projects/45kW_SynRM/overview]] — 45kW SynRM design project

---

## Templates

- [[templates/paper_summary_template]]
- [[templates/equation_template]]
- [[templates/concept_template]]
- [[templates/motorcad_variable_template]]
- [[templates/motorcad_workflow_template]]
- [[templates/motorcad_api_template]]
- [[templates/experiment_template]]
- [[templates/failure_template]]
- [[templates/decision_template]]

---

## Software

- [[software/pymotorcad]] — PyMotorCAD usage notes
- [[software/numpy]] — NumPy for motor design
- [[software/scipy]] — SciPy optimization tools

---

## References

- [[references/boldea]] — Boldea textbook
- [[references/pyrhonen]] — Pyrhonen textbook
- [[references/motorcad_manual]] — MotorCAD manual
- [[references/pymotorcad_docs]] — PyMotorCAD official docs
