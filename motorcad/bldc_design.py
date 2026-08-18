#!/usr/bin/env python3
"""
bldc_design.py — Analytical design of a 500 W, 48 V, 3000 rpm BLDC motor
=========================================================================
Design from first principles (electrical machine theory, Pyrhönen / Gieras /
Boldea D^2*L sizing framework). Outputs the complete parameter set that is
then implemented in Ansys Motor-CAD by design_bldc.py.

Design decisions (confirmed with user):
  - Topology : 8-pole / 12-slot surface PM (SPM), concentrated double-layer
               winding, q = 0.5, winding factor k_w = 0.866
  - Magnet   : NdFeB N42 (B_r = 1.30 T @ 20 C, ~1.22 T @ 80 C operating)
  - Supply   : 48 V DC bus, sinusoidal (FOC) current drive
  - Speed    : 3000 rpm rated (f_e = 200 Hz)
  - Envelope : compact, rotor OD ~60 mm, stack ~45 mm

All quantities are computed from electrical theory. Run:  python bldc_design.py
"""

import math

# ---------------------------------------------------------------------------
# 1. RATINGS
# ---------------------------------------------------------------------------
P_OUT   = 500.0          # W   mechanical output
N_RPM   = 3000.0         # rpm rated speed
V_DC    = 48.0           # V   DC bus voltage
ETA_TGT = 0.90           # target efficiency (IEC-ish for this size class)

omega   = 2.0 * math.pi * N_RPM / 60.0          # rad/s
T_RATED = P_OUT / omega                          # Nm
P_IN    = P_OUT / ETA_TGT                        # W
I_DC    = P_IN / V_DC                            # A  mean DC current

# ---------------------------------------------------------------------------
# 2. POLE / SLOT COMBINATION
# ---------------------------------------------------------------------------
P = 8                 # poles
Q = 12                # slots
f_e = (P / 2) * N_RPM / 60.0                     # Hz electrical frequency
q_frac = Q / (3.0 * P)                           # slots / pole / phase = 0.5

# winding factor for concentrated double-layer 12s/8p (coil pitch = 1 slot
# = 120 degE -> pitch factor sin(60)=0.866, distribution factor = 1)
k_w = math.sin(math.radians(60.0))

# ---------------------------------------------------------------------------
# 3. MAGNETIC LOADING (N42, surface magnets)
# ---------------------------------------------------------------------------
B_r_20   = 1.30        # T  N42 remanence at 20 C
alpha_Br = 0.0012      # 1/K  Br temperature coefficient (N42)
T_mag    = 80.0        # C  assumed magnet operating temperature
B_r      = B_r_20 * (1.0 - alpha_Br * (T_mag - 20.0))   # ~1.23 T at 80 C

L_MAG    = 3.0e-3      # m  magnet radial thickness
GAP      = 0.5e-3      # m  mechanical airgap
MU_R     = 1.05        # relative recoil permeability of NdFeB

# airgap flux density, ideal reluctance model
B_g_ideal = B_r / (1.0 + MU_R * GAP / L_MAG)
K_LEAK    = 0.90       # leakage + Carter + saturation factor
B_g       = B_g_ideal * K_LEAK

# ---------------------------------------------------------------------------
# 4. SIZING  (T = tau_shear * pi/2 * D^2 * L)
# ---------------------------------------------------------------------------
D_ROTOR   = 64.0e-3    # m  rotor OD incl. magnets  (58 core + 2x3 magnet)
D_BORE    = D_ROTOR + 2.0 * GAP                   # 65 mm stator bore
D_CORE    = D_ROTOR - 2.0 * L_MAG                 # 58 mm rotor lamination core OD
L_STACK   = 45.0e-3    # m  axial stack length

A_lin     = 25.0e3     # A/m  electric loading (typical for small BLDC)
tau_shear = B_g * A_lin / 2.0                      # Pa
T_CAP     = tau_shear * (math.pi / 2.0) * D_ROTOR**2 * L_STACK

# check shear stress & sizing law
D2L_REQ   = T_RATED / (tau_shear * math.pi / 2.0)  # m^3
D2L_ACT   = D_ROTOR**2 * L_STACK

# pole pitch & flux per pole (fundamental)
TAU_P   = math.pi * D_ROTOR / P                    # m
PHI_1   = (2.0 / math.pi) * B_g * TAU_P * L_STACK  # Wb fundamental flux/pole

# ---------------------------------------------------------------------------
# 5. WINDING — turns from torque requirement
# ---------------------------------------------------------------------------
# PM flux linkage:  psi_pm = k_w * N_s * Phi_1
# Torque (SPM, id=0):  T = (3/2) * p * psi_pm * I_q_peak
I_PEAK_TARGET = 12.7        # A  peak phase current (9 A rms)
N_S = T_RATED / (1.5 * (P / 2) * k_w * PHI_1 * I_PEAK_TARGET)

# round to integer turns per coil (single-layer: 2 coils/phase, 6 coils total)
COILS_PER_PHASE = 2.0                    # single-layer 12s/8p (pitch 2)
TURNS_PER_COIL  = round(N_S / COILS_PER_PHASE)
N_S_FINAL       = TURNS_PER_COIL * COILS_PER_PHASE
COND_PER_SLOT   = TURNS_PER_COIL          # single layer: 1 coil side per slot

# ---------------------------------------------------------------------------
# 6. ELECTRICAL CHECKS
# ---------------------------------------------------------------------------
# back-EMF:  E_ph_rms = 4.44 * f * N_s * Phi_1 * k_w
E_PH_RMS = 4.44 * f_e * N_S_FINAL * PHI_1 * k_w
E_LL_RMS = math.sqrt(3.0) * E_PH_RMS

# phase resistance estimate (MLT ~ 2*(L + 2*coil_arc))
coil_arc   = math.pi * (D_BORE / 2.0 + 0.006) / 6.0   # ~ mean coil arc (6 = 12 slots/2)
MLT        = 2.0 * (L_STACK + 2.0 * coil_arc)
A_CU       = 2.5e-6                                   # m^2  ~1.8 mm dia copper
RHO_CU     = 1.68e-8                                  # ohm*m @ 20C (x1.25 @ 100C)
R_PH       = RHO_CU * MLT * N_S_FINAL / A_CU

# inductance estimate (cylindrical airgap, fundamental)
G_EFF    = GAP + L_MAG / MU_R
L_PH     = 1.5 * 4.0e-7 * math.pi * N_S_FINAL**2 * (math.pi * D_BORE * L_STACK) / (4.0 * (P/2)**2 * G_EFF) * k_w**2
X_L      = 2.0 * math.pi * f_e * L_PH

I_PH_RMS = I_PEAK_TARGET / math.sqrt(2.0)
V_PH_REQ = math.sqrt((E_PH_RMS + I_PH_RMS * R_PH)**2 + (I_PH_RMS * X_L)**2)
V_LL_REQ = math.sqrt(3.0) * V_PH_REQ

# ---------------------------------------------------------------------------
# 7. LOSSES & EFFICIENCY
# ---------------------------------------------------------------------------
P_CU   = 3.0 * I_PH_RMS**2 * R_PH                 # copper loss
P_FE   = 18.0                                     # W  iron loss @200Hz (est.)
P_LOSS = P_CU + P_FE
ETA    = T_RATED * omega / (T_RATED * omega + P_LOSS)

J       = I_PH_RMS / A_CU / 1.0e6                 # A/mm^2
V_TIP   = math.pi * D_ROTOR * N_RPM / 60.0        # rotor surface speed m/s

# ---------------------------------------------------------------------------
# 8. REPORT
# ---------------------------------------------------------------------------
def mm(x): return x * 1000.0

print("=" * 72)
print("500 W BLDC — ANALYTICAL DESIGN SUMMARY")
print("=" * 72)
print(f"RATINGS          P_out={P_OUT:.0f} W  n={N_RPM:.0f} rpm  T={T_RATED:.3f} Nm  "
      f"V_dc={V_DC:.0f} V")
print(f"                 P_in={P_IN:.0f} W  I_dc(mean)={I_DC:.1f} A  f_e={f_e:.0f} Hz")
print(f"TOPOLOGY         {P}-pole / {Q}-slot SPM  q={q_frac:.2f}  k_w={k_w:.3f}")
print(f"MAGNETIC         N42  B_r={B_r:.2f} T @{T_mag:.0f}C  l_m={mm(L_MAG):.1f} mm  "
      f"gap={mm(GAP):.2f} mm")
print(f"                 B_g(ideal)={B_g_ideal:.3f} T  B_g(design)={B_g:.3f} T")
print(f"SIZING           D_rotor(mag OD)={mm(D_ROTOR):.1f} mm  core={mm(D_CORE):.1f} mm  "
      f"D_bore={mm(D_BORE):.1f} mm  L_stack={mm(L_STACK):.0f} mm")
print(f"                 tau_shear={tau_shear/1000:.1f} kPa  T_cap={T_CAP:.2f} Nm  "
      f"(need {T_RATED:.2f})")
print(f"                 D^2*L req={D2L_REQ*1e6:.1f} cm^3  act={D2L_ACT*1e6:.1f} cm^3")
print(f"WINDING          N_s={N_S_FINAL:.0f} series turns/phase  "
      f"{TURNS_PER_COIL:.0f} turns/coil x {COILS_PER_PHASE:.0f} coils/ph  "
      f"{COND_PER_SLOT:.0f} conductors/slot (single-layer)")
print(f"                 R_ph~{R_PH*1000:.0f} mOhm  L_ph~{L_PH*1000:.2f} mH  "
      f"X_L~{X_L:.2f} Ohm  MLT={mm(MLT):.0f} mm")
print(f"CURRENT          I_ph,rms={I_PH_RMS:.1f} A  I_ph,peak={I_PEAK_TARGET:.1f} A  "
      f"J={J:.2f} A/mm2")
print(f"VOLTAGE          E_ph,rms={E_PH_RMS:.1f} V  E_LL,rms={E_LL_RMS:.1f} V  "
      f"V_LL,req={V_LL_REQ:.1f} V  (bus {V_DC:.0f} V)")
print(f"LOSSES           P_cu={P_CU:.1f} W  P_fe~{P_FE:.0f} W  total~{P_LOSS:.0f} W")
print(f"EFFICIENCY       eta~{ETA*100:.1f} %")
print(f"MECH             tip speed={V_TIP:.1f} m/s  (banding NOT required <15 m/s)")
print("-" * 72)
print("MOTOR-CAD VARIABLE TABLE")
print(f"  Pole_Number={P}  Slot_Number={Q}  BPMRotor=0 (Surface Radial)")
print(f"  Stator_Lam_Dia=105  Stator_bore={mm(D_BORE):.1f}  Stator_Lam_Length={mm(L_STACK):.0f}")
print(f"  RotorDiameter={mm(D_CORE):.0f}  Shaft_Dia=20  Rotor_Lam_Length={mm(L_STACK):.0f}")
print(f"  Airgap={mm(GAP):.1f}  Magnet_Thickness={mm(L_MAG):.0f}  Magnet_Arc_[ED]=140  "
      f"Magnet_Length={mm(L_STACK):.0f}")
print(f"  DCBusVoltage={V_DC:.0f}  PeakCurrent={I_PEAK_TARGET:.1f}  RMSCurrent={I_PH_RMS:.1f}")
print(f"  ConductorsPerSlot={COND_PER_SLOT:.0f}  ParallelPaths=1  PhaseAdvance=0  CurrentAngle=0")
print(f"  Shaft_Speed_[RPM]={N_RPM:.0f}")
print("=" * 72)
