---
type: optimization_method
name: Particle Swarm Optimization
aliases: [PSO, swarm intelligence]
topics: [optimization, metaheuristic, population_based]
confidence: Verified
---

# Particle Swarm Optimization (PSO)

## Overview

Population-based metaheuristic inspired by bird flocking. Particles move through design space guided by personal best and global best positions.

## Key Concepts

- **Particles**: Design candidates with position and velocity
- **Personal best**: Best position found by each particle
- **Global best**: Best position found by any particle
- **Inertia weight**: Controls velocity decay

## Algorithm

```
for each particle:
    initialize position and velocity
    evaluate objective function
    set personal best = current position
    set global best = best among all particles

for each iteration:
    for each particle:
        update velocity using personal best and global best
        update position
        evaluate objective
        update personal best if improved
        update global best if improved
```

## MotorCAD Application

- Rotor barrier optimization
- Multi-parameter design studies
- Good for discrete and continuous variables

## Related Pages

- [[optimization/bayesian_optimization]]
- [[optimization/nsga2]]
- [[optimization/doe]]
