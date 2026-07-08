Special Issue: Permanent-Magnet Synchronous Reluctance Machines and their Applications

![](_page_0_Picture_2.jpeg)

# Fast synthesis of permanent magnet assisted synchronous reluctance motors

ISSN 1751-8660 Received on 8th June 2015 Revised on 3rd November 2015 Accepted on 7th December 2015 doi: 10.1049/iet-epa.2015.0240 www.ietdl.org

Nicola Bianchi<sup>1</sup>, Hanafy Mahmoud<sup>1,2</sup> ⋈, Silverio Bolognani<sup>1</sup>

<sup>1</sup>Department of Industrial Engineering, University of Padova, 35131 Padova, Italy <sup>2</sup>Electrical Power and Machines Department, Cairo University, 12613 Giza, Egypt 

⊠ E-mail: eng.hanafy4@yahoo.com

Abstract: This paper describes a procedure for a practical synthesis of both a synchronous reluctance motor and a permanent magnet assisted synchronous reluctance motor. The procedure is completely analytical, yielding a rapid drawing of the motor geometry, taking into account both magnetic and mechanical considerations. From the application requirements, the external volume of the motor is computed. The further practical needs, such as maximum outer space, maximum available length, existing stator lamination, and so on are considered. Then, the design of the rotor geometry is carried out. The PM size is determined considering the demagnetisation limit according to the maximum current loading.

#### 1 Introduction

The synchronous reluctance (REL) machine is becoming of great interest in the last years, due to two key reasons: (i) the increase of rare earth permanent magnet (PM) cost and (ii) the increasing request of high-efficiency machines. Therefore, the REL motor and the ferrite PM assisted REL (PMAREL) motor are becoming competitors of both surface-mounted PM machines and induction machines in many applications [1]. Such motors are also becoming particularly interesting when the control is based on the sensorless rotor position detection [2–4].

A sketch of a four-pole synchronous REL rotor with three flux barriers per pole is shown in Fig. 1. The synchronous PMAREL motor is achieved when PMs are inset within the flux barriers [5, 6]. The PMs are introduced into the flux barriers to the aim of saturating the iron ribs, increasing the power factor (PF), which is quite low in the REL machines.

Even if there is a great interest in this kind of machines, there is a poor knowledge about their design, e.g. about the effective size for a given torque and how to select the rotor geometry. To fill this gap, this paper aims to give useful suggestions for reaching a preliminary motor geometry, needed for a fast comparison with other motor types or as starting point for a successive optimisation.

At first, the stator size is estimated adopting a torque density factor derived from past experience. The proper stator has to be characterised by a number of slots per pole per phase greater than two and a distributed winding, so as to reduce the stator magneto-motive force (MMF) harmonics, avoiding a high torque ripple. In the following, the stator is selected with three slots per pole per phase and a distributed winding.

The attention is mainly focused on the rotor geometry, that is, on the flux barriers geometry. There is a high influence of such a geometry on the machine capability, as far as both average torque and ripple are concerned [7]. To achieve a high rotor saliency, the number of flux barriers per pole ranges between two and four. Hereafter, a rotor with three flux barriers per pole will be referred to. Their thickness is computed from magnetic considerations, as will be shown in Section 4. Magnetic ribs are determined according to the centrifugal forces on the rotor islands bordered by the flux barriers themselves (Section 5). PMs are inset in each flux barrier to assist the REL motor. The width of the PMs is linked to the magnetic flux in the air gap (Section 6). The thickness of each

PM is selected accordingly to prevent the irreversible demagnetisation due to the maximum current reaction (Section 7).

#### 2 Determination of the main motor dimensions

The determination of the main dimensions of the REL motor (outer stator diameter  $D_{\rm e}$  and the stack length  $L_{\rm stk}$ ) is based on the past experience about this kind of machines. Being the rated torque  $T_n$  of the machine related to the active volume, the adopted procedure is based on the ratio between the torque and the outer volume of the machine itself. To this aim the factor  $k_{\rm TV}$  is defined, which corresponds to this ratio.

The air gap volume is typically related to the rated motor torque, since the tangential (shear) stress due to the interaction between the electric and magnetic fields occurs at the air gap surface. However, the volume considered here refers to the outer diameter. For the application point of view, the outer volume has a more direct link with the machine size.

Since the ratio between outer and inner stator diameters,  $D_{\rm e}$  and  $D_{\rm i}$ , respectively, changes with the machine dimensions (small size machines exhibit a  $D_{\rm e}$ -to- $D_{\rm i}$  ratio larger than large size machines), it results that the factor  $k_{\rm TV}$  also depends on the rated torque. Anyway, for typical application requirements, e.g. rated torque in the range between 5 and 50 N m, a proper value (expressed in N m over litre) is

$$k_{\rm TV} \simeq 10 \,\mathrm{N}\,\mathrm{m}/\mathrm{l}$$
 (1)

Table 1 shows the computation of the factor  $k_{\rm TV}$  for different motors used in the literature. It is noted that the value of  $k_{\rm TV}$  is within the range between 8 and 12 N m/l. This range depends on the cooling effectiveness.

Once the outer volume is fixed,  $D_{\rm e}$  and  $L_{\rm stk}$  are segregated on the basis of further practical needs, such as maximum outer space, maximum available length, existing stator lamination, and so on.

## 3 Selection of the ends of the flux barriers

The selection of the ends of the flux barriers is a design step requiring a particular care. Even if such a choice affects only marginally the

<span id="page-1-0"></span>![](_page_1_Picture_1.jpeg)

Fig. 1 Synchronous reluctance rotor

**Table 1** Determination of the factor  $k_{TV}$  in different cases of the literature

| $D_{\rm e}$ , mm | $L_{\rm stk}$ , mm | $T_n$ , N m | $k_{\text{TV}}$ , N m/l | Reference |
|------------------|--------------------|-------------|-------------------------|-----------|
| 72               | 60                 | 2.4         | 9.82                    | [8]       |
| 112              | 40                 | 4.5         | 11.42                   | [9]       |
| 150              | 105                | 18          | 9.7                     | [10]      |
| 135              | 60                 | 7           | 8.2                     | [11]      |
| 200              | 70                 | 20          | 9.1                     | [11]      |
| 340              | 250                | 260         | 11.45                   | [11]      |
| 125              | 27                 | 2           | 6                       | [11]      |
| 203.2            | 133.4              | 57.3        | 13.2                    | [12]      |
| 203.2            | 133.4              | 35          | 8.1                     | [12]      |

average torque in a multi-flux-barrier machine, it plays a very important role in the torque ripple production.

There are some techniques proposed in the literature to reduce the torque ripple in synchronous REL machines [13–16]. The rotor skewing can be considered to reduce the ripple, even if this technique is not enough to smooth completely the torque [7]. Another strategy consists of introducing a slight shift of the flux barriers [17, 18] or adopting two different flux-barrier geometries in the same lamination [19, 20], so as to compensate the impact of the stator MMF harmonics [21, 22]. The resulting motor is referred to as 'Machaon' motor. Several optimisations were carried out to the purpose of smoothing the torque and several solutions can be found [23–25].

In [26], a relationship is suggested, linking the number of stator slots per pole pair  $n_s = Q_s/p$  to the number of equivalent rotor slots per pole pair  $n_t$ , that is

$$n_r = n_s \pm 4 \tag{2}$$

The flux-barrier ends (actual or fictitious) are assumed to be equi-spaced along the rotor periphery. Even if this technique does not always give the solution with the lowest torque ripple [19, 27], it provides a good starting point in the rotor geometry definition. Among the others, the main advantage is that the position of the rotor flux barriers can be determined analytically. It results to be a good starting point for the design. A successive optimisation can be used to refine the geometry.

## 4 Selection of the flux-barrier geometry

For the purpose of taking into account the thickness of the flux barrier, which affects the level of machine saturation, a coefficient  $k_{\text{air}}$  [28] has been defined as

$$k_{\rm air} = \frac{\sum_{i} t_{\rm bi}}{(D_{\rm r} - D_{\rm sh})/2}$$
 (3)

where the term  $t_{bi}$  is the thickness of the *i*th flux barriers,  $D_{\rm r}$  is the external rotor diameter, and  $D_{\rm sh}$  is the shaft diameter.

Coefficient  $k_{\rm air}$  has to be chosen according to the stator tooth width and back-iron height. It is possible to define a coefficient  $k_{\rm air,s} = (p_{\rm s} - w_{\rm t})/p_{\rm s}$  in which  $p_{\rm s}$  is the stator slot pitch, defined as  $p_{\rm s} = \pi \ D_{\rm i}/Q_{\rm s}$ , and  $w_{\rm t}$  is the stator tooth width. The  $k_{\rm air}$  of the rotor should be close to the  $k_{\rm air,s}$  of the stator, so as the machine results to be equally saturated. For the purpose of limiting the iron losses,  $k_{\rm air}$  should be slightly higher than  $k_{\rm air,s}$ . A too high value causes a decrease of torque and power since the rotor path limits the flux along the d-axis direction [28]: the stator iron path is characterised by a lower flux density (since it is limited by the rotor) so that the stator iron losses decrease, while both PF and efficiency do not exhibit considerable variations with  $k_{\rm air}$ .

Once the total rotor iron width has been decided, the width of each rotor iron path is computed referring to the flux density distribution of the d-axis flux. As shown in Fig. 2a, the width of the rotor path  $w_{r_p}$  results to be proportional to the average flux density in that path. The width  $w_{r_{r_i}}$  of ith path (with i = 1, 2, 3, and 4) is given by

$$w_{r_{pi}} = (1 - k_{air}) \left[ \frac{D_{r} - D_{sh}}{2} \right] \frac{1 / \left(\theta_{b_{i+1}}^{e} - \theta_{b_{i}}^{e}\right) \int_{\theta_{b_{i}}^{e}}^{\theta_{b_{i+1}}^{e}} \sin \theta^{e} d\theta^{e}}{1 / (\pi / 2) \int_{0}^{\pi / 2} \sin \theta^{e} d\theta^{e}}$$
(4)

where  $2\theta_{b_i}^e$  is the electrical angle of the *i*th flux-barrier end (i = 1, 2, and 3 in the example), as shown in Fig. 2a. Let us note that superscript 'e' is used for electrical angles.

The profiles of the barriers are based on the potential lines of the magnetic field [5, 29, 30], as in Fig. 2b. This lines are described in polar coordinates by

$$c = \sin(p\theta) \frac{(2r/D_{\rm sh})^{2p} - 1}{(2r/D_{\rm sh})^p}$$
 (5)

and

$$r = \frac{D_{\rm sh}}{2} \left[ \frac{c + \sqrt{c^2 + 4\sin^2(p\theta)}}{2\sin(p\theta)} \right]^{1/p}, \quad 0 \le \theta \le \frac{\pi}{p}$$
 (6)

where r and  $\theta$  are the radius and angle of a point on the potential line. Each barrier is defined by three potential lines, as shown in Fig. 2b [31]. The central potential line is defined by substituting the barrier end angle and the outer rotor radius  $D_{r}/2$  in (5). The radius of the mid-point of this line is computed at angle  $\pi/2p$  from (6). Then, depending on the barrier thickness, the upper and lower points surrounding the mid-point of the barrier are computed. After that, by substituting these points in (5), the potential lines of the barrier boarders can be obtained.

## 5 Computation of the iron rib thickness

The typical flux-barrier geometries are represented in Figs. 3a and c: a rectangular and a circular flux barrier. In Figs. 3b and d, there are the corresponding geometrical approximations. The rotor magnetic island between the flux barrier and the air gap is highlighted in grey colour. According to Fig. 3b, the cross-area section of the rotor island is

$$S_{\rm isl} = \frac{R_{\rm r}^2}{2} \left[ 2\theta_{\rm b} - \sin(2\theta_{\rm b}) \right] \tag{7}$$

and the cross-area section of the rotor island of Fig. 3d is two times the previous one.

The force acting on these rotor islands is the sum of the magnetic force and the centrifugal force.

The magnetic force is computed from the magnetic pressure  $B^2/(2\mu_0)$  on the rotor surface  $\theta_b D_r L_{\rm stk}$ , according to the air-gap flux

<span id="page-2-0"></span>![](_page_2_Figure_1.jpeg)

**Fig. 2** Sketch of a single pole of the REL motor which shows a Iron path width referring to the d-axis flux density distribution

b Drawing the flux barrier according to the potential lines of the rotor field

density B. A reasonable value for such a flux density is between 1 and 1.2 T. This value tends to overestimate the magnetic force, increasing the mechanical safety margin.

The centrifugal force is computed as  $m\omega_m^2 R_c$ , where  $m = \gamma S_{\rm isl} L_{\rm stk}$  is the mass of the iron island,  $\omega_m$  is the rotor speed, and  $R_c$  is the radius of the centre of gravity of the rotor island. It can be assumed to be about  $R_c = (D_{\rm rcos}\theta_{\rm b})/2$ . This is correct in case of the island of Fig. 3d, while it is slightly underestimated in case of the island of Fig. 3b. In commonly used lamination, the mass density  $\gamma$  is about 7800 kg/m<sup>3</sup>.

Referring to the circular flux barrier, the total force that the rotor ribs have to sustain is given by

$$F_{\rm r} = \theta_{\rm b} D_{\rm r} L_{\rm stk} \left\{ \frac{B^2}{2\mu_0} + \frac{\gamma D_{\rm r}^2 \omega_m^2 \cos \theta_{\rm b}}{4} \left[ 1 - \frac{\sin(2\theta_{\rm b})}{2\theta_{\rm b}} \right] \right\}$$
(8)

The tensile strength of non-oriented steel is in the range between 400 and 500 N/mm<sup>2</sup>. A safety factor between 2 and 3 is kept [32], so as to limit the strength of the rib  $\sigma_r$  to 150 and 200 N/mm<sup>2</sup>.

Finally, the total rib thickness corresponding to the flux barrier under study [32] is given by

$$\sum t_{\rm r} = \frac{F_{\rm r}}{\sigma_{\rm r} L_{\rm orb}} \tag{9}$$

#### 6 Selection of the PM width

The purpose of this section is to choose the width of the PM to be inset in each flux barrier. Such a PM width determines the magnetic flux of the PM  $(\phi_m)$ . Part of this flux flows through the iron ribs  $(\phi_{sat})$  up to saturate them, and the other part flows

![](_page_2_Picture_13.jpeg)

Fig. 3 Approximation of the region between the flux barrier and the air gap

- a Rectangular flux-barrier geometry
- b Geometrical approximation of the rectangular flux barrier
- c Circular flux barrier geometry
- d Geometrical approximation of the circular flux barrier

through the air gap  $(\phi_g)$  linking the stator winding. This is referred to as the no-load flux linkage due to the PM. The flux saturating the iron ribs  $(\phi_{sat})$  remains almost the same, while the air-gap flux  $(\phi_g)$  increases with the PM width. The PM widths are limited by the length of the flux barriers themselves. Starting from the PM remanence flux, that is,  $\phi_{rem} = B_{rem} w_m L_{stk}$ , it is useful to define an effective remanence flux  $\phi'_{rem}$  given by

$$\phi'_{\text{rem}} = \phi_{\text{rem}} - \phi_{\text{sat}} = B_{\text{rem}} w'_{m} L_{\text{stk}}$$
(10)

where  $B_{\rm rem}$  is the remanence flux density of the PM and  $w'_m$  is the effective PM width useful for the air-gap flux density. This is an useful trick to determine how much PM volume is lost due to the iron ribs (the actual PM flux-density will be computed later). Fig. 4 shows  $w'_m$ , as well as, the PM width  $\Delta w_m = w_m - w'_m$  lost to saturate the iron ribs whose total thickness is  $t_{\rm r}$ . It is

$$\Delta w_m = \frac{B_{\text{sat}}}{B_{\text{rown}}} t_{\text{r}} \tag{11}$$

where  $B_{\rm sat}$  is the saturation flux density in the iron ribs which ranges between 1.8 and 2 T. Using ferrite magnet, since  $B_{\rm rem} \simeq 0.35$  T, it is  $\Delta w_m \simeq 0.6 t_{\rm r}$ .

The computation of the PM widths is based on the air-gap flux density distribution at no load, as shown in Fig. 5. It is staircase distribution and it is approximated as a sine wave distribution. The average air-gap flux density  $(B_{\mathbf{g}_{i_{\text{avg}}}})$  in front to each *i*th flux barrier

![](_page_2_Figure_25.jpeg)

**Fig. 4** *PM* width and flux lines:  $\phi_g$  is the useful flux through the air gap and  $\phi_{sat}$  is the flux lost in the ribs

<span id="page-3-0"></span>![](_page_3_Figure_1.jpeg)

Fig. 5 Air-gap flux density distribution at no load for half pole

is given by

$$B_{g_{i_{avg}}} = \frac{1}{\theta_{b_i} - \theta_{b_{i-1}}} \int_{\theta_{b_{i-1}}}^{\theta_{b_i}} \hat{B}_g \cos(p\theta) d\theta$$
$$= \hat{B}_g \frac{\sin(\theta_{b_i}^e) - \sin(\theta_{b_{i-1}}^e)}{\theta_{b_i}^e - \theta_{b_i}^e}$$
(12)

where  $\hat{B}_{g}$  is the peak of the air-gap flux density at no load. Using ferrite PM, the flux in the air-gap is quite low. Therefore,  $\hat{B}_{g}$  is assumed to be  $\leq 0.1$  T.

Then, the average flux flowing through the air gap in front to the rotor island bordered by the ith flux barrier can be computed as

$$\phi_{g_i} = B_{g_{i_{ava}}} (l_{b_i} - l_{b_{i-1}}) L_{stk}$$
 (13)

where  $l_{b_i}$  is the length of *i*th flux barrier, which can be assumed to be

the same of the rotor arc in front of it, i.e.  $l_{b_i} \simeq \theta_{b_i} D_i$ . The computation procedure for the PM widths is based on a practical simplified magnetic network of the motor at no load. According to Fig. 6 showing a rotor with three flux barriers per pole, some assumptions are:

- the air-gap flux density in front to the rotor island bordered by the first flux barrier is referred to as  $\phi_{g_1}$ . This flux flows through a portion of the PMs in the three flux barriers, whose width is  $w'_{m1}$ , that is, the same effective width of the first PM.
- the remaining width of the second PM is  $(w'_{m2} w'_{m1})$ . The air-gap flux flowing between the first and the second flux-barrier ends is referred to as  $\phi_{\mathrm{g}_2}$ . It flows in the portions of PM of the second and third flux barriers, whose width is  $(w'_{m2} - w'_{m1})$ .
- similarly, the remaining width of the third flux barrier is  $(w'_{m3} w'_{m2})$ . The air-gap flux  $\phi_{g_3}$  flows through this remaining width.

![](_page_3_Figure_13.jpeg)

Fig. 6 Sketch of a rotor pole with approximated paths of the no load air-gap flux due to the different PMs

Fig. 7a shows the magnetic network corresponding to the first assumption: all PM widths are equal to  $w'_{m1}$  and there is no flux in the air-gap regions in front of the island bordered by the second and third flux barriers. Then, air-gap flux  $\phi_{g_1}$  can be easily computed. From Fig. 7b, the air-gap flux in front to the second flux barrier  $\phi_{g_2}$  can be computed in the similar way. The general equation of air-gap flux corresponding to the portions of air gap in front to the island bordered by the ith flux barrier is

$$\phi_{g_i} = \frac{\phi'_{\text{rem}_i} R_{m_i}}{R_{g_i} + R_{m_i}}$$
 (14)

where  $R_{g_i}$  is the magnetic reluctance corresponding to the portions of air gap in front to the *i*th flux barrier and  $R_{m_i}$  is the magnetic reluctance of the ith PM. They are given by

$$R_{g_i} = \frac{g}{\mu_{\circ}(l_{b_i} - l_{b_{i-1}})L_{\text{stk}}}$$
 and  $R_{m_i} = \frac{t_{b_i}}{\mu_{\circ}l_{m_i}L_{\text{stk}}}$  (15)

By substituting (12), (13), and (15) in (14),  $w'_m$  can be computed as

$$w'_{m_i} = \left[ \frac{B_{\text{rem}} t_{b_i}}{B_{\text{rem}} t_{b_i} - B_{\text{avg}_i} g} \right] \left[ w'_{m_{i-1}} + (l_{b_i} - l_{b_{i-1}}) \frac{B_{\text{avg}_i}}{B_{\text{rem}}} \right]$$
(16)

Finally, the total width of the *i*th PM is given by

$$w_{m_s} = w'_{m_s} + \Delta w_{m_s} \tag{17}$$

## Computation of the PM thickness

The stress on the PMs caused by the flux due to the stator current has to be computed to check if the PM thickness is enough to avoid the PM demagnetisation or not (i.e. the flux density of PM operating point is higher than the flux density at knee point  $B_{\rm knee}$ ). The worst condition is when the stator current (referred to as the demagnetisation current) produces a flux completely against the PM flux. The flux due to the current is computed applying the superposition of the effect: the PMs are removed and the computation is carried out on a REL motor. The actual PM flux density is achieved by subtracting the demagnetisation current flux density from the no-load flux density.

An analytical approach based on the magnetic network is used to compute the PM stress. The network is simplified using appropriate assumptions so as to enable the designer to predict the PM stress by using practical equations. Fig. 8 shows the sketch of one rotor pole with three flux barriers of a REL motor and Fig. 9 shows the corresponding magnetic network.

To maximise the average torque in REL and PMAREL machines, the air-gap thickness is kept as low as possible and the flux-barrier thickness is designed quite high so as to limit the q-axis flux (i.e. to increase the rotor saliency). It results that the reluctance corresponding to the portions of air gap in front to the island bordered by the ith flux barrier is negligible with respect to the ith flux-barrier reluctance itself. Therefore, the complete magnetic network shown in Fig. 9 can be simplified by neglecting the reluctances  $R_{g_i}$ . The flux flowing in the *i*th flux barrier is directly computed as

$$\phi_{b_i} = \frac{U_{s_i} - U_{s_{i+1}}}{R_{b_i}} \tag{18}$$

In addition, the general equation of the stress on the PMs is given by

$$B_{b_i} = \frac{\mu_{o}}{t_{b_i}} \left( U_{s_i} - U_{s_{i+1}} \right) \tag{19}$$

<span id="page-4-0"></span>![](_page_4_Picture_1.jpeg)

Fig. 7 Magnetic networks at no load according to

a First assumption

b Second assumption, described in the text

where  $U_{\mathbf{s}_i}$  is the average value of the stator magnetic potential in front of each *i*th flux barrier. Assuming a stator MMF with sinusoidal waveform, as in Fig. 8 it is given by

$$U_{s_{i}} = \frac{1}{\theta_{b_{i}} - \theta_{b_{i-1}}} \int_{\theta_{b_{i-1}}}^{\theta_{b_{i}}} \hat{U}_{s} \cos(p\theta) d\theta$$

$$= \hat{U}_{s} \frac{\sin(\theta_{b_{i}}^{e}) - \sin(\theta_{b_{i-1}}^{e})}{\theta_{b_{i}}^{e} - \theta_{b_{i-1}}^{e}}$$
(20)

From (19), the stress on the PMs depends on the electrical loading and flux-barrier thickness. Therefore, in order to avoid the demagnetisation of the PMs or to reduce the stress on the PMs, the flux-barrier thickness should be increased. Since  $R_{g_i}$  have been neglected, the flux density stress is overestimated, that means a high safety margin.

According to the rotor design technique [7, 33, 34], rotor with equal space between rotor equivalent slots per pole pair  $(n_r)$  is selected. The magnetic stress on the PM is given by

$$B_{b_i} = \frac{\mu_{\circ} \hat{U}_s}{t_{b_i}} \left[ \frac{2\sin(k_i \Delta \theta_b^e) \left[1 - \cos(\Delta \theta_b^e)\right]}{\Delta \theta_b^e} \right]$$
(21)

where  $\Delta \theta_b^c$  is the electrical angle between each two equivalent rotor slots, given by  $\Delta \theta_b^c = 2\pi/n_r$ , and  $k_i$  is a constant depending on the rotor geometry. As in [7], there are no virtual points if  $n_r/2$  is even and  $k_i = 0.5$ , 1.5, 2.5. On the contrary, there are virtual points if  $n_r/2$  is odd and  $k_i = 1, 2, 3$ .

![](_page_4_Picture_11.jpeg)

Fig. 8 Sketch of one pole of REL motor with three flux barriers per pole

Let  $B_{mo_i}$  be the no-load flux density in the PM inset in the *i*th flux barrier. Let  $B_{bn_i}$  be the stress on the *i*th flux barrier at rated current (*n* is added as subscript). Then, the maximum overload current which causes the PM irreversible demagnetisation is given by

$$I_{\text{demg}} = I_n \frac{B_{mo_i} - B_{\text{knee}}}{B_{mo_i} - B_{\text{bn}_i}}$$
 (22)

where  $B_{\rm knee}$  is the flux density at the knee point.

## 8 Example

The design procedure described above is applied hereafter to determine the main dimensions of a PMAREL motor. The required nominal torque  $T_{\rm N}$  and speed  $n_{\rm N}$  are 12.5 N m and 5000 rpm, respectively.

As stated above, a torque density  $k_{\rm TV} \simeq 10$  N m/l is assumed to determine the outer stator volume. Then,  $D_{\rm e}^2 L_{\rm stk}$  is computed and it is equal to 0.00159 m<sup>3</sup>.

From the application needs, the external diameter of the motor  $D_{\rm e}$  is selected to be 200 mm. Consequently, the stack length of the motor results in 40 mm. The inner diameter  $D_{\rm i}$  of the stator is estimated to be equal to  $D_{\rm i} \simeq 0.6 D_{\rm e}$  resulting in 120 mm. Rather than a custom stator geometry, a commercial lamination is selected according to  $D_{\rm e}$  and  $D_{\rm i}$ . The selected commercial lamination is a MEC 132 for a four-pole machine. Its geometrical data are given in Table 2.

The design of the rotor is a crucial point. It is split into six steps. The first step is to determine the end points of the flux barriers. A number of three flux barriers per pole is chosen. As a preliminary choice, rotor geometry with equal spaced equivalent slots per pole pair is selected, as suggested in [7]. The number of stator slots per pole pair is  $n_s = 18$ , then  $n_r$  is computed as in (2) and it is equal to 14. Then, the rotor of this example can be expressed as shown in Fig. 10. Referring to [7], it can be defined as a 'complete' rotor with one 'virtual' point. Hence,  $k_i = 1$ , 2, 3. Then, the angular distance between each two points is  $\Delta \theta_b^c = 25.71^\circ$ , and hence,  $\theta_{b_1}^c$ , and  $\theta_{b_3}^c$  are equal to 25.71°, 51.42°, and 77.13°, respectively.

![](_page_4_Figure_21.jpeg)

Fig. 9 Magnetic network of REL motor, referring to one pole with three flux barriers

<span id="page-5-0"></span>Table 2 Geometrical data of the commercial lamination MEC 132 for a four-pole machine

| external stator diameter | $D_{\rm e}$  | 200  | mm |
|--------------------------|--------------|------|----|
| inner stator diameter    | $D_{\rm i}$  | 125  | mm |
| number of slots          | $Q_{\rm s}$  | 36   |    |
| tooth width              | $w_{t}$      | 6    | mm |
| slot height              | $h_{\rm s}$  | 17.5 | mm |
| slot opening height      | $h_{\rm so}$ | 0.5  | mm |
| slot opening width       | $W_{so}$     | 2.5  | mm |
|                          |              |      |    |

![](_page_5_Figure_3.jpeg)

**Fig. 10** Sketch of a rotor pole with three flux barriers per pole, equally spaced flux-barrier ends and different types of the iron ribs

The second step deals with the computation of the flux-barrier thickness, according to the coefficient  $k_{\rm air}$  which is fixed to 0.45. The total air thickness is computed and then it is split into the three barriers. According to the position of the barrier ends, rotor iron paths are computed from (4), then the barrier thicknesses  $t_{\rm b1}$ ,  $t_{\rm b2}$ , and  $t_{\rm b3}$  are chosen to be 3, 6, and 10 mm, respectively.

The third step is the computation of the flux barriers length. Starting from the barrier ends and the outer rotor diameter, the lengths area  $l_{\rm b_1}=28$  mm,  $l_{\rm b_2}=56$  mm, and  $l_{\rm b_3}=84$  mm.

The fourth step is the computation of the iron rib thickness. Fig. 10 shows the positions of the rotor iron ribs. It is worth noting that the minimum thickness of the rib should be equal to the thickness of the lamination, e.g. 0.4 mm for a lamination thickness of 0.35 mm. The outer iron ribs (at the end of each flux barrier) are set equal to the minimum practical thickness since these ribs have a limited mechanical capacity. The thickness computed using (8) and (9) yields 0.1, 0.33, and 0.72 mm for the first, second, and third barrier ribs, respectively. Then, the inner iron ribs of the first flux barrier (the shortest one) can be omitted considering that the two ribs at the barrier ends are enough ( $t_{r_1} = 0.8$  mm). The total iron rib thicknesses for the second and third barriers are split into four ribs whose thickness is fixed to 0.4 mm, i.e. two ribs for the outer iron ribs and two ribs for the inner iron ribs, as shown in Fig. 10, according to the minimum practical constraint. Thus, the total thickness of the iron ribs results in  $t_{r_2} = 1.6$  mm and  $t_{r_3} = 1.6$  mm.

The fifth step is the computation of the PMs widths. From (16) and (17), they result  $w_{m_1}=13$  mm,  $w_{m_2}=25$  mm, and  $w_{m_3}=29$  mm, respectively.

The sixth step is the computation of the maximum magnetic stress on each PM. This stress depends on the electrical loading  $\hat{K}_s$  of the motor which is linked to the conductor current density  $J_s$ . In aircooled machines, the recommended current density ranges between  $6 \, \text{A/mm}^2$  (for continuous duty) and  $9 \, \text{A/mm}^2$  (for intermittent duty). The current density  $J_s$  is selected to be equal to  $6 \, \text{A/mm}^2$ , the electrical loading  $\hat{K}_s$  resulting in 33500 A/m.

From (19) or (21), the maximum stress on the first, second, and third flux barriers are 0.107, 0.094, and 0.069 T, respectively. The PM operating points are  $B_{m_1} = 0.200$ T,  $B_{m_2} = 0.213$ T, and  $B_{m_3} = 0.238$  T,

![](_page_5_Figure_11.jpeg)

**Fig. 11** Flux density map of PMAREL motor with electrical loading  $\hat{K}_s = 42500$  A/m at rotor position  $\theta_m = 0^\circ$ 

![](_page_5_Figure_13.jpeg)

**Fig. 12** Experimental torque in a REL motor prototype b PMAREL motor prototype

<span id="page-6-0"></span>respectively. It is possible to verify that all operating points of the PMs are above the knee point  $B_{\rm knee} \simeq 0.1$  T. Therefore, the thickness of the PMs is enough for this electrical loading. It was also verified that the maximum electrical loading which causes a PM irreversible demagnetisation is equal to 290% of the nominal current, computed from (22).

Once defined the rotor geometry, it has been verified by means of a finite-element analysis, [35]. A flux density map is shown in Fig. 11. The resulting average torque is 12.47 N m and the torque ripple is around 26%. Consequently, this result highlights that the proposed design procedure rapidly yields a satisfactory initial motor sizing. Then, the rotor has been optimised adopting finite-element method to reduce the torque ripple.

The optimisation mainly focused on the position of the flux-barrier ends. After that, two motors prototypes, a synchronous REL motor and a PMAREL motor were manufactured. Fig. 12 shows the measured torque of two motor prototypes at rated current.

#### 9 Conclusions

A rapid procedure to estimate the main dimensions of a synchronous reluctance motor, with or without the assistance of a PM, is fully described in the paper.

A practical torque density factor is given so as the motor size is rapidly determined. According to the practical approach followed by the industry, the geometry of the stator lamination is selected from the geometries available of the induction motors.

On the contrary, the rotor required a deeper computation. Its geometry is achieved step-by-step, starting from the selection of the flux-barrier ends, lengths, and thicknesses. The iron ribs and PM sizes are determined according to centrifugal and magnetic forces, no-load flux density distribution, and stator current reaction, respectively. Finally, a practical example concludes the paper.

### 10 References

- Barcaro, M., Bianchi, N.: 'Interior PM machines using ferrite to substitute rare-earth surface PM machines'. Conf. Record of Int. Conf. of Electrical Machines, ICEM, Marsille (F), June 2012, pp. 1–7
- 2 Guglielmi, P., Pastorelli, M., Vagati, A.: 'Cross-saturation effects in IPM motors and related impact on sensorless control', *IEEE Trans. Ind. Appl.*, 2006, 42, (6), pp. 1516–1522
- Bianchi, N., Bolognani, S., Jang, J.-H., et al.: 'Comparison of PM motor structures and sensorless control techniques for zero-speed rotor position detection', IEEE Trans. Power Electron., 2007, 22, (6), pp. 2466–2475
- Trans. Power Electron., 2007, 22, (6), pp. 2466–2475
   Wang, L., Lorenz, R.D.: 'Rotor position estimation for permanent magnet synchronous motor using saliency-tracking self-sensing method'. Conf. Record of the 2000 IEEE Industry Applications, 2000, vol. 1, pp. 445–450
- of the 2000 IEEE Industry Applications, 2000, vol. 1, pp. 445–450

  Fratta, A., Vagati, A., Villata, F.: 'Permanent magnet assisted synchronous reluctance drive for constant-power application: drive power limit'. Proc. of Intelligent Motion European Conf., PCIM, Nurnberg, Germany, April 1992, pp. 196–203
- 6 Kim, W.H., Kim, K.S., Kim, S.J., et al.: 'Optimal PM design of PMA-SynRM for wide constant-power operation and torque ripple reduction', *IEEE Trans. Magn.*, 2009, 45, (10), pp. 4660–4663
- Vagati, A., Pastorelli, M., Francheschini, G., et al.: 'Design of low-torque-ripple synchronous reluctance motors', *IEEE Trans. Ind. Appl.*, 1998, 34, (4), pp. 758–765
- 8 Han, S.-H., Jahns, T.M., Soong, W.L.: 'Torque ripple reduction in interior permanent magnet synchronous machines using the principle of mutual harmonics exclusion'. Conf. Record of the 2007 IEEE Industry Applications, 2007, pp. 558–565
- 9 Imamura, K., Sanada, M., Morimoto, S., et al.: 'Improvement of demagnetization by rotor structure of IPMSM with Dy-free rare-earth magnet'. Proc. Int. Conf. on Electrical Machines, ICEM, October 2012, pp. 1–6

- 10 Guglielmi, P., Boazzo, B., Armando, E., et al.: 'Permanent magnet minimization in PM-assisted synchronous reluctance motors for wide speed range', *IEEE Trans. Ind. Electron.*, 2013, 49, (1), pp. 31–41
- Bianchi, N., Degano, M., Fornasiero, E.: 'Sensitivity analysis of torque ripple reduction of synchronous reluctance and interior PM motors', *IEEE Trans. Ind. Appl.*, 2015, 51, (1), pp. 187–195
- 12 Kamper, M.J., van der Merwe, F.S., Williamson, S.: 'Direct finite element design optimisation of the cageless reluctance synchronous machine', *IEEE Trans. Energy Convers.*, 1996, 11, (3), pp. 547–555
- 13 Fratta, A., Troglia, G.P., Vagati, A., et al.: 'Evaluation of torque ripple in high performance synchronous reluctance machines'. Conf. Record of the 1993 IEEE Industry Applications Society Annual Meeting, Toronto, Canada, October 1993, pp. 163–170
- 14 Jahns, T.M., Soong, W.L.: 'Pulsating torque minimization techniques for permanent magnet AC motor drives-a review', *IEEE Trans. Ind. Electron.*, 1996, 43, (2), pp. 321–330
- 15 Park, J.M., Kim, S.I., Hong, J.P., et al.: 'Rotor design on torque ripple reduction for a synchronous reluctance motor with concentrated winding using response surface methodology', *IEEE Trans. Magn.*, 2006, 42, (10), pp. 3479–3481
- Han, S.-H., Jahns, T., Soong, W., et al.: 'Torque ripple reduction in interior permanent magnet synchronous machines using stators with odd number of slots per pole pair', *IEEE Trans. Energy Convers.*, 2010, 25, (1), pp. 118–127
- Bianchi, N., Bolognani, S.: 'Reducing torque ripple in PM synchronous motors by pole shifting'. Proc. of Int. Conf. on Electrical Machines, ICEM, Helsinki, August 2000, pp. 1222–1226
- Sanada, M., Hiramoto, K., Morimoto, S., et al.: 'Torque ripple improvement for synchronous reluctance motor using an asymmetric flux barrier arrangement', IEEE Trans. Ind. Appl., 2004, 40, (4), pp. 1076–1082
- 19 Bianchi, N., Bolognani, S., Bon, D., et al.: 'Rotor flux-barrier design for torque ripple reduction in synchronous reluctance and PM-assisted synchronous reluctance motors', IEEE Trans. Ind. Appl., 2009, 45, (3), pp. 921–928
- 20 Ionel, D.: 'Interior permanent magnet motor including rotor with unequal poles'. US Patent, 8,102,091, 2102
- 21 Barcaro, M., Bianchi, N.: 'Torque ripple reduction in fractional-slot interior PM machines optimizing the flux-barrier geometries'. Int. Conf. on Electrical Machines (ICEM), 2012, September 2012
- 22 Alberti, L., Barcaro, M., Bianchi, N.: 'Design of a low torque ripple fractional-slot interior permanent magnet motor', *IEEE Trans. Ind. Appl.*, 2014, 50, (3), pp. 1801–1808
- 23 Pellegrino, G., Cupertino, F.: 'FEA-based multi-objective optimization of IPM motor design including rotor losses'. IEEE Energy Conversion Congress and Exposition (ECCE), September 2010
- 24 Bianchi, N., Degano, M., Fornasiero, E.: 'Sensitivity analysis of torque ripple reduction of synchronous reluctance and interior PM motors'. IEEE Energy Conversion Congress and Exposition (ECCE), September 2013
- 25 Sizov, G.Y., Zhang, P., Ionel, D.M., et al.: 'Modeling and analysis of effects of skew on torque ripple and stator tooth forces in permanent magnet AC machines'. IEEE Energy Conversion Congress and Exposition (ECCE), September 2012
- 26 Vagati, A.: 'Synchronous reluctance electrical motor having a low torque-ripple design'. US Patent 5,818,140, 6 October 1998
- 27 Moghaddam, R.R.: 'Rotor for a synchronous reluctance machine'. US Patent 13/ 230, 2011
- 28 Ferrari, M., Bianchi, N., Fornasiero, E.: 'Rotor saturation impact in synchronous reluctance and PM assisted reluctance motors'. IEEE Energy Conversion Congress and Exposition (ECCE), September 2013
- 29 Binns, K.J., Lawrenson, P.J., Trowbridge, C.W.: 'The analytical and numerical solution of electric and magnetic fields' (John Wiley and Sons, New York, 1992)
- 30 Moghaddam, R.R.: 'Synchronous reluctance machine (SYNRM) in variable speed drives (VSD) applications'. PhD dissertation, Stockholm, Sweden, 2011
- 31 Gamba, M., Pellegrino, G., Cupertino, F.: 'Optimal number of rotor parameters for the automatic design of Synchronous Reluctance machines'. International Conference on Electrical Machines (ICEM), Bernino (Germany), 2–5 Sept. 2014, pp. 1334–1340
- 32 Barcaro, M., Meneghetti, G., Bianchi, N.: 'Structural analysis of the interior PM rotor considering both static and fatigue loading', *IEEE Trans. Ind. Appl.*, 2014, 50, (1), pp. 253–260
- 33 Barcaro, M., Meneghetti, G., Bianchi, N.: 'Design of ferrite-assisted synchronous reluctance machines robust toward demagnetization', *IEEE Trans. Ind. Appl.*, 2014, 50, (3), pp. 1768–1779
- 34 Boazzo, B., Vagati, A., Pellegrino, G., et al.: 'Multipolar ferrite-assisted synchronous reluctance machines: a general design approach', *IEEE Trans. Ind. Electron.*, 2015, 62, (2), pp. 832–845
- 35 Meeker, D.: 'Finite Element Method Magnetics', Ver. 4.2 User's Manual, February 5, 2009. Available at http://www.femm.info/Archives/doc/manual.pdf