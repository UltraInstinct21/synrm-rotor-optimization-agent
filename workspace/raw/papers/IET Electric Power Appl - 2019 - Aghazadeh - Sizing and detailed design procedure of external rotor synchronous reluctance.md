![](_page_0_Picture_3.jpeg)

# **Sizing and detailed design procedure of external rotor synchronous reluctance machine**

ISSN 1751-8660 Received on 5th November 2018 Revised 7th February 2019 Accepted on 22nd March 2019 E-First on 13th May 2019 doi: 10.1049/iet-epa.2018.5802 www.ietdl.org

*Hadi Aghazadeh<sup>1</sup> , Ebrahim Afjei<sup>1</sup> , Alireza Siadatan<sup>2</sup>*

*<sup>1</sup>Department of Electrical Engineering, Shahid Beheshti University, Tehran, Iran*

**Abstract:** Finding an optimally designed synchronous reluctance machine with desired performance among all possible combinations of the stator and rotor with different shapes of barriers requires long execution time, which is an overwhelming task. Selecting the number of flux barriers, for instance, in accordance with the pre-designed stator has a significant effect on the torque ripple. To tackle these issues, this study presents a comprehensive design procedure of an external rotor synchronous reluctance machine suitable for an electric bike application that includes considerations such as electro-magnetic and mechanical aspects. Dimensions of the internal stator with tapered slots are calculated. Additionally, a global parameter, insulation ratio in the *q*-axis, is used to link the microscopic parameters. Seeking for the optimal design through the insulation ratio effectively reduced the number of geometric parameters involved in the rotor shape optimisation. The preliminary rotor design is used to run multi-objective optimisation to provide further improvement to the average torque and torque ripple. Utilising the finite-element method, thermal and structural analyses are conducted to guarantee the safe operation of the designed motor under a steady-state condition. Finally, measurement results of a 250 W-fabricated motor are compared with the predicted results, which validate the effectiveness of the proposed method.

# **1Introduction**

During the past decade, cost-effective synchronous reluctance machines (SynRMs) have been deployed as a promising alternative to induction machines, which offer higher efficiency and higher torque density [\[1\]](#page-7-0). Possessing augmented bore diameter, a SynRM with external rotor architecture (Ex-SynRM) has a wider stator slot area, which enhances the torque producing capability of the motor [[2](#page-7-0), [3](#page-7-0)]. This feature in adjunct to other advantages of the SynRM such as magnet-free, simple and rigid rotor structure make Ex-SynRM a suitable choice to in-wheel motors in electric vehicle applications and domestic appliances instead of costly permanent magnet machines [\[4](#page-7-0), [5](#page-7-0)].

However, since the introduction of the SynRM as the 'reaction synchronous motor' in 1923 by Kostko [\[6\]](#page-8-0), it has been recognised that the performance characteristics of this machine in terms of efficiency and power factor would not be good enough as long as its saliency ratio (the ratio of the machine's inductance along the two orthogonal *d*- and *q*-axes) is low. The SynRM produces reluctance torque by utilising two different flux paths along *d*- and *q*-axes in the rotor structure. Half-section view of a six-pole Ex-SynRM is shown in Fig. 1. In fact, the SynRM has a rotor with a geometrically complex structure because it has flux barriers, which involves many parameters to be dimensioned and optimised [[1](#page-7-0), [5](#page-7-0), [7](#page-8-0), [8](#page-8-0)]. Several research efforts have dedicated to tackle this issue and to reduce the number of parameters in the rotor design [\[9–11](#page-8-0)].

![](_page_0_Picture_13.jpeg)

designed stator geometry to alleviate the output torque ripple. **Fig. 1** *Scheme of an external rotor synchronous reluctance motor*

These studies intensively have focused on the barrier shape optimisation to improve different performance indices of the motor such as average torque, torque ripple, power factor, and efficiency. Although, optimal design studies on the Ex-SynRM are limited in the literature [[12,](#page-8-0) [13\]](#page-8-0). Indeed, contrary to immense interest in external rotor SynRM, the general analytical design studies on this subject are quite limited. Most of the investigations are based on precise results from finite element analysis (FEA) of some special cases, though these time-consuming FEA solutions lose generality [[3](#page-7-0)]. In order to deal with a lot of geometrical parameters involved in the design of the rotor and decrease the optimisation time, for both internal and external rotor SynRM, analytical studies have presented detailed magnetic lumped parameter models including the saturation effect [\[8,](#page-8-0) [14](#page-8-0), [15\]](#page-8-0). Although, FEA is finally used to correct the inaccuracy of the model and optimisation result.

On the other hand, the performance of the SynRM strongly relies on the interaction of stator magneto motive force (MMF) and magnetic anisotropy of the rotor [\[16](#page-8-0), [17](#page-8-0)]. Thus, the stator geometry has to be in accordance with the rotor's one in the machine design. The stator of the SynRM is conceptually similar to the stator of conventional synchronous machines and induction machines. Therefore, the stator design of the SynRM has received little attention from the researchers. The study is even scarcer when it comes to the stator design of a three-phase SynRM with external rotor architecture and distributed stator winding. Most of the works on the Ex-SynRM are related to the five-phase motor with the concentrated stator winding [\[5,](#page-7-0) [13](#page-8-0)].

To narrow this gap, the present study proposes a comprehensive design procedure, which addresses magnetic, electrical and mechanical considerations of both stator and rotor of the Ex-SynRM, concurrently. At first and based on the crucial constraints of the E-bike application, the volume envelop of the motor is estimated adopting both specific magnetic and electric loadings. Afterwards, considering various design aspects of the stator in a set of assigned parameters, internal stator dimensions are calculated. In the next step, the main focus is on the rotor design wherein the number of flux barriers is selected in accordance with the pre-

*<sup>2</sup>Department of Energy Systems, Faculty of Applied Science and Engineering, University of Toronto, Toronto, Canada E-mail: e-afjei@sbu.ac.ir*

<span id="page-1-0"></span>Secondly, according to the anisotropic nature of the rotor, a macroscopic geometric parameter, called insulation ratio in the *q*axis, is defined in a logically selected external rotor geometry. Utilising the insulation ratio effectively links the microscopic parameters. The optimal value of the insulation ratio is achieved by running a limited number of finite element sensitivity analyses. The main advantage of using the insulation ratio is the reduction of the number of cases, which have to be analysed through the optimisation process. The idea is to optimally shape the rotor barriers for a pre-designed stator. Assuming sinusoidal profiling of the air-gap flux density, a simple but accurate analytic method is used to determine the flux barriers and iron segments' widths on the rotor body. In addition, the effect of the end point angle of the barriers (rotor slot pitch) on the output torque ripple is considered. The preliminary design is used as a starting point to conduct a multi-objective optimisation process with different objectives.

# **2Relation between rating and dimensions of the machine**

A survey of the literature reveals that several attempts have done to relate the rating of SynRMs to their dimensions [\[16](#page-8-0), [18\]](#page-8-0). Two major dimensions of the machine are rotor bore diameter *D*so (m) and stator stack length *L* (m) with which the output power can be determined as [\[19](#page-8-0)]

$$Q = C_0(D_{so}^2 L) n_s, \tag{1}$$

where *n*<sup>s</sup> is the synchronous speed (rps) and the quantity *C*<sup>o</sup> is output coefficient, which is defined as follows:

$$C_{\rm o} = 11B_{\rm avg}ack_{\rm w} \times 10^{-3},\tag{2}$$

where *k*w is the winding factor, ac is the specific electric loadings, and *B*avg is the specific magnetic loading.

The number of stator ampere-conductors per metre of stator periphery at the air-gap is known as specific electric loadings (ac), which is presented by

$$ac = \frac{I_z Z}{\pi D_{so}},\tag{3}$$

where *I<sup>z</sup>* (A) is the current in each conductor, and *Z* is the total number of conductors. Accordingly, the average flux density over the air-gap of a machine is known as specific magnetic loading *B*avg (T) and it is defined by

$$B_{\text{avg}} = \frac{p\phi_{\text{m}}}{\pi D_{\text{so}}L} = \frac{\phi_{\text{m}}}{\tau L},\tag{4}$$

where *p* is the number of poles, *ϕ*m (wb) is the flux per pole and *τ* (m) is pole pitch, which is calculated as

$$\tau = \frac{\pi D_{\text{so}}}{p} \,. \tag{5}$$

The volume of the active part of the machine is (*π*/4)*D*2*L*. Thus, it is clear from (1) for a constant output power the volume of active parts is inversely proportional to the speed and the value of output coefficient. However, the maximum speed is limited practically, for instance, in the SynRM, the speed is limited by the mechanical stress on the rotor tangential ribs.

Specific magnetic loading and specific electric loading are two types of loadings generally used in the design of rotating electrical machines. According to (2), the output coefficient is proportional to the product of magnetic and electric loadings. Generally, the specific electric loading compared to the specific magnetic loading has a wider range of variation between different machine designs [[20\]](#page-8-0).

## *2.1 Assigned parameters*

As a first step in the sizing process of the SynRM, some initial data as assigned key parameters should be provided. These parameters are crucial in electrical, magnetic and geometric calculations in conjunction with the finite element method (FEM) analysis of the designed motor. They are introduced as follows:

- Stack aspect ratio: this ratio is defined as the ratio of the stator stack length and pole pitch, which leads to the stator outer diameter. The lower stack aspect ratio for a fixed value of stack length refers to a longer pole pitch, hence a larger stator outer diameter, which is suitable for low-speed applications such as Ebikes. However, to separate the value of *D*2*L* into its components, some additional data is required. In a certain circumstance, the application requirement dictates the value of the stator outer diameter or its stack length. Different relative values for different types of machines based on their operating characteristics can be defined. For instance, for a fixed number of poles, a stack aspect ratio with the value of one is suggested aimed at the generally suitable design [[19\]](#page-8-0).
- Current density *J* (A/m<sup>2</sup> ): the typical value of the current density is in the range of 2–5 A/m<sup>2</sup> . However, employing a cooling system equipped with water–glycol or oil jackets the current density can be increased up to 10 A/m<sup>2</sup> in traction applications [[16\]](#page-8-0).
- Specific magnetic loading: the maximum flux density in any part of the magnetic circuit must be below a certain value, depending on the material used in the lamination of the machine. Generally, in a well-designed machine, the maximum value of flux density occurs in the teeth of the stator (0.2 T ≤ *B*avg ≤ 0.8  T).
- Specific electric loading: a high value of specific electric loading mainly can be utilised where high temperature rise is allowed.
- Fill factor: the slot fill factor is defined by

$$k_{\text{fill}} = \frac{A_{\text{cu}}}{A_{\text{ss}}},\tag{6}$$

where *A*cu (m<sup>2</sup> ) is the total copper area and *A*ss (m<sup>2</sup> ) is the stator slot area. The winding loss mostly decreases by increasing the fill factor. A reasonable value of a fill factor for a neat wounded coil is between 0.3 and 0.4. Although, the value of 0.6 is achievable if the concentrated winding (CW) is used [[21\]](#page-8-0). Additionally, the value of the slot fill factor depends on the insulation thickness and shape of the conductors (rectangular or round).

- Power factor: the main drawback of the SynRM is the lowpower factor, especially when the motor operates along the maximum torque per-ampere trajectory [[20\]](#page-8-0).
- Convertor factor *k*vo: regarding the limitation in the output voltage of the voltage source inverter (VSI) the converter factor is considered in the range of 0.8–1.

The assigned parameters used in stator design of an external rotor (internal stator) SynRM is presented in Table [1](#page-2-0).

## **3Stator design**

## *3.1 Stator volume estimation*

Based on the required output power, speed and assumed magnetic and electric capability, it is thus possible to estimate the stator volume. Using (7) *Q* (kVA) rating of the machine is

$$Q = \frac{P_{\rm o}}{\eta p \cdot f},\tag{7}$$

where *P*<sup>o</sup> (kW) is the rated power, *η* is the efficiency, and *p·f* is the power factor.

**Table 1** Assigned parameters

<span id="page-2-0"></span>

| Parameter | Definition                         | Value           |
|-----------|------------------------------------|-----------------|
| Po        | rated power                        | 0.25 kW         |
| Ns        | rated speed                        | 520 rpm         |
| η         | efficiency                         | 80%             |
| p.f       | power factor                       | 0.6             |
| P         | number of pole pairs               | 3               |
| Bavg      | specific magnetic loading          | 0.7 T           |
| ac        | specific electric loading          | 12,000 A.turn/m |
| qs        | number of slots per pole per phase | 2               |
| L/τ       | stack length to pole pitch ratio   | 1               |
| L         | stack length                       | 50 mm           |
| J         | current density                    | 5 A/mm2         |
| kst       | laminations stacking factor        | 0.95            |
| kw        | winding factor                     | 0.955           |
| kvo       | converter factor                   | 0.8             |
| kfill     | slot fill factor                   | 0.45            |
| Vo        | DC link voltage                    | 48 V            |

Considering the given values of the stack aspect ratio and stack length, the outer diameter of the stator can be calculated as

$$\frac{L}{\tau} = 1 \Rightarrow D_{\text{so}} = \frac{pL}{\pi} \,. \tag{8}$$

As a deduction, output coefficient and specific electric loading are determined, using ([2](#page-1-0)) and [\(3\)](#page-1-0), respectively. The calculated value of the specific electric loading should be in the range of 8000–25,000  A.turn/m, otherwise the stack aspect ratio should be changed to satisfy the design requirement.

The stator design essentially refers to its magnetic and electric circuit design [\[22](#page-8-0)]. Therefore, at this step, stator-winding specifications such as phase current, number of turns and crosssection area of each conductor are required before the stator geometry calculation.

## *3.2 Ampere-turn per slot calculation*

The machine terminal has a delta connection and it is supplied by VSI, so the phase voltage is obtained by [\[22](#page-8-0)]

$$E_{\rm ph} = \frac{\sqrt{6}}{\pi} k_{\rm vo} V_{\rm o},\tag{9}$$

where *k*vo is the convertor factor and *V*<sup>o</sup> (V) is the DC link voltage. Hence, each phase current is

$$I_{\rm ph} = \frac{p_{\rm in}}{3E_{\rm ph}p \cdot f\eta} \,. \tag{10}$$

There are several advantages of utilising CW mentioned in the literature, some of which are short end winding and consequently lower Joule loss, high slot fill factor especially when a segmented stator structure is adopted, wide speed range of constant power, high efficiency, magnetically decoupled winding sets and easy to manufacture [[21\]](#page-8-0). However, the CW suffers from high-torque ripple and low-power factor. The high-harmonic content of MMF is introduced as the root cause of challenges for applying CW to SynRM [[21](#page-8-0)]. Furthermore, the increased harmonic content leads to higher eddy and hysteresis losses compared with the conventional sinusoidal distributed winding.

One the other side, the distributed overlapping winding produces a semi-sinusoidal shape MMF and most commonly, it is used in brushless ac machines. Therefore, considering practically the windings are distributed in the stator slots, the distribution factor *k*<sup>d</sup> is given by

$$k_{\rm d} = \frac{\sin(\delta/2)}{q_{\rm s}\cos(\delta/2q_{\rm s})},\tag{11}$$

where *δ* is the slot-pitch in electrical degrees. The slot-pitch for a three-phase winding will be presented as

$$\delta = \frac{\pi}{3q_{\rm s}},\tag{12}$$

where *q*<sup>s</sup> is the number of slots per pole per phase.

As depicted in [[23\]](#page-8-0) using chorded winding in SynRM will not necessarily reduce the amplitude of the low-order MMF rotating harmonics and generally, chording has a little effect on the torque ripple reduction. Moreover, it may reduce the machine output power by 7–12%. Therefore, the winding is considered without chording, *k*<sup>c</sup>  = 1.

Skewing the stator has been considered as one of the torque ripple reduction techniques but it is not a proper solution due to the reduction in the machine output torque [\[23](#page-8-0)]. Hence, the skew factor is taken as *k*<sup>s</sup>  = 1. In general, for a winding with distributed, chorded and skewed coils, the winding factor is defined as

$$k_{\rm w} = k_{\rm d}k_{\rm c}k_{\rm s}\,. \tag{13}$$

Therefore, the total number of turns per phase can be determined as

$$T_{\rm ph} = \frac{E_{\rm ph}}{4.44 \times f_{\rm s} \times \phi_{\rm m} \times K_{\rm w}},\tag{14}$$

where *E*ph (V) is the induced voltage per phase and the flux per pole is calculated by

$$\phi_{\rm m} = B_{\rm av} \times \tau \times L \,. \tag{15}$$

Assuming a constant current density, the cross-section area of each conductor for the calculated phase current *I*ph (A) is defined as

$$a_z = \frac{I_{\rm ph}}{J},\tag{16}$$

where *a<sup>z</sup>* (m<sup>2</sup> ) is the area of each conductor.

Therefore, the useful cross-section area of the slot is defined as

$$A_{\rm ss} = \frac{Z_{\rm s} a_z}{K_{\rm fill}},\tag{17}$$

where *Z*<sup>s</sup> is the total number of conductors per slot.

## *3.3 Stator dimensions' calculation*

Flux density in the tooth of the stator is related to the average flux density in the air-gap. A stator with tapered slots has parallel-sided teeth and therefore the tooth width is the same over the entire length of the tooth, which is shown in Fig. [2](#page-3-0).

Adopting an average tooth flux density *B*ts (*B*ts = 1.7 T), the tooth width *b*ts (m) can be determined as

$$b_{\rm ts} = \frac{p\phi_{\rm m}}{B_{\rm th}S_{\rm s}L_{\rm i}},\tag{18}$$

where *S*<sup>s</sup> is the number of slots and the useful length of stator *L*<sup>i</sup> (m) is calculated as

$$L_{\rm i} = k_{\rm st} L \,. \tag{19}$$

Assuming maximum flux density in the stator core (yoke) is *Bc*max (*Bc*max = 1.5 T), the core height *h*cs (m) can be obtained by

$$h_{\rm cs} = \frac{\phi_{\rm m}/2}{B_{\rm cmax}L_i}.$$
 (20)

<span id="page-3-0"></span>![](_page_3_Picture_1.jpeg)

**Fig. 2** *Stator dimensions with parallel-sided tooth and tapered slot*

**Table 2** Design parameters of stator

| Parameter | Definition               | Value    |
|-----------|--------------------------|----------|
| Dso       | stator outer diameter    | 120 mm   |
| Ass       | slot cross section area  | 29.5 mm2 |
| bs1       | slot width at the bottom | 2.7 mm   |
| bs2       | slot width at the top    | 5 mm     |
| bst       | stator tooth width       | 5 mm     |
| hs        | slot height              | 13.2 mm  |
| hcs       | stator core height       | 14.5 mm  |
| hs1       | slot opening height      | 3 mm     |
| hs2       | slot wedge height        | 2 mm     |
| bss       | slot opening width       | 2.5 mm   |

Next, the useful cross-section area of the slot shown in Fig. 2 is expressed as

$$A_{ss}(h_s) = \frac{1}{2}(b_{s1} + b_{s2})h_s, \tag{21}$$

where *b*s1 and *b*s2 are slot widths at the bottom and the top of the slot which can be expressed by (22) and (23), respectively

$$b_{\rm s1}(h_{\rm s}) = \frac{(D_{\rm so} - 2h_{\rm s1} - 2h_{\rm s2} - 2h_{\rm s})\pi}{S_{\rm s}} - b_{\rm ts},\tag{22}$$

$$b_{s2} = \frac{(D_{s0} - 2h_{s1} - 2h_{s2})\pi}{S_s} - b_{ts},$$
 (23)

where the slot height *h*<sup>s</sup> (m) is unknown in (21) and (22).

Substituting (22) and (23) into (21) gives a quadratic equation, which can be expressed by

$$ah_{\rm s}^2 + bh_{\rm s} + c = 0, (24)$$

where *a*, *b*, and *c* are the coefficients of the quadratic equation and they are defined as

$$a = \pi/S_{\rm s},\tag{25}$$

$$b = -b_{s2},$$
 (26)

$$c = A_{\rm ss} \,. \tag{27}$$

Solving (24) yields the slot height and consequently the slot width at the bottom. Therefore, all needed parameters to design the geometry of the stator are calculated. The calculated dimensions of the stator are listed in Table 2.

# **4Rotor design of Ex-SynRM**

The SynRM utilises the concept of anisotropy in the rotor structure along two orthogonal *d*- and *q*-axes to produce the reluctance torque. The output torque of SynRM is defined by

$$T_{\rm em} = \frac{3}{2} p (L_{\rm md} - L_{\rm mq}) i_{\rm md} i_{\rm mq} = \frac{3}{2} p (L_{\rm md} - L_{\rm mq}) I_{\rm m} \sin(2\gamma), \qquad (28)$$

where *L*m*d*and *L*m*<sup>d</sup>* are *d*- and *q*-axes components of the air-gap magnetising inductance, *i*m*<sup>d</sup>* and *i*m*d*are stator currents along the *d*and *q*-axes, *I*m is the stator current vector amplitude and *Ȗ* is the current angle.

Equation (28) implies the dependency of the developed torque to the difference of magnetising inductances. Therefore, the torque producing capability of the motor is directly related to the shape and position of the flux barriers in the rotor. However, working with several geometric parameters involved in the rotor structure to find an optimal geometry will be a time consuming process.

In order to connect the detailed geometric parameters of the rotor, the insulation ratio in the *q*-axis is defined as

$$k_{wq} = \frac{l_a}{l_y} = \frac{(D_{ro}/2) - (D_{so}/2) - g - \sum_{k=1}^{nb+1} S_k}{\sum_{k=1}^{nb+1} S_k},$$
 (29)

where *l<sup>a</sup>* (m) is the total insulation layers, *l<sup>y</sup>* (m) is the total iron segments, *D*ro (m) is the rotor outer diameter, *g* (m) is the air-gap length, and *S<sup>i</sup>* is the width of the *i*th flux carrier (iron segment) in the *q*-axis. The main goal is to find an appropriate procedure to size the flux barriers and consequently the segments in the rotor body for a specific number of barriers and a constant value of the insulation ratio.

### *4.1 Flux barrier shaping*

Among the different parameters, the barrier numbers and position of the barrier end points are of great importance in reducing the torque ripple [\[7\]](#page-8-0). Based on this issue, a relationship between the number of stator slots per pole pair (*n*<sup>s</sup> ) and the number of rotor slots per pole pair (*n*<sup>r</sup> ) is suggested in [[24\]](#page-8-0) as

$$n_{\rm s} - n_{\rm r} = \pm 4.$$
 (30)

The main rule is that the barrier number and its position have to be selected in accordance with the stator slot number. The number of stator slots per pole pair is 12, then the number of rotor slots per pole pair is equal to 8, which leads to two barriers in each pole of the rotor. The rationally shaped rotor geometry with two flux barriers in each pole and its geometric parameters are shown in Fig. [3.](#page-4-0)

To position the end point of the barriers, the rotor slot pitch is assumed to be constant. This means the flux barrier end points are distributed uniformly along the rotor periphery. In addition, to have an extra degree of freedom for adjusting the end points, an imaginary point with the angle of *ȕ* from the *q*-axis is considered. The parameter *ȕ*, which is called the rotor slot pitch angle controller, could be then optimised with the objective to minimise the torque ripple [[6](#page-8-0)]. Therefore, barrier end angle *α<sup>i</sup>* in the air gap should follow the rotor slot pitch *αm* which is expressed by

$$\alpha_i = \frac{1}{2}(2i-1)\alpha_m, \quad i = 1, ..., n_b,$$
 (31)

$$\alpha_m = (\pi/p - 2\beta)/(2n_b + 1),$$
 (32)

where *n*<sup>b</sup> is the number of barriers in the rotor per pole.

According to the method proposed in [\[25](#page-8-0)], a sinusoidal distribution of the stator MMF along the *d*- and *q*-axes is assumed. Hence, staircase functions of the stator MMF are calculated as the average per unit value of MMF over the iron segments. Distribution of MMF components in *d*- and *q*-axes for a rotor with

<span id="page-4-0"></span>![](_page_4_Picture_1.jpeg)

**Fig. 3** *One pole sketch of the proposed rotor with related parameters*

![](_page_4_Figure_3.jpeg)

**Fig. 4** *Distribution of per unit MMF (a)* MMF distribution along the *d*-axis, *(b)* MMF distribution along the *q*-axis

![](_page_4_Figure_5.jpeg)

**Fig. 5** *Effect of insulation ratio on the barrier geometry for (a) k*w*q* = 0.2, *(b) k*w*q* = 0.6, *(c) k*w*q* = 1.2

![](_page_4_Figure_7.jpeg)

**Fig. 6** *Average torque for different values of insulation ratio*

two barriers per pole is presented in Figs. 4*a* and *b*, respectively. A simple rule for the segment sizing assumes the width of the *i*th iron segment is directly proportional to the average *d*-axis MMF*<sup>d</sup>* [[7](#page-8-0)], then this rule is expressed by

$$\frac{S_{i+1}}{S_i} = \frac{f_{di+1}}{f_{di}}, \quad i = 1, ..., n_b,$$
(33)

where *fdi*is the average MMF over the *i*th segment due to MMF*<sup>d</sup>* .

In a similar way to the latter rule, a general rule of distribution of the total insulation between the barriers considers the flux

![](_page_4_Figure_13.jpeg)

**Fig. 7** *Developed torque profile for four different rotor slot pitch angle controller values*

barriers have constant and equal permeance, which is as follows [[7](#page-8-0)]:

$$\frac{p_i}{p_j} = (cte.) = 1 \Rightarrow \frac{W_{bi}}{W_{bi}} = \left(\frac{\Delta f_i}{\Delta f_1}\right)^2 \quad i = 2, ..., n_b$$
 (34)

$$\Delta f_i = f_{qi+1} - f_{qi} \tag{35}$$

where *p<sup>i</sup>* is the permeance of the *i*th barrier, *W*b*<sup>i</sup>* is the width of the *i*th flux barrier in the *q*-axis, and Δ*f<sup>i</sup>* is the differential average MMF over the *i*th barrier due to MMF*<sup>q</sup>* .

Now, *n*<sup>b</sup>  + 1 unknown width values of the segments can be calculated by using (33) and (36)

$$l_{y} = \sum_{i=1}^{nb+1} S_{i} = \frac{(D_{ro}/2) - (D_{so}/2) - g}{1 + k_{wq}}.$$
 (36)

Additionally, the widths of barriers can be calculated by solving the system of *n*<sup>b</sup> equations using (34) and (37)

$$l_a = \sum_{i=1}^{nb} W_{bi} = \frac{(D_{ro}/2) - (D_{so}/2) - g}{1 + (1/k_{wq})}.$$
 (37)

# **5FEM analysis results**

In this section, the presented design procedure for the stator and rotor is used to develop a preliminary design of the Ex-SynRM. The first step to design suitable rotor geometry is finding the optimum insulation ratio where the average torque maximisation is targeted. A limited number of FEA sensitivity analysis simulations are conducted to achieve the optimum value of the insulation ratio. The influence of the insulation ratio on the barriers geometry illustrated in Fig. 5 reveals increasing the insulation ratio widens the flux barriers. The average torque for six different values of the insulation ratio is presented in Fig. 6. According to the results, the optimum insulation ratio is around 0.6.

In order to consider the effect of the rotor slot pitch angle controller (*ȕ*) on the output torque of the machine, torque comparison for different values of *ȕ* is shown in Fig. 7. Furthermore, multi-objective shape optimisation process with two objectives simultaneously to maximise the average torque and to minimise the torque ripple is conducted on the preliminary design. Based on the results given in Table [3](#page-5-0) change in *ȕ* dramatically affects the torque ripple. The optimisation result with an objective function, which uses the same weighting coefficient (50%) shows both the average torque and torque ripple are improved. However, the case *ȕ* = *αm* has higher average torque compared to the optimal design one. It is worthwhile to mention, the average torque maximisation and torque ripple minimisation are two conflicting objectives, and then improvement in the torque ripple may lead to a reduction in the average torque.

<span id="page-5-0"></span>**Table 3** Performance results comparison

| Characteristic     | β = 0.5αm | β = αm | Optimal design |
|--------------------|-----------|--------|----------------|
| average torque, Nm | 4.167     | 4.468  | 4.242          |
| torque ripple, %   | 49.366    | 29.858 | 19.677         |

![](_page_5_Picture_3.jpeg)

**Fig. 8** *Flux line distribution over a pole of Ex-SynRM (a) ȕ* = 0.5*αm*, and *(b) ȕ* = *αm*

**Table 4** Results comparison for two values of the rotor slot pitch angle controller

| Characteristic            | β = 0.5αm | β = αm |
|---------------------------|-----------|--------|
| air gap flux density THD% | 32.33     | 28.53  |

Undesirable interactions between the rotor and stator MMF harmonic components are introduced as the main source of torque ripple [\[26](#page-8-0)]. To investigate the major cause of torque ripple deeply, the distribution of the magnetic flux lines relevant to two values of *ȕ* shown in Fig. [7,](#page-4-0) *ȕ* = 0.5*αm* and *ȕ* = *αm* are presented in Fig. 8. According to Fig. 8*a,* the end of each barrier is right at the top of the slot opening area. Thus, having the same slot pitch angle in rotor and stator leads to high torque ripple. On the contrary, as is shown in Fig. 8*b* rotor slot pitch angle has a certain value that one end of each barrier is positioned before its related slot opening area and the other end is located after the corresponding slot opening area. It can be concluded from the provided results in Figs. [7](#page-4-0) and 8 to achieve a low torque ripple, the rotor slot pitch angle needs to differ from the stator slot pitch angle. It is in accordance with a similar rule for the internal rotor SynRM [[21\]](#page-8-0).

Additionally, the air-gap flux densities of the two cases are shown in Fig. 9. The difference between the two flux density waveforms is clear in Fig. 9. Subsequently, the harmonic spectrum comparisons of two air-gap flux densities are illustrated in Fig. 10. As a matter of fact, the case *ȕ* = 0.5*αm* having a high level of harmonic content, as total harmonic distortion (THD), equal to

![](_page_5_Figure_9.jpeg)

**Fig. 9** *Air-gap flux density distribution*

![](_page_5_Figure_11.jpeg)

**Fig. 10** *Harmonic content of the flux density for different rotor slot pitch angle controller*

![](_page_5_Figure_13.jpeg)

**Fig. 11** *Effect of air-gap on the inductance of Ex-SynRM*

32.33% has the highest torque ripple. Related two THD values are shown in Table 4.

Essentially, the effect of the air-gap length on the output torque is of significant importance. As Fig. 11 shows by increasing the airgap length *L<sup>d</sup>* decreases while *L<sup>q</sup>* remains almost unchanged. The air gap length is much less than the total insulation layer (*l<sup>a</sup>* ), and then the flux in the *q*-axis is not as sensitive as the flux in the *d*axis to the change in the air gap width. Therefore, to have a higher developed torque the air-gap length must be as low as possible. However, from the torque ripple point of view by reducing the airgap length Carter's factor increases like all ac machines with a slotted stator, so the torque ripple grows as well. The motor torque for a different length of air gap is represented in Fig. [12](#page-6-0), where the case with the air-gap length of 0.4 mm has an acceptable average torque along with a low torque ripple. Furthermore, Fig. [13](#page-6-0) shows the maximum flux density on the teeth of the stator at the rated current is 1.66 Tesla, which is lower than 1.7 Tesla considered in the design steps.

<span id="page-6-0"></span>![](_page_6_Figure_1.jpeg)

**Fig. 12** *Effect of air-gap on the developed torque of Ex-SynRM*

![](_page_6_Figure_3.jpeg)

**Fig. 13** *Flux density on the stator and rotor of Ex-SynRM at the rated current*

**Table 5** Specifications of the non-oriented steel M-27

| Definition             | Value       |  |
|------------------------|-------------|--|
| thickness              | 0.36 mm     |  |
| thermal conductivity   | 25 W/m °C   |  |
| specific heat capacity | 490 J/kg °C |  |
| mass density           | 7600 kg/m3  |  |

![](_page_6_Figure_7.jpeg)

**Fig. 14** *Temperature distribution of the Ex-SynRM*

### *5.1 Multi-physics analysis*

In order to guarantee the safe operation of the motor, thermal and structural behaviour of the optimally designed motor has been tested at the rated speed. The heat transfer has an absolutely crucial role in the external rotor architecture wherein the motor directly is coupled to the wheel. The material specification of the M27 steel used for the stator and rotor cores is provided in Table 5.

It is assumed that the motor works under steady state condition and the ambient temperature is 20°C. The temperature distribution of the motor is shown in Fig. 14. The copper loss on the stator

![](_page_6_Figure_12.jpeg)

**Fig. 15** *Deformation of the Ex-SynRM (a)* Contour plot, *(b)* Scaled plot of the rotor by scaling factor of 5000

![](_page_6_Figure_14.jpeg)

**Fig. 16** *Test setup (a)* External rotor with housing, *(b)* Stator, *(c)* Ex-SynRM test bench

windings is the main source of heat in the motor. Generally, the type of insulation material used in the machine windings determines the maximum allowable temperature rise. This temperature may vary from 105 to 180°C for materials such as mica and glass fibre bounded with silicon, respectively. The E-bike application has the merit of natural convection for the heat transfer mechanism. Besides, no rotor cage in the SynRM results in a quiet cool rotor that is evident in Fig. 14.

Additionally, the mechanical robustness of the rotor structure may be considered as a challenging issue because of its unique geometry in the Ex-SynRM. The centrifugal and electro-magnetic forces on the sensitive points such as the ribs may cause metal fatigue or displacement on the rotor laminations. Therefore, the structural analysis has been conducted on the designed motor and the result is presented in Fig. 15. Displacement contour plot shown in Fig. 15*a* confirms the maximum value of 0.7 µm which is by far less than the value of 0.4 mm air gap length.

The scaled view of the rotor by a factor of 5000 shown in Fig. 15*b* reveals that the critical point is the tangential rib. However, the centrifugal forces push the rotor towards the outside and electro-magnetic forces pull it towards the stator. Therefore, the low-speed requirement of the E-bike application ensures the safe mechanical operation of the motor.

# **6Experimental results**

In order to evaluate the effectiveness of the proposed design procedure, a prototype Ex-SynRM is fabricated with the same specifications used at the design steps. Rotor and stator of the motor along with the test bench are shown in Fig. 16.

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

**Fig. 17** *Inductance of Ex-SynRM: FEM result and experimental result*

![](_page_7_Figure_3.jpeg)

**Fig. 18** *Torque-angle characteristic of Ex-SynRM: (I) FEM result and (II) experimental result*

Firstly, the locked rotor test has been performed to determine the phase inductance of the motor by changing the rotor position. As is shown in Fig. 17 the phase inductance has a maximum of 33.15 mH on the *d*-axis and a minimum of 11.65 mH on the *q*-axis. The experimental and simulation results are lightly different and it is related to the impedance calculation and measurement inaccuracy.

Secondly, an industrial drive module that is modified for the synchronous reluctance motor has provided the sensor-less direct torque control technology. Then, the torque-angle characteristic of the machine has been identified, as well. In this test, the rotor is locked and the maximum torque of the machine at different rotor angles is measured. As is illustrated in Fig. 18, the trend line extrapolated from the torque measurement confirms the capability of the prototype motor to produce maximum torque value close to the predicted value by the FEM analysis. The simulation and experimental results, though, are slightly different. It should be noted from [\(28](#page-3-0)), for a constant value of stator current the maximum torque occurs at *Ȗ* = 45°. However, due to the saturation effect when the current angle increases above 45° the increase in the inductance difference between *d*- and *q*-axes is more than the decrease in the terms of sin(2*Ȗ*) in ([28\)](#page-3-0). Therefore, as is shown in Fig. 18 the current angle related to the maximum torque is around 55°.

The output torque of the motor at the nominal phase current (4.52 A) and the rated speed (520 rpm) resulted from the FEM simulation and experimental test are demonstrated in Fig. 19. The average torque of the test result is 4.11 N m, which is 3% reduced compared to the simulation result due to the added 3D leakage inductance because of changes in the motor dimensions during the fabrication process. Additionally, the tested motor torque has a lower ripple (4.2%) compared to the FEM simulation result (19.11%). High mass of the motor housing and also a mechanical coupling shaft in the torque measurement system essentially damps the output torque ripple.

Finally, the Ex-SynRM performance is summarised in Table 6. The most dominant portion of the total losses is the copper loss, which is 85% of the total losses. The power factor of the SynRM is 0.64, which is generally lower than the power factor of the permanent magnet machines. Therefore, the SynRM requires an extra volt-ampere, which oversizes the inverter, and as a result, it decreases the overall system efficiency. However, the provided performance results are in a suitable agreement with the considered specification of the motor at the design step in Table [1.](#page-2-0)

![](_page_7_Figure_9.jpeg)

![](_page_7_Figure_10.jpeg)

**Fig. 19** *Torque of Ex-SynRM (a)* FEM result, *(b)* Experimental result

**Table 6** Calculated performance results of EX-SynRM

| Parameter | Definition                  | Value  |  |
|-----------|-----------------------------|--------|--|
| Ploss     | total losses                | 57 W   |  |
| Pcu       | stator copper losses        | 49 W   |  |
| Pc        | core losses                 | 6.25 W |  |
| Pf&w      | friction and windage losses | 1.82 W |  |
| Po        | output power                | 250 W  |  |
| η         | motor efficiency            | 81%    |  |
| PF        | power factor                | 0.64   |  |
|           |                             |        |  |

# **7Conclusion**

In this study, a thorough design procedure of the Ex-SynRM, including both the stator and rotor, is presented. Based on the design requirements in terms of electromagnetic and mechanical issues, the general dimension of the motor along with the stator geometrical and electrical specification is determined. As a next step, according to the variable reluctance concept, an analytical explanation is used to optimally shape the flux barriers into the rotor body. Different effecting parameters on the performance of the motor are considered by FEM analysis. The conducted thermal and structural analyses ensure the safe operation of the designed Ex-SynRM. A comparison of the measurement results and predicted results proves the validity of the proposed design procedure.

## **8References**

- [1] Baek, J., Kwak, S., Toliyat, H.A.: 'Optimal design and performance analysis of permanent magnet assisted synchronous reluctance portable generators', *J. Magn.*, 2013, **18**, (1), pp. 65–73
- [2] Bonthu, S.S.R., Choi, S., Gorgani, A.*, et al.*: 'Design of permanent magnet assisted synchronous reluctance motor with external rotor architecture'. Proc. – Int. Electric Machines and Drives Conf., IEMDC, Coeur d′Alene, USA, May 2015, pp. 220–226
- [3] Azhagar Raj, M., Kavitha, A.: 'Effect of rotor geometry on peak and average torque of external rotor synchronous reluctance motor (Ex-R SynRM) in comparison with switched reluctance motor for low speed direct drive domestic application', *IEEE Trans. Magn.*, 2017, **53**, (11), pp. 1–8
- [4] Bianchi, N., Bolognani, S., Carraro, E.*, et al.*: 'Electric vehicle traction based on synchronous reluctance motors', *IEEE Trans. Ind. Appl.*, 2016, **52**, (6), pp. 4762–4769
- [5] Bonthu, S.S.R., Choi, S., Baek, J.: 'Design optimization with multi-physics analysis on external rotor permanent magnet assisted synchronous reluctance motors', *IEEE Trans. Energy Convers.*, 2017, **33**, (1), pp. 290–298

- <span id="page-8-0"></span>[6] Kostko, J.K.: 'Polyphase reaction synchronous motors', *J. Am. Inst. Electr. Eng.*, 1923, **42**, (11), pp. 1162–1168
- [7] Moghaddam, R.R., Gyllensten, F.: 'Novel high-performance SynRM design method: an easy approach for a complicated rotor topology', *IEEE Trans. Ind. Electron.*, 2014, **61**, (9), pp. 5058–5065
- [8] Sudheer, S., Bonthu, R., Choi, S.: 'Optimal torque ripple reduction technique for outer rotor permanent magnet synchronous reluctance motors', *IEEE Trans. Energy Convers.*, 2017, **33**, (3), pp. 1184–1192
- [9] Matsuo, T., Lipo, T.A.: 'Rotor design optimization of synchronous reluctance machine', *IEEE Trans. Energy Convers.*, 1994, **9**, (2), pp. 359–365
- [10] Pina, A.J., Cai, H., Alsmadi, Y.*, et al.*: 'Analytical model for the minimization of torque ripple in permanent magnets assisted synchronous reluctance motors through asymmetric rotor poles'. IEEE Energy Convers. Congr. Expo. ECCE 2015, Montreal, QC, Canada, September 2015, pp. 5609–5615
- [11] Pellegrino, G., Cupertino, F., Gerada, C.: 'Automatic design of synchronous reluctance motors focusing on barrier shape optimization', *IEEE Trans. Ind. Appl.*, 2015, **51**, (2), pp. 1465–1474
- [12] Islam, M.Z., Bonthu, S.S.R., Choi, S.: 'Obtaining optimized designs of multiphase PMa-SynRM using lumped parameter model based optimizer'. 2015 IEEE Int. Electric Machines & Drives Conf. (IEMDC), Coeur d′Alene, USA, May 2015, pp. 1722–1728
- [13] Bonthu, S.S.R., Choi, S.: 'Design procedure for multi-phase external rotor permanent magnet assisted synchronous reluctance machines'. Conf. Proc. – IEEE Applied Power Electronics Conf. and Exposition – APEC, Long Beach, CA, USA, March 2016, pp. 1131–1137
- [14] Lovelace, E.C., Jahns, T.M., Lang, J.H.: 'A saturating lumped parameter model for an interior PM synchronous machine', *IEEE Trans. Ind. Appl.*, 2002, **38**, (3), pp. 645–650
- [15] Bonthu, S.S.R., Arafat, A., Choi, S.: 'Comparisons of rare-earth and rareearth free external rotor permanent magnet assisted synchronous reluctance motors', *IEEE Trans. Ind. Electron.*, 2017, **0046**, (330), pp. 1–1
- [16] Taghavi, S., Pillay, P.: 'A sizing methodology of the synchronous reluctance motor for traction applications', *IEEE J. Emerg. Sel. Top. Power Electron.*, 2014, **2**, (2), pp. 329–340

- [17] Bianchi, N., Degano, M., Fornasiero, E.: 'Sensitivity analysis of torque ripple reduction of synchronous reluctance and interior PM motors', *IEEE Trans. on Ind. Applications*, 2014, **51**, (1), pp. 187–195
- [18] Bolognani, S., Mahmoud, H., Bianchi, N.: 'Fast synthesis of permanent magnet assisted synchronous reluctance motors', *IET Electr. Power Appl.*, 2016, **10**, (5), pp. 312–318
- [19] Sawhney, A.K.: '*A course in electrical machine design*' (Dhanpat Rai & Sons, New Delhi India, 2016)
- [20] Pellegrino, G., Jahns, Th.M., Bianchi, N.*, et al.*: 'The rediscovery of synchronous reluctance and ferrite permanent magnet motors'. Tutorial Course Notes, 2016
- [21] Spargo, C.M., Mecrow, B.C., Widmer, J.D.*, et al.*: 'Application of fractionalslot concentrated windings to synchronous reluctance motors', *IEEE Trans. Ind. Appl.*, 2015, **51**, (2), pp. 1446–1455
- [22] Boldea, I.: '*Reluctance synchronous machines and drives*' (Clarendon Press-Oxford, New York, NY, USA, Oxford, 1996)
- [23] Bomela, X.B., Kamper, M.J.: 'Effect of machine design on performance of reluctance synchronous machine'. Conf. Rec. 2000 IEEE Ind. Appl., Rome, Italy, October 2000, pp. 515–522
- [24] Vagati, A., Pastorelli, M., Franceschini, G.*, et al.*: 'Design of low torque ripple synchronous reluctance motors', *IEEE Trans. Ind. Appl.*, 1998, **34**, (4), pp. 758–765
- [25] Moghaddam, R.R., Magnussen, F., Sadarangani, C.: 'Novel rotor design optimization of synchronous reluctance machine for high torque density'. 6th IET Int. Conf. Power Electron. Mach. Drives (PEMD), Bristol, UK, March 2012, pp. 1–4
- [26] Bianchi, N., Bolognani, S., Bon, D.*, et al.*: 'Rotor flux-barrier design for torque ripple reduction in synchronous reluctance and PM-assisted synchronous reluctance motors', *IEEE Trans. Ind. Appl.*, 2009, **45**, (3), pp. 921–928