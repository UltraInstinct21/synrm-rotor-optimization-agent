---
type: optimization_method
name: Design of Experiments
aliases: [DOE, experimental design]
topics: [optimization, statistical, screening]
confidence: Verified
---

# Design of Experiments (DOE)

## Overview

Statistical methods for planning experiments to efficiently explore design space and understand variable effects.

## Common DOE Types

| Type | Purpose | Runs |
|------|---------|------|
| Full factorial | All combinations | $k^n$ |
| Fractional factorial | Screen important factors | Reduced |
| Latin hypercube | Space-filling sampling | Custom |
| Taguchi | Robust design | Orthogonal arrays |
| Central composite | Response surface | $2^k + 2k + c$ |

## MotorCAD Application

- Initial screening of design variables
- Sensitivity analysis
- Response surface generation
- Input for surrogate-based optimization

## Related Pages

- [[optimization/bayesian_optimization]]
- [[optimization/pso]]
- [[optimization/nsga2]]
