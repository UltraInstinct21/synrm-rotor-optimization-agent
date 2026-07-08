# **Design of Rotors for Synchronous Reluctance Motor: Analytical Treatment and Optimization**

Svetlana Orlova<sup>1</sup> , Vladislav Pugachov<sup>1</sup> , Anton Rassõlkin<sup>2</sup> , Ants Kallaste<sup>2</sup> , Toomas Vaimann<sup>2</sup> 1 Institute of Physical Energetics, Riga, Latvia <sup>2</sup>Tallinn University of Technology, Tallinn, Estonia E-Mail: sorlova@edi.lv

# **Acknowledgements**

The research has been supported by the European Regional Development Fund within the project "Development of a high-efficiency rare-earth metal-free electric motor". No. 1.1.1.2/VIAA/1/16/173 and by the Estonian Research Council under grant PUT1260 "Lifecycle Influenced Optimization Methodology for Electrical Motor-Drives".

# **Keywords**

«Design», «efficiency», «modelling», «synchronous motor», «test bench»

# **Abstract**

Various rotor designs have been investigated for synchronous reluctance motor (SynRM). In the investigation, the rotor geometry parameters are presented in view of the influence exerted on the *d-*axis and q-axis inductance of SynRMs, and an optimum combination of design parameters has been achieved for improvement the saliency ratio as well as the performance of the machine.

# **Introduction**

The first synchronous reluctance motor (SynRM) with rotating magnetic field was created by J. K. Kostko in 1923. Since then, much work has been done in order to optimize the rotor design of SynRM. The interest in such motors rapidly increased after the ABB had started commercial production of SynRMs for pump, fan, compressor, extruder, conveyor, and mixer applications. It was also necessary to find an alternative for permanent magnet motors because of their limited supply and high cost of rare-earth magnets [1]. ln the last century, SynRMs had low indications, their power did not exceed hundred watts, so these motors were of a limited use. Recently, with the advance of technologies for power converters and increasing requirements as to the conservation of energy, such machines have attracted considerable interest of manufacturers.

The principle of their operation is based on different reluctance in the direct (*d*) and the quadrature (*q*) axes and developed reluctance torque. When a magnetic field is applied through the rotor from the motor stator, a torque is created as the rotor tries to align itself in the best flux conducting angle relative to the stator field. The strength of the torque produced by the SynRM is directly proportional to the ratio of inductance of the q- and d-axis. SynRM electromagnetic torque is described by the equation:

$$T_{em} = \frac{m \cdot p \cdot U^2}{2 \cdot \omega} \cdot \left(\frac{1}{x_q} - \frac{1}{x_d}\right) \cdot \sin 2\gamma,\tag{1}$$

where *p* is the number of pole pairs; *m* is the number of phases;

- *U* is the phase voltage;
- *ω* is the angular frequency of armature current;
- *x<sup>d</sup>* is the direct axis synchronous reactance;
- *x<sup>q</sup>* is the quadrature axis synchronous reactance;
- is the load angle between the supply voltage and the fundamental harmonic of no-load EMF.

From this equation it is seen that the maximum torque value is directly proportional to the difference between the synchronous reactance along the longitudinal and the transversal rotor axes. Therefore, to raise the power developed by a machine of the same sizes it is necessary – at the maximum rotor permeance in the *d-*direction – to considerably reduce such permeance in the *q*-direction.

The ratio between d-axis and q-axis inductances defines the rotor saliency, that is, *ξ=xd/xq*. It should be noted that *xd>>xq* allows obtaining higher rotor saliency and, respectively, increased torque.

# **Analytical Treatment of the Rotor Designs**

The stator of a SynRM is similar to that of induction motor, so this can be produced in the existing assembly lines. The rotor of a such type of machine has no winding and no permanent magnets. As of now, three main types of the rotors (Fig.1.a, b,c) are known: salient pole, axially laminated anisotropy and transversally laminated anisotropy rotors.

It is commonly considered that the salient-pole rotors (Fig.1.a) have poor properties such as torque, power factor *etc.* to make them competitive in comparison with other mentioned rotors. The features of this type rotors are reviewed in the works: [1]-[9].

![](_page_1_Picture_12.jpeg)

Fig.1: Types of synchronous reluctance rotors: a) salient pole; b) axially laminated anisotropy; c) transversally laminated anisotropy, d) magneto-isolated poles

Axially laminated rotor (Fig.1b) – has axial laminations suitably shaped at each pole and insulated from each other using electrically and magnetically passive materials; the resulting stacks are connected through the pole holders to the central region to which the shaft is linked. A design analysis of this type rotor is presented in [2]- [4] where it is concluded that such a rotor has the best performance. The most lucrative feature of the design is the ability to drastically increase the number of flux barriers, which leads to increase in the magnetic saliency. In this work, the design of such type rotor is not investigated, since the process of its manufacturing is difficult and expensive.

Transversally laminated rotor (Fig.1.c) has laminations that are punched in the manufacturing process in a traditional way. Thin ribs are left at punching, thus various rotor segments are connected to each other by these ribs. The high number of holes and air inside the rotor makes the rotor structure weaker. A smooth motor torque is achieved by choosing the correct number of flux guides and flux barriers against the ratio of the stator slot number to the number of pole pairs. The main parameters to be chosen in designing the optimum rotor are: the number of magnetic barriers, the air/iron ratio, the width of radial and tangential ribs, the width of air gap, and the number of poles. A smooth motor torque is achieved by choosing the correct number of flux guides and flux barriers against the ratio of the stator slot number to the number of pole pairs [10].

The reluctance machine where radial poles were replaced by circumferential segments was earlier presented [11]. It was demonstrated that the new type of machine has an advantage over salient pole machine and with smaller number of poles these advantages are more distinct. It was also analytically revealed that this machine design has higher torque characteristics and the power factor, but no experimental testing was carried out. The consideration of flux paths demonstrates the advantage of this design, particularly in the fact that the radial expansion of the "interpolar space" has only a slight effect on the paths of direct axes and has more significant effect on the paths of the quadrature-axis. For the time being, the design of a rotor with magneto-isolated poles has not been studied sufficiently. The rotor of the reviewed motor is made as an iron cylinder divided by narrow radial-axial gaps into separate sectors, the number of which corresponds to the number of poles of the machine. The design of such rotor for a four-pole motor is presented in Fig.1.d.When a three-phase alternating current is supplied to the stator winding a rotating magnetic field arises, which is represented by two components: longitudinal *Ф<sup>d</sup>* and transverse *Ф<sup>q</sup>* actuated by magnetomotive force (MMF) components of the stator winding and *.* As a result of the interaction of the corresponding components of the magnetic flux with the stator's MMF an electromagnetic torque arises, which is defined by the equation:

$$T_{em} = F_{ad}\Phi_q - F_{aq}\Phi_d, \tag{2}$$

and is driving the rotor. At the same time, in the considered motor with poles shaped as separate sectors the air gap of magnetic fluxes along the transverse axis is much less than the total air gap along the longitudinal axis when and are equal, the magnetic flux *Ф<sup>d</sup>* is considerably less than flux *Фq,* which, in turn, causes the appearance of electromagnetic torque.

# **The Results of Numerical Modelling and Optimization of Rotor Designs**

A numerical modelling has been executed for three rotor designs: the salient pole rotor (Type 1), the transversally laminated rotor (Type 2), and the rotor with magneto-isolated poles (Type 3). In order to determine the best rotor design for SynRM, an optimization process has been carried out, which resulted in selection of the best option from various alternative solutions, thus making it possible to raise the torque of the motor, i.e. its efficiency. The main motor design parameters (which are constant for all types of rotors) are presented in Table I.

**Table I: SynRM geometrical data**

| Name                  | Unit | Value  |
|-----------------------|------|--------|
| Stator core length    | m    | 0.156  |
| Stator inner diameter | m    | 0.136  |
| Stator outer diameter | m    | 0.219  |
| Number of slots       | -    | 36     |
| Air-gap height        | m    | 0.0005 |
| Rotor inner diameter  | m    | 0.04   |
| Rotor outer diameter  | m    | 0.135  |

To optimize the rotor designs of SynRM an evolutionary strategy was applied. The evolutionary strategy operates with vectors of real numbers. Developing a solution begins with a mutation and crossing of individuals to obtain descendants, then it is followed by selection without repetition of the best individuals from the common generation of parents and descendants. The mutation is often implemented as an addition of a normally distributed random variable to each component of the vector. In this case, the parameters of the normal distribution are selfadapting during the execution of the algorithm. The stator part of all three presented motors is exactly the same; the main difference in the construction and materials comes from the rotor part. In order to determine the best rotor design for SynRM the optimization process was carried out, which resulted in selection of the best option from various alternative solutions and led to higher torque of the motor and, respectively, to its higher efficiency.

The influence of a rotor's tooth sizes on the SynRM performance was investigated using the equation for the pole coverage coefficient (Fig.2a, Fig.4):

$$\alpha_{\tau} = \frac{\alpha_{tooth}}{(\alpha_{tooth} + \alpha_{slot})} = \frac{\alpha_{tooth}}{\tau}$$
(3)

where ℎ is the tooth pitch angle; is the slot pitch angle; is the pole pitch.

*Type 1- SynRM with salient pole rotor*

The rotor design of Type 1 with salient pole is presented in Fig.2 in dependence on the pole coverage coefficient. As shown in Fig.2, the maximum is achieved when the pole coverage coefficient is equal to 0.5, which implies the equal tooth and slot pitch angles.

![](_page_3_Figure_8.jpeg)

Fig. 2: Identification of the SynRM rotor Type 1 design parameters and torque *vs*. pole coverage coefficient.

#### *Type 2- SynRM with transversally laminated anisotropy*

It has to be noted that the currently most widely applied type of rotor – i.e. transversally laminated rotor – has not been considered in our optimization, as it is accepted that the current design is the optimum one as shown in Fig.3.

![](_page_4_Picture_2.jpeg)

Fig. 3: Identification of the SynRM rotor Type 2 design parameters

*Type 3- SynRM with magneto-isolated poles*

Optimization of the rotor Type 3 with magneto-isolated poles was made using two parameters: the pole coverage coefficient and the tooth height in compliance with the evolutionary strategy. The cross-section with the main parameter of SynRM Type 3 is presented in Fig.4. The maximum of torque is achieved with the pole coverage coefficient equal to 0.85-0.9, and the tooth height – to 0.035-0.040 m. As can be seen from Fig.5.b, the tooth relative height does not exert any significant influence on the torque, but it can be important taking into account the specific torque. As is shown, with the relative height decreasing lower than 0.15 the pole saturation – and, respectively, the torque – are decreasing.

![](_page_4_Picture_6.jpeg)

Fig. 4: Identification of the SynRM rotor Type 3 design parameters

![](_page_5_Figure_2.jpeg)

Fig. 5: SynRM rotor Type 3 design: torque *vs.* the pole coverage coefficient and the relative tooth height Fig. 6 shows the results obtained by numerical modelling using the 2D finite element method applied for magnetic fields of the SynRM rotor Type3 *d*- and *q*-axes.

![](_page_5_Figure_4.jpeg)

Fig. 6: Magnetic flux and flux density distribution of SynRM rotor Type 3: a) magnetic flux in the quadrature axis b) magnetic flux in direct axis

The electromagnetic torque curves for three studied types of rotors are presented in Fig.7. The results obtained evidence that the maximum torque is achieved for the rotor with transversal lamination.

![](_page_5_Figure_7.jpeg)

Fig. 7: Torque *vs.* rotational angle for three rotor types

# **Test Setup**

The test bench, contributes to the reduction of the number of test runs and safe maintenance, reports of the test benches developed in different research centers cover many different areas for motor-drive testing. In this study, the efficiency map of SynRM motor-drive with Type 2 rotor is received. Fig.8 shows the experimental test setup including drive and load motor. SynRM are driven by a 30 kW industrial frequency converter (ABB ACS880) with control algorithm Direct Torque Control (DTC). A 37 kW frequency converter (ABB ACS800) induction motor setup is used as a load. The experiments are performed in a real-time setup including motor and frequency converter. The line currents are precisely measured in terms of total magnitude and harmonics. To measure the total current and low frequency current harmonics, the Fluke 1400s AC current clamps were used. The voltages are directly measured by the Dewetron data acquisition system in both terms of fundamental magnitude and low frequency harmonics. The Oxygen software designed to work with Dewetron were used for all needed adjustments and required values calculation. Motors speed and torque were measured by NCTE 4000-0250 torque transducer which is mechanically coupled between the loading and testing motors. Measurement system works with 10 kHz sampling frequency. The parameters of the tested motor are shown in Table II.

**Table II.** Parameter of the studied motor

| Parameter         | Unit  | SynRM  |
|-------------------|-------|--------|
| Motor frame size  | -     | 132 MA |
| Rated Power       | kW    | 10.5   |
| Rated Current     | A     | 22     |
| Rated Speed       | rpm   | 1500   |
| cosϕ              | -     | 0.6    |
| Moment of inertia | kg m2 | 0.048  |

![](_page_6_Picture_6.jpeg)

Fig.8: Test setup (a) and rotor of the tested machine (b)

Ratio of the motor shaft power (*mech\_motor*) to the total output power (*conv\_out\_total*) of the frequency converter is taken as motor efficiency:

$$\eta_{motor} = P_{mech\ motor}/P_{conv\ out\ tota} \tag{4}$$

The efficiency map of the SynRM are depicted in Fig. 9. SynRM has region of efficiency above 90% between 900…1800 rpm and 30..50 Nm.

![](_page_7_Figure_2.jpeg)

Fig.9: Efficiency map of the SynRM

The work earlier presented [12] was shown that the motor-drive system efficiency resembles the motor efficiency, which implies to the big effect of the motors on the whole system. In this essence, the drive systems losses can be ignored in some applications and studies. In case of the SynRM, the motor-drive system efficiency is similar to the motor efficiency, which is highly speed dependent in lower speeds.

# **Conclusions**

Based on the results obtained the following conclusions can be drawn:

- The rotor design features for SynRM have been investigated and technical parameters of three different rotor typeshave been compared. The values of electromagnetic torque have been defined for all studied rotor types that were modelled numerically using finite-element software.
- Comparison provided in the paper shows that SynRM with magneto-isolated poles rotor after design optimization can be comparable with a same size transversally-laminated rotor.
- Torque of reluctance motor with a rotor having a transversally laminated anisotropy where *xd* >> *xq* can be raised up to 40%. In motors with magneto-isolated poles type rotors where *xq* >> *xd* the increase in the electromagnetic torque reaches 25%.

For the future studies magneto-isolated poles rotor would be manufactured and the imperial comparison using described test setup would be made.

# **References**

- [1] Rassõlkin A., Orlova S**.,** Vaimann T., Belahcen A., Kallaste A. Enviromental and Life Cycle Cost Analysis of a Synchronous Reluctance Machine //Power and Electrical Engineering of Riga Technical University (RTUCON), 2016 57th International Scientific Conference
- [2] Hudak P. and Hrabovcova V. "Geometrical dimension influence of multi-barrier rotor on reluctance synchronous motor performances". International Symposium on Power Electronics, Electrical Drives, Automation and Motion SPEEDAM, May 2006, pp. S42-24 – S42-29.
- [3] Barta J., Ondrusek C., "Rotor design and optimization of synhronous reluctance machine". Science Journal 2015, pp.555- 559.
- [4] Pellegrino G., Jahns Th. M., Bianchi N., Soong W., Cupertino F.: The Rediscovery of Synchronous Reluctance and Ferrite Permanent Magnet Motors, Springer, pp. 136, 2016.

- [5] Dirba J., Lavrinovicha L., Dobriyan R., "Prospects for use of synchronous reluctance motors in low-power electrical devices", Latvian Journal of Physics and Technical Sciences, 2015, N2, pp.40-47.
- [6] Matsuo T., Lipo T. A., "Rotor design optimization of synchronous reluctance machine". IEEE Transactions on Energy Conversion, Vol. 9. No. 2, June 1994, pp. 359 – 365
- [7] Kamper M.J. and Volschenk A.F., "Effect of rotor dimensions and cross magnetization on Ld and Lq inductances of reluctance synchronous machine with cage less flux barrier rotor", IEE Proc.-Electr. Power Appl., vol. 141, no. 4, July 1994, pp. 213-220,
- [8] Moghaddam R. R., "Synchronous Reluctance Machine (SynRM) Design", Master Thesis, Royal Institute of Technology, Stockholm, 2007.
- [9] Dobriyan R., Vitolina S., Lavrinovicha L., Dirba J., "Theoretical and experimental research of synchronous reluctance motor", Latvian Journal of Physics and Technical Sciences, 2017, N 5, pp.38-47
- [10] Orlova S.**,** Vezzini A., Pugachov V., Analysis of parameters for optimal design of Synchronous Reluctance Motor // Power and Electrical Engineering of Riga Technical University (RTUCON), 2015 56th International Scientific Conference, pp. 345-348.
- [11] Lawrenson P. J. and Agu L. A., "Theory and performance of polyphase reluctance machines," Proc. Inst. Elect, Eng., vol. 111, no. 8, pp. 1435-1445, Aug. 1964.
- [12] Rassõlkin A., Heidari H., Kallaste A., Vaimann T., Pando J., Romero-Cadaval E. "Efficiency Map Comparison of Induction and Synchronous Reluctance Motors. 26th International Workshop on Electric Drives: Improvement in Efficiency of Electric Drives (IWED), Moscow, Russia, 2019. 978-1-5386-9453-4/19/\$31.00 ©2019 IEEE