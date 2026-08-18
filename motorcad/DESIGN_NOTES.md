# 500 W BLDC Motor Design — Research & Design Record

**Date:** 2026-08-09 · **Target file:** `D:\SRM\Agent\motorcad\bldc1.mot`
**Design script:** `motorcad/bldc_design.py` (analytical) · `motorcad/design_bldc.py` (Motor-CAD implementation)

## 1. Requirements

| Item | Value |
|---|---|
| Output power | 500 W |
| Rated speed | 3000 rpm |
| Rated torque | T = P/ω = 500 / 314.16 = **1.59 Nm** |
| DC bus | 48 V |
| Efficiency target | ≥ 90 % (design goal ~93–95 %) |
| Drive | BLDC, sinusoidal (FOC) current drive |

## 2. Topology selection

For a 500 W class motor the dominant choices are brushed DC, BLDC (outrunner or
inrunner), and PMSM. BLDC with surface-mounted NdFeB magnets (SPM) wins on
power density, efficiency, and reliability (no brushes).

Pole/slot candidates at 3000 rpm (f_e = poles/2 × rpm/60):

| Poles | Slots | q = s/(3p) | f_e | Comment |
|---|---|---|---|---|
| 4 | 18 | 1.5 | 100 Hz | distributed-ish, longer end windings |
| 4 | 24 | 2.0 | 100 Hz | fine but bulky winding |
| **8** | **12** | **0.5** | **200 Hz** | **concentrated double-layer, k_w = 0.866, short end windings — chosen** |
| 8 | 18 | 0.75 | 200 Hz | unbalanced forces possible |
| 8 | 24 | 1.0 | 200 Hz | 24 coils, more copper, heavier |

**Chosen: 8-pole / 12-slot SPM, concentrated double-layer winding** — the classic
compact 500 W BLDC layout (small end-winding overhang, good fault tolerance,
q = 0.5 keeps cogging manageable with 140°ED magnet arc). Winding factor
k_w = sin(60°) = 0.866 (pitch factor; distribution factor = 1 for q = 0.5).

## 3. Magnetic loading (NdFeB N42)

N42: B_r = 1.30 T @ 20 °C, −0.12 %/K → B_r ≈ 1.22 T @ 80 °C.
Magnet thickness l_m = 3 mm, mechanical airgap g = 0.5 mm, μ_r ≈ 1.05.

Ideal reluctance model:

    B_g = B_r / (1 + μ_r·g/l_m) = 1.22 / (1 + 1.05·0.5/3) ≈ 1.03 T

Design value with leakage/Carter/saturation factor 0.9: **B_g ≈ 0.92 T**.
(2 mm magnets → 0.85 T; 4 mm → 1.03 T. 3 mm chosen as the cost/leakage sweet spot.)

## 4. Sizing (D²L law, shear-stress method)

Shear stress τ = B_g·A/2 with electric loading A = 25 kA/m (typical small BLDC):

    τ = 0.92 × 25000 / 2 = 11.5 kPa
    T = τ · (π/2) · D² · L

Dimensions chosen: rotor OD (incl. magnets) **64 mm**, rotor core **58 mm**,
stator bore **65 mm**, stack **45 mm**, airgap **0.5 mm**.

    T_cap = 11.5e3 · (π/2) · 0.064² · 0.045 = 3.3 Nm   (2.1× margin over 1.59 Nm)

## 5. Winding design

Torque equation (SPM, id = 0):  T = (3/2)·p·Ψ_pm·I_q,peak,  Ψ_pm = k_w·N_s·Φ_1

    Φ_1 = (2/π)·B_g·τ_p·L = 0.6366 · 0.92 · 0.0251 · 0.045 = 6.1e-4 Wb
    N_s = 1.59 / (1.5 · 4 · 0.866 · 6.1e-4 · 12.7) ≈ 36  series turns/phase

Winding: 12 slots, double layer → 4 coils/phase → **9 turns/coil → 18 conductors
per slot, 36 series turns per phase** (see note in §8 on the iteration result).

Back-EMF check (sinusoidal): E_ph,rms = 4.44·f·N_s·Φ_1·k_w = 18.4 V
→ E_LL,rms = 31.9 V < 48 V bus ✓ (34 % headroom for impedance drops).

## 6. Electrical operating point

| Quantity | Value |
|---|---|
| I_ph, rms | 9.0 A |
| I_ph, peak | 12.7 A |
| J (1.8 mm wire) | 3.6 A/mm² (low → high efficiency) |
| R_ph (est.) | ~41 mΩ |
| L_ph (est.) | ~0.08 mH → X_L ≈ 0.10 Ω |
| V_LL,peak required | ~33 V (bus 48 V) |
| P_cu | ~10 W (2 %) |
| P_fe @200 Hz (M250-35A, est.) | ~18 W |
| η (est.) | ~94.7 % |

## 7. Mechanical

- Rotor surface speed: π·0.064·3000/60 = **10.1 m/s** → retaining banding NOT
  required (rule of thumb: banding only above ~15–20 m/s). `Banding_Thickness = 0`.
- Shaft 20 mm, stack 45 mm, stator OD 105 mm, housing 110 mm.

## 8. Motor-CAD implementation & results

Implementation (`design_bldc.py`) converts the stock BPM-Therm template
(`bldc1.mot`) from Interior U-Shape IPM to Surface Radial SPM:

| Setting | Value |
|---|---|
| `BPMRotor` | 0 (Surface Radial) — verified in raw PyMotorCAD docs |
| `Pole_Number` / `Slot_Number` | 8 / 12 (+ `create_winding_pattern()`) |
| `Stator_Lam_Dia` / `Stator_bore` / `Stator_Lam_Length` | 105 / 65 / 45 mm |
| `RotorDiameter` / `Shaft_Dia` / `Airgap` | 58 / 20 / 0.5 mm |
| `Magnet_Thickness` / `Magnet_Arc_[ED]` / `Magnet_Length` | 3 / 140 / 45 |
| `ConductorsPerSlot` / `ParallelPaths` | 18 / 1 |
| Materials | Magnet **N42SH**, lams **M250-35A** (0.35 mm, low 200 Hz loss) |
| `DCBusVoltage` / `PeakCurrent` / `RMSCurrent` | 48 V / 12.7 A / 9.0 A |
| `PhaseAdvance` / `CurrentAngle` | 0 / 0 (SPM → MTPA at 0°) |
| `Shaft_Speed_[RPM]` | 3000 |

(Fill in from run log.) Final EMag results: torque ____ Nm, P_out ____ W,
η ____ %, V_LL,peak ____ V, wire ____ mm, fill ____ %.

**Verification targets:** T within ±2 % of 1.59 Nm · P_out ≥ 490 W ·
η ≥ 90 % · V_LL,peak ≤ 48 V.

## 10. Run 1 & 2 results — winding rework (2026-08-09)

**Run 1 (double-layer auto pattern, broken):** T = 1.57 Nm ✓ but η = 17.5 %,
V_LL,peak = 66.7 V — the auto 8p/12s pattern produced 100 turns/phase with
0.574 mm wire (fill 11.8 %), P_cu ≈ 2300 W.

**Run 2 (explicit single-layer pattern, 6 coils × 18 turns):** pattern verified
correct (A:(1,3)(4,6) · B:(5,7)(8,10) · C:(9,11)(12,2), all slots used), but
two problems remained:

| Issue | Root cause |
|---|---|
| Wire stuck at 0.574 mm copper (fill 4.2 %) | `Wire_Type=AWG_Table` + `Armature_Winding_Definition=2` — calc sizes wire from AWG gauge table (index 44), ignoring direct `Copper_Diameter` set |
| V_LL,peak = 88.4 V > 48 V bus | 36 series turns/phase → back-EMF ≈ 79.5 V at 3000 rpm (2.21 V/turn) |

Measured (run 2): T = 1.624 Nm ✓ (at 12.7 A pk), P_out = 510 W,
η = 72.7 % (165 W copper loss from thin wire), V_LL,peak = 88.4 V ✗.

**Fix (run 3):**
- Turns: 18 → **10 turns/coil** (20 series turns/phase) → back-EMF ≈ 44 V
  at 3000 rpm, fits 48 V bus with margin
- Wire: `Wdg_Definition=0` (Input_Slot_Fill) + `Slot_Fill=0.40` → Motor-CAD
  sizes wire ≈ 2.5 mm copper (slot ≈ 126 mm², 10 conductors/slot)
  → R_ph ≈ 11 mΩ → P_cu ≈ 8–10 W
- Current: 12.7 → ~22.5 A peak (T ∝ N·I; 20/36 × 36/20 keeps T = 1.59 Nm)
- Predicted η ≈ 93–94 % (P_cu ≈ 9 W + P_fe ≈ 21 W + windage/friction)

**Run 3 — CRITICAL GOTCHA (wire keeps reverting to 0.574 mm):**
`Wire_Type=AWG_Table` (`Armature_Winding_Definition=1` = "wire size" mode)
overrides any direct `Wire_Diameter`/`Copper_Diameter` set **when the calc
runs on a fresh session** — the calc re-derives the wire from the AWG gauge
table (index 44 → 0.574 mm copper). Result: η collapses to ~60 %, P_cu ≈ 300 W.

**FIX (verified):** after applying the full design and `save_to_file`, **reload
the model** (`load_from_file`), then re-apply wire + materials + drive settings.
After the reload the explicit wire override survives the EMag calc. In the
iteration loop, re-assert `Wire_Diameter`/`Copper_Diameter` before every
`do_magnetic_calculation()`.

## 11. FINAL VERIFIED RESULTS (run 3, 2026-08-09)

```
FINAL VERDICT (iteration 2)
    [PASS] Power >= 500 W +/-2%      500.9 W
    [PASS] Torque ~= 1.59 Nm +/-2%   1.595 Nm
    [PASS] Efficiency >= 90%         92.0 %
    [PASS] V_LL,peak <= 48 V bus     41.6 V
    Wire: 2.500 mm covered / 2.350 mm copper, slot fill 40.0 %
    PeakCurrent 22.47 A  RMSPhaseCurrent 15.89 A
    ConductorLoss 17.1 W  StatorIronLoss 21.5 W
    RotorIronLoss 0.87 W  MagnetLoss 3.9 W
```

Loss breakdown: P_cu 17.1 + P_fe 21.5 + P_rotor 0.9 + P_mag 3.9 ≈ 43 W
at 501 W output → η = 92.0 %. Model saved as `bldc1_design.mot`.

## 9. References

- Wikipedia: Brushless DC electric motor; Motor constants (K_t = 60/(2π·K_v))
- Pyrhönen, Jokinen, Hrabovcová — *Design of Rotating Electrical Machines* (D²L sizing)
- Gieras — *Permanent Magnet Motor Technology*
- Ansys Motor-CAD raw PyMotorCAD example scripts (`workspace/raw/pymotorcad_markdown/`)
- Motor-CAD parameter database (`workspace/wiki/motorcad/parameter_database/`)
