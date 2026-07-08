# We are IntechOpen, the world's leading publisher of Open Access books Built by scientists, for scientists

Open access books available 3,900

International authors and editors 116,000 120M

Downloads

Our authors are among the

154 TOP 1%

most cited scientists

12.2%

Countries delivered to Contributors from top 500 universities

![](_page_0_Picture_11.jpeg)

Selection of our books indexed in the Book Citation Index in Web of Science™ Core Collection (BKCI)

Interested in publishing with us? Contact book.department@intechopen.com

> Numbers displayed above are based on latest data collected. For more information visit www.intechopen.com

![](_page_0_Picture_16.jpeg)

# **Reliable Design of PMaSynRM**

Carlos López-Torres, Antoni Garcia-Espinosa and Jordi-Roger Riba

Additional information is available at the end of the chapter

http://dx.doi.org/10.5772/intechopen.76355

#### Abstract

Electric vehicles require highly reliable and resilient electric motors, due to the harsh operating conditions they must withstand. To this end, there is a current trend to design rareearth-free machines. Traction electric motors must be optimized in terms of efficiency, torque density, power factor, constant power speed ratio, and cost. Although different technologies are available, permanent magnet assisted synchronous reluctance motors (PMa-SynRM) are promising candidates for such applications. Nowadays, the optimal design process of electrical motors is based on finite element method (FEM) simulations. However, it is very time consuming with a heavy computational burden process, so in order to speed up the optimization process, it is very appealing to have an accurate pre-design of the machine. In this chapter, the electromagnetic pre-design of a PMaSynRM is developed. In the proposed electromagnetic pre-design process, the geometry of the machine is calculated based on analytical equations that take into account the thermal, electrical, magnetic, and mechanical behavior of the machine to ensure a suitable and reliable design.

Keywords: synchronous reluctance machines, pre-design, multi-physics, permanent magnet, electrical machines

## 1. Introduction

Electric motors for traction applications have been optimized in terms of power density, efficiency, cost, power factor, and wider speed range. There are different motor topologies to meet the requirements of such application, for instance, permanent magnet synchronous motors (PMSM), induction motors (IM), switched reluctance motors (SRM), and synchronous reluctance motors (SynRM). PMSMs have the best power density ratio and can maintain the power in a wide speed range. However, the material cost due to the rare-earth magnets and

![](_page_1_Picture_10.jpeg)

concerns about availability and supply of the magnets makes it necessary to use other type of motors. In this context, the concept of rare-earth-free-motors gains attention [1]. Synchronous reluctance motors are good candidates in terms of material and manufacture cost; however, the power density and power factor are low. Then, the idea of permanent magnet-assisted synchronous reluctance motors (PMa-SynRM) appears, since they improve the performances of SynRMs by using ferrite magnets. Ferrite magnets have lower electrical conductivity than rare-earth magnets, so the eddy current losses are much lower, and thus the temperature rise due to eddy current losses. Although ferrite magnets exhibit a lower remanent magnetic flux density compared to neodymium magnets, ferrite magnets have a higher Curie temperature. As a consequence, ferrite magnets are well suited to be applied in high-temperature environments, such as electric vehicles, thus offering improved reliability with respect to the use of rare-earth permanent magnets.

The design of a motor usually consists of a multi-physics analysis where the thermal, electric, magnetic, and mechanic domains are analyzed. In the electromagnetic pre-design stage, the geometry of the machine is often calculated based on criteria taking into account different domains. The electromagnetic domain allows calculating the necessary amount of the magnet, the thermal domain settles the size of the slots of the stator, and the mechanical domain settles the size of the radials ribs.

The final geometry of the motor is obtained after an optimization process, where the values of the motor's parameters are variated to determine the best solution. However, the starting point of the design is based on the electromagnetic pre-design. This work aims at guiding the electromagnetic pre-design of the PMa-SynRM.

The pre-design is performed with the basic specifications of the machine, such as mechanical power, corner speed, phase current, pole number, or efficiency required, among others. Since FEA is often not applied to speed up the design process, the parameters calculated must be very accurate, so several refinement loops are introduced. In this context, the whole process is a combination of analytical equations with iterative loops to refine the estimated parameters, which are required to start the electromagnetic pre-design.

The starting point consists of estimating some parameters, such as efficiency, power factor, air gap flux density, or back EMF, in order to determine the required phase current, electrical power, or number of turns per phase, among others. These estimated values depend on the machine type, for instance in the SynRM, the power factor can be selected around 0.7, and the efficiency around 95%.

# 2. Calculation of electrical parameters

The initial set of equations is given by:

$$P_e = \frac{P_{mec}}{\eta} \tag{1}$$

where " $P_{mec}$ " is the output mechanical power, which is one of the inputs of the electromagnetic pre-design, " $\eta$ " is the estimated efficiency, and " $P_e$ " is the required electrical power. Using the electrical power calculated in (1), the phase current is given by:

$$I_f = \frac{P_e}{mU_f \cos(\varphi)} \tag{2}$$

Being, "m" and " $U_f$ " are the number of phases and the RMS phase voltage, respectively, which are an inputs, and " $\cos(\varphi)$ " is the estimated power factor.

To finalize with the electrical part of the design, the number of turns per phase can be calculated according to (3):

$$N_s = \frac{\sqrt{2}E}{\omega_e k_{w1} l_{eff} \tau_p \frac{D_{is}}{2} \alpha_i \widehat{B}_g}$$
 (3)

where "E" is the back EMF, which is estimated according to 0.97 of the phase RMS voltage [2]; " $\omega_e$ " is the mechanical speed in electrical rad/s of the base point; " $l_{eff}$ " is the effective length of the machine; " $\widehat{B}_g$ " is the peak flux density in air gap, which is an estimated value; " $k_{w1}$ " is the winding factor of the fundamental component, which is fixed by the winding distribution; " $\alpha_i$ " is the coefficient to obtain the arithmetical average of the flux density; " $D_{is}$ " is the inner stator diameter; and " $\tau_p$ " is the slot pitch.

Considering a sinusoidal flux density, the value of " $\alpha_i$ " is 0.64 (2/ $\pi$ ). However, " $\alpha_i$ " is related in [2].

Note that the effective length and the pole pitch cannot be determined since the air gap volume is unknown. The mains dimensions must be calculated before the number of turns per phase.

#### 3. Main dimensions

The first step to calculate the motor geometry is the determination of the main dimensions of the motor. These parameters are the outer and inner diameter of the rotor, the outer and inner diameter of the stator, and the stack length. It is worthy to mention that depending on the restrictions of the application, the outer dimensions can be fixed. **Figure 1** shows several motor's parameters, such as inner and outer rotor radius ( $R_{ir}$  and  $R_{or}$ , respectively), inner and outer stator radius ( $R_{is}$  and  $R_{os}$ , respectively), air gap length (g), slot pitch (g), and pole pitch (g). The stack length (g) is the length of the active part, that is, the end winding length is not considered.

The calculation of the motor's geometry starts determining the air gap volume/surface or the outer volume/surface of the machine. In this context, different approaches can be found in the literature to calculate the motor geometry using the data obtained from the specifications. On the one hand, Bianchi et al. [3] and Gamba [4] calculate the exterior geometry, which is represented

![](_page_4_Picture_2.jpeg)

Figure 1. Motor basic geometry.

by the outer stator diameter and the stack length. The first one uses a relation between the torque generated and the volume (Kv), meanwhile the second one relates the losses generated with the outer surface (K<sup>j</sup> ). According to Bianchi et al. [3], the K<sup>v</sup> for these kinds of machines is around 10 Nm/L. However, these values can change depending on the value of the torque. In the second approach, the thermal loading depends on the coolant system, so it is required to determine the outer motor geometry. If the outer geometry is fixed, the thermal loading determines the coolant system required [5]. On the other hand, the electrical loading (A) is used to calculate the geometry of the air gap [6]. In this case, the allowed electrical loading is also determined by the coolant system. Another interesting approach relates the mechanical power of the machine with the air gap volume.

This approach is based on the mechanical constant [2, 7], which is given by:

$$C_{mec} = \frac{P_{mec}}{D_{is}^2 l_{eff} n_{syn}} \tag{4}$$

where "nsyn" is the rated electrical frequency.

The proposed pre-design starts with the mechanical constant, so a further explanation of the different values of such constant is required. The value of the mechanical constant is obtained by analyzing several motors of the same typology and coolant systems. Figure 2, extracted from [1], shows the relation between the mechanical constant and efficiency for different motor types.

Nevertheless, when using the electrical loading, mechanical constant, or other parameters to obtain the volume or surface of the air gap, the relation between diameter and length is required. The form factor "X" is given by:

![](_page_5_Figure_2.jpeg)

**Figure 2.** Machines comparison based on the maximum efficiency point and machine constant of mechanical power. Data presented have been collected from [8–24].

$$X \approx \frac{\pi}{4\sqrt{p}} \tag{5}$$

"p" being the number of pole pairs.

Using (5) and (6), the effective length  $l_{eff}$  and the bore diameter  $D_{is}$  can be calculated. The stack length is obtained according to:

$$L_{stk} = l_{eff} - 2g \tag{6}$$

In order to maximize the saliency ratio, the air gap thickness must be as low as possible [3]. According to Pyrhönen et al. [2], the air gap should be smaller compared to induction machines. The air gap in induction machines is given by:

$$g = \frac{0.18 + 0.006P_{mec}^{0.4}}{1000} \tag{7}$$

where " $P_{mec}$ " is given in watts.

## 4. Stator geometry

The stator geometry is completed when the size of the slot, teeth, and yoke are determined. The width of the teeth ( $b_t$ ) and slots ( $b_s$ ) can be constant or radial. However, some simplifications can be realized in order to determine the size of these parts. **Figure 3A** shows the geometry of the teeth and slots using the smaller dimension, which it is the most restrictive

![](_page_6_Figure_2.jpeg)

Figure 3. A) Approximate geometry using the most restricted dimensions. B) Flux lines in teeth.

width. The slot opening (S<sup>o</sup> ) is dimensioned to be higher than the diameter of the conductors. The height of the slot (h<sup>s</sup> ) and yoke height (h<sup>y</sup> ) are shown in Figure 3B. Finally, the height of tooth tip (htip) is not important in this stage of the design, although it can be fixed at 1 mm, depending on the machine. In the same way, the "Δ" is not important in the pre-design and can be fixed at 0.5 mm depending on the machine.

In order to calculate the size of the slots, the number of conductors in each slot and the tooth size are required. Then, (3) can be solved since the pole pitch is known. When the number of turns in series per phase is calculated, the number of conductors in each slot (zq) can be determined as follows:

$$z_q \approx \frac{2mN_{ph}}{Q_s} \tag{8}$$

being, "m" is the number of phases and "a" is the number of parallel paths.

Note that "zq"must be an integer, so the result obtained needs to be round to obtain the final number of conductors in each slot. Then, the number of turns in series per phase must be updated as:

$$N_{ph\_new} = \frac{z_q Q_s}{2m} \tag{9}$$

In this point, the estimated flux density within the air gap changes, so it is calculated as:

$$\widehat{B}_{g\_new} = \frac{\sqrt{2}E}{\omega_e k_{w1} l_{eff} \tau_p \frac{D_{is}}{2} \alpha_i N_{ph\_new}}$$
(10)

Considering a sinusoidal magnetic flux distribution within the air gap and how this magnetic flux distributes through the stator, the size of the teeth and yoke are calculated to obtain a magnetic saturation below a pre-defined value. The teeth have to be sized to withstand the magnetic flux that comes from the air gap. The magnetic flux will enter in the teeth instead of the slots, so the magnetic flux in the pole is divided in the different teeth. However, the teeth are dimensioned considering the worse scenario. Figure 3B shows the magnetic fluxes lines of air gap entering in the teeth. The sinusoidal magnetic flux density is superimposed to understand the different quantity or density of magnetic flux (blue arrows) in both teeth. Then, the width of teeth is calculated considering the teeth with higher magnetic flux. In order to oversize the teeth, the magnetic flux density is considered constant at the maximum value as can be observed in Figure 3B (blue line in the teeth):

$$\phi_t = \widehat{B}_{g\_new} l_{eff} \tau_s \frac{D_{is}}{2} \tag{11}$$

where "τs" is the slot pitch, which is given by:

$$\tau_s = \frac{2\pi}{Q_s} \tag{12}$$

"Qs" being the number of slots.

In order to obtain a correct size of teeth, the maximum allowed magnetic flux density on this motor part is fixed between 1.5 and 1.8 T. Therefore:

$$b_t = \frac{\phi_t}{k_{sf}\widehat{B}_t} L_{stk} \tag{13}$$

where "Bbt" is the maximum allowed magnetic flux density and "ksf " is the stacking factor.

On the other hand, the yoke's width must be calculated to drive half of the air gap's magnetic flux on one magnetic pole as can be observed in Figure 4.

Then, the magnetic flux in the air gap is calculated as follows:

$$\phi_g = \frac{2}{\pi} \widehat{B}_{g\_new} l_{eff} \tau_p \frac{D_{is}}{2} \tag{14}$$

where the term "2Bbg=π" is used to obtain the average value of a sinusoidal waveform, and "τp" is the pole pitch, which are calculated as follows:

$$B_{g_{av}} = \frac{1}{\pi} \int_0^{\pi} \widehat{B}_{g\_new} \sin(\theta) d\theta = \frac{1}{\pi} \widehat{B}_{g\_new} (-\cos(\pi) + \cos(0)) = \frac{2}{\pi} \widehat{B}_{g}$$
 (15)

$$\tau_p = \frac{2\pi}{2p} \tag{16}$$

Then, the width of the yoke is:

$$h_y = \frac{\phi_g}{2k_{sf}\widehat{B}_y} L_{stk} \tag{17}$$

where "Bby" is the maximum allowed magnetic flux density in yoke, which is fixed between 1.4 and 1.6 T, corresponding to the knee point of the B-H curve of the magnetic steel laminations.

![](_page_8_Picture_2.jpeg)

Figure 4. Detail of the magnetic flux in the yoke.

According to Figure 3A, when the width of the teeth is known, the slot's width can be determined as:

$$b_s = \tau_s \frac{D_{is}}{2} - b_t \tag{18}$$

Then, height of the slot is determined by:

$$S_{slot} = b_s h_s = \frac{z_q I_{ph}}{J k_u} \to h_s = \frac{z_q I_{ph}}{J k_u b_s}$$
 (19)

where "J" is the current density [A/m<sup>2</sup> ] and variates with the coolant system [2, 6] and "ku" is the winding factor, which can be fixed at 0.40.

The height of the teeth is given by:

$$h_t = h_s + h_{tip} + \Delta \tag{20}$$

Then, the outer stator diameter is obtained as:

$$D_{os} = D_{is} + 2h_t + 2h_y (21)$$

# 5. Rotor geometry

The rotor of the SynRMs is punched to create the anisotropy. The insulation, which is the air cavity created in the rotor's perforation, is called flux barrier. The magnetic steel material between flux barriers is called segment or flux carrier. The rotor structure is completed by ribs; there are two different ribs. The first one is the tangential rib, which connects the segments. The other type is the radial rib, which increases the mechanical integrity of the machine. The mentioned parts are depicted in Figure 5.

A good saliency ratio can be enhanced by a correct design of the rotor [25]. It starts choosing the proper number of flux barriers [3, 26–28], which is given by:

$$k = \frac{Q_s}{2p} \pm 2 \tag{22}$$

![](_page_9_Picture_2.jpeg)

Figure 5. (A) Basic geometry of the rotor of SynRM. (B) Flux barriers distribution.

Note that according to (22), there are two possibilities for k. The choice depends on the application or the rotor size.

Then, the positioning of the barriers is realized to obtain a good distribution of the magnetic flux, that is, a reduction of the torque ripple. The ripple reduction is obtained by means of an optimization process, where the angle of the barriers is changed to find the best solution [29–31]. However, during the pre-design stage, the angle between the end points of the barriers is fixed according to [28, 32]:

$$\alpha_i = \frac{\pi/p}{k+1} \tag{23}$$

Note that (23) calculates the angle between barriers. The angle between the last barrier and the pole center is 3αm=2 as can be observed in Figure 5B.

The magnetic flux flows through the segments, so a correct sizing is mandatory. Note that the low reluctance of the magnetic steel is related to the magnetic saturation of the segments. Then, the calculation of the width of the flux carriers considers the rotor position with the highest magnetic flux. In this position, which it is called direct axis (d-axis), the maximum magnetomotive force (MMF) in the stator is located between the magnetic poles, meanwhile the zero MMF is in the middle of the magnetic pole, as can be observed in Figure 6A. It is worthy to mention that the MMF is considered sinusoidal in order to simplify the calculation of the rotor's geometry.

The widths of the different segments (S<sup>i</sup> ) are dimensioned to obtain the same magnetic saturation in each segment. In order to estimate the magnetic saturation, the magnetic flux (φ) must be calculated. Considering the geometry shown in Figure 6A, an equivalent magnetic circuit can be built to determine the relation between the magnetic fluxes, as depicted in Figure 7A. Only one-half of the pole is represented due to the magnetic symmetry.

Note that the reluctance of the air gap is much bigger than the segments' reluctances, so the latter can be disregarded. Then, the magnetic fluxes are given by:

$$\phi_i = \frac{MMF_{di}}{\mathfrak{R}_g} \tag{24}$$

![](_page_10_Figure_2.jpeg)

**Figure 6.** MMF distribution in the dq-positions. The blue arrows represent the magnetic flux in the rotor. (A) d-position (B) q-position.

Therefore, the value of fluxes depends on the MMF. The MMF of each segment is represented by stairs function where the value is the average value of the MMF distribution shown in **Figure 6A**. Since all position angles of the barriers have been fixed, the average MMF of each segment can be calculated as follows:

$$MMF_{di} = \frac{\int \frac{2i-1}{2} p\alpha_{i}}{p\alpha_{i}} \cos(\alpha)d\alpha$$

$$MMF_{di} = \frac{\int \frac{2i-3}{2} p\alpha_{i}}{p\alpha_{i}} = \frac{\sin\left(\frac{2i-1}{2}p\alpha_{i}\right) - \sin\left(\frac{2i-3}{2}p\alpha_{i}\right)}{p\alpha_{i}}$$

$$p\alpha_{i}$$

$$MMF_{dn_{b}+1} = \frac{\int \frac{2n_{b}-3}{2} p\alpha_{i}}{p\frac{3}{2}\alpha_{i}} = \frac{1-\sin\left(\frac{2n_{b}-3}{2}p\alpha_{i}\right)}{p\frac{3}{2}\alpha_{i}}$$

$$(25)$$

Then, taking into account (24), where the flux is proportional to the MMF, and the condition of obtaining an equal magnetic saturation on each segment, the relation of segment's width is given by:

$$\frac{S_i}{S_{i+1}} = \frac{MMF_i}{MMF_{i+1}} \tag{26}$$

![](_page_11_Picture_2.jpeg)

Figure 7. d-Axis equivalent magnetic circuit used to determine the width of the segments. (A) d-position (B) q-position.

The magnetic saturation is calculated using the magnetic flux and the cross section, so (26) is deducted as follows:

$$B_i = \frac{\phi_i}{S_i L_{stk}} \to B_i = B_{i+1} \to \frac{\phi_i}{S_i L_{stk}} = \frac{\phi_{i+1}}{S_{i+1} L_{stk}} \to \frac{\frac{MMF_{di}}{\Re_g}}{S_i L_{stk}} = \frac{\frac{MMF_{di+1}}{\Re_g}}{S_{i+1} L_{stk}}$$
(27)

In addition, it is worthy to mention that (26) must be adapted in segment 1, since the magnetic flux is divided in the two magnetic poles, so the final equation to determine the relationship between S<sup>1</sup> and S<sup>2</sup> is given by:

$$\frac{2S_1}{S_2} = \frac{MMF_1}{MMF_2} \tag{28}$$

Finally, there are one more unknowns that equations, so one more equation is required to find out the width of the segments. Since the width of all the segments is equal to the total iron length in the rotor, the last equation results in:

$$L_{s} = \sum_{i=1}^{i=nb+1} S_{i} = \frac{h_{rotor}}{1 + k_{insq}}$$
 (29)

where "hrotor" is calculated as hrotor ¼ ð Þ Dor - Dir =2, and "kinsq" is the insulation ratio in the qaxis. Note that "kinsq", which has values around 1 [2], is defined by:

$$k_{insq} = \frac{L_a}{L_s} \tag{30}$$

"La" being the total length of width of air in the rotor given in (37) in the q-axis and "Ls" is the t width of all the segments of magnetic steel along the q-axis.

On the other hand, the flux barriers must be designed to offer a large magnetic resistance to the flow of the magnetic flux. In this context, the sizing of the flux barriers is carried out when the magnetic flux is positioned in the quadrature position, as can be observed in **Figure 6B**. The MMF distribution in the q-position is calculated as in the d-position, that is, using the average value of the MMF considering a sinusoidal distribution, as shown in **Figure 6B**. In this case, the MMF is given by:

$$MMF_{qi} = \frac{\int_{\frac{2i-3}{2}p\alpha_{i}}^{\frac{2i-1}{2}p\alpha_{i}}\sin(\alpha)d\alpha}{p\alpha_{i}} = \frac{-\cos\left(\frac{2i-1}{2}p\alpha_{i}\right) + \cos\left(\frac{2i-3}{2}p\alpha_{i}\right)}{p\alpha_{i}}$$

$$MMF_{qn_{b}+1} = \frac{\int_{\frac{2n_{b}-3}{2}p\alpha_{i}}^{\frac{\pi}{2}}\cos(\alpha)d\alpha}{\frac{3}{2}\alpha_{i}} = \frac{\cos\left(\frac{2n_{b}-3}{2}p\alpha_{i}\right)}{\frac{3}{2}\alpha_{i}}$$
(31)

**Figure 7B** depicts the equivalent magnetic circuit in the q-position to calculate the size of the different flux barriers.

Note that the  $MMF_{q1}$  is zero, so the path of flux 1 can be removed. As can be observed, the magnetic flux in the q-axis is given by the addition of fluxes 1–4. Then, the purpose of the barriers' sizing is to minimize the q-flux. Then, the relation between the widths of each barrier is given by:

$$\frac{W_{qi}}{W_{qi+1}} = \frac{MMF_{i+1} - MMF_i}{MMF_{i+2} - MMF_{i+1}} = \frac{\Delta MMF_i}{\Delta MMF_{i+1}}$$
(32)

A demonstration of the procedure to obtain (32) is further developed. However, the following example is realized with two barriers for the sake of simplification. **Figure 8** shows a rotor with two flux barriers, the magnetomotive force in each segment, which has been calculated with (31), and the variable to optimize, which is the size of the first barrier.

![](_page_12_Figure_8.jpeg)

Figure 8. Example of two barriers to determine the relation between the widths of the barriers.

As mentioned before, the sizing of the barriers aims to reduce the total flux in the q-axis (blue arrows). Then, the flux in each barrier is given by:

$$\phi_i = \frac{MMF_{qi+1} - MMF_{qi}}{\mathfrak{R}_{bi}} = \frac{\Delta MMF_i}{\mathfrak{R}_{bi}}$$
(33)

The reluctance of the barriers is given by:

$$\mathfrak{R}_{bi} = \frac{W_{qi}}{\mu_o l_{qi} L_{stk}} \tag{34}$$

Therefore, the total flux is given by:

$$\phi = \frac{\Delta MMF_1}{W_{q1}} \mu_o l_{q1} L_{stk} + \frac{\Delta MMF_2}{W_{q2}} \mu_o l_{q2} L_{stk}$$
(35)

Note that the total flux is a function of the reluctances of the flux barriers, that is, the total flux is a function of the variable "x" (see Figure 8). Hence:

$$\phi(x) = \frac{\Delta MMF_1}{x} \mu_o l_{q1} L_{stk} + \frac{\Delta MMF_2}{L_a - x} \mu_o l_{q2} L_{stk}$$
(36)

where the total width of air in the rotor is given by:

$$L_a = \sum_{i=1}^{i=nb} W_{qi} = \frac{h_{rotor}}{1 + \frac{1}{k_{insq}}}$$
 (37)

Then, the minimization of the flux is obtained as follows:

$$\frac{d\phi(x)}{dt} = -\frac{\Delta MMF_1}{x^2} \mu_o l_{q1} L_{stk} + \frac{\Delta MMF_2}{(L_a - x)^2} \mu_o l_{q2} L_{stk} = 0$$
(38)

Then, the final result is:

$$\frac{\Delta MMF_1}{x^2} l_{q1} = \frac{\Delta MMF_2}{(L_a - x)^2} l_{q2} \to \frac{\Delta MMF_1}{W_{q1}^2} l_{q1} = \frac{\Delta MMF_2}{W_{q2}^2} l_{q2}$$
(39)

Finally, the permeance of each barrier can be assumed constant in order to obtain a better distribution of the flux in the air gap:

$$\frac{l_{q1}}{W_{q1}} = \frac{l_{q2}}{W_{q2}} \tag{40}$$

Finally, by introducing (40) in (39), (32) appears.

It is worthy to mention that there is another approach [27, 28], which relates the size of the barriers as follows:

$$\frac{W_{qi}}{W_{qi+1}} = \frac{\Delta MMF_i^2}{\Delta MMF_{i+1}^2} \tag{41}$$

As can be observed in Figure 6B, there is another variable to define, which it is the width of the flux barrier in the lateral location (Wdi). The relation between the widths of the barriers in the q-axis with the thickness in the d-axis is given by [28]:

$$\frac{W_{di}}{W_{di+1}} = \frac{W_{qi}}{W_{qi+1}} \tag{42}$$

Note that one more equation is required to solve the sizing of the barriers. The total length of the barriers can be determined by using the insulation ratio in the d-axis:

$$L_{ad} = \sum_{i=1}^{i=nb} W_{di} = L_s k_{insd}$$

$$\tag{43}$$

"kinsd" being the insulation ratio in the d-axis, which is applied to determine the width of the barriers according to the mechanical angle defined in Figure 5B. "Ls" is the total thickness of the segments, which it is constant in the whole segment.

In this point, the sizing of the rotor is explained. However, there are several uncertain points. These undefined variables are the inner rotor diameter and the insulation ratios (kinsd and kinsq).

On the one hand, the inner rotor diameter (DirÞ determines the total space in the rotor, since the outer rotor diameter is known:

$$D_{or} = D_{is} - 2g \tag{44}$$

Then, the inner rotor diameter is defined as:

$$D_{ir} = D_{or} - 2h_{rotor} (45)$$

"hrotor" is required to calculate the width of the barriers and segments, as can be observed in (29) and (37). Then, an iterative system to determine the correct size of the rotor is proposed as can be observed in Figure 9. Depending on the design restrictions, this part must be adapted. For instance, the use of magnets makes necessary to size the barriers with thickness greater than a certain value, which depends on the magnet's manufacturer (around 3 mm), or to increase the rotor size to obtain a desired saliency ratio, or to introduce the necessary quantity of magnet to improve the motor performances in terms of constant power ratio. In this context, Figure 9 shows the iterative design procedure. Furthermore, an example of the differences is depicted. In the first iteration (i = 1), the width of the last barrier is 0.5 mm, however, the specifications only allow values higher than 3 mm. Then, after the iterative procedure (i = n), the solution is obtained according to the restrictions imposed. Note that the inner diameter of

![](_page_15_Figure_2.jpeg)

Figure 9. Iterative loop to size the rotor segments and barriers in the q-position.

the rotor in the first case is 90 mm meanwhile in the final solution is 75 mm. The insulation ratio in the q-axis is defined by the designer, and probably the best option is obtained after an optimization. However, values around 1 are good solutions.

On the other hand, the d-axis insulation ratio is not defined. As explained before, this insulation ratio is determined to locate the barriers according to Figure 5. Then, the value of this variable is swept to obtain the final design. In this case, the criterion to halt the iterative process is the correct position of the last barrier (the angle is 1:5αm). Figure 10 shows the iterative procedure and the solutions of two different iterations.

It is noted that a posterior mechanical verification is required to ensure a suitable mechanical strength of the rotor configuration obtained in this step.

After the calculation of the rotor size, the magnet quantity must be determined in order to obtain a suitable behavior of the machine during the operation. The north of the magnet is located in the negative direction of the q-axis (see Figure 11) in order to improve the motor capabilities, such as torque, base speed, and angle between voltage and current (see Figure 11B).

The motor capability within the flux-weakening region is related with the magnet contribution [33, 34]. It means that the magnets can be or not be inserted in all the barriers, depending on the requirements. In the case of not inserting magnets in all barriers, it is recommended to put the magnets in the innermost barrier, since the outset barriers are more magnetically stressed, so the magnet can suffer demagnetization [3, 35].

![](_page_16_Figure_2.jpeg)

Figure 10. Rotor iterative loop to size the segments and barriers in d-position.

![](_page_16_Figure_4.jpeg)

Figure 11. (A) Magnet orientation in the rotor. (B) Phasor diagram with and without magnets.

To compute the inductances and the magnet flux linkage, a fast and simple magnetic model is introduced. It is important to mention that a complex magnetic model is required in the optimization stage [36, 37]; however, in the electro-magnetic pre-design, the proposed magnetic model is good enough to calculate the magnet and improve the accuracy of the geometry.

The magnetic model based on two reluctance networks (RN) not only calculates the magnetic flux linkage but also estimates the dq-inductances, so the motor performances can be calculated. Using this magnetic model, the back EMF, power factor, efficiency, saturation factor, and air gap flux density can be defined with more accuracy and the electromagnetic pre-design can be improved (see Algorithm 1).

There are two reluctance networks to analyze, the d- and q-axis. The q-reluctance network (RN) allows calculating the q-inductances and the magnet flux linkage. Figure 12 shows an equivalent magnetic model to determine the mentioned parameters of the machine.

![](_page_17_Picture_2.jpeg)

![](_page_17_Picture_3.jpeg)

Figure 12. Simple reluctance network in q-axis.

Note that, the magnet is only located in the innermost barrier, however, it can be removed or more magnets can be introduced in the remaining barriers. The RN is formed by MMF generators and reluctances. The first one is created by the coils and magnets:

$$MMF_{winding} = \sum NI \tag{46}$$

"N" being the number of conductors in the coil and "I" the current in each phase (in this, select the rated current).

It is worthy to be mentioned that this magnetic model is not complete. The winding MMF generator is only represented in one tooth, so the whole contribution of the different teeth has to be added. In [38], there is more information to calculate the MMFwinding according to a given winding distribution:

$$MMF_{magnet} = H_c W_{qi} (47)$$

where "Hc" is the coercive force and "Wqi" is the width of the magnet, which is the same width as that of the flux barriers. Then, the reluctances are calculated as follows:

$$\Re = \frac{l}{\mu_o \mu_r S} \tag{48}$$

where "l" is the length of the magnetic reluctance, "S" is the cross section of the magnetic reluctance, "μ<sup>o</sup> " is the magnetic permeability of the vacuum, and "μ<sup>r</sup> " is the relative magnetic permeability, which in the air is equal to 1 meanwhile in the magnetic steel varies with the saturation. Note that the magnetic steel is not saturated along the q-axis. Finally, the air gap reluctance must be multiplied by Carter's coefficient to reflect the effect of the slot opening.

On the other hand, the d-axis RN is shown in Figure 13. In this case, the magnet is not reflected since it only influences the q-axis. The magnetic saturation of the magnetic steel must be considered. The magnetic saturation in the teeth and yoke can be fixed at the value chosen in the design stage (13) and (17), and in the rotor can be fixed at 1 T.

![](_page_18_Picture_2.jpeg)

![](_page_18_Picture_3.jpeg)

Figure 13. Simple reluctance network in d-axis.

The unknown magnetic flux is calculated using two different equations. The first one (49) relates the MMF obtained in a closed path with the reluctances and the magnetic flux in this path:

$$MMF = \sum \Re \phi \tag{49}$$

The second one relates the total magnetic fluxes in a node (see Figure 12):

$$\sum \phi = 0 \tag{50}$$

The q-axis is solved twice; the first one only considers the MMF generated by the magnets in order to calculate the magnet flux linkage ( $\Psi_{mpq}$ ), meanwhile the second one takes into account both MMF generators. The inductances and flux magnet linkage are calculated as follows:

$$L_{d} = 2pN\frac{\phi_{d}}{I}; L_{q} = \frac{2pN\phi_{q} - \Psi_{mpq}}{I}; \Psi_{mpq} = 2pN\phi_{q} \text{ where } I_{q} = 0$$
 (51)

By using these values, the motor performances can be deducted, so the process could be restarted with these new values. The back EMF is calculated as follows:

$$E_d = -\omega_e L_q i_q - \omega_e \Psi_{mpq}; E_q = \omega_e L_d i_d$$
 (52)

The current angle is given according to the MTPA rule, so the d- and q-currents are known. Then, the power factor can be deducted by calculating the phase shift between the current and voltage. Finally, the torque and output power can be calculated:

$$T = \frac{m}{2} p\left(\left(L_d - L_q\right) i_d i_q - \Psi_{mpq} i_d\right) \tag{53}$$

$$P_{out} = \omega_e T \tag{54}$$

Then, the losses, which are composed by copper and iron losses, are given by:

$$P_{cu} = mR_s I_{rms}^2 \tag{55}$$

$$P_{fe} = k_h \frac{\omega_e}{2} \widehat{B}^{n_i} + k_e \left(\frac{\omega_e}{2} \widehat{B}\right)^2$$
 (56)

" $R_s$ " being the phase resistance calculated with the geometry obtained during the calculation of the stator geometry, "m" the number of phases, and " $I_{rms}$ " the rated current in rms value. On the other hand, the iron losses are composed by hysteresis and eddy current components. The hysteresis and eddy current coefficients ( $k_{lv}$   $k_e$ ,  $n_i$ ) are obtained by using the material specific losses obtained from the manufacturer's datasheets. The iron loses are per unit of mass, so the final value must be multiplied by the mass of the different parts. The computed parts can be the yoke, teeth, and rotor, since these three parts have different magnetic saturation. Then, the efficiency is given by:

$$\eta = \frac{P_{out}}{P_{out} + P_{cu} + P_{fe}} \tag{57}$$

In this point, the thermal behavior of the machine has been considered in the sizing of the slot. The magnetic behavior is analyzed by using the proposed simple magnetic model. Then, the oversize of the slots and the magnet compensated situation ensure the reliability of the motor in terms of magnetic and thermal behaviors. However, the mechanical stress has to be considered to ensure the correct behavior of the machine, since the rotor structure reduces the mechanical integrity.

The mechanical problems are solved by the correct sizing of the radial ribs. Several authors deal with this problem [39–41]. The centrifugal force is given according to:

$$F_c = M\omega_m^2 R_G \tag{58}$$

where "M" is the mass that the calculated radial rib has to support, " $R_G$ " is the radius of the gravity center of the mass, and " $\omega_m$ " is the mechanical speed.

Then, the width of the radial ribs  $(W_r)$  is given as:

$$W_r = \frac{k_s F_c}{\sigma_r L_{stk}} \tag{59}$$

where " $k_s$ " is the safety factor, which is chosen over 2 and " $\sigma_r^{|m|}$  is the tensile strength of the lamination.

#### 6. Summary of the design procedure

In this point, the whole process to obtain the electromagnetic pre-design according to the given requirements is realized. A summary detailing the parameters and equations required in each step is shown in Algorithm 1.

1: Introduce the desired performances (power, rated speed) 2: Introduce the fixed parameters (pole pairs, phase number, slots, Bus DC) 3: Start electro-magnetic pre-design process 4: Estimate parameters (efficiency, power factor, back EMF, saturation factor) 5: while stop criterion is not achieved do 6: Basic parameters calculation: Electric power (1), phase current (2) 7: Estimate Cmec according to Figure 2 8: Calculate Dis and leff using (4) and (5). Compute the g (7) and Lstk (6) 9: Estimate number of turns in series Nph (3) 10: Calculates the number of conductors in slot (8) 11: Calculates the number of turns in series Nph new (9) and the B<sup>g</sup> (10) 12: Calculates the stator geometry (teeth, yoke, and slots dimensions) (11–21) 13: Chose the number of flux barriers (22) 14: Calculates the position of the barriers (23) Calculation of rotor in q-axis (Figure 9) 15: while stop criterion is not achieved do 16: Define hrotor 17: Calculates the width of the segments and barriers (25–30) and (31–32) 18: Evaluates stop criterion 19: end Calculation of rotor in d-axis (Figure 10) 20: while stop criterion is not achieved do 21: Define kinsd 22: Calculates the width of the barriers in d-axis(42–43) 23: Evaluates stop criterion 24: end 25: Solve Magnetic model (Figure 12 and Figure 13) 26: Calculates Inductances, magnetic flux linkage (51) 27: Calculates losses (55–56)

28: Calculates motor performances: Torque (53), output power (54)

factor, peak air gap flux density (using the d-flux from magnetic model).

30: Evaluates stop criterion (error of estimated parameters)

32: Calculates the thickness of the radial ribs (58–59)

29: Calculates the estimated values: Back EMF (52), efficiency (57), power factor, saturation

7. Conclusions

31:end

Due to the harsh operating conditions, electric vehicles require highly reliable and resilient electric motors. To this end, rare-earth-free PMaSynRMs are appealing candidates. In this chapter, a design procedure of PMaSynRMs has been presented, which includes electromagnetic, thermal, and mechanical restrictions in order to ensure a reliable and resilient operation within extended operational limits. For example, in the event of a major demagnetization failure, the PMaSynRM designed following the proposed approach is able to work as a synchronous reluctance machine, thus providing about 75% of the rated torque. In addition, the use of ferrite magnets allows the machine to operate in higher temperature environments.

### Author details

Carlos López-Torres\*, Antoni Garcia-Espinosa and Jordi-Roger Riba

\*Address all correspondence to: carlos.lopez.torres@upc.edu

Electrical Engineering, Universitat Politècnica de Catalunya (UPC), Terrassa, Spain

### References

- [1] Riba J-R, López-Torres C, Romeral L, Garcia A. Rare-earth-free propulsion motors for electric vehicles: A technology review. Renewable and Sustainable Energy Reviews. 2016; 57:367-379
- [2] Pyrhönen J, Jokinen T, Hrabovkowá V. Design of Rotating Electrical Machines. second ed. Wiley; 2014
- [3] Bianchi N, Mahmoud H, Bolognani S. Fast synthesis of permanent magnet assisted synchronous reluctance motors. IET Electric Power Applications. 2016;10(5):312-318
- [4] M. Gamba, "Design of Non Conventional Synchronous Reluctance Machine," Politecnico di Torino, 2017
- [5] Lu C, Ferrari S, Pellegrino G. Two design procedures for PM synchronous Machines for Electric Powertrains. IEEE Transactions on Transportation Electrification. 2017;3(1): 98-107
- [6] Hendershot JR a M. T.J.E., Design of Brushless Permanent-Magnet Motors (Monographs in Electrical and Electronic Engineering). Hillsboro, OH : Oxford: Magna Physics Pub: Motor Design Books LLC; 1994
- [7] Huppunen J. High-Speed Solid-Rotor Induction Machine Electromagnetic Calculation and Design. Finland: Lappeenranta University of Technology; 2004
- [8] Dorrell DG, Knight AM, Popescu M, Evans L, Staton DA. Comparison of different motor design drives for hybrid electric vehicles. In: 2010 IEEE Energy Conversion Congress and Exposition. 2010. pp. 3352-3359
- [9] Petrov I, Pyrhonen J. Performance of low-cost permanent magnet material in PM synchronous machines. Industrial Electronics, IEEE Transactions on. 2013;60(6):2131-2138
- [10] Montalvo-Ortiz EE, Foster SN, Cintron-Rivera JG, Strangas EG. Comparison between a spoke-type PMSM and a PMASynRM using ferrite magnets. In: Electric Machines & Drives Conference (IEMDC), 2013 IEEE International; 2013. pp. 1080-1087

- [11] Chiba A, Takeno M, Hoshi N, Takemoto M, Ogasawara S, Rahman MA. Consideration of number of series turns in switched-reluctance traction motor competitive to HEV IPMSM. IEEE Transactions on Industry Applications. 2012;48(6):2333-2340
- [12] Morimoto S, Ooi S, Inoue Y, Sanada M. Experimental evaluation of a rare-earth-free PMASynRM with ferrite magnets for automotive applications. IEEE Transactions on Industrial Electronics. 2014;61(10):5749-5756
- [13] Chiba K, Chino S, Takemoto M, Ogasawara S. Fundamental analysis for a ferrite permanent magnet axial gap motor with coreless rotor structure. In: Electrical Machines and Systems (ICEMS), 2012 15th International Conference on, 2012. pp. 1-6
- [14] Sone K, Takemoto M, Ogasawara S, Takezaki K, Akiyama H. A ferrite PM in-wheel motor without rare earth materials for Electric City commuters. IEEE Transactions on Magnetics. 2012;48(11):2961-2964
- [15] Miura T, Chino S, Takemoto M, Ogasawara S, Akira C, Nobukazu H. A ferrite permanent magnet axial gap motor with segmented rotor structure for the next generation hybrid vehicle. In: Electrical Machines (ICEM), 2010 XIX International Conference on, 2010. pp. 1-6
- [16] Chiba A, Kiyota K, Hoshi N, Takemoto M, Ogasawara S. Development of a rare-earth-free SR motor with high torque density for hybrid vehicles. IEEE Transactions on Energy Conversion. 2015;30(1):175-182
- [17] Obata M, Morimoto S, Sanada M, Inoue Y. Performance evaluation of high power and low torque ripple structure of rare-earth free PMASynRM with ferrite magnet. In: Power Electronics and Drive Systems (PEDS), 2013 IEEE 10th International Conference on, 2013. pp. 714-719
- [18] Obata M, Morimoto S, Sanada M, Inoue Y. Performance of PMASynRM with ferrite magnets for EV/HEV applications considering productivity. Industry Applications, IEEE Transactions on. 2014;50(4):2427-2435
- [19] Pellegrino G, Vagati A, Boazzo B, Guglielmi P. Comparison of induction and PM synchronous motor drives for EV application including design examples. IEEE Transactions on Industry Applications. 2012;48(6):2322-2332
- [20] Dorrell DG, Knight AM, Evans L, Popescu M. Analysis and design techniques applied to hybrid vehicle drive machines—Assessment of alternative IPM and induction motor topologies. Industrial Electronics, IEEE Transactions on. 2012;59(10):3690-3699
- [21] Mishra P, Saha S. Design modeling and simulation of low voltage squirrel cage induction motor for medium weight electric vehicle. In: Advances in Computing, Communications and Informatics (ICACCI), 2013 International Conference on, 2013. pp. 1697-1704
- [22] Chino S, Ogasawara S, Miura T, Chiba A, Takemoto M, Hoshi N. Fundamental characteristics of a ferrite permanent magnet axial gap motor with segmented rotor structure for the hybrid electric vehicle. In: 2011 IEEE Energy Conversion Congress and Exposition. 2011. pp. 2805-2811

- [23] Liu Y, Zhao J, Wang R, Huang C. Performance improvement of induction motor current controllers in field-weakening region for electric vehicles. IEEE Transactions on Power Electronics. 2013;28(5):2468-2482
- [24] Kiyota K, Kakishima T, Chiba A. Comparison of test result and design stage prediction of switched reluctance motor competitive with 60-kW rare-earth PM motor. Industrial Electronics, IEEE Transactions on. 2014;61(10):5712-5721
- [25] Niazi P, Toliyat HA, Dal-Ho C, Jung-Chul K. A low-cost and efficient permanent-magnetassisted synchronous reluctance motor drive. Industry Applications, IEEE Transactions on. 2007;43(2):542-550
- [26] Niazi P, Toliyat HA. Permanent magnet assisted synchronous reluctance motor, design and performance improvement, College Station, Tex.: Texas A&M University, 2006. [Online]. Available: http://hdl.handle.net/1969.1/3178
- [27] Vagati A, Pastorelli M, Francheschini G, Petrache SC. Design of low-torque-ripple synchronous reluctance motors. Industry Applications, IEEE Transactions on. 1998;34(4):758-765
- [28] Moghaddam RR, Gyllensten F. Novel high-performance SynRM design method: An easy approach for a complicated rotor topology. IEEE Transactions on Industrial Electronics. 2014;61(9):5058-5065
- [29] Pellegrino G, Cupertino F, Gerada C. Automatic Design of Synchronous Reluctance Motors Focusing on barrier shape optimization. Industry Applications, IEEE Transactions on, 2015;51(2):1465-1474
- [30] Ferrari M, Bianchi N, Doria A, Fornasiero E. Design of synchronous reluctance motor for hybrid electric vehicles. In: Electric Machines & Drives Conference (IEMDC), 2013 IEEE International. 2013. pp. 1058-1065
- [31] Barcaro M, Pradella T, Furlan I. Low-torque ripple design of a ferrite-assisted synchronous reluctance motor. IET Electric Power Applications. 2016;10(5):319-329
- [32] Khan KS. Design of a Permanent-Magnet Assisted Synchronous Reluctance Machine for a Plug-In Hybrid Electric Vehicle. School of Electrical Engineering, KTH, Stockholm, Sweden: Electrical Machines and Power Electronics; 2011
- [33] Carvajal Almendros C. Design and Analysis of a Fractional-Slot Concentrated-Wound Permanent-Magnet-Assisted Synchronous Reluctance Machine. Electrical Engineering, KTH Royal Institute of Technolog, Stockholm, Sweeden: Electronic Power Engineering; 2015
- [34] Wang Y, Bacco G, Bianchi N. Geometry analysis and optimization of PM-assisted reluctance motors. IEEE Transactions on Industry Applications. 2017;53(5):4338-4347
- [35] Bianchi N, Fornasiero E, Carraro E, Bolognani S, Castiello M. Electric vehicle traction based on a PM assisted synchronous reluctance motor. In: Electric Vehicle Conference (IEVC), 2014 IEEE International. 2014. pp. 1-6

- [36] Torres CL, Michalski T, Espinosa AG, Romeral L. Fast optimization of the magnetic model by means of reluctance network for PMa-SynRM. In: IECON 2016 - 42nd Annual Conference of the IEEE Industrial Electronics. Society. 2016. pp. 1642-1647
- [37] Torres CL, Garcia A, Riba J, Romeral L. Design and optimization for vehicle driving cycle of rare-earth-free SynRM based on coupled lumped thermal and magnetic networks. IEEE Transactions on Vehicular Technology. 2017;99:1-1
- [38] Lopez Torres C, Michalski T, Garcia A, Romeral L. Rotor of Synchronous Reluctance Motor optimization by means reluctance network and genetic algorithm. ed. Electrical Machines and Systems (ICEMS), 2016
- [39] Barcaro M, Meneghetti G, Bianchi N. Structural analysis of the interior PM rotor considering both static and fatigue loading. IEEE Transactions on Industry Applications. 2014; 50(1):253-260
- [40] Cupertino F, Palmieri M, Pellegrino G. Design of high-speed synchronous reluctance machines. In: 2015 IEEE Energy Conversion Congress and Exposition (ECCE). 2015. pp. 4828-4834
- [41] Babetto C, Bacco G, Bianchi N. Analytical approach to determine the power limit of highspeed synchronous reluctance machines. In: 2017 IEEE International Electric Machines and Drives Conference (IEMDC). 2017. pp. 1-7