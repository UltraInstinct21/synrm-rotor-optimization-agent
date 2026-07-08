---
type: research_paper
title: "Fast Analytical Synthesis of PM-Assisted Reluctance Synchronous Motors"
authors: ["Bianchi et al."]
year: 2016
venue: "IET Electric Power Applications"
motor_types: ["PMaSynRM", "PMAREL"]
topics: ["analytical synthesis", "design procedure", "sizing", "rotor barrier design", "PM insertion"]
tags: [pmasynrm, pmarel, analytical, synthesis, sizing, rotor-design, bianchi, iet]
source_file: "raw/papers/bianchi_2016_fast_synthesis_pmarel.pdf"
related_pages: ["[[pmasynrm-topology]]", "[[sizing-equation]]", "[[rotor-barrier-design]]"]
confidence: high
---

# Bianchi et al. (2016) — Fast Analytical Synthesis of PMaSynRM/PMAREL

## Citation

Bianchi, N. et al. (2016). "Fast analytical synthesis of PM-assisted reluctance synchronous motors." *IET Electric Power Applications*, 2016.

**Motor type:** Permanent Magnet Assisted Reluctance Synchronous Motor (PMaSynRM / PMAREL)
**Method:** Fast analytical synthesis procedure
**Scope:** From specifications to rotor geometry in a systematic step-by-step process

---

## Problem Statement

Designing a PMaSynRM requires determining both the **stator sizing** (from power/speed requirements) and the **rotor barrier geometry** (for saliency and torque optimization). Conventional design relies on iterative FEA, which is time-consuming. This paper provides a **fast analytical synthesis procedure** that systematically converts specifications into a complete motor geometry.

**Core question:** How can an engineer go from power/speed/torque specifications to a complete PMaSynRM geometry using only analytical equations, without initial FEA?

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | PMaSynRM / PMAREL |
| Rotor type | Interior multi-barrier with PM insertion |
| PM material | Ferrite (typical for PMaSynRM cost advantage) |
| Application | General purpose drive, traction |
| Design approach | Analytical synthesis (step-by-step) |
| Validation | FEA comparison after synthesis |

---

## Method / Theory — Synthesis Procedure

The synthesis procedure follows a **sequential design flow**:

### Step 1: Specify Requirements

Input specifications:
| Parameter | Symbol | Units |
|---|---|---|
| Rated power | P_rated | W |
| Rated speed | n_rated | RPM |
| Rated torque | T_rated | Nm |
| Maximum speed | n_max | RPM |
| DC bus voltage | V_dc | V |
| Target efficiency | η_target | % |
| Target power factor | PF_target | — |
| Cooling method | — | — |

### Step 2: Sizing — D²L Equation

The motor active volume is determined from the electromagnetic loading:

$$D^2 \cdot L = \frac{P_{rated}}{C_0 \cdot n_{rated}}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| D | Stator bore diameter | m |
| L | Stack length | m |
| C₀ | Machine constant (depends on loading, pole count, winding) | W·s/m³ |

The machine constant:

$$C_0 = \frac{\pi^3}{12\sqrt{2}} \cdot k_w \cdot B_{avg} \cdot A_{spec} \cdot \cos(\phi)$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| k_w | Winding factor | — |
| B_avg | Average airgap flux density | T |
| A_spec | Specific electric loading | A/m |
| cos(φ) | Power factor | — |

### Step 3: Electrical and Magnetic Loading Selection

**Specific electric loading (A_spec):**

$$A_{spec} = \frac{m \cdot N \cdot I}{\pi \cdot D}$$

Where:
- m = number of phases
- N = conductors per phase
- I = phase current (RMS)

Typical range: 30,000–80,000 A/m for industrial motors

**Specific magnetic loading (B_avg):**

$$B_{avg} = \frac{\Phi_{pole}}{A_{pole}}$$

Where:
- Φ_pole = flux per pole
- A_pole = pole face area

Typical range: 0.4–0.8 T for SynRM/PMaSynRM

### Step 4: Current Density Selection

$$J = \frac{I}{A_{cu}}$$

Where A_cu is the copper cross-sectional area per conductor.

Typical range: 4–10 A/mm² (natural convection) to 15–25 A/mm² (forced liquid cooling)

### Step 5: Airgap Determination

The airgap affects L_d and the magnetizing current:

$$g = k_g \cdot \sqrt[3]{D}$$

Where k_g is a design constant (typically 0.001–0.003 for small-medium motors).

Smaller airgap → higher L_d, better torque, but tighter manufacturing tolerance.

### Step 6: Number of Poles

Pole count selection based on speed and frequency:

$$f = \frac{p \cdot n}{60}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| f | Electrical frequency | Hz |
| p | Pole pairs | — |
| n | Speed | RPM |

**Constraint:** f ≤ f_max (typically 400–1000 Hz for lamination losses)

For n = 3000 RPM, f_max = 500 Hz:
- 2-pole: f = 50 Hz ✓
- 4-pole: f = 100 Hz ✓
- 6-pole: f = 150 Hz ✓
- 8-pole: f = 200 Hz ✓

### Step 7: Slot/Pole Combination

$$Q_s = 2 \cdot p \cdot m \cdot q$$

Where q = slots per pole per phase (typically 2, 3, or 4)

Common combinations:
| Poles | q | Slots |
|---|---|---|
| 4 | 3 | 36 |
| 4 | 4 | 48 |
| 6 | 3 | 54 |

### Step 8: Winding Design

- Concentrated vs distributed winding
- Series/parallel turns
- Wire gauge from current density and slot area

### Step 9: Rotor Barrier Geometry

This is the **key step** unique to PMaSynRM. The barrier parameters are determined from the required inductances:

$$L_d = \frac{N^2 \cdot k_w^2}{R_d(g, \text{barriers})}$$

$$L_q = \frac{N^2 \cdot k_w^2}{R_q(\text{bridges})}$$

Required saliency:

$$\xi_{required} = \frac{L_d}{L_q} = \frac{T_{required}}{\frac{3}{2} \cdot p \cdot i_d \cdot i_q}$$

### Step 10: PM Sizing and Insertion

PM volume is determined from the required PM flux linkage:

$$\lambda_{PM} = B_{PM} \cdot A_{PM} \cdot N_{turns}$$

Where:
- B_PM = remanent flux density of PM material
- A_PM = PM cross-sectional area
- N_turns = equivalent turns linking PM flux

### Step 11: Thermal Validation

Check that the selected current density and losses are within thermal limits:

$$T_{winding} = T_{ambient} + R_{th,total} \cdot P_{cu}$$

Where R_th,total is the total thermal resistance from winding to coolant.

---

## Key Design Equations — Synthesis Summary

### Power Equation

$$P_{rated} = T_{rated} \cdot \omega_{rated} = T_{rated} \cdot \frac{2\pi \cdot n_{rated}}{60}$$

### Torque Equation (PMaSynRM)

$$T = \frac{3}{2} \cdot p \cdot \left[(L_d - L_q) \cdot i_d \cdot i_q + \lambda_{PM} \cdot i_q\right]$$

The torque has two components:
1. **Reluctance torque** — (L_d - L_q) · i_d · i_q (from SynRM)
2. **PM torque** — λ_PM · i_q (from permanent magnets)

### Inductance from Geometry

$$L_d = \frac{3}{2} \cdot \frac{(N \cdot k_w)^2 \cdot \mu_0 \cdot D \cdot L}{g_{eff,d} \cdot K_{sat}}$$

$$L_q = \frac{3}{2} \cdot \frac{(N \cdot k_w)^2 \cdot \mu_0 \cdot D \cdot L}{g_{eff,q} \cdot K_{sat}}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| g_eff,d | Effective airgap for d-axis (includes barriers) | m |
| g_eff,q | Effective airgap for q-axis (includes barriers) | m |
| K_sat | Saturation factor | — |

### PM Flux Linkage

$$\lambda_{PM} = \frac{2}{\pi} \cdot B_{PM} \cdot l_{PM} \cdot w_{PM} \cdot N_{eq}$$

Where:
- l_PM = PM length in flux direction
- w_PM = PM width in flux direction
- N_eq = equivalent turns linking PM flux

### Efficiency

$$\eta = \frac{P_{out}}{P_{out} + P_{copper} + P_{iron} + P_{PM\_eddy} + P_{mech}} \times 100\%$$

---

## Key Design Insights

1. **Analytical synthesis provides a good starting point** — the step-by-step procedure yields a geometry that is within ~10–15% of the final optimized design, saving significant FEA time.

2. **D²L sizing is universal** — the same fundamental sizing equation applies to SynRM, PMaSynRM, and IPMSM, with the machine constant C₀ accounting for the motor type.

3. **Barrier geometry determines the reluctance torque share** — more barriers and thinner bridges increase the reluctance component relative to the PM component.

4. **PM insertion is optional but beneficial** — even a small amount of PM flux improves power factor and adds torque without significantly increasing cost (using ferrite).

5. **The synthesis procedure is iterative within itself** — some parameters (like current density) require thermal validation, which may require adjusting the D²L sizing.

6. **Winding factor matters** — the choice of slot/pole combination and winding distribution affects the machine constant and thus the motor size.

7. **Saturation must be accounted for** — the analytical model includes a saturation factor K_sat to correct for iron saturation at high flux densities.

---

## Limitations

- Analytical model assumes sinusoidal MMF and uniform airgap flux
- Saturation factor is an approximation — detailed FEA needed for accurate saturation
- End-winding effects not included in 2D synthesis
- Cogging torque not predicted by analytical model
- Manufacturing tolerances not considered
- PM demagnetization check requires separate analysis
- Thermal model is simplified — CFD or detailed thermal FEA may be needed for high-power designs

---

## Propagation into Wiki

### Concepts to update
- [[pmasynrm-topology]] — add analytical synthesis procedure context
- [[sizing-equation]] — add D²L sizing for PMaSynRM

### Equations to update
- [[sizing-equation]] — add complete D²L derivation with C₀
- [[torque-equation]] — add PMaSynRM torque with both reluctance and PM components
- [[inductance-equations]] — add effective airgap formulation

### Design guidelines to update
- [[rotor-barrier-design]] — add analytical barrier sizing procedure
- [[pmasynrm-barrier-design]] — create if not exists, add PMaSynRM-specific guidelines
- [[winding-design]] — add slot/pole selection guidelines

### MotorCAD pages to update
- [[motorcad/workflows/create-pmasynrm-model]] — add sizing inputs
- [[motorcad/variables/airgap]] — add effective airgap concept

---

## Related Pages

- [[pmasynrm-topology]] — PMaSynRM overview and advantages
- [[sizing-equation]] — motor sizing equations (D²L method)
- [[rotor-barrier-design]] — practical barrier design guidelines
- [[flux-barriers]] — flux barrier theory
- [[inductance-equations]] — inductance definitions and calculations
- [[winding-design]] — winding selection and design
- [[thermal-design]] — thermal considerations in motor design
