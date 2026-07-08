# An Optimized Rotor Design of Synchronous Reluctance Motor for Improved Torque Characteristics

Atul Nagarkar\* *IEEE, Student Member Department of Electrical Engineering Indian Institute of Technology, Madras* Chennai, India 600036 Email: <sup>∗</sup> ee19s023@smail.iitm.ac.in

Srirama Srinivas<sup>+</sup> *IEEE, Member Department of Electrical Engineering Indian Institute of Technology, Madras* Chennai, India 600036 Email: <sup>+</sup>srsrini12@ee.iitm.ac.in

*Abstract*—Permanent Magnet Synchronous Motors (PMSM) are known to be preferred over other motors in electric vehicle (EV) application. However, due to over-dependence of expensive rare-earth magnets in these motors, lookout for alternate motors is on the anvil. In this paper, an optimized rotor design of Synchronous Reluctance Motor (SynRM) that is devoid of rareearth materials is proposed in order to demonstrate its suitability in the EV category. Firstly, an analytical design method to determine the dimension of the stator and rotor structure of the SynRM is introduced. Without altering the stator design, an optimized design of rotor structure using the unit-less variables is proposed in this paper with the dual aim of maximizing the electromagnetic torque of the SynRM and minimizing torque ripple in it. Finite element analysis (FEA) is used to verify the analytical design and optimization of the rotor structure. The results of the SynRM design and optimization are presented to showcase the effectiveness of the envisaged design methodology.

*Index Terms*—Electric vehicle, synchronous reluctance motor, finite element analysis, design, optimization.

# I. INTRODUCTION

The demand for electric motors is increasing rapidly in the electric vehicle (EV) and a hybrid electric vehicle (HEV) due to the trend of electrification of vehicles in automotive industry. The permanent magnet synchronous motor (PMSM), especially the interior permanent magnet (IPM) motor with buried rare-earth permanent magnets, is ideal candidate in many EVs and HEVs because it offers high torque density and efficiency [1]–[3]. However, high price and availability of rare-earth permanent magnets (PMs) has become a matter of concern in automotive application. This has motivated researchers into investigations of alternative machine designs and topologies that reduce or eliminate the use of rare-earth content from machines. On such potential candidate is Synchronous Reluctance Motor (SynRM). The major advantage of SynRM is that it is a rare-earth magnet free motor, hence reduced cost.

The disadvantage of the SynRM are high torque ripple and low torque density. In order to address these two issues, many efforts have been made to optimize the rotor geometry [4]– [7]. By adopting an optimal composition of PMs within the

![](_page_0_Picture_9.jpeg)

Fig. 1. d and q axes definition in SynRM [10].

flux barriers can improve torque density, power factor and efficiency [8], [9].

SynRM has complex rotor structure, which increases the number of rotor design variables involved in its design to seek optimal performance. The large number of variables makes optimization difficult. Several analytical and finite element analysis methods on the design and optimization of SynRM are reported in [11]–[15], but the mutual effects of multiple geometrical parameters were not explored in detail.

This paper introduces unit-less parameters for studying the mutual effects of SynRM rotor geometries and proposes an alternative design methodology to illustrate the torque performance variation over its rotor geometric space. These unit-less parameters are further used to optimize the rotor geometry with an aim of achieving both high and smooth torque. The optimal torque performance and geometrical parameters were determined by the use of a genetic algorithm (GA) [16], [17]. The copper loss and volume are kept constant during the optimization. To accurately consider the iron saturation and non-linearity effects, FEA is used in this paper.

#### II. SYNCHRONOUS RELUCTANCE MOTOR MODEL

A 2D sectional view of a SynRM along with its d and q axes definition is shown in Fig. 1. The SynRM operates on the principle of differences of reluctances in d and q axes to produce the torque. It is similar to the conventional salient pole synchronous motor with excitation winding removed from its rotor. Hence, eliminating both the field winding and damper winding equations from Park's equations [15], the d-q equations for a synchronous reluctance machine can be obtained as follows:

$$V_{ds} = r_s I_{ds} + \frac{d\lambda_{ds}}{dt} - w_e \lambda_{qs} \tag{1}$$

$$V_{qs} = r_s I_{qs} + \frac{d\lambda_{qs}}{dt} + w_e \lambda_{ds}$$
 (2)

$$\lambda_{ds} = L_{ls}I_{ds} + L_{md}I_{ds} = L_dI_{ds} \tag{3}$$

$$\lambda_{qs} = L_{ls}I_{qs} + L_{mq}I_{qs} = L_qI_{qs} \tag{4}$$

$$I_{ds} = \sqrt{2}I_s\cos(\gamma), I_{as} = \sqrt{2}I_s\sin(\gamma) \tag{5}$$

where  $L_{md}$ ,  $L_{mq}$ ,  $L_{ls}$ ,  $r_s$  and  $w_e$  are direct axis magnetizing inductance, quadrature axis magnetizing inductance, stator leakage inductance, stator resistance per phase and speed of rotor, respectively. The d and q axes components of stator voltage are  $V_{ds}$  and  $V_{qs}$  respectively whereas  $I_{ds}$  and  $I_{qs}$  are d and q axes components of stator current  $(I_s)$  respectively.  $\gamma$  is phase angle between  $I_{ds}$  and  $I_{qs}$ .

The expression of electromagnetic torque of SynRM is given as [18]:

$$T_e = \frac{3}{2} \frac{P}{2} (\lambda_{ds} I_{qs} - \lambda_{qs} I_{ds}) - \frac{\partial W_{mc}(I_{ds}, I_{qs}, \vartheta_m)}{\partial \vartheta_m}$$
 (6)

where P is the number of poles,  $\vartheta_m$  is rotor position and  $W_{mc}$  is magnetic co-energy. The magnetic co-energy variation averages to zero for a single rotor rotation. So, this term is usually ignored for determining average torque.

#### III. ANALYTICAL DESIGN PROCEDURE

The specifications of the machine to be designed are listed in Table I. The number of poles are four since the higher number of poles reduce the reluctance torque. Table II shows the assigned parameters of SynRM.

For the M19 steel, the flux densities chosen for the stator teeth  $(B_{ts})$  and core  $(B_{cs})$  are 1.6 T and 1.5 T respectively, and for the rotor core  $(B_{cr})$  is 1.4 T.

### A. Stator Design

The stator design of SynRM is based on  $D_o^3 L_{sk}$  sizing expressions in [19]. The ratio of inner to outer diameter of stator is given by (7) [20] as:

$$\frac{D_{is}}{D_o} = \frac{b}{a} + \frac{2K_s}{ak_{cu}J_sD_o} \pm \sqrt{\left(\frac{b}{a} + \frac{2K_s}{ak_{cu}J_sD_o}\right)^2 - \frac{1}{a}}$$
 (7)

where,

$$a = (G_t + G_c)^2 - (1 - G_t)^2, b = G_t + G_c$$
 (8)

TABLE I SYNRM MACHINE SPECIFICATION

| Parameter               | Symbol    | Quantity |
|-------------------------|-----------|----------|
| Rated Power             | $P_n$     | 7.5 HP   |
| Rated Torque            | $T_n$     | 35.6 Nm  |
| Rated Speed             | $N_r$     | 1500 rpm |
| Rated Current           | $I_s$     | 11.8 A   |
| Number of poles         | P         | 4        |
| Number of slots         | $S_1$     | 36       |
| Number of phases        | m         | 3        |
| Rated Line-Line Voltage | $V_{L-L}$ | 415 V    |

TABLE II ASSIGNED PARAMETERS

| Parameter                                | Symbol   | Quantity              |
|------------------------------------------|----------|-----------------------|
| Stator outer diameter (frame IEC132)     | $D_o$    | 208 mm                |
| Maximum fundamental air gap flux density | $B_{g1}$ | 0.78 T                |
| Maximum flux density in stator teeth     | $B_{ts}$ | 1.6 T                 |
| Maximum flux density in stator core      | $B_{cs}$ | 1.5 T                 |
| Maximum flux density in rotor core       | $B_{cr}$ | 1.4 T                 |
| Stack aspect ratio                       | λ        | 1.5                   |
| Current Density                          | $J_s$    | 4.5 A/mm <sup>2</sup> |
| Surface Current density                  | $K_s$    | 25 A/mm               |
| Winding Factor                           | $k_w$    | 0.945                 |
| Copper slot fill factor                  | $k_{cu}$ | 0.4                   |
| Coefficient of E.m.f                     | $K_E$    | 0.97                  |
| Stacking factor                          | $k_{is}$ | 0.95                  |

$$G_t = \frac{B_{g1}}{B_{ts}k_{is}}, G_c = \frac{2}{P} \frac{B_{g1}}{B_{cs}k_{is}}$$
(9)

The stack length is obtained from aspect ratio and pole pitch  $(\tau)$  whereas air gap length (g) is calculated by (11) [21]

$$\tau = \frac{\pi D_{is}}{P}, L_{sk} = \lambda \tau \tag{10}$$

$$g = 0.2 + 2\sqrt{D_{is}L_{sk}} (11)$$

The stator slot geometry is shown in Fig. 2. The stator teeth, slot, core dimensions can be obtained from (12)-(15) [19]

$$t = \frac{\pi D_{is} B_{g1}}{S_1 B_{ts} k_{is}}, t_y = \frac{D_{is} B_{g1}}{P B_{cs} k_{is}}$$
(12)

$$b_{s1} = \frac{\pi}{S_1} [D_{is}(1 - G_t) + 2(h_{s0} + h_{s1})]$$
 (13)

$$b_{s2} = \frac{\pi}{S_1} [D_o - D_{is}(G_t + G_c) - 2r]$$
 (14)

$$h_{s2} = (b_{s2} - b_{s1}) \frac{S_1}{2\pi} \tag{15}$$

To minimise air gap ripple, the smallest possible dimensions for the slot opening is chosen. As a result,  $b_o = 2$ mm,  $h_{s0} = 1$ mm, and  $h_{s1} = 1$ mm in this paper. The stator has distributed type winding as in the conventional induction motor.

The useful slot area  $(A_s)$ , conductor area  $(A_{cu})$  and number of turns per phase  $(N_1)$  can be obtained from (16)-(18) [19].

![](_page_2_Picture_0.jpeg)

Fig. 2. Stator Geometry.

$$A_s = \frac{h_{s2}(b_{s1} + b_{s2})}{2} + (b_{s2} - c_1 r)r \tag{16}$$

$$A_{cu} = A_s k_{cu} \tag{17}$$

$$N_1 = \frac{K_E V_{L-L} P}{4.44 f k_w 2 D_{is} L_{sk} B_{g1} \sqrt{3}}$$
 (18)

where,

$$c_1 = \frac{4 - \pi}{2} \tag{19}$$

### *B. Rotor Design*

The number of barriers per pole is decided first. In [5], relationship between number of stator slots (ns) and rotor slots (nr) per pole pair is presented and is give by (20)

$$n_r = n_s \pm 4 \tag{20}$$

Since the stator has 36 slots, the rotor should have 22 or 14 rotor slots per pole pair from (20). This means the rotor must have three flux barriers or four flux barriers per pole. Due to large number of variables and low mechanical strength, three flux barrier rotor is selected in this paper. The torque ripple can be calculated by following formula:

$$T_{rip} = \frac{T_{max} - T_{min}}{T_{avg}} \times 100 \tag{21}$$

where Tavg(= Tn), Tmax, Tmin are the average, maximum, minimum values of electromagnetic torque (Te) respectively.

The torque produced by SynRM is proportional to the difference of the inductances (Ld-Lq). This means rotor structure should be designed to increase the flux along d aixs and decrease the flux along q-axis (Fig. 1 and Fig. 3). The flux barriers in these figures are also called fluid barriers, inspired from the flux lines which would flow if the rotor were a solid rotor [22] [23]. But these fluid barriers are difficult to manufacture and has less mechanical strength. To avoid the complexity, the geometry of flux barriers shown in Fig. 4 is adopted in this paper.

This paper introduces six parameters (β<sup>w</sup>ri , β<sup>d</sup>bj , β<sup>θ</sup>b<sup>1</sup> , β<sup>θ</sup>b(j+1) , β<sup>w</sup>b<sup>1</sup> , β<sup>w</sup>b(j+1) ) which can be easily set to design the shape of flux barriers similar to the fluid flux barriers. To complete the rotor geometry two additional parameters (wr1, db1) are introduced. The unit-less variables for changing the shape of flux barriers are as follows:

$$\beta_{w_{ri}} = \frac{w_{r(i+1)}}{w_{ri}} \tag{22}$$

$$\beta_{d_{bj}} = \frac{d_{b(j+1)}}{d_{bj}} \tag{23}$$

$$\beta_{\theta_{b1}} = \frac{\theta_{b1}}{(\pi/P)} \tag{24}$$

$$\beta_{\theta_{b(j+1)}} = \frac{\theta_{b(j+1)}}{\theta_{bj}} \tag{25}$$

$$\beta_{w_{b1}} = \frac{w_{b1}}{(D_{sh}/2) + w_{r1}} \cot\left(\frac{\pi}{P}\right)$$
 (26)

$$\beta_{w_{b(j+1)}} = \frac{w_{b(j+1)}}{w_{bj}} \tag{27}$$

where, i varies from 1 to 3 and j varies from 1 to 2. The expressions of (wr1, db1) will be derived and presented in Section IV. The geometrical parameters considering three flux barriers in rotor is shown in Fig. 4. The rotor outer (Dr) and inner diameter (Dsh) are calculated using (28) and (29) respectively.

$$D_r = D_{is} - 2g (28)$$

$$D_{sh} = D_r - 2(w_{r1} + w_{r2} + w_{r3} + w_{r4} + d_{b1} + d_{b2} + d_{b3})$$
(29)

![](_page_2_Picture_25.jpeg)

Fig. 3. Fluid flux barrier in SynRM [23].

![](_page_2_Picture_27.jpeg)

Fig. 4. Geometrical parameters of 3 flux barriers in rotor.

## IV. INITIAL DESIGN EVALUATION AND VERIFICATION

In this section, the dimensions of stator geometry obtained in Section III is used for initial design. The dimensions of rotor geometry is obtained by assigning values to unit-less variables as per Table III. To derive the expressions of wr<sup>1</sup> and db1, two important set of coefficients Kair,r and Kair,s [18] are introduce in this paper. These coefficients are given in (30) and (31) respectively, where p<sup>s</sup> is the stator slot pitch (32). The values of both these coefficients Kair,r and Kair,s must be close to each other to keep the machine equally saturated [18].

$$K_{air,r} = \frac{d_{b1} + d_{b2} + d_{b3}}{d_{b1} + d_{b2} + d_{b3} + w_{r1} + w_{r2} + w_{r3} + w_{r4}}$$
 (30)

$$K_{air,s} = \frac{p_s - t}{p_s} \tag{31}$$

$$p_s = \frac{\pi D_{is}}{S_1} \tag{32}$$

The coefficient Kair,r is set equal to Kair,s ,i.e, 0.48. The parameter db<sup>1</sup> can be derived using Kair,r and (22)-(27). The flux per pole (φp) in the rotor can be expressed as in (34) with an assumption that flux flowing into the rotor is equal to flux flowing out of the rotor. The equation of wr<sup>1</sup> can be derived by substituting value of φ<sup>p</sup> and expressing in terms of unit-less parameters.

$$d_{b1} = \frac{K_{air,r}}{1 - K_{air,r}} \frac{w_{r1} + w_{r2} + w_{r3} + w_{r4}}{1 + \beta_{d_{b1}} + \beta_{d_{b1}} \beta_{d_{b_2}}}$$
(33)

$$\phi_p = 2(w_{r1} + w_{r2} + w_{r3} + w_{r4})B_{cr}L_{sk}k_{is}$$
 (34)

$$w_{r1} = \frac{B_{g1}D_{is}}{B_{cr}Pk_{is}(1 + \beta_{w_{r1}} + \beta_{w_{r1}}\beta_{w_{r2}} + \beta_{w_{r1}}\beta_{w_{r2}}\beta_{w_{r3}})}$$
(35)

$$\phi_p = \frac{2B_{g1}D_{is}L_{sk}}{P} \tag{36}$$

The parameter bec<sup>i</sup> is set equal to slot opening (bo) to minimize torque ripple [24]. The calculated design parameters and initial values of unit-less variables are shown in Table III. The 2D Finite Element Analysis (FEA) is used to verify the analytical design procedure presented in Section III. The variation of air gap flux density and magnetic flux density distribution is shown in Fig. 5 and 6 respectively, at stator current phase angle (γ) of 69◦ . By analysing the results shown in Fig. 5 and 6, the flux density in air gap (Bg1), stator teeth (Bts), stator core (Bcs) and rotor core (Bcr) are 0.82 T, 1.65 T, 1.55 T, 1.5 T respectively.

Also, Tavg of 34.42 Nm and Trip of 39.13% is obtained at rated speed of 1500 rpm.

# V. PARAMETRIC SENSITIVITY STUDY

The parametric sensitivity study is carried out to show the influence of the variation of the rotor geometrical parameters on the SynRM torque production . The stator, air gap and rotor dimensions are fixed and equal to the values given in Table II and III. For example, if β<sup>θ</sup>b<sup>2</sup> , β<sup>θ</sup>b<sup>3</sup> , and β<sup>θ</sup>b<sup>1</sup> are varied other parameters are as per Table II and III.

TABLE III CALCULATED DIMENSION AND INITIAL VALUES OF SYNRM

| Symbol | Value     | Symbol   | Value     |
|--------|-----------|----------|-----------|
| Dis    | 129.8 mm  | Acu      | 58.68 mm2 |
| τ      | 101.94 mm | N1       | 144       |
| Lsk    | 153 mm    | βdbj     | 1         |
| g      | 0.5 mm    | βwri     | 1         |
| t      | 5.8 mm    | βθbi     | 1         |
| ty     | 17.8 mm   | βwbi     | 0.7       |
| bs1    | 5.9 mm    | wr1      | 4.76 mm   |
| bs2    | 9.1 mm    | db1      | 5.86 mm   |
| hs2    | 18.4 mm   | r        | 1 mm      |
| As     | 146.7 mm2 | wtr, wrr | 1 mm      |

![](_page_3_Figure_16.jpeg)

Fig. 5. Air-gap flux density distribution.

![](_page_3_Figure_18.jpeg)

Fig. 6. Magnetic flux density distribution.

## *A. Influence of flux barrier angle on torque production*

The effect of barrier angle is discussed in this section by varying β<sup>θ</sup>b<sup>2</sup> and β<sup>θ</sup>b<sup>3</sup> in a range between 0.8 to 1.3 with step size of 0.1. The value of β<sup>θ</sup>b<sup>1</sup> is fixed at 0.8, 1, and 1.3 for Case 1, 2 and 3 respectively. For Case 1, it can be seen from Fig. 7 that β<sup>θ</sup>b<sup>2</sup> = 1.2 and β<sup>θ</sup>b<sup>3</sup> = 1.3, provides maximum average torque (33.06 Nm) whereas β<sup>θ</sup>b<sup>2</sup> = β<sup>θ</sup>b<sup>3</sup> = 0.8 provides minimum torque ripple (53.74%). For Case 2 in Fig. 8, β<sup>θ</sup>b<sup>2</sup> = 1.3 and β<sup>θ</sup>b<sup>3</sup> = 1.3, provides maximum average torque (35.71 Nm) whereas β<sup>θ</sup>b<sup>2</sup> = 1.2 and β<sup>θ</sup>b<sup>3</sup> = 0.8 provides minimum torque ripple (23.84%). For Case 3 in Fig. 9, β<sup>θ</sup>b<sup>2</sup> = 1.1 and β<sup>θ</sup>b<sup>3</sup> = 1.2, provides maximum average torque (35.73 Nm) whereas β<sup>θ</sup>b<sup>2</sup> = 1.2 and β<sup>θ</sup>b<sup>3</sup> = 1.1 provides minimum torque ripple (11.74%).

The maximum value of average torque for Case 1 is 33.06 Nm. This value increases to 35.71 Nm for Case 2 and 35.73 Nm for Case 3. This variation is mainly due to the fact that wider flux barriers allow easy path to d-axis flux but when magnetic saturation sets in especially around flux barrier ribs average torque cannot increase further.

From above analysis, we can say that maximum average torque and minimum torque ripple can be achieved by keeping wider flux barriers.

![](_page_4_Figure_2.jpeg)

Fig. 7. Case 1: The influence of barrier angle on (a) Average torque (b) Torque ripple.

![](_page_4_Figure_4.jpeg)

Fig. 8. Case 2: The influence of barrier angle on (a) Average torque (b) Torque ripple.

# *B. Influence of flux barrier width and length on torque production*

In this section, the influence of the width and length of flux barrier on average torque and torque ripple is studied. The influence of width of flux barrier is discussed first. The variables β<sup>d</sup>b<sup>1</sup> and β<sup>d</sup>b<sup>2</sup> are varied in a range between

![](_page_4_Figure_8.jpeg)

Fig. 9. Case 3: The influence of barrier angle on (a) Average torque (b) Torque ripple.

![](_page_4_Figure_10.jpeg)

Fig. 10. Case 1: The influence of width of flux barrier on (a) Average torque (b) Torque ripple.

0.5 to 1 with step size of 0.1. The width db<sup>1</sup> is fixed at 4mm and 6mm for Case 1 and 2 respectively. For Case 1 in Fig. 10, β<sup>d</sup>b<sup>1</sup> = 1 and β<sup>d</sup>b<sup>2</sup> = 0.9 provides maximum average torque (33.81 Nm) whereas β<sup>d</sup>b<sup>1</sup> = β<sup>d</sup>b<sup>2</sup> = 1 provides minimum torque ripple (50.18%). For Case 2 in Fig. 11, β<sup>d</sup>b<sup>1</sup> = 0.8 and β<sup>d</sup>b<sup>2</sup> = 1 provides maximum average torque (34.53 Nm) whereas β<sup>d</sup>b<sup>1</sup> =β<sup>d</sup>b<sup>2</sup> = 1 provides minimum torque ripple (39.95%). Thus, in general, by increasing width of flux barriers along q-axis increases torque. This is primarily due to an increase in q-axis magnetic reluctance, which in turn decreases q-axis inductance. The ripple in both the cases is still high due to interaction between the spatial harmonics of the magnetomotive force of the stator currents and the rotor geometry. Note that db<sup>1</sup> is not changing as per equation (33).

The effect of length of flux barriers is investigated by changing β<sup>w</sup>b<sup>2</sup> and β<sup>w</sup>b<sup>3</sup> in a range between 0.4 to 0.8 with

![](_page_5_Figure_0.jpeg)

Fig. 11. Case 2: The influence of width of flux barrier on (a) Average torque (b) Torque ripple.

step size of 0.1. The variable  $\beta_{w_{b1}}$  is fixed at 0.4 and 0.8 for Case 1 and 2 respectively. From Fig. 12 and 13, it is evident that, in general, the maximum torque (35.97 Nm) is obtained by keeping  $\beta_{w_{b1}}$ ,  $\beta_{w_{b2}}$  and  $\beta_{w_{b3}}$  higher and closer to each other. This is because keeping  $\beta_{w_{b1}}$ ,  $\beta_{w_{b2}}$  and  $\beta_{w_{b3}}$  close to each other results in higher length of innermost flux barriers compared to outermost flux barriers which in turn assist the flux along d-axis. The ripple in both the cases is still high due to the same reason stated in case of variation of width of flux barrier.

![](_page_5_Figure_3.jpeg)

Fig. 12. Case 1: The influence of length of flux barrier on (a) Average torque (b) Torque ripple.

![](_page_5_Figure_5.jpeg)

Fig. 13. Case 2: The influence of length of flux barrier on (a) Average torque (b) Torque ripple.

## C. Influence of flux carrier width on torque production

The effect of changing  $w_{r1}$  is discussed first by varying it from 4mm to 8mm with step size of 1mm. It can be seen in Fig. 14 that average torque increases with  $w_{r1}$  and reaches maximum at 6mm and there after decreases. This is because lower value of  $w_{r1}$  results in saturation at the rotor shaft, which reduces the d-axis inductance, hence average torque. The average torque increases as we go beyond this value. But for larger value of  $w_{r1}$ , the q-axis inductance increases and average torque falls. Additionally, the smallest torque ripple can also be seen at  $w_{r1}$ = 6mm.

The effect of variation of  $\beta_{w_{r1}}$  on average torque and torque ripple is studied by varying it in a range between 0.6 to 1 with step size of 0.1 and  $w_{r1}$  is set to 6mm. From Fig. 15, it can be deduced that maximum average torque and minimum torque ripple is achieved for equal value of flux carrier width along q-axis. Similar results where obtained for  $\beta_{w_{r2}}$  and  $\beta_{w_{r3}}$ .

![](_page_5_Figure_10.jpeg)

Fig. 14. Effect of flux carrier width  $(w_{r1})$  on average torque and torque ripple.

All in all, we found from above sensitivity study that there are no single values of these design parameters that will give optimal torque performance. In order to achieve the optimized

![](_page_6_Figure_0.jpeg)

Fig. 15. Effect of  $\beta_{w_{r1}}$  on average torque and torque ripple.

rotor geometry of SynRM for maximum average torque and minimum torque ripple, all the design parameters must be considered simultaneously.

#### VI. OPTIMIZATION

The optimization mainly focuses on rotor part and is carried out using GA coupled with FEM. The GA has been popularly used in motor design application. It is a stochastic optimization method based on principles of genetics and natural selection. The main parameters of GA are listed in Table IV.

TABLE IV PARAMETERS OF GA

| Parameter                     | Value |
|-------------------------------|-------|
| Number of Individuals         | 30    |
| Maximum number of generations | 100   |
| Crossover Probability         | 0.75  |
| Mutation Probability          | 0.05  |

The number of rotor geometry variables should be as low as possible to make optimization easier. For that the following assumptions are made.

- The shape of all flux barrier ends has been selected as round. It is reported in [25] that round end barriers provides more uniform von Mises stress distribution and smaller maximum stress compare to sharp end barriers.
- From sensitivity analysis, maximum average torque and minimum ripple is obtained for equal width of all flux carriers along q-axis. So,  $\beta_{w_{ri}}$  and  $w_{r1}$  are set to 1 and 6mm respectively.
- To ensure good electromagnetic performance and structural integrity, the widths of both tangential  $(w_{tr})$  and radial ribs  $(w_{rr})$  are fixed at 1 mm.
- The parameter  $bec_i$  is equal to slot opening and the coefficient  $K_{air,r}$  is set to 0.48.

The main goal of optimization is to find the optimal rotor geometry of SynRM to achieve maximum average torque and minimum torque ripple, which are evaluated at single stator current (11.8A) and phase angle (69°). The upper and lower bonds of these variables are shown in Table V, where i varies from 1 to 3 and j varies from 1 to 2. This gives large search region for GA and avoids unfeasible geometries of rotor.

TABLE V
DESIGN PARAMETERS AND THEIR SEARCH LIMIT

| Parameter             | Min value | Max value |
|-----------------------|-----------|-----------|
| $\beta_{d_{bj}}$      | 0.5       | 1         |
| $\beta_{\theta_{bi}}$ | 0.7       | 1.3       |
| $\beta_{w_{bi}}$      | 0.4       | 0.8       |

This paper examines three different design cases to validate the effectiveness of this approach. The three cases are given as:

- Case 1: Maximize average torque  $(T_{avg})$
- Case 2: Minimize torque ripple  $(T_{rip})$
- Case 3: Minimize objective function  $(F_1)$ , given in (37). The objective is to achieve  $T_{avg}$ = 38 Nm and  $T_{rip}$ = 10%.

$$F_{1} = \left(\frac{T_{c-avg}}{T_{i-avg}} - \frac{T_{d-avg}}{T_{i-avg}}\right)^{2} W_{1} + \left(\frac{T_{c-rip}}{T_{i-rip}} - \frac{T_{d-rip}}{T_{i-rip}}\right)^{2} W_{2}$$
(37)

where,  $W_1 = 1$ ,  $W_2 = 2$ ,  $T_{c-avg}$  and  $T_{c-rip}$  are calculated values of average torque and torque ripple,  $T_{i-avg}$  and  $T_{i-rip}$  are the initial design values of average torque and torque ripple,  $T_{d-avg}$  and  $T_{d-rip}$  are desired values of average torque and torque ripple.  $W_1$  and  $W_2$  are the weighting factors determining the priority of optimization.

#### A. Optimization Results

The optimization study is performed on Intel Xeon based cluster machine with 12 cores. The total time taken for Case 1,2 and 3 are 12.3 hours, 9 hours and 12.2 hours respectively.  $T_{avg}$  and  $T_{rip}$  results for all the design cases are listed in Table VI. The comparison of torque characteristics of initial and three design cases are shown in Fig. 16.

![](_page_6_Figure_23.jpeg)

Fig. 16. Comparison of torque waveform of initial and three cases of rotor designs.

In Case 1, both  $T_{avg}$  and  $T_{rip}$  increases by about 8.17% and 9.07% respectively compared to the initial design. In Case 2,  $T_{avg}$  decreases by about 8.25%, while  $T_{rip}$  decreases significantly by about 71.61% compared to the initial design. Lastly, a 5.96% increase in  $T_{avg}$  and 73.90% decrease in  $T_{rip}$  is obtained for Case 3.

The efficiency and power factor at rated load and rated speed conditions are also calculated for various design cases and results obtained are tabulated and presented in Table VI. The mechanical losses is assumed to be 2%. By skewing of rotor stack, a further reduction in torque ripple can be obtained but with an expense of reduced torque as can be seen from the results presented in Table VII.

TABLE VI COMPARISON OF INITIAL AND OPTIMIZED DESIGNS

| Performance    | Initial  | Case 1   | Case 2   | Case 3   |
|----------------|----------|----------|----------|----------|
| Index          | Design   | Design   | Design   | Design   |
| Average torque | 34.42 Nm | 37.23 Nm | 31.58 Nm | 36.47 Nm |
| Torque ripple  | 39.13%   | 42.68%   | 11.11%   | 10.21%   |
| Efficiency     | 91.2%    | 91.56%   | 90.74%   | 91.91%   |
| Power factor   | 0.70     | 0.73     | 0.64     | 0.75     |

TABLE VII SKEW EFFECT ON CASE 1 DESIGN

| Skew angle (Deg) | Average Torque | Torque Ripple |
|------------------|----------------|---------------|
| 5                | 36.62 Nm       | 30.51%        |
| 7.5              | 35.87 Nm       | 17.52%        |
| 10               | 34.92 Nm       | 6.27%         |

# CONCLUSION

In this paper, the rotor design optimization of SynRM is presented using unit-less variables introduced to address its poor torque characteristics. Only the average torque and torque ripple characteristics were studied in this work. Three different design cases have been considered to show effectiveness of proposed design methodology. The optimization results show improved performance over initial design in atleast one performance index. Moreover, the rotor geometry is such that standard rectangular PM pieces can be inserted into the flux barriers to further enhance the performance of SynRM.

# ACKNOWLEDGMENT

The authors would like to thank ANSYS, Inc. for providing Maxwell, the finite element analysis software. We also acknowledge the use of the computing resources at HPCE, IIT Madras.

## REFERENCES

- [1] J. de Santiago, H. Bernhoff, B. Ekergard, S. Eriksson, S. Ferhatovic, ˚ R. Waters, and M. Leijon, "Electrical motor drivelines in commercial all-electric vehicles: A review," *IEEE Transactions on Vehicular Technology*, vol. 61, no. 2, pp. 475–484, 2012.
- [2] G. Pellegrino, A. Vagati, P. Guglielmi, and B. Boazzo, "Performance Comparison Between Surface-Mounted and Interior PM Motor Drives for Electric Vehicle Application," *IEEE Transactions on Industrial Electronics*, vol. 59, no. 2, pp. 803–811, 2012.
- [3] D. G. Dorrell, A. M. Knight, L. Evans, and M. Popescu, "Analysis and Design Techniques Applied to Hybrid Vehicle Drive Machines—Assessment of Alternative IPM and Induction Motor Topologies," *IEEE Transactions on Industrial Electronics*, vol. 59, no. 10, pp. 3690–3699, 2012.

- [4] A. Vagati, "The synchronous reluctance solution: a new alternative in AC drives," in *Proceedings of IECON'94 - 20th Annual Conference of IEEE Industrial Electronics*, vol. 1, 1994, pp. 1–13 vol.1.
- [5] A. Vagati, M. Pastorelli, G. Francheschini, and S. Petrache, "Design of low-torque-ripple synchronous reluctance motors," *IEEE Transactions on Industry Applications*, vol. 34, no. 4, pp. 758–765, 1998.
- [6] N. Bianchi, S. Bolognani, D. Bon, and M. D. Pre, "Rotor flux-barrier design for torque ripple reduction in synchronous reluctance motors," in *Conference Record of the 2006 IEEE Industry Applications Conference Forty-First IAS Annual Meeting*, vol. 3, 2006, pp. 1193–1200.
- [7] A. Vagati, G. Franceschini, I. Marongiu, and G. Troglia, "Design criteria of high performance synchronous reluctance motors," in *Conference Record of the 1992 IEEE Industry Applications Society Annual Meeting*, 1992, pp. 66–73 vol.1.
- [8] P. Niazi, H. A. Toliyat, D.-H. Cheong, and J.-C. Kim, "A Low-Cost and Efficient Permanent-Magnet-Assisted Synchronous Reluctance Motor Drive," *IEEE Transactions on Industry Applications*, vol. 43, no. 2, pp. 542–550, 2007.
- [9] S. Ooi, S. Morimoto, M. Sanada, and Y. Inoue, "Performance Evaluation of a High-Power-Density PMASynRM With Ferrite Magnets," *IEEE Transactions on Industry Applications*, vol. 49, no. 3, pp. 1308–1315, 2013.
- [10] N. Bianchi, *Electrical machine analysis using finite elements*. CRC press, 2005.
- [11] R.-R. Moghaddam, F. Magnussen, and C. Sadarangani, "Novel rotor design optimization of Synchronous Reluctance Machine for low torque ripple," in *2012 XXth International Conference on Electrical Machines*, 2012, pp. 720–724.
- [12] S. Taghavi and P. Pillay, "A Sizing Methodology of the Synchronous Reluctance Motor for Traction Applications," *IEEE Journal of Emerging and Selected Topics in Power Electronics*, vol. 2, no. 2, pp. 329–340, 2014.
- [13] A. Vagati, A. Canova, M. Chiampi, M. Pastorelli, and M. Repetto, "Design refinement of synchronous reluctance motors through finiteelement analysis," *IEEE Transactions on Industry Applications*, vol. 36, no. 4, pp. 1094–1102, 2000.
- [14] G. Pellegrino, F. Cupertino, and C. Gerada, "Barriers shapes and minimum set of rotor parameters in the automated design of Synchronous Reluctance machines," in *2013 International Electric Machines Drives Conference*, 2013, pp. 1204–1210.
- [15] T. Matsuo and T. A. Lipo, "Rotor design optimization of synchronous reluctance machine," *IEEE Transactions on Energy Conversion*, vol. 9, no. 2, pp. 359–365, 1994.
- [16] L. Davis, "Handbook of genetic algorithms," *Van Nostrand Reinhold New York*, 1991.
- [17] D. E. Goldberg, *Genetic Algorithms in Search, Optimization and Machine Learning*, 1st ed. USA: Addison-Wesley Longman Publishing Co., Inc., 1989.
- [18] G. Pellegrino, T. M. Jahns, N. Bianchi, W. L. Soong, and F. Cupertino, *The Rediscovery of Synchronous Reluctance and Ferrite Permanent Magnet Motors: Tutorial Course Notes*. Springer, 2016.
- [19] V. Honsinger, "Sizing equations for electrical machinery," *IEEE Transactions on Energy Conversion*, no. 1, pp. 116–121, 1987.
- [20] T. A. Lipo, *Introduction to AC machine design*. John Wiley & Sons, 2017.
- [21] M.G.Say, *Performance & Design of AC Machines*. London, U.K.:Pitman, 1968.
- [22] C. Babetto, G. Bacco, and N. Bianchi, "Synchronous Reluctance Machine Optimization for High-Speed Applications," *IEEE Transactions on Energy Conversion*, vol. 33, no. 3, pp. 1266–1273, 2018.
- [23] M. Gamba, G. Pellegrino, and F. Cupertino, "Optimal number of rotor parameters for the automatic design of Synchronous Reluctance machines," in *2014 International Conference on Electrical Machines (ICEM)*, 2014, pp. 1334–1340.
- [24] S. Taghavi and P. Pillay, "A Novel Grain-Oriented Lamination Rotor Core Assembly for a Synchronous Reluctance Traction Motor With a Reduced Torque Ripple Algorithm," *IEEE Transactions on Industry Applications*, vol. 52, no. 5, pp. 3729–3738, 2016.
- [25] M. Di Nardo, M. Degano, M. Galea, C. Gerada, M. Palmieri, F. Cupertino, N. Bianchi, and D. Gerada, "End barrier shape optimizations and sensitivity analysis of synchrnous reluctance machines," in *IECON 2015 - 41st Annual Conference of the IEEE Industrial Electronics Society*, 2015, pp. 002 914–002 919.