---
type: optimization_method
name: NSGA-II
aliases: [Non-dominated Sorting Genetic Algorithm II, multi-objective optimization]
topics: [optimization, multi_objective, evolutionary]
confidence: Verified
---

# NSGA-II

## Overview

Multi-objective evolutionary algorithm that finds a Pareto front of optimal trade-off solutions.

## Key Concepts

- **Pareto front**: Set of non-dominated solutions
- **Non-dominated sorting**: Rank solutions by dominance
- **Crowding distance**: Maintain diversity in objective space
- **Elitism**: Preserve best solutions across generations

## When to Use

- Multiple conflicting objectives (e.g., maximize torque, minimize ripple)
- Need trade-off solutions, not a single optimum
- Design space exploration

## MotorCAD Application

- Multi-objective SynRM optimization
- Torque vs. power factor trade-off
- Torque vs. torque ripple trade-off
- Efficiency vs. cost trade-off

## Related Pages

- [[optimization/bayesian_optimization]]
- [[optimization/pso]]
- [[optimization/doe]]
