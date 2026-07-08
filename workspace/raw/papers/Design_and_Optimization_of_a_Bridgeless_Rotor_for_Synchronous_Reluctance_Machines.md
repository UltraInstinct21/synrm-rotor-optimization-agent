![](_page_0_Picture_0.jpeg)

Received 5 April 2024, accepted 30 April 2024, date of publication 8 May 2024, date of current version 15 May 2024.

Digital Object Identifier 10.1109/ACCESS.2024.3398798

![](_page_0_Picture_3.jpeg)

# **Design and Optimization of a Bridgeless Rotor for Synchronous Reluctance Machines**

ARASH ALLAHYARI<sup>©1</sup>, (Graduate Student Member, IEEE), ILYA PETROV<sup>©1</sup>, JUHA J. PYRHÖNEN<sup>©1</sup>, (Senior Member, IEEE), LASSI AARNIOVUORI<sup>©1</sup>, (Senior Member, IEEE), PIA LINDH<sup>©1</sup>, AND MIIKA PARVIAINEN<sup>2</sup>

<sup>1</sup>Department of Electrical Engineering, Lappeenranta-Lahti University of Technology, 53850 Lappeenranta, Finland <sup>2</sup>Department of Mechanical Engineering, Lappeenranta-Lahti University of Technology, 53850 Lappeenranta, Finland

Corresponding author: Arash Allahyari (arash.allahyari@lut.fi)

Arash Allahyari received funding from the European Union (EU)'s Horizon Europe research and innovation program EU MSCA DN (Marie Skłodowska-Curie Actions Doctoral Network) under grant agreement no. 101072580, Integrated high-speed power systems for industry and mobile applications (HIPO). Ilya Petrov and Juha J. Pyrhönen received funding from the Research Council of Finland's Centre of Excellence in High-Speed Energy Conversion Systems (HiECSs).

**ABSTRACT** A bridgeless rotor of a synchronous reluctance machine is proposed to enhance the performance of high-power and -speed synchronous reluctance machines (SynRMs). Unlike traditional transversally laminated designs that rely on radial and tangential ribs or bridges to provide mechanical integrity for the rotor, the suggested rotor incorporates separate flux guides attached to non-magnetic back plates to form SynRM rotor modules that are stacked on the shaft of the machine. This innovative structure eliminates the need for radial and tangential bridges which form a performance-deteriorating bottleneck in the design of high-power SynRMs. The paper presents a detailed analysis of the electromagnetic and mechanical aspects of the proposed bridgeless rotor synchronous reluctance machine (BLRSynRM). Furthermore, a comprehensive optimization method is implemented to demonstrate the capabilities of the proposed BLRSynRM along with comparison with conventional transversally laminated SynRM. The results show a significant increase in torque and power factor compared with conventional structure rotor. However, the proposed bridgeless structure introduces new electromagnetic and mechanical challenges to machine design and they are explained and overcome in this research.

**INDEX TERMS** Synchronous reluctance machine, bridgeless rotor, high power, high speed, multi objective optimization.

#### I. INTRODUCTION

At the end of the era of internal combustion engines (ICE), close to 100 million cars and 20 million heavy vehicles have been manufactured annually. Considering the ongoing trend in transportation electrification, electric traction motors serve at the heart of this shift. The demand for high-power and high-speed electrical machines has risen and will rise significantly in the coming years. So far, the majority of the electric traction motor market has been dominated by interior permanent magnet motors (IPMs) that apply rare-earth permanent magnets. However, the scarcity of rare earth (RE) materials

The associate editor coordinating the review of this manuscript and approving it for publication was Sinisa Djurovic.

suggests that all future electric vehicles cannot necessarily be equipped with RE-magnet motors. Moreover, given the limitations related to the availability and expense of these PMs it is obvious that there is a need for alternative material-efficient machine types enabling future massive market of electric traction motors.

In general, all the machines utilized in transportation applications are supplied with a frequency converter to enable speed control. In transportation applications, the target is to have highly efficient but cheap and lightweight machines. In addition, the recyclability of the machine is getting more and more important.

Magnet-free machines such as synchronous reluctance machine (SynRM), switched reluctance and induction

![](_page_1_Picture_1.jpeg)

machine are attractive options for the industry. However, exclusion of PMs from a machine easily leads into a bulky machine and lower efficiency. The benefits of using permanent magnet excitation cannot be denied. Therefore, when permanent magnets are not utilized, the optimization of the specific power and efficiency of the machine is extremely important.

A synchronous reluctance rotor is a composition of flux guides and flux barriers. The rotor design of SynRMs presents a significant level of complexity due to considerable number of geometry variables, which can extend to as many as five variables for each barrier based on the method used for geometric parametrization. As a result, the adoption of an appropriate parametric approach, optimization methods, or sensitivity analysis becomes extremely important in achieving an acceptable rotor design.

In this context, to simplify the analysis, researchers try to find relations between rotor geometry and critical performance factors such as average torque and torque ripple. This can be partially achieved through analytical analysis of the harmonics of the magnetic voltage (MV) distribution in the machine's air gap [\[1\],](#page-11-0) [\[2\].](#page-11-1)

<span id="page-1-1"></span><span id="page-1-0"></span>Complexity of torque ripple minimization in SynRMs comes from the fact that the interaction between the stator, especially stator teeth, and the rotor structure strongly affects the torque ripple. Hence, both rotor structure and stator geometries should be considered in the design of SynRMs in detail.

In this regard, [1] [and](#page-11-0) [2] [pro](#page-11-1)pose an analytical explanatory method to minimize torque ripple and maximize average torque simultaneously. The original idea is to decouple the effect of stator and rotor on average torque and torque ripple by introducing d- and q-axis insulation ratio and rotor slot pitch in d-axis. Results in [1] [and](#page-11-0) [\[2\]sho](#page-11-1)w that average torque can be maximized by finding the best insulation ratio, while the minimum torque ripple can be determined by the rotor slot pitch in d-axis. The proposed method in [1] [and](#page-11-0) [2] [is e](#page-11-1)ffective in reducing torque ripple and maximizing the average torque. However, in these studies, stator design is not considered effectively along with rotor design which suggests that this method might be affected by slot/pole combination.

Moreover, due to the existence of a high number of variables in SynRM rotor design there easily can be millions of possible rotor constructional combinations. In such a situation, explanatory approaches are not sufficiently accurate to reach an optimized rotor design. Hence, utilizing multi objective algorithms and careful design of models are imperative. It is also ingenious to limit the range of variables in the optimization process based on understandings from the machine operation principles [\[3\].](#page-11-2)

<span id="page-1-5"></span><span id="page-1-4"></span><span id="page-1-3"></span>References [4] [and](#page-11-3) [5] [pre](#page-11-4)sent a multi objective optimization process of a 2 kW, 4-pole/24-slot SynRM. The two cases studied have three flux barriers and five flux barriers on the rotor. Only rotor design geometries are considered for optimization. Reference [6] [inv](#page-11-5)estigates the effect of the number and shape of flux barriers in rotor design in a 1500 rpm, 800 W 4-pole 36-slot SynRM.

<span id="page-1-8"></span><span id="page-1-7"></span><span id="page-1-6"></span>References [\[7\]](#page-11-6) and [\[8\]](#page-11-7) study a 700 W 4-pole/30-slot 3000 rpm motor design and the optimization of its three-fluxbarrier rotor to reach a lower torque ripple. Reference [9] [pro](#page-11-8)poses an optimization method based on structural approach to design a 1500 rpm, 200 W, 8-pole/24-slot SynRM. Mechanical design is considered in this study as a post process to check the stress in the rotor. Reference [\[10\]](#page-11-9) proposes a 12 kW SynRM for an elevator application where the speed of the machine is 167 rpm and the rated torque 700 Nm. Acceptable torque ripple is 6 %.

<span id="page-1-11"></span><span id="page-1-10"></span><span id="page-1-9"></span>Design of a high-speed high-power SynRMs brings additional challenges because of mechanical limitations that set considerable boundary conditions to the rotor design. Hence, the mechanical boundary conditions can highly affect the electromagnetic design of a machine. References [\[11\]](#page-11-10) and [\[12\]](#page-11-11) investigate design of a water cooled, 5 kW 4-pole/24 slot motor with maximum speed of 80,000 rpm. Three flux barriers were chosen for the rotor design. The torque ripple varies between 6%-18%. The rated power factor does not exceed 0.5 [\[11\].](#page-11-10)

<span id="page-1-12"></span>Reference [\[13\]](#page-11-12) discusses a design of a 20kW, 4-pole/24 slot SynRM with the maximum speed of 30,000 rpm. The rotor has thick radial ribs so that it can withstand the high speed. The ribs deteriorate the saliency and therefore diminish the performance of the machine.

<span id="page-1-13"></span>Reference [\[14\]](#page-11-13) explains design of a SynRM for high-speed traction application. The machine is designed with six poles and 36 slots with natural streamline rotor flux guides as it is claimed that the streamline flux guides can give a better performance than other shapes such as rectangular flux guides. Reference [\[14\]](#page-11-13) considers both electromagnetic and mechanical design of the rotor to increase performance. The study includes the design of radial ribs between the barriers. However, results do not show significant enhancements in torque and power factor. A similar approach was adopted in the design of a 75 kW, 12 000 rpm SynRM for hybrid electric vehicle application [\[15\].](#page-11-14)

<span id="page-1-15"></span><span id="page-1-14"></span>Reference [\[16\]](#page-11-15) proposes a new parametrization for the flux barriers to enhance the performance of a 10 000 rpm SynRM. A 6-pole rotor with three flux barriers and 36 stator slots is considered. However, torque ripple is high in this research (> 14%). Only average torque measurements are presented. The maximum torque reached is 85 Nm.

<span id="page-1-16"></span>In [\[17\], d](#page-11-16)esign guidelines for high-speed SynRMs and PMaSynRMs are explained, and these methods are applied in the design of a 4-pole/24-slot PMaSynRMs with maximum speed of 80,000 rpm.

<span id="page-1-2"></span>In a rotor of a high-speed SynRM utilizing iron ribs and bridges it is essential to guarantee the mechanical integrity of the rotor [\[11\],](#page-11-10) [\[12\],](#page-11-11) [\[13\],](#page-11-12) [\[14\],](#page-11-13) [\[15\],](#page-11-14) [\[16\]. H](#page-11-15)owever, existence of iron in q-axis causes increased quadrature axis armature reaction, resulting in increased q-axis inductance, and reduced saliency of the machine and, as a result, deteriorates

![](_page_2_Picture_1.jpeg)

the performance of the machine. Hence, [\[18\],](#page-11-17) [\[19\],](#page-11-18) [\[20\]](#page-11-19) proposes using nonmagnetic ribs and bridges to increase the saliency of the machine. This is done by special type of lamination steel which is called dual phase (DP) material. After cutting the intended rotor geometry, the bridges and ribs are exposed to nitriding process to reduce their permeability [\[18\]. M](#page-11-17)oreover, DP materials have low magnetic saturation limit of 1.5 T and maximum permeability close to half of that of conventional lamination steels. This will highly reduce the overload capability of these machines [\[18\],](#page-11-17) [\[19\]. M](#page-11-18)easurement and comparison results presented in [\[18\]](#page-11-17) suggest that DP materials exhibit nonlinearity in magnetic properties which can bring additional challenges in the design process. Similar issues related to the existence of iron ribs and bridges are present in interior permanent magnet machines. Thus, using nonmagnetic ribs can improve the performance of the machine as proposed in [\[20\]. R](#page-11-19)esults in [\[20\]](#page-11-19) suggest that using DP materials reduces core loss considerably and thereby increases the efficiency by 1% - 2%.

Another approach to eliminate the iron bridges and ribs is to use an axially laminated rotor (ALR). The challenge in ALR design is how to connect the layers together reliably.

<span id="page-2-4"></span><span id="page-2-3"></span>References [\[21\]](#page-12-0) and [\[22\]](#page-12-1) present a design of a 2-pole 24-slot 12 kW axially laminated SynRM with maximum speed of 24,000 rpm. The rotor is made of ferromagnetic and non-magnetic material with a total of 47 layers of S355J0 and Inconel 718 for high saliency. Rotor layers are connected to teach other with hot isostatic pressing or vacuum brazing. The axially laminated SynRM is compared with a solid-rotor induction machine and slitted-solid-rotor induction machine in case of efficiency and power factor at maximum speed of 24,000 rpm [\[21\],](#page-12-0) [\[22\].](#page-12-1)

<span id="page-2-5"></span>In literature [\[23\], a](#page-12-2) method to remove radial and tangential ribs by using adhesive resin material inside rotor barriers to hold the rotor together is proposed. This concept is applied in the design of a 700 W, 6000 rpm, 4-pole/24-slot SynRM with 3 flux barriers per pole. The obtained results reported torque enhancement by around 17% - 35%. Simultaneously the motor power factor increased from 0.62 to 0.72. It should be mentioned that utilizing adhesive materials to maintain rotor integrity is not a mechanically strong method. Due to existing high centrifugal forces in high-power and -speed traction applications where the required power and speed can be above 100 kW and 10,000 rpm respectively such a construction cannot be used. Hence, the suggested method in [\[23\]](#page-12-2) is not feasible to be compared with the proposed method in this research.

The paper is organized as follows, Section [II](#page-2-0) introduces the bridgeless rotor (BLR) technology for SynRMs and initial machine design parameters. Section [III](#page-3-0) is a deep dive into electromagnetic design including multi-objective optimization for case of a 250 kW BLRSynRM. Section [IV](#page-7-0) provides details on design/optimization of conventional SynRM with ribs and bridges and performance comparison between proposed BLR and conventional machines in detail.

# <span id="page-2-2"></span><span id="page-2-0"></span>**II. THE PROPOSED BRIDGELESS SYNCHRONOUS RELUCTANCE MACHINE**

This study suggests an innovative rotor structure to enhance the performance of SynRMs including torque and power factor to make these machines more feasible for various high-speed and high-power applications. To withstand centrifugal forces, the radial and tangential bridges must be thicker as the rotor speed increases. Existence of these bridges deteriorates the motor electromagnetic performance significantly. Thus, design of a high-power (that requires larger rotor diameter) and high-speed rotor with the traditional technology for a SynRM is challenging.

This study proposes to eliminate traditional radial and tangential bridges in SynRM rotors to improve electromagnetic performance. An innovative method for attaching the rotor

<span id="page-2-1"></span>![](_page_2_Picture_10.jpeg)

![](_page_2_Picture_12.jpeg)

![](_page_2_Picture_14.jpeg)

**FIGURE 1.** The proposed bridgeless rotor SynRM in comparison with a conventional SynRM.

flux guides to the backplates is proposed. In the design process of any machine such as conventional SynRMs, to reach a higher torque with certain electromagnetic stress, the volume of the rotor has to be increased as the torque requirement increases. However, a higher rotor diameter creates mechanical issues at high operational speeds. In fact, mechanical integrity of the conventional transversally laminated SynRM rotor must be ensured through thicker radial and tangential bridges (Fig. [1a\)](#page-2-1). These thicker bridges create unintended flux paths and hence, create leakage flux, also increase q axis inductance and result in reducing mean torque and power factor. Because the innermost radial bridge is supposed to provide support for most of the rotor steel parts against centrifugal forces, it is always the thickest one. Hence, the thickness of the innermost radial bridge increases with maximum operational speed of the machine and outer diameter of the rotor. Consequently, a bridgeless rotor structure is proposed in this study (Fig. [1b\)](#page-2-1). In the proposed rotor structure, the radial and tangential bridges are eliminated and back plates in the axial direction are utilized to hold the rotor flux guides in place. The flux guides can be connected to the backplates e.g. by laser welding and in some cases even just using glue. However, glue is not suggested in this case because the mechanical properties of the glue weaken as temperature rises. Technically, whether to use glue depends on the value of shear stress between backplates and flux guides at the highest operating speed.

Several initial attempts have been made to manufacture a bridgeless rotor (BLR) through welding. One test sample is shown in Fig. [1b.](#page-2-1) Thus, it is shown in Fig. [1b](#page-2-1) that manufacture of the rotor modules with backplates is possible and further electromagnetic design and optimization is presented in this paper.

#### <span id="page-3-0"></span>**III. ELECTROMAGNETIC DESIGN OF THE PROPOSED BLRSynRM**

This section explains the details of electromagnetic design and aims to provide an in-depth investigation of the design and optimization process for the proposed BLRSynRM with main goal of achieving high performance while addressing existing limitations primarily associated with manufacturability.

Different applications set different requirements for an electrical machine design. In mobile applications, the system parameters have a direct effect on the design choices. The utilized power electronics together with the battery DC voltage level determine the terminal voltage of the machine.

The ratings of the power electronic switches set the maximum current that can be utilized. The mechanical transmission system and the tire dimensions fix the rotational speed of the machine considering vehicle speed demands. The effectiveness of the cooling system dictates the maximum continuous current density in the conductors.

The maximum speed of the machine in this study is 10,000 rpm and the motor power rating is 250 kW. Therefore, this machine requires a relatively large rotor and for

<span id="page-3-1"></span>**TABLE 1.** Initial Specifications of the machine under study.

| Variables                                      | value           |  |
|------------------------------------------------|-----------------|--|
| Stator external diameter, D <sub>se</sub> [mm] | 375             |  |
| Stack length, l [mm]                           | 210             |  |
| Machine volume (liter)                         | 23.2            |  |
| No. of poles, $2p$                             | 6               |  |
| No. of stator slots, $Q_s$                     | 36              |  |
| No. of phases, m                               | 3               |  |
| Base speed, $n_n$ [r/min]                      | 4000            |  |
| Maximum speed, $n_{\text{max}}$ [r/min]        | 10,000          |  |
| Terminal voltage, $U$ [rms, line-line]         | 500             |  |
| Airgap, $\delta$ [mm]                          | 0.8             |  |
| Stator steel material                          | M270-35A        |  |
| Rotor steel material                           | S355            |  |
| Cooling method                                 | water jacket    |  |
| Winding arrangement                            | 5/6 short pitch |  |

<span id="page-3-2"></span>![](_page_3_Figure_11.jpeg)

**FIGURE 2.** Introduction of Flux guides (FGs) with and w/o tooth tips (a) FGTs with tooth tips, (b) FGs w/o tooth tips, (c) effect of using tooth tips on the torque ripple and average torque.

a conventional SynRM the thickness of radial and tangential bridges should be calculated through mechanical stress analysis of the rotor. A study will be presented in Section [IV](#page-7-0) regarding mechanical analysis. Table [1](#page-3-1) shows the specifications of the machine under study.

In general, machine design is always a trade-off between performance and manufacturability. From electromagnetic point of view, it is better to have a high number of flux guides to increase the difference between d-axis and q-axis inductance (*L*d− *L*q) and reach higher saliency (*L*d/*L*q) to increase the average torque and power factor (PF). However, there are many geometrical limitations in the design of SynRMs.

![](_page_4_Picture_1.jpeg)

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

**FIGURE 3.** Optimization method.

In the case of a BLR, due to the existence of welding process, having more flux guides results in more welding. Hence, the total number of welding operations and manufacture cost of the given rotor will increase.

Thus, selection of a low number of flux guides is beneficial to ensure simpler manufacture and reliable operation of the rotor at high speeds. However, a higher number of flux guides was also studied, and the performance improvement was shown marginal. Hence, for this machine three flux guides are chosen.

Having tangential bridges on the rotor surface smoothens the rotor reluctance variations and helps in reducing torque ripple. However, increased q-axis armature reaction via these bridges causes machine performance to drop significantly. Thus, this innovative geometry is added to the flux guides close to airgap without any mechanical compromise. This geometry, called flux guide tooth tips (FGTT), partially seen in Fig. [1b,](#page-2-1) is used to help with the torque ripple and increasing average torque by decreasing the effective airgap of the machine. This approach resembles semi-closed rotor slots in other types of electrical machines such as induction machines.

Fig. [2a](#page-3-2) presents the proposed FGTT in each flux guide. Furthermore, the effect of utilizing FGTT on the torque ripple mitigation and average torque improvement is presented in Fig[.2c.](#page-3-2) Finite element analysis (FEA) results show that using FGTT decreases the torque ripple significantly and it also helps in increasing the average torque. Considering the benefits of using tooth tips on the flux guides (FG), it is worth using such an arrangement in the BLR and optimize the geometry of the FGTT to maximize the average torque and minimize torque ripple.

#### A. MULTI OBJECTIVE OPTIMIZATION OF THE BLRSynRM

In the design of conventional SynRMs the geometry of flux barriers is parametrized and optimized to reach a high saliency and to reduce torque ripple. However, in this study optimization approach is different, the geometry of flux guides that directly carry flux for the proposed BLRSynRM are optimized.

Due to the high number of geometry variables in the rotor, the design of SynRMs is complicated. Therefore, an effective optimization method should be utilized. To achieve this, a parametric FEA model is developed in Ansys Maxwell.

<span id="page-4-2"></span>**TABLE 2.** Rotor and stator geometry variables.

| Variable names in Fig. 4a | Definition                                      |
|---------------------------|-------------------------------------------------|
| <b>x</b> 1                | Distance of FG from shaft center [mm]           |
| x2                        | Height of FG in the shaft center [mm]           |
| x3                        | Height of FG in the arm [mm]                    |
| x4                        | Width of FG middle body [mm]                    |
| x5                        | Angle of FG arm from q axis [deg]               |
| x6                        | Width of FG tooth tips [mm]                     |
| x7                        | Height of FG tooth tips [mm]                    |
| x8                        | Stator inner Diameter [mm]                      |
| x9                        | Width of stator teeth under the tooth tips [mm] |
| x10                       | Slot body height [mm]                           |
| x11                       | Width of stator teeth at yoke [mm]              |
| x12                       | Yoke height* [mm]                               |
| x13                       | Slot opening width [mm]                         |
| x14                       | Stator tooth tip root height [mm]               |

<span id="page-4-1"></span>![](_page_4_Picture_14.jpeg)

![](_page_4_Picture_17.jpeg)

**FIGURE 4.** Geometry variables (a) rotor, (b) stator and (c) 3D view of proposed BLR with flux guides and backplates.

Later, with help of Pyaedt library a connection between Ansys Maxwell and MATLAB is created, and the optimization process is carried out using multi objective genetic

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

![](_page_5_Figure_4.jpeg)

**FIGURE 5.** Optimization results of proposed BLRSynRM (a) Pareto front, (b) Final selected design.

algorithm in MATLAB. Fig. [3](#page-4-0) demonstrates the main blocks of the implemented optimization method.

The model consisted of geometry variables for the rotor and stator are shown in Fig. [4a-b](#page-4-1) and explained in Table [2.](#page-4-2) There are five variables for every FG plus two variables for FG tooth tips and seven variables for stator geometry. Hence, in total there are 17 variables for the rotor with three FGs.

The yoke height (x12) is automatically calculated from the external diameter of the stator, hence, 6 variables for the stator are considered in the optimization process. Consequently, in total there are 23 variables to be optimized. Due to a high number of geometry variables, this machine is optimized in one operating point [current density equals 6 A/mm<sup>2</sup> , current vector angle measured from the d-axis is 60◦ ] at speed of 4000 rpm. Selection of this operating point has two main reasons:

- In theory of reluctance torque creation, maximum torque is achieved at current vector angle equal to 45 degrees. However, in practice, the rated torque is achieved with a current vector angle between 55-65 degrees considering saturation level of the stator and rotor [\[23\],](#page-12-2) [\[24\].](#page-12-3)
- 6 A/mm<sup>2</sup> current density is selected for continuous output power of the machine. This value is also related to the heat extraction capabilities of the water jacket to be used.

<span id="page-5-1"></span>**TABLE 3.** Geometry values of the selected design.

|                                          | FG1  | FG2     | FG3  |
|------------------------------------------|------|---------|------|
| x1 [mm]                                  | 34.8 | 70.4    | 87.2 |
| x2 [mm]                                  | 11.8 | 8.3     | 8.3  |
| x3 [mm]                                  | 14.5 | 9.6     | 9.9  |
| x4 [mm]                                  | 38.9 | 23.5    | 16.6 |
| x5 [deg]                                 | 34.1 | 24.3    | 15.7 |
| Width of FG tooth tips (x6               | 5)   | 1.6 m   | m    |
| Height of FG tooth tips (x'              | 7)   | 1.3 m   | m    |
| Stator Diameter (x8)                     |      | 209.3 r | nm   |
| Width of stator teeth under to tips (x9) | ooth | 9.6 m   | m    |
| Slot body height (x10)                   |      | 49.4 n  | nm   |
| Width of stator teeth at yoke (x11)      |      | 10.9 n  | nm   |
| Yoke height (x12)                        |      | 29.9 n  | nm   |
| Slot opening width (x13)                 | )    | 4 mr    | n    |
| Stator tooth tip root height (x          | k14) | 2.5 m   | m    |

Hence, 6 A/mm<sup>2</sup> current density and 60-degree current vector angle are adopted as the main operating point for the optimization.

The optimization objectives are:

- Maximizing average torque
- Minimizing torque ripple (percentage of peak to peak to average torque)

Fig. [5a](#page-5-0) shows the results of optimization. Optimization algorithm is a multi-objective genetic algorithm. A point (a design) which has the maximum average torque and torque ripple less than 10% is selected from pareto front.

It should be mentioned that if needed, rotor skew can be used to decrease torque ripple which can help with the noise and vibration of the powertrain. Investigation of rotor skew is presented in the following section.

Table [3](#page-5-1) shows the values of the geometry variables for the selected design shown in Fig. [5b.](#page-5-0)

Since this machine is designed for traction applications, investigation of the machine performance at various current densities and current vector angles is important. Fig. [6](#page-6-0) shows the average torque, torque ripple percentage and PF at current density up to 12 A/mm<sup>2</sup> which is meant for max. overload operation of the machine.

#### B. MECHANICAL ANALYSIS OF THE PROPOSED BRIDGELESS ROTOR

Stress analysis is performed to ensure the mechanical integrity of the proposed bridgeless rotor at high speeds. The backplate material used in this case is austenitic stainless steel 316L with yield strength of 290 MPa. Much stronger austenitic materials are available in case of higher stresses.

<span id="page-5-2"></span>In stress analysis of the proposed BLR, it is assumed that FGs are spot welded to the backplates. Hence, the stresses in the backplates are of high importance. Results of stress analysis at 12,000 rpm are shown in Fig. [7.](#page-6-1)

![](_page_6_Picture_1.jpeg)

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**FIGURE 6.** Performance of the selected BLR design vs. current density and current vector angle.

<span id="page-6-1"></span>![](_page_6_Figure_4.jpeg)

**FIGURE 7.** Result of stress analysis in the backplate of the proposed BLR at 12,000 rpm (front and back view).

The thickness of the backplates is 0.2 mm and the total thickness of the flux guides is 3 mm respectively. There are two 0.2 mm backplates per module with total axial length of 3.4 mm. Results show that the stress level is well in an acceptable range in the backplate. Furthermore, it should be noted that this analysis is performed at 12,000 rpm safety speed while the actual machine maximum speed is 10,000 rpm. Hence, the stress level will be significantly less than those shown in Fig. [7.](#page-6-1)

<span id="page-6-2"></span>**TABLE 4.** Effect of backplates and skew on the performance of the proposed BLRSynRM.

|                                                                                                                           | Average<br>torque<br>(Nm) | Torque<br>ripple<br>(%) | Power<br>factor | Computation time (sec)* |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------|-----------------|-------------------------|
| 2D FEA with rotor and<br>stator space factor of 0.97<br>(no skew)                                                         | 557.2                     | 6.5                     | 0.65            | 58                      |
| 2D FEA with rotor space<br>factor of 0.88 and stator<br>space factor of 0.97 (no<br>skew)                                 | 535.7                     | 6.2                     | 0.64            | 62                      |
| 3D FEA with flux guide<br>thickness of 4 mm and<br>backplate thickness of 0.5<br>mm (no skew)                             | 532.4                     | 7.6                     | 0.61            | 170,000                 |
| 2.5D FEA with rotor and<br>stator iron space factor of<br>0.97<br>(rotor skew with 6 slices)                              | 551.1                     | 2.4                     | 0.65            | 379                     |
| 2.5D FEA with rotor iron<br>space factor of 0.88 and<br>stator iron space factor of<br>0.97<br>(rotor skew with 6 slices) | 528.9                     | 3.1                     | 0.64            | 383                     |

### C. STUDY ON EFFECT OF BACKPLATES ON THE PERFORMANCE OF THE BLRSYNRM

The existence of backplates as shown in Fig. [1b](#page-2-1) and Fig. [4c,](#page-4-1) decreases the rotor iron core space factor. Moreover, the iron space factor (stacking factor) is different for the rotor and stator.

The length of one rotor steel lamination stack is 3 mm and the axial length of backplate is 0.2 mm. The flux guides are manufactured from 1 mm S355 constructional steel and the backplates from 0.2 mm austenitic stainless steel. Hence, two backplates of 0.2 mm will be welded to one the lamination of 3 mm and thereby rotor space factor will be (3/3.4 = 0.88).

The effect of using backplates can be analyzed from the view of dq inductances. Due to existence of backplates the d-axis inductance will decrease (because the permeance in the d-axis decreases) and a slight decrease also in the q-axis inductance can be expected. Hence, (*L*d− *L*q) and saliency (*L*d/*L*q) can decrease and as a result, average torque and power factor will decrease. Furthermore, torque ripple is expected not to be affected significantly.

To calculate the actual torque with the presence of backplates, two methods are utilized. First, the rotor space factor is set to 0.88 instead of 0.97 in 2D FEA which allows to get results fast (in a minute). Second, a 3D model is implemented while considering backplates as shown in Fig. [3c](#page-4-0) and FEA results are obtained. 3D FEA is time consuming (>40 hours) to simulate a full electrical period and requires a high computation power. Table [4](#page-6-2) shows the duration of each simulation case. Thereby, 3D FEA is not practical to be utilized for optimization where thousands of steps are required to reach an acceptable result.

<span id="page-7-1"></span>![](_page_7_Figure_2.jpeg)

![](_page_7_Figure_4.jpeg)

**FIGURE 8.** Results of finding optimum skew angle and optimum number of slices.

Table [4](#page-6-2) demonstrates a comparison between the results obtained by three different methods that have been used to calculate the performance of the machine with current density 6 A/mm<sup>2</sup> and current vector angle 60 degrees.

As it is summarized in Table [4,](#page-6-2) adding backplates reduces the average torque by roughly 4% (from 2.5D FEA).

# D. UTILIZATION OF ROTOR SKEW TO DECREASE TORQUE RIPPLE

To decrease the torque ripple step skew in rotor is utilized. A parametric analysis is performed to figure out the optimized number of slices and skew angle. Torque ripple is calculated based on ratio of peak to peak to average torque.

Fig. [8](#page-7-1) shows the effect of the number rotor skew slices and skew angle on the torque ripple and average torque using 2.5D FEA. It is seen that as the skew angle increases the average torque decreases which is not favorable.

Furthermore, high number of slices will complicate the rotor manufacture. Hence, considering three factors of average torque, torque ripple and number of skew slices, skew angle of 5 degrees with 6 slices is selected as follows for the slices, (−2.5deg, −1.5deg, −0.5deg, 0.5deg, 1.5deg, 2.5deg).

2.5D FEA calculations show that a step skew consisting of 6 slices and 5 mechanical degrees total skew angle will result in a small torque ripple of 2.4% and average torque of 551.1 Nm (at 6 A/mm<sup>2</sup> current density and 60 degrees of current vector angle).

It should be noted that since backplates are used, a reduction in average torque is expected. The effects of skew and backplates are summarized in Table [4.](#page-6-2) Adding backplates reduces the average torque roughly by 4% (from 2.5D FEA). Furthermore, using both backplates and skew (6 slices and 5 degree) reduces the average torque of the BLRSynRM by

<span id="page-7-2"></span>![](_page_7_Figure_15.jpeg)

![](_page_7_Figure_17.jpeg)

![](_page_7_Figure_19.jpeg)

**FIGURE 9.** (a) Depiction of proposed step skew, (b-c) Torque ripple contour map vs. current density and current vector angle using rotor skew with 6 slices and 5 mechanical degrees.

around 5%. Hence, choosing a careful value for skew angle will ensure a slight decrease in the average torque (1%) which is demonstrated in Fig. [8.](#page-7-1)

Moreover, Fig. [9a](#page-7-2) shows the proposed step skew and to demonstrate the effectiveness of selected skew Figs. [9b-c](#page-7-2) show the torque ripple percentage at various current vector angles and current densities with the suggested step rotor skew. By comparing Fig. [6b](#page-6-0) and Fig. [9c,](#page-7-2) it is shown that the rotor skew implemented decreases the torque ripple by 50%-60%. Moreover, it should be mentioned that if torque ripple of 6-9% is acceptable there is no need to perform rotor skewing.

#### <span id="page-7-0"></span>**IV. DESIGN AND OPTIMIZATION OF A CONVENTIONAL SYNRMS AND COMPARISON WITH BLRSynRM**

To better demonstrate the advantages of the proposed BLRSynRM a fair comparison with existing technology is essential. Thus, a conventional SynRM with the same dimensions and the same maximum available current is optimized using the same methods that have been used to optimize

![](_page_8_Picture_1.jpeg)

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

**FIGURE 10.** Stress analysis for the rotor of conventional transversally laminated rotor SynRM at 10,000 rpm.

the proposed BLRSynRM. Both machines have a 36-slot stator with 5/6 short pitch winding with six parallel paths and 18 turns/phase.

In this section the design method for conventional transversally laminated rotor SynRM design is presented. Firstly, a mechanical stress analysis is performed to figure out the thickness of radial and tangential bridges at maximum speed of 10,000 rpm. Then, a similar optimization method is used to optimize the geometry of rotor and stator.

#### A. INITIAL MECHANICAL ANALYSIS OF CONVENTIONAL SYNRM ROTOR

A stress analysis is performed to ensure the mechanical integrity of the rotor at the maximum speed. This is done by keeping mechanical safety factor higher than 1.5 in the critical bridges at the maximum operating speed (10,000 rpm).

After several iterations to reach an acceptable stress level as shown in Fig. [10,](#page-8-0) it is found that:

- The width of innermost radial bridge (b1) should be higher than 8 mm.
- The width of b2 should be higher than 4 mm.
- The width of tangential bridges on the surface should be higher than 2 mm.

Such thick bridges are required to maintain the rotor strength with a safe margin at the maximum operating speed (diameter of the rotor is 220 mm). Moreover, these thick bridges cause the saliency and difference between dq axis inductances (*L*d−*L*q) to reduce and as a result average torque and power factor decreases significantly. Thus, the machine's active length needs to be increased to reach the required torque. Consequently, as the operating speed increases, the design of the conventional SynRM gets more complicated, and a bulky machine is inevitable.

#### B. MULTI OBJECTIVE OPTIMIZATION OF THE CONVENTIONAL SYNRM

An optimization process identical to BLRSynRM optimization is implemented for the conventional SynRM using multi objective genetic algorithm. In this optimization there are 15 optimization variables in total for a three-barrier structure of the rotor and six optimization variables for the stator geometry.

<span id="page-8-1"></span>![](_page_8_Figure_15.jpeg)

![](_page_8_Figure_17.jpeg)

**FIGURE 11.** Optimization results for the conventional SynRM.

Fig. [11](#page-8-1) shows the optimization results for the conventional SynRM design. From the results it is seen that the conventional transversally laminated SynRM can hardly reach 445 Nm average torque while the proposed BLRSynRM can reach 560 Nm (26% increase) with the same current density.

The rated-point power factor (PF) of the conventional SynRM is 0.5 versus the PF of 0.65 of the BLRSynRM. Moreover, the performance of the conventional SynRM versus current density and current vector angle is shown in Fig. [12.](#page-9-0) The generated torque at maximum current density is roughly equal to 774 Nm. In Fig. [12b,](#page-9-0) the torque ripple is between 7 % − 15 %. Hence, skew is essential to achieve an acceptable torque ripple.

Based on 2.5D FEA, with a rotor skew of 6 slices and 5 degrees skew angle for the conventional SynRM (similar to BLR skew), the torque ripple drops to 2% - 6% and the average torque also drops to 433 Nm at 6 A/mm<sup>2</sup> current density and 774 Nm at maximum current density. Besides, Fig. [12c](#page-9-0) shows that PF is at maximum value of 0.5 and significantly decreases with increase of current density to 0.31. Hence, for the conventional SynRM, operation at high current densities requires high power inverters and may not be practical.

#### C. PERFORMANCE COMPARISON OF CONVENTIONAL SYNRM AND PROPOSED BLRSYNRM

This section provides a detailed performance comparison between the proposed BLRSynRM and conventional SynRM.

Table [5](#page-9-1) presents the performance of proposed BLRSynRM with considering effect of backplates and rotor skew and

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

**FIGURE 12.** Performance of selected conventional SynRM vs. current density and current vector angle.

compares it with the performance of conventional SynRM with rotor skew at nominal and maximum current densities.

2.5D FEA results shown in Table [5](#page-9-1) indicate that at nominal and maximum current densities BLRSynRM generates 22%−27% more average torque and roughly 30% higher power factor than the conventional SynRM while applying similar skew. Hence, increments in both average torque and power factor (PF) are considerable. It should be noted that 0.49 PF at nominal current density is very low and might not be practical to run the conventional SynRM at this current.

PF equal to 0.64 of the proposed BLRSynRM is an acceptable value for a 6-pole SynRM, but low in comparison with PF of interior permanent magnet machines or even induction machines. Moreover, to have a better understanding of variable speed operation, efficiency and PF maps of both machines are calculated and are shown in Fig. [13.](#page-10-0)

In these maps, maximum input current fundamental is 1000 Arms and voltage limit is 500 Vrms line-to-line. It should be mentioned that high frequency harmonic losses induced by the PWM supply, mechanical losses, AC winding losses and rotor eddy current losses are not included in Fig. [13.](#page-10-0)

<span id="page-9-1"></span>**TABLE 5.** Comparison of conventional synRM and BLRSynRM.

| Performance at 6 and 12 A/mm <sup>2</sup> current density and                                                           | Average torque        | Torque<br>ripple | Power factor  |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------|---------------|
| current vector angle of 60                                                                                              | (Nm)                  | (%)              |               |
| degrees                                                                                                                 |                       |                  |               |
| BLRSynRM 2.5D FEA with rotor space factor of 0.88 and stator space factor of 0.97 (rotor skew with 6 slices, 5 degree)  | 528.9 Nm,<br>984.1 Nm | 3.1 %,<br>6.1 %  | 0.64,<br>0.49 |
| Conventional SynRM<br>2.5D FEA with rotor and<br>stator space factor of 0.97<br>(rotor skew with 6 slices, 5<br>degree) | 432.8 Nm,<br>774.5 Nm | 1.8 %,<br>5.5 %  | 0.49,<br>0.38 |

Therefore, the efficiency values shown in the maps are optimistic.

In Fig. [13a](#page-10-0) and Fig. [13b,](#page-10-0) it is seen that much wider areas of efficiency maps are above 0.95 for the proposed BLRSynRM in comparison with the conventional SynRM. BLRSynRM has bigger areas of 0.96 efficiency values, too. It should be noted that FEA calculations show that the iron loss in the rotor of the proposed BLRSynRM is 50% less than in the rotor of the conventional SynRM at peak current. These calculations are made without considering the effect of backplates and manufacturing processes where galvanic contacts between the laminates are established. Thereby the rotor iron losses can increase due to eddy currents in the FGs. However, originally, lower iron losses are expected in the proposed BLR because radial and tangential bridges have been eliminated. These bridges in the conventional SynRMs get saturated which increases the rotor core loss especially at peak current.

Furthermore, the BLRSynRM shows a maximum average torque of approximately 1000 Nm, which is notably higher than the conventional SynRM's 800 Nm, both at the same input current. This represents a 25% increase in average torque. The substantial increase of 200 Nm in the average torque of the BLRSynRM demonstrates its potential as a highly competitive solution in the realm of magnet-free machine.

It should be noted that as shown in Table [5,](#page-9-1) utilizing both backplates and rotor skew in BLRSynRM would decrease the average torque by around 5% and rotor skew in conventional SynRM would also reduce the average torque by around 2%.

Even considering these reductions, the increase in the average torque of BLR design would be 96.1 Nm (22%) and 209.6 Nm (27%) at 6 A/mm<sup>2</sup> and 12 A/mm<sup>2</sup> current densities respectively. Values of power factor for variable speed operation are shown in Fig. [13c](#page-10-0) and Fig. [13d.](#page-10-0) Because utilizing backplates and rotor skew do not affect the PF considerably.

![](_page_10_Picture_1.jpeg)

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**FIGURE 13.** Efficiency and PF maps of selected design both machines in variable speed operation up to 10,000 rpm while effect of backplates is not considered in BLR SynRM and effect of rotor skew is not considered in both BLR and conventional SynRM (current and voltage limits are 1000 Arms and 500 Vrms line-to-line).

Thus, comparison of PF maps of two machines is straightforward.PF values of the BLRSynRM are higher than 0.6 in most operating points and there are big areas with PF higher than 0.65 while in conventional SynRM, the PF is at maximum 0.52 and minimum 0.4. Hence, 25% - 30% increase in PF value is seen in the proposed BLRSynRM which is considerable and important from the inverter sizing point of view. Increase in PF results in lower inverter power rating and consequently a cheaper drive system.

Comparison of the output power of BLR and conventional SynRM is shown Fig. [14.](#page-10-1) Unfortunately, SynRMs are not good at keeping power after the base speed and power will drop significantly. Hence, the design of a machine and selection of its base speed should be done carefully. As shown in Fig. [14](#page-10-1) the proposed BLR can reach roughly 440 kW power while the conventional SynRM can reach 300 kW (with identical winding structure and input current). This demonstrates 47% increase in the power rating of the machine. Another important factor is that the drop of power in the BLR design is less than in the conventional SynRM in variable speed operation. Moreover, the power output at 10,000 rpm for BLR and conventional SynRMs are 157 kW and 65 kW. Hence, at maximum speed BLR SynRM can deliver 2.4 times more power with the same input current.

Consequently, even though the manufacture of the proposed BLR structure seems harder than manufacturing conventional rotors the achieved performance shows that the correct path for the rotor design of SynRMs is to eliminate bridges, especially, in case of high-power high-speed machines.

<span id="page-10-1"></span>![](_page_10_Figure_7.jpeg)

**FIGURE 14.** Output power comparison of BLR and conventional SynRMs.

It is worth mentioning the switched reluctance motors (SRMs) as another type of magnet free motor. Hence, it makes sense to compare SynRMs with SRMs from sizing and machine design point of view. However, SRMs require a dedicated converter to operate and design of a dedicated converter with peak power of 400 kW is a challenge. Hence, it might not be practical to design a SRM with high powers. While frequency converter for SynRMs is readily available on the market and there is a significant advantage for mass production as the converter hardware stays the same for different rotating field motor types.

#### **V. CONCLUSION**

A bridgeless rotor was proposed in this study to enhance the performance of synchronous reluctance machines at high power levels and speeds. In this structure, non-magnetic backplates are used to support the flux guides in the rotor and

![](_page_11_Picture_1.jpeg)

hence bridges over flux barriers are eliminated from the rotor lamination. This improves the electromagnetic performance (saliency and dq axis inductance) of the machine.

Firstly, an optimization method utilizing multi objective genetic algorithm was implemented for the proposed BLRSynRM and the geometry variables (in total 23) of the rotor and stator were optimized to reach maximum average torque and minimize the torque ripple. Usage of flux guide tooth tips was suggested to reduce torque ripple and help increase the average torque. Flux-guide tooth tips were also included in the optimizations. The optimization method implemented was able to decrease the torque ripple to 7% and achieve average torque up to 557 Nm at current density of 6 A/mm<sup>2</sup> and current vector angle of 60 degrees.

Then, 2.5D FEA and 3D FEA were utilized to calculate the effect of backplates in the rotor over average torque, torque ripple and power factor. A thorough analysis regarding rotor skew and the effect of the number of rotor slices was provided.

Secondly, a conventional SynRM was designed and optimized with the same optimization method with identical dimensions, and current density of BLRSynRM. Moreover, a mechanical stress analysis was performed to calculate the thickness of bridges required to maintain the rotor integrity at maximum speed of 10,000 rpm.

Thirdly, efficiency and PF maps of both machines up to 10,000 rpm with the identical current and voltage limits were calculated and performance of optimized conventional SynRM is compared with the optimized BLRSynRM. Results show that the proposed BLRSynRM can deliver considerably higher torque and PF in comparison with the conventional SynRM.

Therefore, this study shows that utilizing the backplate construction to support flux guides instead of bridges can considerably enhance the performance of SynRMs and bring these magnet-free machines to more applications such as automotive. It should be noted that from the manufacturability point of view the proposed BLR structure seems challenging. Nevertheless, given the benefits and ongoing efforts, manufacture of this type of bridgeless rotor is actively under development.

#### **ACKNOWLEDGMENT**

The content of this publication does not reflect the official opinion of the European Union (EU). Responsibility for the information and views expressed in the publication lies entirely with the authors.

#### **REFERENCES**

- <span id="page-11-0"></span>[\[1\] R](#page-1-0).-R. Moghaddam, F. Magnussen, and C. Sadarangani, ''Novel rotor design optimization of synchronous reluctance machine for low torque ripple,'' in *Proc. 20th Int. Conf. Electr. Mach.*, Marseille, France, Sep. 2012, pp. 720–724, doi: [10.1109/ICElMach.2012.6349952.](http://dx.doi.org/10.1109/ICElMach.2012.6349952)
- <span id="page-11-1"></span>[\[2\] R](#page-1-1).-R. Moghaddam and F. Gyllensten, ''Novel high-performance SynRM design method: An easy approach for a complicated rotor topology,'' *IEEE Trans. Ind. Electron.*, vol. 61, no. 9, pp. 5058–5065, Sep. 2014, doi: [10.1109/TIE.2013.2271601.](http://dx.doi.org/10.1109/TIE.2013.2271601)

- <span id="page-11-2"></span>[\[3\] C](#page-1-2). Madariaga, C. Gallardo, J. A. Tapia, W. Jara, A. Escobar, and M. Degano, ''Fast assessment of rotor barrier dimensional allowances in synchronous reluctance machines,'' *IEEE Access*, vol. 11, pp. 58349–58358, 2023, doi: [10.1109/ACCESS.2023.3284753.](http://dx.doi.org/10.1109/ACCESS.2023.3284753)
- <span id="page-11-3"></span>[\[4\] F](#page-1-3). Cupertino, G. Pellegrino, and C. Gerada, ''Design of synchronous reluctance motors with multiobjective optimization algorithms,'' *IEEE Trans. Ind. Appl.*, vol. 50, no. 6, pp. 3617–3627, Nov. 2014, doi: [10.1109/TIA.2014.2312540.](http://dx.doi.org/10.1109/TIA.2014.2312540)
- <span id="page-11-4"></span>[\[5\] G](#page-1-4). Pellegrino, F. Cupertino, and C. Gerada, ''Automatic design of synchronous reluctance motors focusing on barrier shape optimization,'' *IEEE Trans. Ind. Appl.*, vol. 51, no. 2, pp. 1465–1474, Mar. 2015, doi: [10.1109/TIA.2014.2345953.](http://dx.doi.org/10.1109/TIA.2014.2345953)
- <span id="page-11-5"></span>[\[6\] M](#page-1-5). Farhadian, M. Moallem, and B. Fahimi, ''Multimodal optimization algorithm for torque ripple reduction in synchronous reluctance motors,'' *IEEE Access*, vol. 10, pp. 26628–26636, 2022, doi: [10.1109/ACCESS.2022.3155158.](http://dx.doi.org/10.1109/ACCESS.2022.3155158)
- <span id="page-11-6"></span>[\[7\] M](#page-1-6). Chowdhury, A. Tesfamicael, M. Islam, and I. Husain, ''Design optimization of a synchronous reluctance machine for high performance applications,'' in *Proc. IEEE Transp. Electrific. Conf. Expo (ITEC)*, Detroit, MI, USA, Jun. 2019, pp. 1–6, doi: [10.1109/ITEC.2019.8790577.](http://dx.doi.org/10.1109/ITEC.2019.8790577)
- <span id="page-11-7"></span>[\[8\] M](#page-1-7). Chowdhury, M. Islam, and I. Husain, ''Modeling of electromagnetic torque including ripple harmonics in synchronous reluctance machines,'' *IEEE Trans. Ind. Appl.*, vol. 57, no. 6, pp. 5851–5863, Nov. 2021, doi: [10.1109/TIA.2021.3107806.](http://dx.doi.org/10.1109/TIA.2021.3107806)
- <span id="page-11-8"></span>[\[9\] C](#page-1-8). Lee and I. G. Jang, ''Topology optimization of synchronous reluctance motors considering the optimal current reference in the fieldweakening and Maximum-torque-per-voltage regions,'' *IEEE Trans. Energy Convers.*, vol. 38, no. 3, pp. 1950–1961, Sep. 2023, doi: [10.1109/TEC.2023.3259392.](http://dx.doi.org/10.1109/TEC.2023.3259392)
- <span id="page-11-9"></span>[\[10\]](#page-1-9) J.-C. Li, M. Xin, Z.-N. Fan, and R. Liu, ''Design and experimental evaluation of a 12 kW large synchronous reluctance motor and control system for elevator traction,'' *IEEE Access*, vol. 8, pp. 34256–34264, 2020, doi: [10.1109/ACCESS.2020.2974414.](http://dx.doi.org/10.1109/ACCESS.2020.2974414)
- <span id="page-11-10"></span>[\[11\]](#page-1-10) M. D. Nardo, G. L. Calzo, M. Galea, and C. Gerada, ''Design optimization of a high-speed synchronous reluctance machine,'' *IEEE Trans. Ind. Appl.*, vol. 54, no. 1, pp. 233–243, Jan. 2018, doi: [10.1109/TIA.2017.2758759.](http://dx.doi.org/10.1109/TIA.2017.2758759)
- <span id="page-11-11"></span>[\[12\]](#page-1-11) G. Gallicchio, M. D. Nardo, M. Palmieri, A. Marfoli, M. Degano, C. Gerada, and F. Cupertino, ''High speed synchronous reluctance machines: Modeling, design and limits,'' *IEEE Trans. Energy Convers.*, vol. 37, no. 1, pp. 585–597, Mar. 2022, doi: [10.1109/TEC.2021.3086879.](http://dx.doi.org/10.1109/TEC.2021.3086879)
- <span id="page-11-12"></span>[\[13\]](#page-1-12) E. Castagnaro, G. Bacco, and N. Bianchi, ''Impact of geometry on the rotor iron losses in synchronous reluctance motors,'' *IEEE Trans. Ind. Appl.*, vol. 55, no. 6, pp. 5865–5872, Nov. 2019, doi: [10.1109/TIA.2019.2939508.](http://dx.doi.org/10.1109/TIA.2019.2939508)
- <span id="page-11-13"></span>[\[14\]](#page-1-13) A. Credo, G. Fabri, M. Villani, and M. Popescu, ''Adopting the topology optimization in the design of high-speed synchronous reluctance motors for electric vehicles,'' *IEEE Trans. Ind. Appl.*, vol. 56, no. 5, pp. 5429–5438, Sep. 2020, doi: [10.1109/TIA.2020.3007366.](http://dx.doi.org/10.1109/TIA.2020.3007366)
- <span id="page-11-14"></span>[\[15\]](#page-1-14) A. Credo, M. Villani, G. Fabri, and M. Popescu, ''Adoption of the synchronous reluctance motor in electric vehicles: A focus on the flux weakening capability,'' *IEEE Trans. Transport. Electrific.*, vol. 9, no. 1, pp. 805–818, Mar. 2023, doi: [10.1109/TTE.2022.3204435.](http://dx.doi.org/10.1109/TTE.2022.3204435)
- <span id="page-11-15"></span>[\[16\]](#page-1-15) O. Korman, M. D. Nardo, M. Degano, and C. Gerada, ''A novel flux barrier parametrization for synchronous reluctance machines,'' *IEEE Trans. Energy Convers.*, vol. 37, no. 1, pp. 675–684, Mar. 2022, doi: [10.1109/TEC.2021.3099628.](http://dx.doi.org/10.1109/TEC.2021.3099628)
- <span id="page-11-16"></span>[\[17\]](#page-1-16) G. Gallicchio, M. D. Nardo, M. Palmieri, A. Marfoli, M. Degano, C. Gerada, and F. Cupertino, ''High speed permanent magnet assisted synchronous reluctance machines—Part I: A general design approach,'' *IEEE Trans. Energy Convers.*, vol. 37, no. 4, pp. 2556–2566, Dec. 2022, doi: [10.1109/TEC.2022.3176382.](http://dx.doi.org/10.1109/TEC.2022.3176382)
- <span id="page-11-17"></span>[\[18\]](#page-2-2) P. B. Reddy, A. El-Refaie, M. Zou, D. Pan, J. P. Alexander, N. Tapadia, K. Grace, K.-K. Huh, and F. Johnson, ''Performance testing and analysis of synchronous reluctance motor utilizing dual-phase magnetic material,'' in *Proc. IEEE Int. Electr. Mach. Drives Conf. (IEMDC)*, Miami, FL, USA, May 2017, pp. 1–8, doi: [10.1109/IEMDC.2017.8002024.](http://dx.doi.org/10.1109/IEMDC.2017.8002024)
- <span id="page-11-18"></span>[\[19\]](#page-2-2) P. B. Reddy, A. M. El-Refaie, S. Galioto, and J. P. Alexander, ''Design of synchronous reluctance motor utilizing dual-phase material for traction applications,'' *IEEE Trans. Ind. Appl.*, vol. 53, no. 3, pp. 1948–1957, May 2017, doi: [10.1109/TIA.2017.2661719.](http://dx.doi.org/10.1109/TIA.2017.2661719)
- <span id="page-11-19"></span>[\[20\]](#page-2-2) Y.-H. Jung, K. Kim, and M.-S. Lim, ''Performance improvement of rare-Earth free high-speed multilayer IPMSM using dual-phase magnetic material,'' in *Proc. IEEE Int. Magn. Conf. Short Papers (INTERMAG Short Papers)*, Sendai, Japan, May 2023, pp. 1–2, doi: [10.1109/intermagshortpa](http://dx.doi.org/10.1109/intermagshortpapers58606.2023.10228792)[pers58606.2023.10228792.](http://dx.doi.org/10.1109/intermagshortpapers58606.2023.10228792)

![](_page_12_Picture_1.jpeg)

- <span id="page-12-0"></span>[\[21\]](#page-2-3) V. Abramenko, I. Petrov, J. Nerg, and J. Pyrhönen, ''Impact of the current vector angle on the performance of a synchronous reluctance motor with an axially laminated anisotropic rotor,'' *IEEE Access*, vol. 9, pp. 102609–102622, 2021, doi: [10.1109/ACCESS.2021.3097539.](http://dx.doi.org/10.1109/ACCESS.2021.3097539)
- <span id="page-12-1"></span>[\[22\]](#page-2-4) V. Abramenko, I. Petrov, J. Nerg, and J. Pyrhönen, ''Synchronous reluctance motors with an axially laminated anisotropic rotor as an alternative in high-speed applications,'' *IEEE Access*, vol. 8, pp. 29149–29158, 2020, doi: [10.1109/ACCESS.2020.2971685.](http://dx.doi.org/10.1109/ACCESS.2020.2971685)
- <span id="page-12-2"></span>[\[23\]](#page-2-5) Y. Bao, M. Degano, S. Wang, L. Chuan, H. Zhang, Z. Xu, and C. Gerada, ''A novel concept of ribless synchronous reluctance motor for enhanced torque capability,'' *IEEE Trans. Ind. Electron.*, vol. 67, no. 4, pp. 2553–2563, Apr. 2020, doi: [10.1109/TIE.2019.2914616.](http://dx.doi.org/10.1109/TIE.2019.2914616)
- <span id="page-12-3"></span>[\[24\]](#page-5-2) O. Iegorov, O. Iegorova, M. Kundenko, and M. Andriy, ''The influence of the phase angle between the rotor magnetic axis and the stator winding current vector on the synchronous reluctance motor efficiency,'' in *Proc. IEEE Int. Conf. Modern Electr. Energy Syst. (MEES)*, Kremenchuk, Ukraine, Sep. 2019, pp. 62–65, doi: [10.1109/MEES.2019.8896480.](http://dx.doi.org/10.1109/MEES.2019.8896480)

![](_page_12_Picture_6.jpeg)

JUHA J. PYRHÖNEN (Senior Member, IEEE) was born in Kuusankoski, Finland, in 1957. He received the Doctor of Science (D.Sc.) degree from Lappeenranta-Lahti University of Technology (LUT), Finland, in 1991. He became a Professor of electrical machines and drives with LUT, in 1997. He is currently engaged in research and development of electric motors and powerelectronic-controlled drives. He has wide experience in the research and development of special

electric drives for, e.g., distributed power production, traction, and highspeed applications. Permanent magnet materials and applying or avoiding the use of them in machines have an important role in his research. He is also studying the possibilities of using carbon-based materials in electrical machines.

![](_page_12_Picture_9.jpeg)

ARASH ALLAHYARI (Graduate Student Member, IEEE) received the B.Sc. degree in electrical engineering and the M.Sc. degree in electrical power engineering from Urmia University, Urmia, Iran, in 2007 and 2011, respectively. He is currently pursuing the D.Sc. degree in electrical engineering with Lappeenranta-Lahti University of Technology (LUT University), Lappeenranta, Finland, which is part of the EU Horizon and the Marie Skłodowska-Curie Actions

(MSCA) Doctoral Network. He was a Research Assistant with Middle East Technical University, from 2020 to 2022, with a focus on the design of traction motors. He is a Researcher with the Laboratory of Electrical Drives, Department of Electrical Engineering, LUT University. His research interests include the design of synchronous reluctance machines, interior permanent magnet machines, and novel permanent magnet machines.

![](_page_12_Picture_12.jpeg)

LASSI AARNIOVUORI (Senior Member, IEEE) received the M.Sc. degree in electrical engineering and the D.Sc. degree in electric motors and drives from Lappeenranta-Lahti University of Technology (LUT), Lappeenranta, Finland, in 2005 and 2010, respectively. From 2017 to 2019, he was a Marie Curie Fellow with the School of Engineering and Applied Science, Aston University, Birmingham, U.K. He is currently an Associate Professor of electric transportation with the LUT

School of Energy Systems. His current research interests include all aspects related to electric transportation systems, especially wide band-gap power switches, high-speed machine technology, modulation methods, simulation of electric drives, efficiency measurements, and calorimetric measurement systems.

![](_page_12_Picture_15.jpeg)

PIA LINDH was born in Helsinki, in 1969. She received the M.Sc. degree in energy technology and the D.Sc. degree in electrical engineering (technology) from Lappeenranta-Lahti University of Technology (LUT), Lappeenranta, Finland, in 1998 and 2004, respectively. She is currently an Associate Professor with the Department of Electrical Engineering, LUT University, where she is engaged in teaching and researching electric motors and electric drives. Her research interests

include electrical machines, especially permanent magnet machines and drives.

![](_page_12_Picture_18.jpeg)

ILYA PETROV received the D.Sc. degree from Lappeenranta-Lahti University of Technology (LUT), Finland, in 2015. He is currently a Research Fellow with the Department of Electrical Engineering, LUT.

![](_page_12_Picture_20.jpeg)

MIIKA PARVIAINEN (Senior Member, IEEE) was born in Joensuu, Finland, in 1998. He received the M.Sc. (Tech.) degree in mechanical engineering from Lappeenranta-Lahti University of Technology (LUT), in 2023, where he is currently pursuing the D.Sc. (Tech.) degree in mechanical engineering.