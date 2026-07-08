# Metamodel-based Optimization of Synchronous Reluctance Motor Rotor

Svetlana Orlova Institute of Physical Energetics Riga, Latvia sorlova@edi.lv Vladislav Pugachov Institute of Physical Energetics Riga, Latvia magneton@edi.lv Janis Auzins Riga Technical University Riga, Latvia auzinsjp@latnet.lv Anton Rassölkin Tallinn University of Technology Tallin, Estonia anton.rassolkin@taltech.ee

Abstract— The optimum design of a magnetic system depends on different factors, attributable to the operation of the electromagnetic device. This research provides the optimization technique part that gives mathematically proven solution of the optimal rotor design of a synchronous reluctance machine with transversally laminated anisotropy. Current work proposes a resource-saving technique for shape optimization of the rotor by using metamodels in the form of local polynomial approximations. The optimal design results were obtained on the basis on proposed shape optimization method and were confirmed by finite element analyses and physical experiment. The object of investigation is synchronous reluctance motor based on modified 1,1 kW W21 WEG induction motor stator.

Keywords— Electric motors; Design optimization; Design for experiments; Response surface methodology;

#### I. INTRODUCTION

In order to define the best design structure of the synchronous reluctance motor rotor, optimization must be carried out implying selection of the best alternative for each specific criterion. The optimization of electrical machine is a complicated work involving the meeting of different criteria during the dealing with a range of constraints [1]. In order to implement the optimization, it is necessary to process a huge number of options, changing the combinations of the factors affecting criteria and restrictions that is a time-consuming process. Optimization involves the best possible methods and procedures applied to find feasible solutions for different technical and mathematical objectives. It includes mathematical results and numerical methods aimed at finding and identifying the best possible alternatives from the variety of options. Optimization methods make it possible to choose the best option without direct testing and evaluation of whole variety of available options. They are closely linked to the use of mathematical methods, logical procedures and algorithms implemented by means of computer hardware.

The basic objective of any optimization is to identify the features of a device or process that ensures the best conditions of functioning according to the previously adopted criteria.

To determine the best construction of the electric machine the optimization is necessary, as a result of which the best option will be chosen from various alternative solutions in relation to any specific criterion. The determination of the optimal and rational construction depends on various factors that characterize the operation of the machine of this design. The main criteria are:

- electromagnetic values;
- thermal quantities:
- manufacturing technology;

The research has been supported by the European Regional Development Fund within the project "Development of a high-efficiency rare-earth metal-free electric motor". No. 1.1.1.2/VIAA/1/16/173.

- geometrical dimensions and mass;
- selection of source material;
- manufacturing and operation costs.

A part of this research provides the optimization technique that gives mathematically proven solution of the optimal rotor design of a synchronous reluctance machine with transversally laminated anisotropy. This work proposes a resource-saving technique for shape optimization of the rotor by using metamodels in the form of local polynomial approximations. The algorithm of design for experiment is presented in Fig.1.

The main tool in planning for experiments is the Response Surface Methodology (RSM): a set of mathematical and statistical methods for modeling and analyzing the task in order to obtain the optimum response affected by several variables [2]. Response is a measure of performance and a quality parameter. The RSM approximation of the response function can be represented as (1):

$$y = f(x_1, x_2, \dots, x_q) + \varepsilon \tag{1}$$

The variables  $x_1$  and  $x_2$  are independent variables where the response y depends on them. The dependent variable y is a function of  $x_1$ ,  $x_2$  - the experimental error term, denoted as. Studying the response surface involves optimal selection of adequate process model and specifying the response effect formula using a set of mathematical methods on the basis on experimental data. It is assumed that independent variables are continuous and can be controlled by the researcher with a negligible error, while the response is a random value.

The surface response method was developed by G.E.P. Box and K.B. Wilson in 1951. In [3] Box and Wilson suggested using a square polynomial model. It was recognized

![](_page_0_Figure_25.jpeg)

Fig. 1. Step by step guide of optimization process using design for experiment and metamodel.

that this was only approximate, not accurate, model, which, however, was simple in evaluation and implementation, even if little was known about the process. In addition, Mead and Pike in [4] stated that the origin of RSM dates back to 1930s rooting in using response curves. Owing to active application and improvements, this method is used in various fields.

The primary task of the RSM is to find the optimal response. If there are several responses, the task is to find a compromise optimum that is optimized not just by a response. The second task is to understand how the response changes when the design variables change. The surface response can be depicted graphically. The graph visualizes the shape of the response surface, i.e. hills, valleys, and lines. This research paper presents a case study of RSM implementation for synchronous reluctance motor (SynRM) rotor.

# II. DESIGN OF EXPERIMENT

## *A. Aim & Objective*

Electric motor drives consume 43-46% of the global electrical power thus causing approximately 6040 Mt of CO2 emissions per year [5]. Considering that fact most of the machines currently in service are becoming worn and obsolete, it is clear that replacing them with new, more efficient ones, will result in significant environmental benefits and resource saving, as well as reducing production costs and, consequently, increase of competitiveness. The aforementioned factors highlight the necessity of designing an electric motor that includes a reduced number of permanent magnets or does not use them at all. In the last few years, SynRM have become popular due to their simplicity, safety and low production costs [6]. The principle of SynRM operation is based on different reluctance in the direct (d) and the quadrature (q) axes and developed reluctance torque. When a magnetic field is applied through the rotor from the motor stator, a torque is created as the rotor tries to align itself in the best flux conducting angle relative to the armature field. The value of the torque produced by the SynRM is directly proportional to the ratio of inductance of the d- and q-axis. SynRM electromagnetic torque is defined by the equation [7], [8], [9]:

$$T_{em} = \frac{m \cdot p \cdot U^2}{2 \cdot \omega} \cdot \left(\frac{1}{x_q} - \frac{1}{x_d}\right) \cdot \sin 2\gamma, \tag{2}$$

where is the number of pole pairs;

is the number of phases;

is the phase voltage;

is the angular frequency of armature current;

is the direct axis synchronous reactance;

is the quadrature axis synchronous reactance;

 is the load angle between the supply voltage and the fundamental harmonic of EMF.

The only component of the torque in a SynRM is the reluctance torque, therefore SynRMs must present a very high saliency ratio to increase the efficiency, maximum torque, power factor and constant power speed range [10].

The experiments were developed for SynRM rotor designs with transversally laminated anisotropy (TLA) rotor. The stator of SynRM is similar to the one of induction motor and was taken from 1,1 kW W21 WEG motor with IE2 efficiency class. The main motor stator design parameters are presented in Table 1.

TABLE I. MAIN MOTOR STATOR DESIGN PARAMETER

| 36 Slot Stator           |       |       |  |  |  |
|--------------------------|-------|-------|--|--|--|
|                          |       |       |  |  |  |
| Parameters               | Unit  | Value |  |  |  |
| Number of Slots          | -     | 36    |  |  |  |
| Outer diameter           | mm    | 139   |  |  |  |
| Inner diameter           | mm    | 91.2  |  |  |  |
| Stack Length             | mm    | 110   |  |  |  |
| Number of Turns          | turns | 47    |  |  |  |
| Number of parallel paths | -     | 2     |  |  |  |
| Coil pitch               | -     | 1-8   |  |  |  |
| Filling factor           | %     | 69.48 |  |  |  |
| Wire diameter            | mm    | 0.56  |  |  |  |

In this motor short-pitched winding with coil span from 1 to 8 are applied, as shown in Fig. 2. The short-pitched winding allows to improve wave-form of generated electromotive force, also eddy-current and hysteresis losses are reduced.

The saliency ratio of the studied SynRM is obtained by inserting flux barriers in the transversally laminated rotor. The number of flux barriers and their thickness decide how much magnetic flux can penetrate the rotor in d- and q-axes. Flux in d-axis should be as high as possible while flux in q-axis should be minimized. To minimize the flux in q-axis, the flux barrier should be as wide as possible, but the same time the amount of iron in d-axis is reduced which causes d-axis flux to decrease. This is why it is so important to find the right thicknesses of flux barriers giving the maximized saliency ratio.

To compile the function of objective optimization it is necessary to determine the desired result. The general objective is maximizing a response, minimizing a response or hitting a target. In this case the objective is the increasing of the maximum torque. Optimization of the SynRM rotor was

![](_page_1_Figure_21.jpeg)

Fig. 2. Short-pitched winding layout of studied electric motor.

![](_page_2_Picture_1.jpeg)

Fig. 3. View of investigated synchronous reluctance synchronous reluctance motor (r<sub>1</sub>-radial rib; r<sub>2</sub>-tangential rib)

performed using five parameters: rotor outer radius, radial rib, tangential rib, insulation ratio, number of barriers (Fig.3).

For correct evaluation of the flux barrier width and flux guide width it is used the coefficient insulation ratio (3):

$$K_W = \frac{w_b}{w_g},\tag{3}$$

where  $W_b$  is the sum of the flux air barrier widths, and  $W_g$  is the sum of the flux guide widths.

The coefficient  $K_W = 0$  means that the rotor is made completely of iron (no saliency), while  $K_W = 1$  signifies that the rotor is designed of lamination segments in which the numbers of air barriers and flux guides are equal. In it is reported that an optimum inductance is reached when this ratio is approximately 50:50 (i.e.  $K_W = 1$ ) [8], [11], [12].

#### B. Factors and Range

Defining the boundaries and factors, that should be independent variables and will affect the result. For the synthesis of metamodels, it is necessary to choose the variable parameters and their ranges, and to conduct of various calculations of the researched machine using the method of the finite elements. The chosen range of variable parameters is presented in Table 2.

TABLE II. MAXIMUM AND MINIMUM RANGE OF THE ALTERATION OF THE CHOSEN PARAMETERS

|    | Variables          | Unit | Limits                            |  |
|----|--------------------|------|-----------------------------------|--|
| x1 | Rotor outer radius | mm   | 45.25 <r<46.05< td=""></r<46.05<> |  |
| x2 | Radial rib         | mm   | 1<71<3                            |  |
| x3 | Tangential rib     | mm   | 1 <r<sub>2&lt;3</r<sub>           |  |
| x4 | Insulation ratio   | -    | 0.2< <i>K</i> <sub>W</sub> <1.2   |  |
| x5 | Number of barriers | -    | 1 <b<5< td=""></b<5<>             |  |

The parameters such as barrier number, tangential rib, radial rib, rotor outer radius and insulation ratio are used in the motor model in FEA to obtain an optimized rotor in terms of efficiency. Some constraints are imposed on each step. The rotor structure is not very strong mechanically due to the flux barriers. The saliency ratio improves as the number of flux barriers increases. Increasing the number of barriers is not recommended from the mechanical and manufacturing point of view – even adding more than 5 barriers does not practically

affect the machine torque [8]. The tangential ribs are designed to reinforce the rotor. Making tangential ribs very thin results in problems for manufacturing processes. Increasing the tangential rib thickness if the rotor causes the torque decrease. The radial ribs width should be proposed as small as possible considering the mechanical limitations. The shapes flux barrier is also significant and two main types of the barriers exist: round barriers and rectangular barriers For current optimization rectangular type of flux barriers is chosen with cut off design of the rotor: steel is partly removed, which present an additional barrier [13]. The outer and inner stator diameter, winding distribution, the stator slot number, the stator, and rotor material are defined as constant in the analysis.

#### C. Plan of numerical experiment

The Latin hyper cube plan of various experiments consisting of 31 combinations of variable parameters for TLA rotor has been drafted. For generating an experimental plan EDAOpt software [14], developed by RTU Scientific research of machine and mechanism dynamics laboratory, was applied; Experimental plan LH type is optimized using Mean Square Error

# D. Modelling of experiment

For simulation of the electromagnetic field of electrical machine and calculation of the necessary physical values a finite element software is used. Prepared Script allow to decrease calculation time.

# E. Synthesis of metamodel

The experimental results were produced in accordance with the chosen range (Table 2) and the experimental plan. The base of synthesis of metamodel is the approximation of the experimental data. The metamodels were synthesized based on the results of numerical calculations of the magnetic field. The coefficients are reduced to five decimal figures after the point. The main advantages of metamodels is the ability to perform simulations and understand the interconnection of input and output parameters, as well as prompt implementation of the optimization processes. The optimum Legendre polynomial items number was selected on the basis of cross-validation value, as shown in Fig. 4. This metamodel is consisting of 14 items. For the optimum cross-validation approximation value is 24.13. Figures in Appendix (Fig. 11) depicts relation of the investigated parameters, such as barrier number, tangential rib, radial rib, insulation ratio and rotor outer radius with the electromagnetic torque. Electromagnetic torque peak difference mainly depends on  $x_4$  and  $x_5$  in Legendre polynomial model, see Fig 5.

![](_page_2_Figure_20.jpeg)

Fig.4. Cross-validation value vs number of terms for response Y1

![](_page_3_Figure_1.jpeg)

Fig. 5. Saliency ratio  $(x_4)$  and number of barriers  $(x_5)$ vs electromagnetic torque (y1)

## F. Verify prediction

Using metamodel the optimal design of the SynRM rotor in five parameter difference it was obtained, see Table III.

TABLE III. THE OPTIMAL DESIGN OF THE SYNRM ROTOR PARAMETERS

| No. | Variables          | Unit | Limits |
|-----|--------------------|------|--------|
| 1.  | Air gap height     | mm   | 0.2    |
| 2.  | Radial rib         | mm   | 1      |
| 3.  | Tangential rib     | mm   | 1      |
| 4.  | Insulation ratio   | -    | 1      |
| 5.  | Number of barriers | -    | 4      |

The received data was examined using numerical calculation and physical experiment. Fig. 6 shows magnetic flux and flux density distribution of SynRM rotor,  $xd = 153 \Omega$  and  $xq=29.1 \Omega$ .

On Figure 7 the value of torque is presented for different current angles, since the maximum input torque is not reached at the theoretical value of 45 elec. deg. This is explained by the fact that with the load increasing the magnetizing force of the stator winding also increases, and the torque peak shifts to larger angles. Therefore, in the optimization process it is also required to find an optimal current phase angle [8], [15].

The main shortcomings of SynRMs are high torque ripple and low torque density which can be partially overcome by an adequate design of the magnetic configuration of the rotor. It states in [16]–[19] that the skewing of the SynRM rotor by one

![](_page_3_Figure_10.jpeg)

Fig. 6. Magnetic flux and flux density distribution of SynRM rotor in direct and axis

![](_page_3_Figure_12.jpeg)

Fig. 7. Torque vs current phase angle

![](_page_3_Figure_14.jpeg)

Fig.8. SynRM rotor angle vs torque with and without rotor skew

slot pitch to reduce the torque ripple drastically and skewing has only a little effect on the average torque. As it can be seen from Fig. 8 SynRM rotor skewing on 4 degrees that is equal one stator slot pitch allows to decrease torque ripple from 53% to 7%, but torque decreased by about 20 %. Torque ripple is calculated from the following equation (4):

$$T_{ripple} = \frac{T_{max} - T_{min}}{T_{avg}} \cdot 100 , \qquad (4)$$

where  $T_{max}$  is maximum value of torque in investigated time interval,  $T_{min}$  is minimum value of torque in investigated time interval and  $T_{avg}$  is average value of torque [20], [21],[22].

## III. EXPERIMENTAL RESULTS

To verify the proposed optimum rotor design, an experimental model was created; the model rotor, stator and experimental setup are shown on Figure 9. The object of investigation is synchronous reluctance motor based on modified induction motor 1,1 kW W21 WEG. Main technical data of the induction motor: 1,1 kW; U =380 V; f=50 Hz; I =2.69A; cos  $\phi$  =0.76; efficiency  $\eta$  = 81.6%; M =7.22 Nm; 2p=4, weight 18 kg. Experimental research was carried out in the laboratory of Riga Technical University, with a partial use of the equipment of Institute of Physical Energetics.

![](_page_4_Picture_1.jpeg)

Figure 9. a) Experimental Setup for motor testing. The motor under test is on the left. The load generator is on the right. The torque meter can be seen between two machines b) experimental rotor model without skew

In course of the experiments, the main energy characteristics of SynRM were determined. The involved motors were powered by variable-frequency drive YASKAWA GA 500 for industrial applications. Motor control was implemented using open-loop vector control. The no load and load tests results are given in Table IV and Table V respectivelly. Current vs. torque and current vs. efficiency graphs of SynRM are given on Fig.10, the maximum efficiency (89%) is achieved at torque equal 7,5 Nm at rated speed 1500 min-1 .

TABLE IV. NO-LOAD TEST RESULT OF THE SYNRM

| Voltage (V)       | 220 | 290  | 340  | 385  |
|-------------------|-----|------|------|------|
| Phase Current (A) | 1.3 | 1.33 | 1.33 | 1.33 |
| Speed (min-1<br>) | 750 | 1050 | 1347 | 1500 |

TABLE V. LOAD TEST RESULT OF THE SYNRM AT 1500 MIN-1

| Voltage (V)       | 380  | 385  | 380  | 380  | 385  | 390  |
|-------------------|------|------|------|------|------|------|
| Phase Current (A) | 1.6  | 2.08 | 2.33 | 2.7  | 3.49 | 5.01 |
| Input Power (W)   | 410  | 814  | 1118 | 1280 | 1650 | 2460 |
| Torque (Nm)       | 2.5  | 4.5  | 6.5  | 7.5  | 8.5  | 11.5 |
| Output Power (W)  | 368  | 670  | 988  | 1140 | 1319 | 1770 |
| Efficiency        | 87   | 87   | 88   | 89   | 80   | 72   |
| Speed (min-1<br>) | 1500 | 1500 | 1500 | 1500 | 1500 | 1500 |

![](_page_4_Figure_8.jpeg)

Fig.10. Motor current vs. torque & efficiency

## IV. CONCLUSION

The research comes up with a resource-saving technique for shape optimization of the rotor by using metamodels by means of local polynomial approximations. The developed technique could be applied for total motor design optimization when it is required. The obtained optimum design data was examined applying numerical calculation and physical experiment. The received experimental data are matching with the numerical experiment data, thus verifying the selected optimization method for analysis and optimization of the SynRM design. It should be noted that major energy savings of SynRM are also gained through the use of variable speed drive systems.

## REFERENCES

- [1] D. Pánek, T. Orosz, and P. Karban, "Artap: Robust Design Optimization Framework for Engineering Applications," *2019 3rd Int. Conf. Intell. Comput. Data Sci. ICDS 2019*, Dec. 2019.
- [2] N. Bradley, "Response surface methodology," *Nippon Shokuhin Kagaku Kogaku Kaishi*, vol. 60, no. 12, pp. 728–729, 2013, doi: 10.3136/nskkk.60.728.
- [3] G. E. P. Box and K. B. Wilson, "On the Experimental Attainment of Optimum Conditions," Journal of the Royal Statistical Society, Vol. 13, No. 1, 1951, pp. 1-45.
- [4] A. I. Khuri, W. H. Carter, and R. H. Myers, "'-" ' -- -i," pp. 1966– 1986, 1986.
- [5] P. Waide and C. U. Brunner, "Energy-Efficiency Policy Opportunities for Electric Motor-Driven Systems," *Int. energy agency*, vol. na, no. na, p. 132, 2011.
- [6] A. Rassõlkin *et al.*, "Life cycle analysis of electrical motor drive system based on electrical machine type," *Proc. Est. Acad. Sci.*, vol. 69, no. 2, pp. 162–177, 2020, doi: 10.3176/proc.2020.2.07.
- [7] J. Dirba, L. Lavrinovicha, and R. Dobriyan, "Prospects for use of synchronous reluctance motors in low-power electrical devices," *Latv. J. Phys. Tech. Sci.*, vol. 52, no. 2, pp. 40–48, 2015, doi: 10.1515/lpts-2015-0010.
- [8] S. Orlova, A. Vezzini, and V. Pugachov, "Analysis of parameters for optimal design of synchronous Reluctance Motor," in *2015 56th International Scientific Conference on Power and Electrical Engineering of Riga Technical University, RTUCON 2015*, 2015, doi: 10.1109/RTUCON.2015.7343178.
- [9] L. Lavrinovicha, J. Dirba, K. Sejejs, and E. Kamolins, "Synthesis of Electronically Commutated Synchronous Motors with Predefined Characteristics," *Latv. J. Phys. Tech. Sci.*, vol. 56, no. 2, pp. 3–11, 2019, doi: 10.2478/lpts-2019-0008.
- [10] J. R. Riba, C. López-Torres, L. Romeral, and A. Garcia, "Rareearth-free propulsion motors for electric vehicles: A technology review," *Renew. Sustain. Energy Rev.*, vol. 57, pp. 367–379, 2016, doi: 10.1016/j.rser.2015.12.121.
- [11] R. R. Moghaddam, F. Magnussen, and C. Sadarangani, "Synchronous Reluctance Machine (SynRM) Design," *Thèse*, pp. 1–103, 2007, doi: 10.1016/j.pragma.2012.06.014.
- [12] S. K. Kashif, *Design of a Permanent-Magnet Assisted Synchronous Reluctance Machine for a Plug-In Hybrid Electric Vehicle*. 2011.
- [13] S. Orlova, V. Pugachov, A. Rassõlkin, A. Kallaste, and T. Vaimann, "Design of Rotors for Synchronous Reluctance Motor : Analytical Treatment and Optimization Keywords Analytical Treatment of the Rotor Designs," *Proceeding EPE'19 ECCE Eur.*, no. 1, pp. 1–9, 2019.
- [14] J. Auzins, A. Janushevskis, and J. Janushevskis, "Optimized Experimental Designs for Metamodeling : Algorithm," vol. 33, no. 2, pp. 25–29, 2010.
- [15] Progress In Electromagnetics Research B, Vol. 35, 369–387,

2011," vol. 35, no. October, pp. 369-387, 2011.

- [16] X. B. Bomela and M. J. Kamper, "Effect of stator chording and rotor skewing on performance of reluctance synchronous machine," *IEEE Trans. Ind. Appl.*, vol. 38, no. 1, pp. 91–100, 2002, doi: 10.1109/28.980362.
- [17] Lappeenrannan teknillinen yliopisto Lappeenranta University of Technology. A comparative performance study of four-pole induction motors and synchronous reluctance issn 1456-4491 Lappeenrannan teknillinen yliopisto Digipaino 2003. 2003.
- [18] J. Dirba, N. Levin, S. Orlova, V. Pugachov, and L. Ribickis, "Optimization of the magnetic circuit of an axial inductor machine based on the calculation and analysis of magnetic field," in 2009 13th European Conference on Power Electronics and Applications, EPE '09, 2009.
- [19] R. Dobriyan, S. Vitolina, L. Lavrinovicha, and J. Dirba, "Theoretical and experimental research of synchronous reluctance motor," *Latv. J. Phys. Tech. Sci.*, vol. 54, no. 5, pp. 38–47, 2017, doi: 10.1515/lpts-2017-0032.
- [20] J. Bárta and Č. Ondrůšek, "Design and optimization of synchronous reluctance machine," *Proc. 16th Int. Conf. Mechatronics, Mechatronika 2014*, no. March 2015, pp. 60–64, 2014, doi: 10.1109/MECHATRONIKA.2014.7018236.
- [21] N. Levin, S. Orlova, V. Pugachov, B. Ose-Zala, and E. Jakobsons, "Methods to reduce the cogging torque in permanent magnet synchronous machines," *Elektron. ir Elektrotechnika*, vol. 19, no. 1, pp. 23–26, 2013, doi: 10.5755/j01.eee.19.1.3248.
- [22] K. Gulbis, E. Kamolins, and U. Brakanskis, "Synchronous reluctance machine with improved design of rotor mechanical strength connections," 2016 IEEE 4th Work. Adfile///C/Users/User/Downloads/Synthesis\_of\_Electronically\_C ommutated\_Synchronous.pdfvances Information, Electron. Electr. Eng. AIEEE 2016 Proc., 2017, doi: 10.1109/AIEEE.2016.7821820.

#### **APPENDIX**

![](_page_5_Figure_10.jpeg)

![](_page_5_Figure_11.jpeg)

![](_page_5_Figure_12.jpeg)

![](_page_5_Figure_13.jpeg)

![](_page_5_Figure_14.jpeg)

Fig 11. Investigated parameters a) outer rotor diameter (x1), b) radial rib (x2), c) tangential rib (x3) d)insulation ratio (x4) and e) number of barriers (x5) vs electromagnetic torque (y1)