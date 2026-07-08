---
type: optimization_method
name: Bayesian Optimization
aliases: [BO, Gaussian process optimization]
topics: [optimization, surrogate, black_box]
confidence: Verified
---

# Bayesian Optimization

## Overview

Sequential model-based optimization for black-box functions. Uses a surrogate model (typically Gaussian Process) to approximate the objective function and an acquisition function to decide where to sample next.

## Key Concepts

- **Surrogate model**: Approximates objective function
- **Acquisition function**: Guides sampling (EI, UCB, PI)
- **Exploration vs exploitation**: Balances trying new areas vs refining known good areas

## When to Use

- Expensive objective function (FEA simulations)
- Limited budget of evaluations
- Continuous design variables
- No gradient information available

## MotorCAD Application

- Rotor geometry optimization
- Multi-objective design (torque, ripple, PF)
- Parameter sensitivity analysis

## Related Pages

- [[optimization/pso]]
- [[optimization/nsga2]]
- [[optimization/doe]]
