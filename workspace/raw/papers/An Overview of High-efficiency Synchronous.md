# An Overview of High-efficiency Synchronous Reluctance Machines

Xuan Li, Yawei Wang, Member, IEEE, Yuhang Cheng, Dawei Li, SeniorMember, IEEE, Ronghai Qu, Fellow, IEEE

<sup>1</sup>Abstract—In recent years the synchronous reluctance machines (SynRMs) have received much attention. They have some good features such as high torque density, high reliability and low cost. This paper aims to give an overview of SynRMs with particular emphasis on the history, research status and industrial application. Besides, concept and basic operating principles of such machines are also described. Moreover, some hot spots of the research on the SynRMs are introduced. Several methods to improve the average torque and reduce torque ripple of the SynRMs in the past literatures are presented including topology design and control strategies. An overview of the methods from different aspects to realize high efficiency for the SynRMs is given which contain rotor optimization, winding configuration, material improvement, control schemes and so on. Some approaches suitable for high speed application are also introduced. It can be seen that the SynRMs have broad development prospects and great potential in industrial application.

Index Terms—Efficiency, High speed, SynRMs, Torque.

#### I. INTRODUCTION

ECENTLY the synchronous reluctance machines have attracted much attention for owning high torque density and relatively high efficiency. Compared with induction machines, the SynRMs have less loss and higher efficiency [1]. They have broad prospects in research field and industrial application [2]–[6]. R

Theory with reference to the SynRMs appeared in the early 1920s [7]. The rotor is insulated by several flux barriers which helps to generate reluctance torque and the cross section is shown in Fig. 1. However, this structure brings strong vibration and the machine volume is larger compared to the induction machine for the same performance. In 1967, Lawrenson and Agu proposed a new rotor topology with higher saliency ratio

Manuscript received November 18, 2021; revised September 23, 2022; accepted February 17, 2023. Date of current version March 12, 2023.

This research was undertaken in part by the National Natural Science Foundation of China (NSFC) under Grant 52107046, and in part by the Fundamental Research Funds for the Central Universities, HUST (2021XXJS009). (Corresponding Author: Yawei Wang )

Xuan Li, Yawei Wang, Yuhang Cheng, Dawei Li, and Ronghai Qu are with the Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: m202172105@hust.edu.cn, yaweiwang@hust.edu.cn, m202171950@hust.edu.cn, daweili@hust.edu.cn, ronghaiqu@hust.edu.cn).

Digital Object Identifier 10.30941/CESTEMS.2023.00030

which showed better performance than the conventional structure. However, the application is limited due to the complex structure, low power factor and high cost. In 1970s [8], two kinds of rotor structure were proposed. As shown in Fig. 2(a), the rotor is axially laminated which has high saliency ratio and high efficiency but the manufacture is relatively difficult. Fig. 2(b) [8] shows the transversely laminated rotor which has low cost and a robust structure. Later on, the transversely laminated rotor has been the basis of the SynRM rotor design and the research on improving the performance of such machine has been going on.

The SynRMs have been gradually used in the industrial landscape. Instead of permanent magnet (PM) motors, the SynRMs with flux barriers on the rotor were applied in water pump [9]. The load angle is higher than that of the PM motor, but the copper losses in the stator are higher because of the higher stator current. The SynRMs are also applied in electric vehicles (EVs) for their wide speed range and the ability of providing high torque in the low speed region and high power in the high speed region. They have been well studied in [10]–[15] and the future work will be focused on the reduction of torque ripple which is significant to EVs [16]. Moreover, the SynRMs can be applied in a flywheel-based energy storage system [17] for their zero no-load electromagnetic losses and relatively low cost. The disadvantages are the low power factor and mechanical limits. A doubly excited brushless reluctance machine is used in wind power generation system [18]. The generation of electromagnetic torque and electromechanical energy conversion are due to the mutual flux linkage variations. The SynRMs can also be applied in all fractional horse power fields including home appliances [19], because of the low cost and the acceptable efficiency level. The SynRM with outer rotor is also a good choice for electric bikes [20] for their inherent advantages.

Many companies have also been focused on the research and production of the SynRMs. The well-known company ABB from Switzerland provides the SynRMs for variable speed application as shown in Fig. 3 [21]. According to the IEC TS 60034-30-2:2016 report, one kind of SynRMs is suitable for four pole machines below 200kW. The rotor volume is small which eliminates rotor iron losses and the efficiency level reaches IE4. Some products made of aluminum also have high efficiency. Another way to improve efficiency is using ferrite magnet to assist magnetizing. The efficiency of one product whose rated power is 5.5kW and rated speed is 3000rpm reaches 90% when operating at rated speed. REEL from France

![](_page_1_Picture_2.jpeg)

Fig. 1. Kostko's rotor in 1923 [7].

![](_page_1_Picture_4.jpeg)

Fig. 2. (a) Axially laminated rotor structure [8]. (b) Transversely laminated rotor structure [8].

![](_page_1_Picture_6.jpeg)

Fig. 3. SynRM provided by ABB [21].

also provides the SynRMs with high output power [22]. Okuma from Japan provides permanent magnet assisted synchronous reluctance machines whose efficiency is increased by 4-9% comparing with induction machines [23]. Siemens company from Germany produces a kind of the SynRM whose efficiency is 14% higher than IE1 and 3% higher than IE3 [24].

In this paper, special attention will be paid on the review of the SynRMs in terms of the torque performance and efficiency. In Section II, basic concepts and the operating principle of the SynRMs will be introduced. Then in Section III, studies on improving the average torque or reducing the torque ripple of the SynRMs are listed. Afterwards, design aspects of the SynRMs for high speed application are investigated in Section IV and an overview of the researches on improving efficiency is given in Section V. Finally, the conclusion is drawn in the end.

### II. BASIC CONCEPTS AND OPERATING PRINCIPLES OF THE SYNRM MOTORS

The basic concepts and mathematical model of the SynRMs have been well studied in [25]–[30]. The stator of the SynRM is almost the same as the induction machine. Three phase AC currents are injected into the stator winding when the SynRM operates and the flux lines close in the direction of a minimum

![](_page_1_Picture_12.jpeg)

Fig. 4. *d-q* axis equivalent circuits of the SynRMs. (a) *d*-axis circuit. (b) *q*-axis circuit [31].

![](_page_1_Picture_14.jpeg)

Fig. 5. Phasor diagram representive of the SynRM [31].

![](_page_1_Figure_16.jpeg)

Fig. 6. The relationship between power factor and saliency ratio [31].

reluctance. Due to the high saliency ratio of the rotor structure, when the stator current vector deviates from d-axis, a reluctance torque is generated to rotate the rotor towards the direction with minimum reluctance. The voltage and current of the SynRMs in the d-q reference frame are expressed as:

$$v_d = R_s i_d + L_d \frac{di_d}{dt} - \omega L_q i_q \tag{1}$$

$$v_d = R_s i_d + L_d \frac{di_d}{dt} - \omega L_q i_q \tag{2}$$

where  $v_d$  and  $v_q$  are d- and q-axis voltage,  $i_d$  and  $i_q$  are d- and q-axis current,  $L_d$  and  $L_q$  are d- and q-axis inductance,  $R_s$  is the resistance of the stator and  $\omega$  is the electric angular velocity. The equivalent circuit is shown in Fig. 4 [31].

When the machine is at steady-state condition, the voltage equations are derived as [31]:

$$V_d = R_s I_d - \omega L_q I_q \tag{3}$$

$$V_a = R_s I_a + \omega L_d I_d \tag{4}$$

The phasor diagram representative of the SynRM is shown in Fig. 5 [31], where  $\phi$  is the angle between terminal voltage and

current,  $\alpha_i^e$  is the current phase angle and  $\delta$  is the phase angle between the flux linkage and d-axis.

The electromagnetic torque of the SynRM can be derived as:

$$T = \frac{3}{2} p(L_d - L_q) i_d i_q = \frac{3}{2} p(\xi - 1) L_q i_d i_q$$
 (5)

where  $\xi$  is defined as the saliency ratio of the machine which is given by:

$$\xi = \frac{L_d}{L_a} \tag{6}$$

The power factor is defined as:

$$\cos \varphi = \frac{\omega_m T}{\frac{1}{2} m VI} \tag{7}$$

where  $\omega_m$  is the mechanical angular speed, V and I are the peak value of the voltage and current and m is the phase number. Then the power factor of the SynRMs can be derived as [31]:

$$\cos \varphi = (\xi - 1) \sqrt{\frac{\sin 2\alpha_i^e}{2\left(\xi^2 \cot \alpha_i^e + \tan \alpha_i^e\right)}}$$
 (8)

The relationship between the power factor and the saliency ratio is shown in Fig. 6 [31]. It can be seen that the power factor increases with the improvement of saliency ratio. It is also noticed that the power factor of the SynRM is quite low which limits its application in high performance fields.

## III. STUDIES ON TORQUE CHARACTERISTICS IMPROVEMENT OF THE SYNRM MOTOR

One of the research hot spots on the SynRMs is the improvement of torque characteristics which includes increasing the average torque and reducing the torque ripple.

#### A. Improvement of the Average Torque

The average torque of the SynRM is significantly af- fected by the rotor structure and especially the flux barrier configuration. Several flux barrier shapes have been pro-posed in the literature, including fluid shaped, rectangular shaped, circular shaped, U shaped and hyperbolic shaped flux barriers as shown in Fig. 7. The influence of rotor geometry parameters including the number of rotor pole pairs and air-gap length has been studied [37], [38] and the average torque can be improved by choosing optimal parameters. Considering magnetic saturation, the single flux barrier is optimized to maximize the saliency ratio and improve the torque [36]. The topology of the investigated machine model is shown in Fig. 8 and the design process is shown in Fig. 9 [36]. Two designs of the SynRMs with different types of flux barriers which are C-type and U-type respectively are investigated and the torque characteristics are compared in [39]. The results showed that the C-type flux barrier design provides slightly higher torque by 2.3% with respect to the U-type flux barrier design for the Ushape case causes some saturation at the bending area which impairs the performance. Single-parameter variable method is utilized to design a U-type flux barrier rotor in [40] and the optimization process is from a one-layer flux barrier to a complex two-layer flux barrier. The models of flux barrier

![](_page_2_Picture_16.jpeg)

Fig. 7. Rotors with different flux barrier shapes and arrangement. (a) Fluid shaped [32]. (b) Rectangular shaped [33]. (c) Rectangular shaped with a cutting rotor [33]. (d) Circular shaped [34]. (e) U shaped [34]. (f) Hyperbolic shaped [35].

![](_page_2_Picture_18.jpeg)

Fig. 8. Topologies of the investigated machine model [36].

parameters are shown in Fig.10 [40].

It can be noticed that the parameters increase with the number of flux barriers [41]. The cross section is shown in Fig.11 [41]. The SynRMs with segmented rotor are studied in [42] and different configurations of the proposed rotors are shown in Fig. 12 [42]. Different rotor structures are optimized and compared for a high speed solid rotor SynRM [43] as shown in Fig. 13 [43]. Axial holes are drilled in a smooth rotor and a jacket with non-magnetic material is added to the rotor to reduce the aerodynamic losses on the rotor when running at high speed. The results show that the proposed model generates 10% better average torque than the classical model and reduce aerodynamic losses which allows the rotor cooling to be simplified.

The electromagnetic design of four models of outer rotor SynRM are reported in [44]. They have the same number of stator slots but different pole numbers. The output power, torque and torque ripple are compared and the best structure is selected. Taguchi method is used to optimize the machine.

#### B. Reduction of Torque Ripple

![](_page_3_Picture_2.jpeg)

Fig. 9. Rotor structure with single flux barrier. (a) Basic structure. (b) Proposed structure [36].

![](_page_3_Picture_4.jpeg)

Fig. 10. Rotor structure with rectangular shaped flux barriers. (a) One layer flux barrier. (b) Two layer flux barriers [36].

![](_page_3_Picture_6.jpeg)

Fig. 11. Rotor structure with multi-flux barriers and winding configuration [41].

![](_page_3_Picture_8.jpeg)

Fig. 12. Different configurations of the segmented rotor [41].

![](_page_3_Picture_10.jpeg)

Fig. 13. Cross section of a solid rotor. (a) Drilled. (b) Drilled and slitted [43].

Rotor slot pitch and flux barrier angle can be selected as the main design parameters for the torque ripple reduction without interfering the average torque [45], [46]. The SynRMs using asymmetric flux barrier arrangement are investigated and the torque ripple can be reduced without sacrificing the average torque [47], [48]. In [49], [50], rotors are designed to be composed of different laminations. Each lamination is designed to cancel a torque harmonic of given order and after the combination the torque ripple is reduced obviously. Torque ripple can also be reduced by configuring auxiliary slots on the rotor [51]. A design method of varying the barrier angles for torque ripple reduction is reported in [52]. The method leads to a phase shift of the flux harmonics which cause torque ripple mainly.

In addition, the torque ripple of the SynRMs can be reduced via control method. The square-wave and sine-wave drive strategies ware compared in [53]. The torque performances were analyzed and the sine-wave drive proved to be able to improve the machine performance. Moreover, the frozen permeability method is used to separate the torque ripple caused by current harmonic and inductance harmonic respectively which illustrates the torque resources. A robust and simple control system for the SynRM drive is presented taking saturation effects into consideration as reported in [54]. It is found that cross-magnetic saturation affects the performance of the system most significantly. In motoring and braking modes of operation the system performs well. Low torque ripple and sinusoidal currents are achieved by applying such control system which show its feasibility. Current vector was directly controlled in [55], [56] and the maximum torque per flux control strategy was used in field weakening region. The torque capability is proved to be improved compared with conventional field weakening control. Different means to improve the torque characteristics of the SynRM are listed and compared in Table I.

#### IV. DESIGN OF THE SYNRM MOTOR FOR HIGH-EFFICIENCY

With the growing concerns over carbon emissions, the energy-saving electric motors have drawn extensive attention over the last decade. Due to the inherent merits, the SynRMs are viewed as the most promising motor topologies, and many researches have been conducted on this topic.

#### A. Rotor Design and Optimization

The SynRMs are able to achieve high efficiency when the rotor is well designed and optimized which enhance the total performance.

An automatic design procedure [57] of the SynRM for higher torque density, fewer losses and lower torque ripple has been proposed. A stochastic optimization algorithm accompanied with finite element analysis is utilized and the computational burden is lightened through a careful subdivision of the design procedure. A two-step procedure for a time-efficient multi-objective genetic algorithm (MOGA) was proposed in [58], having as output a front of the SynRM motor designs that are Pareto optimized in terms of torque characteristics.

| TABLE I                                                          |
|------------------------------------------------------------------|
| COMPARISON OF MAIN METHODS TO IMPROVE THE TORQUE CHARACTERISTICS |
| OF THE SYNRM                                                     |

| OF THE STINKIN                          |                   |               |                             |  |
|-----------------------------------------|-------------------|---------------|-----------------------------|--|
| Design                                  | Average<br>torque | Torque ripple | Shortcomings                |  |
| Barrier<br>shape<br>design<br>[33]–[35] | Improved          | Reduced       | High design complexity      |  |
| Multi-flux<br>barriers<br>[40], [41]    | Improved          | Reduced       | Increased design parameters |  |
| Asymmetric<br>flux barrier<br>[47]–[50] | Unchanged         | Reduced       | Manufacturing difficulty    |  |
| Auxiliary<br>slots<br>[16],[51]         | Unchanged         | Reduced       | Power density<br>decreased  |  |
| Control<br>strategies<br>[53], [55]     | Improved          | Reduced       | Higher hardware cost        |  |

In [59], the motor parameters such as stator slot tooth width, the web thicknesses of the rotor, and the rotor flux barriers were optimized to obtain high torque with low torque ripple at the steady-state operation. In the optimization step, the stator outer diameter, the rotor diameter and the air gap were kept constant. A multi-objective genetic algorithm was used with two different fitness functions as maximizing average torque and minimizing torque ripple. The structure of the designed motor and optimized parameters are given in Fig. 14 [59]. The optimized SynRM motor was determined in IE5 efficiency class while it can be easily manufactured in IE4 efficiency class.

It was reported in [60] that with the same stator diameter, number of stator slots and stack length as a premium efficiency induction motor, the SynRM drive system efficiency was shown to be superior to that of the premium efficiency (IE3) induction machine drive system on a certain power level. The algorithm called Modified Method of Feasible Direction (MMFD) was used which has been found to be good at finding at least a local optimum. The optimized result was shown in Fig.15 [61]. For pump and fan VSD applications the 5.5 kW RSM with a weighted efficiency of 92.2%, satisfies the requirements of the IE4 classification.

It was proved that the performance of the SynRMs could be improved by appropriately selecting the number of barriers and placing them at an optimum location in [61]. Based on the flux path analysis, the segment to barrier thicknesses were defined and a high-performance multi- barrier design was proposed.

A new design strategy of the SynRMs for pump and fan applications is reported in [62]. The rotor and stator geometry are different from classical design and fractional slot windings are applied which results in torque ripple reduction. The new design reduces the number of stator slots and the slot area is thus bigger which allows increasing the filling factor and the efficiency. The cross section of the designed model is shown in Fig. 16(a) [62]. Fig. 16(b) [62] shows a series of optimization parameters.

In [63], the SynRM was designed to achieve the IE4 efficiency class and to be competitive to the benchmark BLDC

![](_page_4_Picture_9.jpeg)

Fig. 14. Motor structure and optimized parameters [59].

![](_page_4_Picture_11.jpeg)

Fig. 15. Cross section of the SynRM motor optimized for maximum drive system efficiency [60].

![](_page_4_Picture_13.jpeg)

Fig. 16. (a) Cross section of four-pole SynRM when q=2.5. (b) Optimization parameters [61].

motor in terms of torque per weight ratio and efficiency. The design was based on the design software tools which were PC-based brushless DC motor analysis (PC-BDC) and finite-element analysis (PC-FEA).

The characteristics of the SynRMs with high efficiency for industrial application were analyzed in terms of design parameters like the number and the ratio of the barrier in [64]. Then the proper design specification that satisfied the requirements was found. An analytical model was proposed to design high-performance SynRMs while the ratio of total flux barrier width to total iron sheet width, the number of flux barriers and additional rotor diameters were selected to be the

design parameters [65]. The selection of the optimization algorithm was influenced by the smoothness of the objective function and the presence of computational errors and the Nelder-Mead method was used which is applicable to non-smooth and noisy functions. Then the Pareto front could be found in which are the optimized solutions. The results showed that the efficiency of the new SynRM at 90% rated speed was 90.7% which met the requirement of the IE5 class.

A methodology for design of high efficiency synchronous reluctance machine series in frame sizes IEC- 80 up to IEC-160 was proposed in [66]. In conventional parametrization, the circular barrier was defined with four main parameters as shown in Fig. 17(a) [66]. It was not suitable for the reason that large intervals of such parameters may lead to a varieties of unfeasible geometries and the computation time is relatively long. Thus, an alternative parametrization of a circular barrier geometry was proposed which is shown in Fig. 17(b).

#### B. Stator Winding

The winding configuration is significant to the performance of the SynRM and the SynRMs using fractional- slot concentration windings (FSCWs) has been investigated [67], [68]. This winding type has the advantage of higher torque density, higher efficiency and robustness of the rotor structure. Due to the rich harmonic contents in the stator magnetomotive force (MMF), the SynRMs with FSCWs shows even lower power factor and higher torque ripple. Low saliency ratio and the reduction of average torque are also observed when FSCWs are applied. Besides, the potential even space harmonics and the lack of slot pole combinations limit the use of FSCWs. In [69], the toroidal windings were studied and different winding configurations are shown in Fig. 18 [69]. It has been proved that the toroidal windings are able to maintain the merits of FSCWs while they eliminate the even space harmonics and allow a wide range of slot pole configurations which have high fundamental winding factors. The efficiency of the machine can also be improved through using toroidal windings.

In [70], the wound field SynRM was investigated and a new design method adopting a dual winding and series/parallel switching was proposed. The schematic diagram is shown in Fig. 19 [70] and the method turned out to be able to extend the speed range and also improve the efficiency of the machine.

#### C. Air-gap

In [71], the impacts of air-gap length on the performance of axially laminated synchronous reluctance machines are investigated and it is found that the eddy current losses on the rotor caused by high-order spatial harmonics which are produced by the stator can be reduced by increasing air-gap length. The stator losses is also reduced when the air-gap length increases. However, thicker air-gap length causes larger current for achieving the same torque, and thus, leads to higher copper losses in the stator. A trade- off between the air-gap thickness and machine performance should be reached during the design procedure.

#### D. Magnetic Materials

![](_page_5_Picture_10.jpeg)

Fig. 17. (a) Parametrization of the SynRM with circular barriers in SPEED PC-BDC software. (b) New parametrization of the SynRM with circular barriers [66].

The influence of electrical steel grades on the torque and efficiency of the SynRMs [72] was investigated. Four steel grades are considered which are M600-100A, M400-50A, M330P-50A and NO20 respectively and the machine geometry are all the same. The analytical model is established and the results are validated through FEA method. The final results show that the material properties have an obvious effect on the efficiency and output power of the SynRMs. For example, the efficiency of the machine using NO20 is 9% higher than that using M600-100A. Two kinds of synchronous reluctance machines which have different iron materials but the same dimensions and iron and winding structure are tested at full loading [73]. It turns out that the efficiency of both reach more than 90% and one is better than the other in high speed region while in high torque region the latter one is better than the former one.

#### E. Control Strategy

Another way to realize high efficiency is to develop a suitable control strategy.

In [74], it is found that there exists many combinations of dand q-axis current while each of them provides a specific torque characteristic. The efficiency is variable and an optimum current vector that provides the maximum efficiency at every operating point can be obtained. For practical realization, an optimum-efficiency controller is used with the help of a loss model and interferences like saturation factors, harmonic effects are taken into account. A small perturbation is added to the d-axis current reference seeking for a minimum input power.

High efficiency was achieved based on a control method called fuzzy control in [75], [76]. The d- and q-axis armature current, flux linkage, armature resistance and equivalent iron loss coefficient were estimated using the extended Kalman filter. In [77], the nonlinear control scheme based on feedback linearization was proposed for higher dynamic performance and efficiency optimization of the SynRMs. A linear torque-speed characteristic was achieved since the torque could be regulated by selecting the product of d- and q-axis torque currents as one of the output variables.

It is reported that the maximum efficiency operation was identical to the Minimum Power Per Torque (MPPT) operation in [78]. The block diagram is shown in Fig.20 [78]. The input power variation corresponding to the current angle could be

![](_page_6_Picture_2.jpeg)

Fig. 18. Different winding configurations [69].

![](_page_6_Picture_4.jpeg)

Fig. 19. The schematic diagram of the armature windings [70].

![](_page_6_Figure_6.jpeg)

Fig. 20. The block diagram of speed control system with MPPT tracking method [78].

obtained by injecting small sinusoidal signal into the current reference angle and it was zero at the MPPT operation point. Then the maximum efficiency point was traced without dependency on motor parameters.

A drive strategy for high efficiency using a neural network was proposed in [79], [80]. The neural network is capable of mapping the nonlinear relation between the input and output signals. Using the proposed method, the high efficiency drive could be achieved even in transient states. Moreover, the number and the shape of the conductor bar were chosen as design variables in [81] and the starting stability of the line-start synchronous reluctance machine was enhanced through such design. Then high efficiency driving could be achieved.

As for the control of the SynRM, the d- and q-axis inductances which varied in the SynRMs were significant factors for motor drive, some methods of calculating the two inductances have been presented in past literatures. One of

![](_page_6_Picture_11.jpeg)

Fig. 21. Rotor with Zukovski barriers [83].

![](_page_6_Picture_13.jpeg)

Fig. 22. Sketch of a one pole SynRM rotor [86].

them taken iron loss and cross magnetic saturation into account [25], [26]. Based on conventional analytical model, the voltage equations were changed and the inductances were calculated through the modified model.

In [82], a loss minimization controller was proposed for SynRM drive. The optimum current oriented to minimal loss was calculated considering cross-magnetic saturation.

#### V. DESIGN OF THE SYNRM MOTORS FOR HIGH-SPEED APPLICATION

The use of the synchronous reluctance machines for high-speed application remains almost unexplored yet. The aim of this section is to present the potential of a high-speed synchronous reluctance machine.

It has been found that the mechanical behavior of the SynRMs can be significantly improved by introducing ribs to the rotor construction [83]. It is effective for the rotor to withstand high speed through adding central ribs in the flux barriers. However, this will cause the generated torque decreasing. To compensate the torque loss, rotor flux barriers are designed and rotors with Zukovski barriers are proved to be able to generate higher torque whose structure is shown in Fig.21 [83].

In [84], a hybrid design approach for the SynRMs suit- able for high-speed operation is proposed. A comparative study on different soft magnetic materials is presented. It is proved that in the lower speed range, the CoFe has better performance mainly due to higher saturation flux density while machines with SiFe provide better performance at high speed due to lower iron losses [85].

To optimize the rotor structure for high-speed application, an optimization procedure which is called the multi- objective differential evolution (DE) algorithm was implemented in [86]. The sketch of a one pole SynRM rotor with some design parameters is shown in Fig. 22 [86]. Further optimizations at different speeds were presented which aimed to determine the influence of the speed on the overall performance and the rotor barriers shape. It had been verified that the flux-barrier geometry was the most suitable solution at the rated speed of 20000 rpm.

#### VI. CONCLUSION

This paper gives an overview of the studies on the SynRMs in the past literatures. The SynRM has advantages including high torque density for making full use of reluctance torque, high efficiency, high reliability and wide speed range. The main shortcoming is that the power factor is relatively low which means more drive energy is needed. The average torque can be improved and the torque ripple is reduced through rotor design. Parameters related to rotor flux barrier geometry are often chosen as design parameters and several different optimization algorithms can be utilized. As for the improvement of efficiency, one way is to design the stator and rotor structure or using different materials and another way is to apply an optimum control strategy.

The future study on the SynRMs will focus on further improvement of average torque and efficiency. If breakthroughs in materials research or innovative development of machine topologies are made, the SynRM will enable higher torque density and efficiency.

#### REFERENCES

- [1] A. Boglietti, A. Cavagnino, M. Pastorelli, D. Staton, and A. Vagati, "Thermal Analysis of Induction and Synchronous Reluctance Motors," IEEE Transactions on Industry Applications, vol. 42, no. 3, pp. 675– 680, May 2006.
- [2] A. Boglietti, A. Cavagnino, M. Pastorelli, and A. Vagati, "Experimental Comparison of Induction and Synchronous Reluctance Motors Performance," in Fourtieth IAS Annual Meeting. Conference Record of the 2005 Industry Applications Conference, Hong Kong, China, vol. 1. Oct. 2005, pp. 474–479.
- [3] J. Germishuizen, F. V. der Merwe, K. V. der Westhuizen, and M. Kamper, "Performance Comparison of Reluctance Synchronous and Induction Traction Drives for Electrical Multiple Units," in Conference Record of the 2000 IEEE Industry Applications Conference. Thirty-Fifth IAS Annual Meeting and World Conference on Industrial Applications of Electrical Energy (Cat. No.00CH37129), Rome, Italy, vol. 1. Oct. 2000, pp. 316–323.
- [4] P. Rafajdus, V. Hrabovcova, P. Lehocky, P. Makys, and M. Sebest, "Analysis and Measurements of New Designed Reluctance Synchronous Rotor," in 2018 IEEE International Conference on Environment and Electrical Engineering and 2018 IEEE Industrial and Commercial Power Systems Europe (EEEIC / I&CPS Europe), Palermo, Italy, Jun. 2018, pp. 1–6.
- [5] A. Zakharov, S. Malafeev, and A. Dudulin, "Synchronous Reluctance Motor: Design and Experimental Research," in 2018 X International Conference on Electrical Power Drive Systems (ICEPDS), Novocherkassk, Russia, Oct. 2018, pp. 1–4.
- [6] A. Agrawal, A. Srivastava, and A. Trivedi, "Performance Investigation of Three Phase Synchronous Reluctance Motor Using Finite Element Analysis," in 2012 IEEE Fifth Power India Conference, Murthal, India, Dec. 2012, pp. 1–5.
- [7] J. K. Kostko, "Polyphase Reaction Synchronous Motors," Journel of the American Institute of Electrical Engineers, vol. 42, no. 11, pp. 1162–1168, Nov. 1923.
- [8] J. Kolehmainen, "Synchronous Reluctance Motor with Form Blocked Rotor," IEEE Transactions on Energy Conversion, vol. 25, no. 2, pp. 450–456, Jun. 2010.
- [9] P. Rafajdus, V. Hrabovcova, P. Lehockv, P. Makys, and M. Kremen, "Low Voltage Reluctance Synchronous Motor with New Reluctance Rotor for Water Pump," in 2018 IEEE 18th International Power

- Electronics and Motion Control Conference (PEMC), Budapest, Hungary, Aug. 2018, pp. 568–573.
- [10] J. Malan and M. Kamper, "Performance of A Hybrid Electric Vehicle Using Reluctance Synchronous Machine Technology," IEEE Transactions on Industry Applications, vol. 37, no. 5, pp. 1319–1324, Sep. 2001.
- [11] H. Cai, B. Guan, and L. Xu, "Low-cost Ferrite PM-Assisted Synchronous Reluctance Machine for Electric Vehicles," IEEE Transactions on Industrial Electronics, vol. 61, no. 10, pp. 5741–5748, Oct. 2014.
- [12] L. Chen, J. Wang, P. Lombard, P. Lazari, and V. Leconte, "Design Optimisation of Permanent Magnet Assisted Synchronous Reluctance Machines for Electric Vehicle Applications," in 2012 XXth International Conference on Electrical Machines, Marseille, France, Sep. 2012, pp. 2647–2653.
- [13] Y. Guan, Z. Q. Zhu, I. A. A. Afinowi, J. C. Mipo, and P. Farah, "Design of Synchronous Reluctance and Permanent Magnet Synchronous Reluctance Machines for Electric Vehicle Application," in 2014 17th International Conference on Electrical Machines and Systems (ICEMS), Hangzhou, China, Oct. 2014, pp. 1853–1859.
- [14] P. Duck, J. Jurgens, and B. Ponick, "Calculation of Synchronous Reluctance Machines Used as Traction Drives," in 2015 IEEE Vehicle Power and Propulsion Conference (VPPC), Montreal, QC, Canada, Oct. 2015, pp. 1–5.
- [15] F. N. Jurca, M. Ruba, and C. Martis, "Design and Control of Synchronous Reluctances Motors for Electric Traction Vehicle," in 2016 International Symposium on Power Electronics, Electrical Drives, Automation and Motion (SPEEDAM), Capri, Italy, Jun. 2016, pp. 1144– 1148.
- [16] R. Rouhani, S. E. Abdollahi, and S. A. Gholamian, "Torque Ripple Reduction of a Synchronous Reluctance Motor for Electric Vehicle Applications," in 2018 9th Annual Power Electronics, Drives Systems and Technologies Conference (PEDSTC), Tehran, Iran, Feb. 2018, pp. 386–391.
- [17] M. Villani, L. Castellini, M. D. Andrea, and D. Macera, "Design of a Synchronous Reluctance Machine for a Flywheel-based Energy Storage System," in 2018 International Symposium on Power Electronics, Electrical Drives, Automation and Motion (SPEEDAM), Amalfi, Italy, Jun. 2018, pp. 1291–1296.
- [18] H. Liu, Y. Zhang, and L. Xu, "Theoretical Analysis of Doubly Excited Brushless Reluctance Machine Used in Wind Power Generation System," in 2009 International Conference on Sustainable Power Generation and Supply, Nanjing, China, Apr. 2009, pp. 1–4.
- [19] A. Ghaempanah, H. A. Moghddam, and R. Nasiri-Zaradndi, "Fractional Horsepower Synchronous Reluctance Motor for Use in Home Appliances," in 2018 International Symposium on Power Electronics, Electrical Drives, Automation and Motion (SPEEDAM), Amalfi, Italy, Jun. 2018, pp. 336–342.
- [20] R. A. Inte and F. N. Jurca, "A Novel Synchronous Reluctance Motor with Outer Rotor for an Electric Bike," in 2016 International Conference and Exposition on Electrical and Power Engineering (EPE), Iasi, Romania, Oct. 2016, pp. 213–218.
- [21] https://www.new.abb.com/cn/.html.
- [22] https://www.reelinternational.com/en/.html.
- [23] https://www.okuma.co.jp/.html.
- [24] https://new.siemens.com/global/en/products/automation.html.
- [25] J.-B. Im, W. Kim, K. Kim, C.-S. Jin, J.-H. Choi, and J. Lee, "Inductance Calculation Method of Synchronous Reluctance Motor Including Iron Loss and Cross Magnetic Saturation," IEEE Transactions on Magnetics, vol. 45, no. 6, pp. 2803–2806, Jun. 2009.
- [26] K. Gulbis, U. Brakanskis, E. Kamolins, and J. Zarembo, "Parameter Calculation Method of Synchronous Reluctance Motor Including Cross Magnetic Saturation," in 2020 IEEE 61th International Scientific Conference on Power and Electrical Engineering of Riga Technical University (RTUCON), Riga, Latvia, Nov. 2020, pp. 1–5.
- [27] G. Stumberger, B. Stumberger, D. Dolinar, and A. Hamler, "Cross Magnetization Effect on Inductances of Linear Synchronous Reluctance Motor Under Load Conditions," IEEE Transactions on Magnetics, vol. 37, no. 5, pp. 3658–3662, Sep. 2001.
- [28] S. Sangwongwanich, "On the Equivalent Circuit of Synchronous Reluctance Motors Based on Complex Inductance Concept," in 2020

- 23rd International Conference on Electrical Machines and Systems (ICEMS), Hamamatsu, Japan, Nov. 2020, pp. 1478–1483.
- [29] J. A. Santos, D. A. Andrade, G. P. Viajante, M. A. A. Freitas, F. S. Silva, and V. R. Bernadeli, "Mathematical Modeling and Computer Analysis Synchronous Reluctance Motor," in 2015 IEEE 13th Brazilian Power Electronics Conference and 1st Southern Power Electronics Conference (COBEP/SPEC), Fortaleza, Brazil, Nov. 2015, pp. 1–5.
- [30] C. Ferraz and C. de Souza, "Considering from Core Losses in Modeling the Reluctance Synchronous Motor," in 7th International Workshop on Advanced Motion Control. Proceedings (Cat. No.02TH8623), Maribor, Slovenia, Jul. 2002, pp. 251–256.
- [31] Y. Wang, "High Performance Synchronous Reluctance Machines: Design and Applications," Ph.D. dissertation, UNIVERSITY OF PADOVA, Sep. 2018.
- [32] Y. Wang, G. Bacco, and N. Bianchi, "Geometry Analysis and Optimization of PM-Assisted Reluctance Motors," IEEE Transactions on Industry Applications, vol. 53, no. 5, pp. 4338–4347, Sep. 2017.
- [33] I. P. A. H. Gedara, "Design Optimization and Performance Improvement of Synchronous Reluctance Machines," Ph.D. dissertation, University of Manitoba, 2019.
- [34] G. Pellegrino, F. Cupertino, and C. Gerada, "Automatic Design of Synchronous Reluctance Motors Focusing on Barrier Shape Optimization," IEEE Transactions on Industry Applications, vol. 51, no. 2, pp. 1465–1474, Mar. 2015.
- [35] M. S. Mirazimi and A. Kiyoumarsi, "Magnetic Field Analysis Of Synrel and Pmasynrel Machines with Hyperbolic Flux Barriersusing Conformal Mapping," IEEE Transactions on Transportation Electrification, vol. 6, no. 1, pp. 52–61, Mar. 2020.
- [36] W. Chai, W. Zhao, and B. il Kwon, "Optimal Design of Wound Field Synchronous Reluctance Machines to Improve Torque by Increasing the Saliency Ratio," IEEE Transactions on Magnetics, vol. 53, no. 11, pp. 1–4, Nov. 2017.
- [37] I. Chabu, J. Cardoso, V. Silva, S. Nabeta, and A. Foggia, "A New Design Technique Based on a Suitable Choice of Rotor Geometrical Parameters to Maximize Torque and Power Factor in Synchronous Reluctance Motors. I. Theory," IEEE Transactions on Energy Conversion, vol. 14, no. 3, pp. 599–604, Sep. 1999.
- [38] S. Cai, H. Hao, M-J. Jin, and J-X. Shen, "A Simplified Method to Analyze Synchronous Reluctance Machine," in Proc. of 2016 IEEE Vehicle Power and Propulsion Conference (VPPC), Hangzhou, China, Oct. 2016, pp. 1–6.
- [39] M. Hsieh, I. Tsai, and Y. Weng, "Cost-effective Design for High Efficiency Synchronous Reluctance Motor," in 2015 IEEE Magnetics Conference (INTERMAG), Beijing, China, May 2015, pp. 1–1.
- [40] H. Yu, X. Zhang, J. Ji, and L. Xu, "Rotor Design to Improve Torque Capability in Synchronous Reluctance Motor," in 2019 22nd International Conference on Electrical Machines and Systems (ICEMS), Harbin, China, Aug. 2019, pp. 1–5.
- [41] M. Takemoto, K. Yoshida, N. Itasaka, Y. Tanaka, A. Chiba, and T. Fukao, "Synchronous Reluctance Type Bearingless Motors with Multi-Flux Barriers," in 2007 Power Conversion Conference - Nagoya. Nagoya, Japan, Apr. 2007, pp. 1559–1564.
- [42] S. Abdollahi, M. Mirzaei, and H. Lesani, "Rotor Optimization of a Segmented Reluctance Synchronous Motor Utilizing Genetic Algorithm," in 2009 International Conference on Electrical Machines and Systems, Tokyo, Japan, Nov. 2009, pp. 1–4.
- [43] M. E. H. Zaim, "High-speed Solid Rotor Synchronous Reluctance Machine Design and Optimization," IEEE Transactions on Magnetics, vol. 45, no. 3, pp. 1796–1799, Mar. 2009.
- [44] M. M. R. Sankestani and A. Siadatan, "Design of Outer Rotor Synchronous Reluctance Motor for Scooter Application," in 2019 10th International Power Electronics, Drive Systems and Technologies Conference (PEDSTC), Shiraz, Iran, Feb. 2019, pp. 132–137.
- [45] R.-R. Moghaddam, F. Magnussen, and C. Sadarangani, "Novel Rotor Design Optimization of Synchronous Reluctance Machine for Low Torque Ripple," in 2012 XXth International Conference on Electrical Machines, Marseille, France, Sep. 2012, pp. 720–724.
- [46] ,X.B. Bomela and M.J. Kamper, "Effect of Stator Chording and Rotor Skewing on Performance of Reluctance Synchronous Machine," IEEE Transactions on Industry Applications, vol. 38, no. 1, pp. 91–100, 2002.

- [47] M. Sanada, K. Hiramoto, S. Morimoto, and Y. Takeda, "Torque Ripple Improvement for Synchronous Reluctance Motor Using Asymmetric Flux Barrier Arrangement," in 38th IAS Annual Meeting on Conference Record of the Industry Applications Conference, Salt Lake City, UT, USA, vol. 1, Oct. 2003, pp. 250–255.
- [48] C. C. Liu, K. L. Wang, S. P. Wang, Y. H. Wang and J. G. Zhu, "Design of Synchronous Reluctance Motor Based on Asymmetric Rotor Structure and Robust Taguchi Optimization Method," Transaction of China Electrotechnical Society, no. 37, pp. 50-61, 2022.
- [49] N. Bianchi, S. Bolognani, D. Bon, and M. D. Pre, "Rotor Flux-barrier Design for Torque Ripple Reduction in Synchronous Reluctance and Pmassisted Synchronous Reluctance Motors," IEEE Transactions on Industry Applications, vol. 45, no. 3, pp. 921–928, May 2009.
- [50] Ahmet Suat KAFADAR, Alper TAP, and Lale T. ERGENE, "Torque Ripple Reduction of SynRM Using Machaon Type Lamination," in 2018 6th International Conference on Control Engineering and Information Technology, Istanbul, Turkey, 2018, pp. 1–5.
- [51] X. Liu, X. Wang, W. Zhao, X. Zhang, and B. Wu, "Suppression of Torque Ripple of Synchronous Reluctance Motor by Optimizing Air-gap Magnetic Field," in 2019 22nd International Conference on Electrical Machines and Systems (ICEMS), Harbin, China, Aug. 2019, pp. 1–5.
- [52] T. Lange, B. Kerdsup, R. D. Doncker, and C. Weiss, "Torque Ripple Reduction in Reluctance Synchronous Machines Using an Asymmetric Rotor Structure," in 7th IET International Conference on Power Electronics, Machines and Drives (PEMD 2014), Manchester, UK, Institution of Engineering and Technology, Apr. 2014, pp. 1–5.
- [53] J.-X. Shen, S. Cai, H. Hao, and M.-J. Jin, "Investigation on Torque Ripple of Synchronous Reluctance Machine with Square-wave Drive," in 2017 20th International Conference on Electrical Machines and Systems (ICEMS), Sydney, NSW, Australia, Aug. 2017, pp. 1–9.
- [54] A. P. Goncalves, S. M. A. Cruz, F. J. T. E. Ferreira, A. M. S. Mendes, and A. T. D. Almeida, "Synchronous Reluctance Motor Drive for Electric Vehicles Including Cross-magnetic Saturation," in 2014 IEEE Vehicle Power and Propulsion Conference (VPPC), Coimbra, Portugal, Oct. 2014, pp. 1–6.
- [55] Kaveh Malekian, Mohammad Reza Sharif, and Jafar Milimonfared, "An Optimal Current Vector Control for Synchronous Reluctance Motors Incorporating Field Weakening," in 2008 10th IEEE International Workshop on Advanced Motion Control, Trento, Italy, 2008, pp. 393–398.
- [56] X. Y. Xu, Y. C. Wang, and J. X. Shen, "DTC-SVM Control Strategy for Synchronous Reluctance Motor Based on Maximum Torque Current Ratio," Transaction of China Electrotechnical Society, vol. 2, no. 35, pp. 246-254, 2020.
- [57] M. Degano, D. Gerada, M. D. Nardo, M. Galea, and C. Gerada, "Global Design Optimization Srategy of a Synchronous Reluctance Machine for Light Electric Vehicles," in 8th IET International Conference on Power Electronics, Machines and Drives (PEMD 2016), Glasgow, UK. Institution of Engineering and Technology, Apr. 2016, pp. 1–5.
- [58] F. Cupertino, G. Pellegrino, E. Armando, and C. Gerada, "A SyR and IPM Machine Design Methodology Assisted by Optimization Algorithms," in 2012 IEEE Energy Conversion Congress and Exposition (ECCE), Raleigh, NC, USA, Sep. 2012, pp. 3686–3691.
- [59] G. Boztas, O. Aydogmus, and M. Caner, "Optimal Design of Ultra-Premium Efficiency Synchronous Reluctance Motor," in 2019 11th International Conference on Electrical and Electronics Engineering (ELECO), Bursa, Turkey, Nov. 2019, pp. 161–165.
- [60] A. T. Loubser and M. J. Kamper, "Design Optimization of Reluctance Synchronous Machine for Drive System Efficiency," in 2015 IEEE Workshop on Electrical Machines Design, Control and Diagnosis (WEMDCD), Turin, Italy, Mar. 2015, pp. 60–65.
- [61] T. Mohanarajah, M. Nagrial, J. Rizk, and A. Hellany, "Design of High-efficiency Synchronous Reluctance Machines," in 2019 International Conference on Electrical Engineering Research Practice (ICEERP), Sydney, NSW, Australia, Nov. 2019, pp. 1–6.
- [62] V. Dmitrievskii, V. Prakht, and V. Kazakbaev, "IE5 Energy-efficiency Class Synchronous Reluctance Motor with Fractional Slot Winding," IEEE Transactions on Industry Applications, vol. 55, no. 5, pp. 4676–4684, Sep. 2019.
- [63] B. Kerdsup and S. Kreuawan, "Design of Synchronous Reluctance Motors with IE4 Energy Efficiency Standard Competitive to BLDC Motors Used for Blowers in Air Conditioners," in 2017 IEEE

- International Electric Machines and Drives Conference (IEMDC), Miami, FL, USA, May 2017, pp. 1–6.
- [64] J.-H. Park, J.-H. Seo, C.-H. Cha, and J. Lee, "Characteristics Analysis of 15kw Industrial Machine Using Synchronous Reluctance Motor for High Efficiency," in 2013 International Conference on Electrical Machines and Systems (ICEMS), Busan, Oct. 2013, pp. 139–142.
- [65] S. J. Mun, Y. H. Cho, and J. H. Lee, "Optimum Design of Synchronous Reluctance Motors Based on Torque/Volume Using Finite-element Method and Sequential Unconstrained Minimization Technique," IEEE Transactions on Magnetics, vol. 44, no. 11, pp. 4143– 4146, Nov. 2008.
- [66] S. Stipetic, D. Zarko, and N. Cavar, "Design Methodology for Series of IE4/IE5 Synchronous Reluctance Motors Based on Radial Scaling," in 2018 XIII International Conference on Electrical Machines (ICEM), Alexandroupoli, Greece, Sep. 2018, pp. 146–151.
- [67] CM Spargo, BC Mecrow, and JD Widmer, "Application of Fractional Slot Concentrated Windings to Synchronous Reluctance Machines," in 2013 International Electric Machines and Drives Conference, Chicago, IL, USA, 2013, pp. 618–625.
- [68] C. M. Spargo, B. C. Mecrow, J. D. Widmer, and C. Morton, "Application of Fractional-slot Concentrated Windings to Synchronous Reluctance Motors," IEEE Transactions on Industry Applications, vol. 51, no. 2, pp. 1446–1455, Mar. 2015.
- [69] Christopher Spargo, Barrie Mecrow, and James Widmer, "Synchronous Reluctance Motors with Toroidal Windings," in 2014 IEEE Energy Conversion Congress and Exposition (ECCE), Pittsburgh, PA, USA, 2014, pp. 1374–1378.
- [70] Myung-Seop Lim and Jung-Pyo Hong, "Design of High Efficiency Wound Field Synchronous Machine With Winding Connection Change Method," IEEE Transactions on Energy Conversion, vol. 33, no. 4, pp. 1978–1987, 2018.
- [71] V. Aramenko, I. Petrov, J. Nerg, and J. Pyrhonen, "Influence of the Air-gap Length and Semimagnetic Wedges on the Performance of a High-speed Synchronous Reluctance Motor with an Axially Laminated Anisotropic Rotor," in 2020 XI International Conference on Electrical Power Drive Systems (ICEPDS), St. Petersburg, Russia, Oct. 2020, pp. 1–6.
- [72] M. N. Ibrahim, P. Sergeant, and E. M. Rashad, "Synchronous Reluctance Motor Performance Based on Different Electrical Steel Grades," IEEE Transactions on Magnetics, vol. 51, no. 11, pp. 1– 4, Nov. 2015.
- [73] M. Takeno, K. Kiyota, Y. Murakami, A. Chiba, N. Hoshi, M. Take- moto, and S. Ogasawara, "Test Results of High Torque and High Efficiency SRMs Designed for 50kw Hybrid Electric Vehicle," in 2012 IEEE Power and Energy Society General Meeting, San Diego, CA, USA, Jul. 2012, pp. 1–2.
- [74] T. Matsuo, A. El-Antably, and T. Lipo, "A New Control Strategy for Optimum-efficiency Operation of a Synchronous Reluctance Motor," IEEE Transactions on Industry Applications, vol. 33, no. 5, pp. 1146–1153, Sep. 1997.
- [75] G. Sousa, B. Bose, and J. Cleland, "Fuzzy Logic Based On-line Efficiency Optimization Control of an Indirect Vector-controlled Induction Motor Drive," IEEE Transactions on Industrial Electronics, vol. 42, no. 2, pp. 192–198, Apr. 1995.
- [76] Faa-Jeng Lin, Ming-Shi Huang, Shih-Gang Chen, and Che-Wei Hsu, "Intelligent Maximum Torque per Ampere Tracking Control of Synchronous Reluctance Motor Using Recurrent Legendre Fuzzy Neural Network," IEEE Transactions on Power Electronics, vol. 34, no. 12, pp. 12 080–12 094, 2019.
- [77] H. D. Lee, S. J. Kang, and S. K. Sul, "Efficiency-optimized Direct Torque Control of Synchronous Reluctance Motor Using Feedback Linearization," IEEE Transactions on Industrial Electronics, vol. 46, no. 1, pp. 192–198, Feb. 1999.
- [78] S. Kim, S.-K. Sul, K. Ide, and S. Morimoto, "Maximum Efficiency Operation of Synchronous Reluctance Machine Using Signal Injection," in the 2010 International Power Electronics Conference - ECCE ASIA -, Sapporo, Japan, Jun. 2010, pp. 2000–2004.
- [79] T. Senjyu, T. Shingaki, and K. Uezato, "A Novel High Efficiency Drive Strategy for Synchronous Reluctance Motors Considering Iron Loss Using Neural Network," in APEC 2001. Sixteenth Annual IEEE Applied Power Electronics Conference and Exposition (Cat. No.01CH37181), Anaheim, CA, USA, vol. 2, Mar. 2001, pp. 1090–1095.

- [80] T. Senjyu, T. Shingaki, A. Omoda, and K. Uezat., "High Efficiency Drives for Synchronous Reluctance Motors Using Neural Network," in 2000 26th Annual Conference of the IEEE Industrial Electronics Society. IECON 2000. 2000 IEEE International Conference on Industrial Electronics, Control and Instrumentation. 21st Century Technologies, Nagoya, Japan, vol. 2, 2000, pp. 777–782 vol.2.
- [81] T. U. Jung, C. H. Yun, H. R. Cha, H. M. Kim, H. Nam, and J. P. Hong, "The Rotor Conductor Design for Starting Stability of Line-start Synchronous Reluctance motor," in IECON 2006 - 32nd Annual Conference on IEEE Industrial Electronics, Paris, France, Nov. 2006, pp. 1107–1112.
- [82] Yamamoto Shu, Adawey, John B., and Ara Takahiro, "Maximum Efficiency Drives of Synchronous Reluctance Motors by a Novel Loss Minimization Controller Considering Cross-magnetic Saturation," in 2009 IEEE Energy Conversion Congress and Exposition, San Jose, CA, USA, 2009, pp. 288–293.
- [83] A. Dziechciarz, C. Oprea, and C. Martis, "Multi-physics Design of Synchronous Reluctance Machine for High Speed Applications," in IECON 2016 - 42nd Annual Conference of the IEEE Industrial Electronics Society, Florence, Italy, Oct. 2016, pp. 1704–1709.
- [84] M. D. Nardo, G. Gallicchio, M. Palmieri, A. Marfoli, G. L. Calzo, M. Degano, C. Gerada, and F. Cupertino, "High Speed Synchronous Reluctance Machines: Materials Selection and Performance Boundaries," IEEE Transactions on Transportation Electrification, pp. 1–1, 2021.
- [85] P. Ramesh and N. C. Lenin, "High Power Density Electrical Machines for Electric Vehicles—Comprehensive Review Based on Material Technology," IEEE Transactions on Magnetics, vol. 55, no. 11, pp. 1–21, Nov. 2019.
- [86] C. Babetto, G. Bacco, and N. Bianchi, "Synchronous Reluctance Ma chine Optimization for High-speed Applications," IEEE Transactions on Energy Conversion, vol. 33, no. 3, pp. 1266–1273, Sep. 2018.

![](_page_9_Picture_26.jpeg)

Xuan Li was born in China. He received the B.S degree from Huazhong University of Science and Technology in 2021. Currently he is a M.S student at the same university. His research focuses on the design of synchronous reluctance machines.

![](_page_9_Picture_28.jpeg)

Yawei Wang (S'14-M' 19) received the B.S. and M.S. degrees in electrical engineering from China University of Mining and Technology, Xuzhou, China, in 2012 and Huazhong University of Science and Technology, Wuhan, China, in 2015, respectively. He also received the Ph.D. degree in electrical engineering from University of Padova, Padova, Italy, in

2019. From 2019 to 2020, he was a Postdoctoral Researcher with the Department of Electrical and Computer Engineering at McMaster University, Hamilton, ON, Canada. He is currently an Associate Professor at Huazhong University of Science and Technology, Wuhan, China. His research interests include the design and analysis of non or less rare-earth machines, and magnetic gears.

![](_page_10_Picture_2.jpeg)

Yuhang Cheng was born in China. He received the B.E.E. degree from the Shenyang University of Technology, Shenyang, China, in 2021. He is currently working towards the master's degree in electrical engineering from the Huazhong University of Science and Technology. His research interests include the design and

optimization of synchronous reluctance machines.

![](_page_10_Picture_5.jpeg)

Dawei Li (Senior Member, IEEE) received his B.E.E. degree from the Harbin Institute of Technology, Harbin, China, in 2010 and the Ph. D degree from the Huazhong University of Science and Technology, Wuhan, China. In 2015, he joined the Huazhong University of Science and Technology. His research areas include the

analysis and design of flux modulation permanent magnet machines.

![](_page_10_Picture_8.jpeg)

Ronghai Qu (Fellow, IEEE) was born in China. He received the B.E.E. and M.S.E.E. degrees from Tsinghua University, Beijing, China, and the Ph.D. degree from the University of Wisconsin–Madison, Madison, WI, USA, in 1993, 1996, and 2002, respectively, all in electrical engineering. In 1998, he joined the

Wisconsin Electric Machines and Power Electronics Consortiums, University of Wisconsin–Madison, WI, USA, as a Research Assistant. He became a Senior Electrical Engineer at Northland, a Scott Fetzer Company, Watertown, NY, USA, in 2002. Since 2003, he had been with the General Electric Global Research Center, Niskayuna, NY, USA, as a Senior Electrical Engineer in the Electrical Machines and Drives Laboratory. He has authored more than 230 published technical papers and is the holder of more than 50 patents/patent applications. Since 2010, he has been a Professor with Huazhong University of Science and Technology, Wuhan, China.