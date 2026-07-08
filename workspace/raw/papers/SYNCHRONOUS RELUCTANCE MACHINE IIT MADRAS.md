# **SYNCHRONOUS RELUCTANCE MACHINE DESIGN AND CONTROL**

*A Project Report*

*submitted by*

#### **SUSHANT SAXENA**

*in partial fulfilment of the requirements for the award of the degree of*

#### **MASTER OF TECHNOLOGY**

![](_page_0_Picture_6.jpeg)

**DEPARTMENT OF ELECTRICAL ENGINEERING INDIAN INSTITUTE OF TECHNOLOGY, MADRAS. JUNE 2022**

### **THESIS CERTIFICATE**

This is to certify that the thesis entitled **SYNCHRONOUS RELUCTANCE MACHINE DESIGN AND CONTROL**, submitted by **Sushant Saxena**, to the Indian Institute of Technology Madras, for the award of the degree of **Master of Technology**, is a bona fide record of the research work carried out by him under my supervision. The contents of this thesis, in full or in parts, have not been submitted to any other Institute or University for the award of any degree or diploma.

#### **Dr. Kamalesh Hatua**

Associate Professor, Department of Electrical Engineering, IIT Madras, Chennai-600036

Place: Chennai

Date:

## **ACKNOWLEDGEMENTS**

<span id="page-2-0"></span>It gives me immense pleasure to express my sincere and heartfelt gratitude to my guide, Dr Kamalesh Hatua, IIT Madras, for giving me the opportunity to learn and flourish under his guidance. I am grateful for his constant support, motivation and valuable feedback throughout my studies, especially during the course of this project. I consider myself fortunate to have the opportunity to work in the Power Electronics and Machines Laboratory under his supervision.

I am extremely thankful for the constant support and valuable suggestions provided by Mr Kunal Layek, PhD scholar, IIT Madras. I also thank Mr Shuvankar Dey, MS scholar, IIT Madras and Mr Pradeep for their support and help during the hardware assembly.

I would like to extend my appreciation to my fellow lab mates and friends for making this a joyful and memorable journey.

## **ABSTRACT**

<span id="page-3-0"></span>KEYWORDS: SynRM Control; Sensored Vector Control; Finite Element Analysis

With the advancements in digital control technology, Synchronous Reluctance Machines can become a viable alternative for Permanent Magnet Synchronous Machine and Induction Machine. The most conventional control is Maximum Torque Per Ampere when the machine is operating below the rated speed. However, oversimplification and neglecting saturation, while estimating the direct and quadrature axis inductances results in an inefficient control strategy. With the help of finite element analysis, we can remove these assumptions and come up with improved control strategies such that drive utilization is maximised.

This project report presents the conventional operating regions for a 22kW SynRM, and then uses finite element analysis to find better operating points for the machine. MATLAB/SIMULINK is used for the verification of sensored vector control. Finite element analysis is performed using Ansys MAXWELL-2D. Back to back converter was also assembled for the upcoming 22kW SynRM.

### **TABLE OF CONTENTS**

|   |     |                 | ACKNOWLEDGEMENTS        |                                             | i    |
|---|-----|-----------------|-------------------------|---------------------------------------------|------|
|   |     | ABSTRACT        |                         |                                             | ii   |
|   |     | LIST OF TABLES  |                         |                                             | vi   |
|   |     | LIST OF FIGURES |                         |                                             | viii |
|   |     | ABBREVIATIONS   |                         |                                             | ix   |
|   |     | NOTATION        |                         |                                             | x    |
| 1 |     |                 | INTRODUCTION            |                                             | 1    |
|   | 1.1 |                 | SynRM Overview          |                                             | 2    |
|   | 1.2 |                 | Control Techniques      |                                             | 3    |
|   | 1.3 |                 | Outline Of the Report . |                                             | 3    |
| 2 |     |                 |                         | SynRM MODELLING and CONTROL                 | 5    |
|   | 2.1 |                 |                         | Dynamic Equations of SynRM .                | 6    |
|   |     | 2.1.1           |                         | Stator Voltage Equations .                  | 7    |
|   |     | 2.1.2           |                         | Developed Torque Equation .                 | 9    |
|   | 2.2 |                 |                         | SynRM Control Below and Beyond Base Speed . | 10   |
|   |     | 2.2.1           |                         | Maximum Torque Per Ampere (MTPA)            | 10   |
|   |     | 2.2.2           |                         | Sensored Vector Control Scheme              | 11   |
|   |     | 2.2.3           |                         | Control Parameters .                        | 12   |
|   |     |                 | 2.2.3.1                 | Current Loop .                              | 13   |
|   |     |                 | 2.2.3.2                 | Speed Loop .                                | 14   |
|   |     | 2.2.4           |                         | Field Weakening Operation                   | 15   |
|   |     |                 | 2.2.4.1                 | Normalization of Machine Equations          | 15   |

|   |     |            | 2.2.4.2<br>Operation Beyond Rated Speed                    | 18 |
|---|-----|------------|------------------------------------------------------------|----|
|   |     | 2.2.5      | Power Factor                                               | 21 |
|   | 2.3 |            | Simulation Results and Inferences                          | 23 |
|   |     | 2.3.1      | Below Base Speed Operation                                 | 24 |
|   |     | 2.3.2      | Beyond Base Speed Operation                                | 25 |
|   |     | 2.3.3      | Inferences                                                 | 27 |
|   | 2.4 |            | Conclusion .                                               | 27 |
| 3 |     |            | SATURATION EFFECT & FINITE ELEMENT ANALYSIS                | 28 |
|   | 3.1 |            | Effect of Saturation                                       | 28 |
|   |     | 3.1.1      | Estimation of<br>Ld<br>and<br>Lq                           | 29 |
|   |     | 3.1.2      | Power Factor                                               | 30 |
|   |     | 3.1.3      | Torque                                                     | 31 |
|   | 3.2 |            | FEA Simulation and Results                                 | 31 |
|   |     | 3.2.1      | Inductance Estimation                                      | 32 |
|   |     | 3.2.2      | Torque                                                     | 34 |
|   |     | 3.2.3      | Power Factor                                               | 36 |
|   | 3.3 |            | Conclusion .                                               | 38 |
| 4 |     |            | HARDWARE ORGANISATION                                      | 39 |
|   | 4.1 |            | Brief overview of Major Components .                       | 39 |
|   |     | 4.1.1      | IGBT Module SKM200GB12E4 & Gate Driver SKYPER-32-<br>PRO R | 39 |
|   |     | 4.1.2      | PD-Card                                                    | 40 |
|   |     | 4.1.3      | Controller-TMS320F28335                                    | 40 |
|   | 4.2 |            | Hardware Setup .                                           | 40 |
|   | 4.3 |            | Conclusion .                                               | 41 |
| 5 |     | CONCLUSION |                                                            | 42 |
|   | 5.1 |            | Summary of the Present Work .                              | 42 |
|   | 5.2 |            | Future Scope of Work .                                     | 43 |

| A | Machine Parameters                | 44 |
|---|-----------------------------------|----|
| В | FEA modelling in Ansys MAXWELL-2D | 45 |

### **LIST OF TABLES**

<span id="page-7-0"></span>

| A.1 | Machine Parameters. |  |  |  |  |  |  |  |  |  |  |  |  |  | 44 |
|-----|---------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|----|
| A.2 | Winding Details     |  |  |  |  |  |  |  |  |  |  |  |  |  | 44 |

### **LIST OF FIGURES**

<span id="page-8-0"></span>

| 1.1  | Reluctance torque.                                                      | 2  |
|------|-------------------------------------------------------------------------|----|
| 1.2  | SynRM rotor cross-section with d-q axes shown                           | 3  |
| 2.1  | SynRM stator (left) and SynRM rotor(right).                             | 5  |
| 2.2  | Equivalent Circuit of SynRM.                                            | 6  |
| 2.3  | Closed loop sensored vector control .                                   | 11 |
| 2.4  | Signal flow graph.                                                      | 12 |
| 2.5  | current angle in d-q frame of reference .                               | 17 |
| 2.6  | Field weakening operation of SynRM .                                    | 20 |
| 2.7  | Phasor diagram for SynRM.                                               | 21 |
| 2.8  | Reference speed vs Measured speed .                                     | 24 |
| 2.9  | Developed torque vs Load torque .                                       | 25 |
| 2.10 | Inverter current waveforms .                                            | 25 |
| 2.11 | Normalized torque vs Normalized speed above rated speed.                | 26 |
| 2.12 | Normalized id vs iq in field weakening region .                         | 26 |
| 3.1  | θ<br>Rotor Reference frame(dq) at<br>w.r.t Stator reference frame(abc). | 30 |
| 3.2  | Unsaturated (left) Saturated(right).                                    | 32 |
| 3.3  | Variation of<br>Ld<br>with<br>β<br>at different<br>Is                   | 32 |
| 3.4  | Ld<br>β<br>Is<br>Variation of<br>with<br>at different                   | 33 |
| 3.5  | β<br>Is<br>Saliency Ratio with<br>at different                          | 33 |
| 3.6  | Ripple in Torque due to rotor position.                                 | 34 |
| 3.7  | Torque variation due to<br>Is<br>and<br>β.                              | 35 |

| 3.8  | Calculated Torque vs FEA Torque when the rotor is unsaturated.  | 35 |
|------|-----------------------------------------------------------------|----|
| 3.9  | Calculated Torque vs FEA Torque when the rotor is saturated.    | 36 |
| 3.10 | β<br>Is<br>Torque(p.u) and Power Factor curves with<br>at rated | 36 |
| 3.11 | Power factor variation with current angle.                      | 37 |
| 3.12 | Torque, Voltage(p.u) and power factor at rated operating point. | 37 |
|      |                                                                 |    |
| 4.1  | Schematic of back to back converter.                            | 39 |
| 4.2  | Assembeled Inverter.                                            | 41 |
| 4.3  | SynRM .                                                         | 41 |
|      |                                                                 |    |
| B.1  | Maxwell-2D model of 22kW SynRM .                                | 45 |
| B.2  | Per Pole model for FEA .                                        | 46 |
| B.3  | Master-slave Boundary .                                         | 46 |
| B.4  | Mesh used for the FEA .                                         | 47 |

### **ABBREVIATIONS**

<span id="page-10-0"></span>**EV** Electric Vehicle

**PMSM** Permanent Magnet Synchronous Machine

**SynRM** Synchronous Reluctance Machine

**d-axis** Direct axis

**q-axis** Quadrature axis

**MTPA** Maximum Torque Per Ampere

**FEA** Finite Element Analysis **PD-card** Protection and Delay Card **MPC** Model Predictive Control

## **NOTATION**

<span id="page-11-0"></span>

| $\xrightarrow{:r}$                                                                                                                          | Chahan arangant nafanna d ta natan         |
|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| $\stackrel{\mathcal{I}'_S}{\Longrightarrow}$                                                                                                | Stator current referred to rotor           |
| $\dot{t}_s^{\acute{s}}$                                                                                                                     | Stator current referred to stator          |
| $\overrightarrow{i_s^r} \atop \overrightarrow{i_s^s} \atop k_p$                                                                             | Proportional gain in PI controller         |
| $k_i$                                                                                                                                       | Integral gain in PI controller             |
| $L_{ls}$                                                                                                                                    | Stator leakage inductance                  |
| $L_{md}$                                                                                                                                    | Direct axis magnetizing inductance         |
| $L_{mq}$                                                                                                                                    | Quadrature axis magnetizing inductance     |
| $L_{sd}$                                                                                                                                    | Total d-axis inductance                    |
| $L_{sq}$                                                                                                                                    | Total q-axis inductance                    |
| $m_d$                                                                                                                                       | Developed torque                           |
| P                                                                                                                                           | No. of poles of the machine                |
| $R_{s}$                                                                                                                                     | Stator resistance                          |
| $\overrightarrow{v}_s^s$                                                                                                                    | Stator voltages referred to rotor          |
| $ \begin{array}{c} \overrightarrow{V}_{s} \\ \overrightarrow{V}_{s} \\ \overrightarrow{\Psi}_{r} \\ \overrightarrow{\Psi}_{m} \end{array} $ | Stator flux vector referred to rotor       |
| $\overline{\Psi_m^r}$                                                                                                                       | Mutual flux vetor in rotor reference frame |
| $\theta$                                                                                                                                    | Rotor angle w.r.t stator axis              |
| $\omega$                                                                                                                                    | rotor speed                                |
| $\tau_b$                                                                                                                                    | Controller bandwidth                       |
| β                                                                                                                                           | Current angle                              |

### **CHAPTER 1**

### **INTRODUCTION**

<span id="page-12-0"></span>2020 was the warmest year recorded by NASA [1]. For past decades, this trend in global warming has pushed every industry to become more power efficient while keeping emissions low. According to a study [2], more than 45% of the electric power consumed globally is by electric motors used in general purpose applications such as fans, pumps or compressors. Almost 90% of those are induction motors which are used due to their simplicity in construction, robustness and low cost. However, induction motors have lower efficiency when compared to other alternatives. Permanent magnet synchronous motors (PMSM) have gained popularity due to their higher efficiency and power density. The automobile industry has seen wide adoption of PMSMs, recently in electric vehicles(EVs). With each passing year share of EVs in the market is increasingly pushing the demand for better machines. But PMSMs use rare earth materials such as neodymium whose supply is predominantly determined by geopolitics. This limited supply of rareearth materials results in higher prices which becomes a major hindrance for the widespread adoption of PMSMs. Synchronous reluctance machines(SynRM) may provide a promising alternative to both induction motors and PMSMs .

SynRMs do not have permanent magnets or windings in the rotor and the stator is similar to that of induction machines. The torque produced is due to reluctance and is caused by the difference in direct axis (d-axis) inductance and quadrature axis (q-axis) inductance. Early SynRMs had poor performance and were neglected for the first half of the 20th century. During the 1960s SynRM was developed for the textile industry as line-start synchronous AC machines [3]. Such motors were fed directly from the mains supply but suffered from low power factor, and it wasn't until the 1990s that research focused on novel control strategies and increased understanding of the motor characteristics [4][12]. Nowadays the focus is on the electromagnetic design of the rotor and its optimization[6]. A welldesigned SynRM with an appropriate control scheme can replace conventional solutions in certain applications.

### <span id="page-13-0"></span>**1.1 SynRM Overview**

<span id="page-13-1"></span>The development of a mathematical model for SynRM started as early as 1923 [5]. The stator of the SynRM has sinusoidally distributed windings just like a traditional induction motor and is fed with a balanced three-phase supply. The rotor has saliency due to flux barriers placed such that the ratio of d-axis inductance to q-axis inductance is maximized giving higher torque. The idea of SynRM is based on reluctance torque. A simple system as shown in Figure [1.1](#page-13-1) shows the concept of reluctance torque.

![](_page_13_Picture_2.jpeg)

Figure 1.1: Reluctance torque.

If the system in Figure [1.1](#page-13-1) is supplied with current then this will result in alignment of iron bar along the magnetic field as shown. This happens because when we apply magnetic field the iron bar will align such that the reluctance is minimized or the inductance is maximised. Figure [1.2](#page-14-2) shows a section of crosssection of a 4-pole SynRM rotor. We can see from the figure that air gaps along the q-axis increase the reluctance compared to d-axis. Here we follow the convention of the d-axis being the path of least reluctance and highest reluctance is observed along the q-axis. This results in higher inductance along the d-axis and lower inductance along the q-axis. The ratio of d-axis to q-axis inductance gives saliency ratio. This ratio is critical to the machine performance and we try to maximize it by the electromagnetic design and optimization of the rotor[6]. As we will see in chapter 2, the torque developed by the SynRM is proportional to the difference between d-axis and q-axis inductances. A good SynRM has a large saliency ratio, which ensures a high power factor, high developed torque and better efficiency.

<span id="page-14-2"></span>![](_page_14_Picture_0.jpeg)

Figure 1.2: SynRM rotor cross-section with d-q axes shown..

## <span id="page-14-0"></span>**1.2 Control Techniques**

During the early 1970's Blaschke proposed vector control for AC motors [7]. [4],[8] discusses the vector control strategy for SynRMs. In vector control, the 3-phase stator currents are represented in a d-q reference frame attached to the rotor, these d-axis and q-axis stator current components are then decoupled in order to have independent control of each component. This transformation from the stator reference frame to rotor reference frame requires prior knowledge of rotor position. The rotor position can be measured by a suitable sensor or we can estimate it based on flux linkage and torque computation giving rise to sensorless control[9]. One can further classify the control techniques[10] as maximum torque per ampere (MTPA), maximum rate of change of torque control (MRCTC), and maximum power factor control (MPFC). MTPA is achieved when d-axis and q-axis current components are equal, and is of interest when one needs to operate the motor at high efficiency below the base speed. MRCTC[11] was developed for high-speed applications like machine tools where the main focus is response to the load torque impulses. In induction machine field weakening is required for the machine to operate beyond base speed. However, it is difficult to define the concept of 'field' in SynRM since torque production does not depend on the interaction of rotor current and magnetic field, but we can define a constant power mode of operation beyond base speed meeting certain criteria like MTPA[10].

### <span id="page-14-1"></span>**1.3 Outline Of the Report**

The goal of this project is to understand the control of SynRM under various operating conditions and use FEA to get better operating points compared to the conventional methods. This report mainly discusses the modelling of SynRMs with vector control as the main focus with a brief discussion on field weakening operation. Later the machine is analysed for the operation under saturated conditions and the influence of variations in machine parameters is studied.

**Chapter-2** gives a detailed description of the mathematical model of SynRM. This chapter is divided into two sections. The first section describes the dynamic equations of the SynRM in rotor d-q reference frame. The second section focuses on control techniques when the motor is operated below and beyond base speed. This section will mainly discuss sensored vector control based on MTPA below base speed operation. Power factor relation is derived which we use in chapter 3 while doing finite element analysis. Later normalization of the machine equations is performed in order to understand the effect of saliency ratio on the machine. This normalized model is then used to study the operation of SynRM beyond base speed. Results obtained from the simulation of a 22kW SynRM are presented. The results were obtained for below base speed operation and beyond base speed operation under constant power. The simulation was done in Simulink and sensored vector control technique is applied to the SynRM.

**Chapter-3** presents a detailed discussion on the Finite Element Analysis (FEA) of the machine under various operating conditions. A brief theory for the inductance calculation method was presented. The results obtained were discussed and based on that look-up table based control was proposed. Also, this chapter briefly discuss the assumptions made in chapter-2 and how they affected the conventional control strategies. Later MTPA was found using FEA. The power factor variations were discussed and its effect on overloading was also explained. This chapter summarizes the things one needs to consider while designing a suitable control for the SynRM.

**Chapter-4** briefly discusses about the hardware setup. A brief description of the components used for the back to back converter is presented.

**Chapter-5** gives a summary of the work done and future scope for improving the work

### **CHAPTER 2**

## <span id="page-16-0"></span>**SynRM MODELLING and CONTROL**

SynRM's stator has distributed windings placed in a uniformly slotted stator core. The rotor has magnetic anisotropy resulting in large difference between d and qaxes inductances. Figure [2.1](#page-16-1) shows the stator and rotor of 4-pole SynRM. From the figure we can observe that stator is similar to that of an induction motor whereas rotor has flux barriers along a particular axis which results in higher reluctance along one axis giving rise to saliency. The SynRM produces torque due to the difference in d-axis inductance(*Ld*) and q-axis inductance(*Lq*). A high saliency ratio (ζ = *Ld*/*Lq*) is required for an acceptable power factor and wider constant power speed range[6][10]. Both the magnetizing current and load torque current component is provided by the stator current and under steady state rotor rotates in synchronism with the stator magnetic field.

<span id="page-16-1"></span>![](_page_16_Picture_3.jpeg)

Figure 2.1: SynRM stator (left) and SynRM rotor(right).

In this chapter first, we will derive machine equations in d-q reference frame based on the equivalent circuit of SynRM in d-q reference frame. Later we will use these equations to understand vector control and formulate a sensored vector control scheme which will be later verified in chapter-3 using simulations. After understanding the behaviour of the machine below base speed, we will develop constraints for operation beyond base speed. Under field weakening, we will derive constraints for the operation of motor in constant power mode beyond base speed.

Convention: In this report a space vector V is represented as  $\overrightarrow{V_x}$ , where subscript(x) denote rotor as r and stator as s. Whereas superscript(y) denotes rotor reference frame as r and stator reference frame as s. For example if  $\overrightarrow{v_s}$  will represent stator voltage refered to rotor reference frame.

### <span id="page-17-0"></span>2.1 Dynamic Equations of SynRM

<span id="page-17-1"></span>Figure 2.2 shows the equivalent circuit of SynRM in d-q reference frame [6].

![](_page_17_Picture_4.jpeg)

Figure 2.2: Equivalent Circuit of SynRM.

From the equivalent circuit we can write stator flux referred to rotor  $(\overrightarrow{\Psi}_s^r)$  as:

$$\overrightarrow{\Psi_s^r} = L_{ls} \overrightarrow{i_s^r} + \overrightarrow{\Psi_m^r} \tag{2.1}$$

where  $L_{ls}$  is stator leakage inductance,  $\overrightarrow{\Psi_m^r}$  is mutual flux vector in rotor reference frame and  $\overrightarrow{i_r^r}$  is stator current refered to rotor.

We can write  $\overrightarrow{\Psi_m'}$  in d-q reference frame as resultant of d-axis mutual flux and q-axis mutual flux:

$$\overrightarrow{\Psi_m^r} = \Psi_{md} + j\Psi_{mq}$$

Similarly, resolving  $\overrightarrow{\Psi}_s^r$  and  $\overrightarrow{i_s}$  in d-q reference frame and substituting in equation 2.1, we get

$$\Psi_{sd} + j\Psi_{sq} = L_{ls}(i_{sd} + ji_{sq}) + L_{md}i_{sd} + jL_{mq}i_{sq}$$

where  $L_{md}$  and  $L_{mq}$  are mutual inductance of d and q axis respectively, and  $i_{sd}$  and  $i_{sq}$  are stator currents along d and q axis.

Equating real and imaginary parts of the above equation gives d-axis and q-axis stator flux:

$$\Psi_{sd} = L_{ls}i_{sd} + L_{md}i_{sd}$$

$$\Psi_{sa} = L_{ls}i_{sa} + L_{ma}i_{sa}$$

If we represent  $L_{sd}$  as total d-axis inductance and  $L_{sq}$  as total q-axis inductance then,

$$\Psi_{sd} = L_{sd}i_{sd}$$

$$\Psi_{sq} = L_{sq}i_{sq}$$

Thus we arrive at equation 2.2 for stator flux referred to rotor in terms of inductances and currents as:

$$\overrightarrow{\Psi}_{s}^{r} = \Psi_{sd} + j\Psi_{sq}$$

$$\overrightarrow{\Psi}_{s}^{r} = L_{sd}i_{sd} + jL_{sa}i_{sa} \tag{2.2}$$

### <span id="page-18-0"></span>2.1.1 Stator Voltage Equations

From figure 2.2, stator voltage in stator reference frame  $(\overrightarrow{v_s})$  is

$$\overrightarrow{v_s^s} = R_s \overrightarrow{i_s^s} + \frac{d}{dt} \overrightarrow{\Psi_s^s}$$

where  $R_s$  is stator resistance,  $\overrightarrow{i_s}$  is stator current referred to stator and  $\overrightarrow{\Psi_s}$  is stator flux linkage in stator reference frame.

Let  $\theta$  be the rotor angle measured from stator axis then we can write a relation between stator voltage in stator reference frame and stator voltage in rotor reference frame as

$$\overrightarrow{v}_{s}^{s} = \overrightarrow{v}_{s}^{r} e^{j\theta}$$

here multiplying by  $e^{j\theta}$  performs rotation of quantities, thus converting from stator frame of reference to rotor's reference frame.

Therefore we can write,

$$\overrightarrow{v_s^r}e^{j\theta} = R_s \overrightarrow{i_s^r}e^{j\theta} + \frac{d}{dt}(\overrightarrow{\Psi_s^r}e^{j\theta})$$

$$\overrightarrow{v_s^r}e^{j\theta} = R_s \overrightarrow{i_s^r}e^{j\theta} + e^{j\theta} \frac{d}{dt} \overrightarrow{\Psi_s^r} + j \overrightarrow{\Psi_s^r}e^{j\theta} \frac{d}{dt} \theta$$

on simplifying we get stator voltage refered to rotor as:

$$\overrightarrow{v_s^r} = R_s \overrightarrow{i_s^r} + \frac{d}{dt} \overrightarrow{\Psi_s^r} + j \overrightarrow{\Psi_s^r} \frac{d}{dt} \theta$$

expressing  $\overrightarrow{v_s}$  and  $\overrightarrow{v_s}$  in their respective d-q axis components gives

$$v_{sd} + jv_{sq} = R_s(i_{sd} + ji_{sq}) + \frac{d}{dt}(L_{sd}i_{sd} + jL_{sq}i_{sq}) + j(L_{sd}i_{sd} + jL_{sq}i_{sq})\frac{d}{dt}\theta$$

On equating real and imaginary parts of the above equation, we will get equations 2.3 and 2.4 which represents stator voltage equations.

$$v_{sd} = R_s i_{sd} + \frac{d}{dt} (L_{sd} i_{sd}) - L_{sq} i_{sq} \frac{d}{dt} \theta$$
 (2.3)

$$v_{sq} = R_s i_{sq} + \frac{d}{dt} (L_{sq} i_{sq}) + j L_{sd} i_{sd} \frac{d}{dt} \theta$$
 (2.4)

We can define electrical rotor speed ( $\omega$ ) as:

$$\omega = \frac{d}{dt}\theta$$

substituting this in equations 2.3 and 2.4, we can write stator voltages of SynRM in d-q frame of reference as shown in equations 2.5 and 2.6.

$$v_{sd} = R_s i_{sd} + \frac{d}{dt} (L_{sd} i_{sd}) - L_{sq} i_{sq} \omega$$
 (2.5)

$$v_{sq} = R_s i_{sq} + \frac{d}{dt} (L_{sq} i_{sq}) + j L_{sd} i_{sd} \omega$$
 (2.6)

#### <span id="page-20-0"></span>2.1.2 Developed Torque Equation

We can derive equation for torque developed in SynRM as:

$$m_d = \frac{2}{3} \cdot \frac{P}{2} (\overrightarrow{\Psi}_s^r \times \overrightarrow{i_s^r}) \tag{2.7}$$

where *P* is total number of poles in the machine and

$$\therefore \overrightarrow{\Psi}_{s}^{r} = L_{sd}i_{sd} + jL_{sq}i_{sq} \& \overrightarrow{i_{s}^{r}} = i_{sd} + ji_{sq}$$

Evaluating cross product in equation 2.7 gives developed torque as;

$$m_d = \frac{2}{3} \cdot \frac{P}{2} \cdot \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ L_{sd}i_{sd} & L_{sq}i_{sq} & 0 \\ i_{sd} & i_{sq} & 0 \end{vmatrix}$$

$$\implies m_d = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_{sd}i_{sd}i_{sq} - L_{sq}i_{sq}i_{sd})$$

Equation 2.8 gives us the final expression for torque produced by the SynRM. As mentioned earlier we can see that torque is proportional to the difference in d and q-axis inductances, as well as it is proportional to the current components. This relation will later be used as the basis for the MTPA control.

$$m_d = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_{sd} - L_{sq}) i_{sq} i_{sd}$$
 (2.8)

We can also define a parameter *k<sup>t</sup>* as given in equation 2.9, this form of representation is useful when we find proportional and integral coefficients for the closed loop control.

$$k_t = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_{sd} - L_{sq}) \tag{2.9}$$

We can express torque in terms of *k<sup>t</sup>* as shown in equation 2.10.

$$m_d = k_t i_{sq} i_{sd} (2.10)$$

## <span id="page-21-0"></span>**2.2 SynRM Control Below and Beyond Base Speed**

Before we study vector control, a basic understanding of MTPA [10] is necessary. Since our study is focoused aroundMTPA and the same is utilised for normalisation of machine equations, which will then be used in the study of field weakening. One can note that we can also develop control strategy based on MRCTC [11] which will only result in the change of current reference calcuation in the control scheme.

### <span id="page-21-1"></span>**2.2.1 Maximum Torque Per Ampere (MTPA)**

To minimise copper loss for a given operating power, we need to use maximum torque per ampere(MTPA) control.

If the magnitude of stator current of the machine is *I<sup>s</sup>* , we can write it as

$$I_s = \sqrt{i_{sd}^2 + i_{sq}^2}$$

then we can write torque developed using equation 2.10 as:

$$m_d = k_t i_{sq} \sqrt{I_s^2 - i_{sq}^2}$$

To maximise torque per ampere, we find derivative of *m<sup>d</sup>* w.r.t *isq* and equate it to 0,

$$\frac{d}{di_{sq}}m_d = 0$$

$$\implies k_t \left[ \frac{-i_{sq}^2}{\sqrt{I_s^2 - i_{sq}^2}} + \sqrt{I_s^2 - i_{sq}^2} \right] = 0$$

Equation 2.11 gives us the d and q-axis currents when the machine operates in MTPA.

$$i_{sq} = i_{sd} = \frac{I_s}{\sqrt{2}}$$
 (2.11)

### <span id="page-22-0"></span>**2.2.2 Sensored Vector Control Scheme**

The control scheme discussed here assumes that rotor speed or position is known. This can be achieved with the help of an encoder or a resolver or any other sensor which gives positional information of the rotor. The control system has an inner current control loop and outer speed control loop as shown in figure [2.3.](#page-22-1)

<span id="page-22-1"></span>![](_page_22_Figure_5.jpeg)

Figure 2.3: Closed loop sensored vector control .

In the speed loop, reference speed is compared with the measured speed of the rotor and the error signal generated is given to the PI controller. The output of the PI controller is Torque(*m*<sup>∗</sup> *d* ) reference. This *m*<sup>∗</sup> *d* is used to calculate reference currents given to d-axis and q-axis current controllers.

In both the d-axis and q-axis current loop, τ is used to compute the reference currents (*i* ∗ *sd* and *i* ∗ *sq*). Since we are operating under MTPA, *i* ∗ *sd* is found using square root operation on  $m_d^*$ . If we reference torque is positive then we take  $i_{sd}^* = i_{sq}^*$ , otherwise we take  $i_{sd}^* = -i_{sq}^*$ . These references are compared with measured  $i_{sd}$  and  $i_{sq}$  and error signals are given to respective PI controllers. The ouptut of these PI controllers give reference voltages  $v_{sd}^*$  and  $v_{sq}^*$ . These voltages are converted to abc reference frame(using Park's transformation) and given as reference to the inverter. It is to be noted that limits to PI controller ouptuts must be applied, which are decided based on the rating of the SynRM.

Figure 2.4 shows signal flow graph of the system. From this graph we get feed forward terms as:

 $effd: -L_{sa}i_{sa}\omega$ 

<span id="page-23-1"></span> $effq: L_{sd}i_{sd}\omega$ 

![](_page_23_Figure_4.jpeg)

Figure 2.4: Signal flow graph.

For text to be more legible, as far as control portion in this report is concerned, we will omit s from the subscript of stator parameters. i.e.  $i_{sd}$ ,  $i_{sq}$ ,  $v_{sd}$ ,  $v_{sq}$ ,  $L_{sd}$ , and  $L_{sq}$  will be written as  $i_d$ ,  $i_q$ ,  $v_d$ ,  $v_q$ ,  $L_d$ , and  $L_q$ .

#### <span id="page-23-0"></span>2.2.3 Control Parameters

For the control shown in figure 2.3 we can calculate controller paremeters as shown in the following sub-sections. For a practical drive application where there is significant inertia it is assumed that the current loop response is much higher than that of speed loop response. Typically desired current loop bandwidth is in 10s of milliseconds and speed loop bandwidth is nearly 10-100 times or higher.

#### <span id="page-24-0"></span>**2.2.3.1 Current Loop**

We have d-axis plant model as:

$$\frac{I_d}{V_d} = \frac{1}{R_s + sL_d}$$

If we use PI controller,

$$\frac{k_{ic}}{s} + k_{pc}$$

where integral and proportional gain for current loop is *kic*,*kpc* respectively. If bandwidth of the PI controller is τ*pc* then ;

$$\frac{k_{ic}}{s} + k_{pc} = \frac{k_{pc}}{s\tau_{pc}} + k_{pc} = \frac{k_{pc}(1 + s\tau_{pc})}{s\tau_{pc}}$$

where;

$$k_{ic} = \frac{k_{pc}}{\tau_{pc}}$$

Then for 1*st* order response of the current control with desired bandwidth of τ ∗ *bc*, we get:

$$\frac{1}{R_s(1+s\frac{L_d}{R_s})} \cdot \frac{k_{pc}(1+s\tau_{pc})}{s\tau_{pc}} = \frac{1}{s\tau_{bc}^*}$$

If we take,

$$\tau_{pc} = \frac{L_d}{R_s} \tag{2.12}$$

we get our gains as:

$$k_{pc} = \frac{L_d}{\tau_{bc}^*} \tag{2.13}$$

$$k_{ic} = \frac{k_{pc}}{\tau_{pc}} \tag{2.14}$$

q-axis control parameters are found in a similar fashion.

#### <span id="page-25-0"></span>**2.2.3.2 Speed Loop**

For the machine with load torque *m<sup>l</sup>* , inertia *J* and frictional coefficient *B*, we can write

$$m_d = m_l + J \frac{d\omega}{dt} + B\omega$$

If we know frictional coefficient of our plant then our model will be as shown in figure.

Without loss of generality, we can consider inner loop(current loop) gain as unity because current loop response is much faster than required speed loop response. If τ ∗ *b*ω is desired speed response then:

$$\frac{k_{p\omega}(1+s\tau_{p\omega})}{s\tau_{p\omega}} \cdot \frac{k_t}{B(1+s\frac{J}{B})} = \frac{1}{s\tau_{b\omega}^*}$$
 (2.15)

If we take

$$\tau_{p\omega} = \frac{J}{B} \tag{2.16}$$

we get our gains as:

$$k_{p\omega} = \frac{J}{k_t \tau_{b\omega}^*} \tag{2.17}$$

$$k_{i\omega} = \frac{k_{p\omega}}{\tau_{p\omega}} \tag{2.18}$$

#### **Symmetrical Pole Placement:**

In most of the practical scenarios we can not determine *B*, thus we treat *B*ω, term in torque equation above as unknown disturbance. We can write our modified open loop gain for speed control as:

$$\frac{k_{p\omega}(1+s\tau_{p\omega})}{s\tau_{p\omega}}\cdot\frac{1}{(1+s\tau_{bi})}\cdot\frac{k_t}{sJ}$$

We get controller bandwidth as geometric mean of current controller and desired bandwidth, i.e τ*p*<sup>ω</sup> = p τ*bi*τ ∗ *b*ω , normally we choose τ ∗ *b*ω = 10 · τ ∗ *bi* & τ*p*<sup>ω</sup> = 10 · τ ∗ *bw*,then we get.

$$k_{p\omega} = \frac{J}{k_t \tau_{b\omega}^*}$$

### <span id="page-26-0"></span>**2.2.4 Field Weakening Operation**

We have SynRM equations as:

$$\begin{bmatrix} v_d \\ v_q \end{bmatrix} = \begin{bmatrix} R_s + L_d \frac{d}{dt} & -\omega L_q \\ \omega L_d & R_s + L_q \frac{d}{dt} \end{bmatrix} \begin{bmatrix} i_d \\ i_q \end{bmatrix}$$
(2.19)

$$\tau = k_t i_{sq} i_{sd} \tag{2.20}$$

Where *vd*, *id*, *L<sup>d</sup>* and *vq*, *iq*, *L<sup>q</sup>* are stator voltages, currents and inductances in d and q axis respectively. ω is rotor speed and τ is generated torque.

#### <span id="page-26-1"></span>**2.2.4.1 Normalization of Machine Equations**

In order to get machine-independent performance information from the above equations we normalize them[10]. This leads the analysis to be dependent only on saliency ratio ζ.

Normalization is based on the rated values when machine is operated under MTPA control.

If ω◦ is rated speed and *i*◦ is rated current then;

$$i_{d\circ} = i_{q\circ} = \frac{i_{\circ}}{\sqrt{2}}$$

Also other bases for the normalization can be calculated as are:

$$\tau_{\circ} = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_{sd} - L_{sq}) \frac{i_{\circ}^{2}}{2}$$
 (2.21)

$$\Psi_{\circ} = \sqrt{\Psi_d^2 + \Psi_q^2} = \frac{i_{\circ}}{\sqrt{2}} \sqrt{L_d^2 + L_q^2}$$
 (2.22)

since *v*◦ = q *v* 2 *d*◦ + *v* 2 *q*◦ ; and neglecting stator resistance and under steady state we can write

$$v_{\circ} = \sqrt{(\omega_{\circ} \Psi_{q})^{2} + (\omega_{\circ} \Psi_{d})^{2}} = \omega_{\circ} \Psi_{\circ}$$

Therefore normalised machine variables can be written as

$$\Psi_n = \frac{\Psi}{\Psi_\circ}$$
;  $\tau_n = \frac{\tau}{\tau_\circ}$ ;  $v_n = \frac{v}{v_\circ}$ ;  $i_n = \frac{i}{i_\circ}$ ;  $\omega_n = \frac{\omega}{\omega_\circ}$ 

Applying above normalizations to machine voltage equations we get:

$$v_{dn}v_{\circ} = R_s i_{dn}i_{\circ} + \frac{d}{dt}(L_d i_{dn}i_{\circ}) - L_q i_{qn}i_{\circ}\omega_n\omega_{\circ}$$

neglecting stator resistance *R<sup>s</sup>* and expressing *v*◦ in terms of ω◦ and Ψ◦ we get;

$$v_{dn} = \frac{1}{\omega_{\circ} \Psi_{\circ}} \left( L_{d} i_{\circ} \frac{d}{dt} i_{dn} - L_{q} i_{qn} i_{\circ} \omega_{n} \omega_{\circ} \right)$$

$$v_{dn} = \frac{1}{\omega_{\circ} \frac{i_{\circ}}{\sqrt{2}} \sqrt{L_d^2 + L_q^2}} \left( L_d i_{\circ} \frac{d}{dt} i_{dn} - L_q i_{qn} i_{\circ} \omega_n \omega_{\circ} \right)$$

$$v_{dn} = \frac{\sqrt{2}}{\sqrt{\left(\frac{L_q}{L_d}\right)^2 + 1}} \left(\frac{1}{\omega_o} \frac{d}{dt} i_{dn} - \frac{L_q}{L_d} i_{qn} \omega_n\right)$$

substituting saliency ratio equation 2.23 in above equation gives us equation 2.24 which represents normalized d-axis stator voltage.

$$\zeta = \frac{L_d}{L_q} \tag{2.23}$$

$$v_{dn} = \frac{\sqrt{2}\zeta}{\sqrt{\zeta^2 + 1}} \left( \frac{1}{\omega_{\circ}} \frac{d}{dt} i_{dn} - \frac{\omega_n}{\zeta} i_{qn} \right)$$
 (2.24)

Similarly if follow the procedure for *vqn* we will arrive at equation 2.25 repre-

senting normalized q-axis stator voltage.

$$v_{qn} = \frac{\sqrt{2}\zeta}{\sqrt{\zeta^2 + 1}} \left( \frac{1}{\zeta\omega_o} \frac{d}{dt} i_{qn} + \omega_n i_{dn} \right)$$
 (2.25)

And we can derive normalized torque (equation 2.26) as follows:

$$\tau_n \tau_\circ = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_d - L_q) i_{dn} i_o i_{qn} i_o$$

$$\implies \tau_n \frac{2}{3} \cdot \frac{P}{2} \cdot (L_{sd} - L_{sq}) \frac{i_o^2}{2} = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_d - L_q) i_{dn} i_o i_{qn} i_o$$

$$\tau_n = 2i_{dn}i_{qn} = i_n \cos \beta \times i_n \sin \beta$$

$$\implies \tau_n = i_n^2 \sin 2\beta \tag{2.26}$$

<span id="page-28-0"></span>where β is current angle which is defined as shown in figur[e2.5.](#page-28-0)

![](_page_28_Figure_8.jpeg)

Figure 2.5: current angle in d-q frame of reference

Now we will use the normalized equations to find a relation between torque, voltage, speed and current angle:

Since normalized current is expressed as:

$$i_n = \sqrt{\frac{\tau_n}{\sin 2\beta}}; i_{dn} = \sqrt{\frac{\tau_n \cot \beta}{2}}; i_{qn} = \sqrt{\frac{\tau_n \tan \beta}{2}}$$

Thus using equations 2.24, 2.25 and 2.26 we can write:

$$v_{dn} = \frac{\sqrt{2}\zeta}{\sqrt{\zeta^2 + 1}} \left( \frac{1}{\omega_{\circ}} \frac{d}{dt} \sqrt{\frac{\tau_n \cot \beta}{2}} - \frac{\omega_n}{\zeta} \sqrt{\frac{\tau_n \tan \beta}{2}} \right)$$

$$v_{qn} = \frac{\sqrt{2}\zeta}{\sqrt{\zeta^2 + 1}} \left( \frac{1}{\zeta\omega_{\circ}} \frac{d}{dt} \sqrt{\frac{\tau_n \tan \beta}{2}} + \omega_n \sqrt{\frac{\tau_n \cot \beta}{2}} \right)$$

Since we know,

$$v_n^2 = v_{dn}^2 + v_{gn}^2$$

we can write;

$$v_n^2 = \frac{\zeta^2}{\zeta^2 + 1} \left( \frac{1}{\omega_o} \frac{d}{dt} \sqrt{\tau_n \cot \beta} - \frac{\omega_n}{\zeta} \sqrt{\tau_n \tan \beta} \right)^2 + \frac{\zeta^2}{\zeta^2 + 1} \left( \frac{1}{\zeta \omega_o} \frac{d}{dt} \sqrt{\tau_n \tan \beta} + \omega_n \sqrt{\tau_n \cot \beta} \right)^2$$

For constant angle operation  $\frac{d\beta}{dt} = 0$  and under steady state  $\frac{d\tau}{dt} = 0$ , above expression reduces to equation 2.27.

$$v_n^2 = \frac{\zeta^2}{\zeta^2 + 1} \left( \frac{\omega_n^2}{\zeta^2} \tau_n \tan \beta + \omega_n^2 \tau_n \cot \beta \right)$$

$$v_n^2 = \frac{\tau_n \omega_n^2}{\zeta^2 + 1} \left( \tan \beta + \zeta^2 \cot \beta \right)$$
(2.27)

Rewriting equation 2.27 as equation 2.28 gives us a relationship between torque, speed, voltage and current.

$$\tau_n = \frac{1}{\omega_n^2} \left( \frac{v_n^2 \left( \zeta^2 + 1 \right)}{\tan \beta + \zeta^2 \cot \beta} \right) \tag{2.28}$$

#### <span id="page-29-0"></span>2.2.4.2 Operation Beyond Rated Speed

When we want to operate machine beyond rated speed i.e. the machine run out of volts, i.e. when  $v_n = 1$ , then

$$\tau_n \propto \frac{1}{\omega_n^2} \tag{2.29}$$

To get constant power operation beyond base speed,

we getτ*<sup>n</sup>* · ω*<sup>n</sup>* = *k*, where *k* is some constant.

for this to hold when we operate beyond base speed when rated voltage is reached, we get,

$$k\omega_n = \left(\frac{(\zeta^2 + 1)}{\tan \beta + \zeta^2 \cot \beta}\right)$$

since we were operating under MTPA till rated operation i.e τ*<sup>n</sup>* = 1 and ω*<sup>n</sup>* = 1, we get

$$k = \tau_n \cdot \omega_n = 1$$

therefore we get the relation:

$$\tan \beta + \zeta^2 \cot \beta - \frac{\zeta^2 + 1}{\omega_n} = 0$$

For a given speed beyond rated value, under constant power operation, the solution of above equation (if exists) will give the *i<sup>d</sup>* and *iq*values in field weakening region.

i.e.

$$\tan^2 \beta - \frac{\zeta^2 + 1}{\omega_n} \tan \beta + \zeta^2 = 0$$

or

$$\tan \beta = \frac{\frac{\zeta^2 + 1}{\omega_n} \pm \sqrt{\left(\frac{\zeta^2 + 1}{\omega_n}\right)^2 - 4\zeta^2}}{2}$$
 (2.30)

For a real solution to exist we get;

$$\left(\frac{\zeta^2 + 1}{\omega_n}\right)^2 - 4\zeta^2 > 0$$

or

$$\omega_n < \frac{\zeta^2 + 1}{2\zeta} \tag{2.31}$$

therefore, <sup>ζ</sup> <sup>2</sup>+1 2ζ sets the limit on ω*n*if we want to operate our machine at constant power in field weakening region. For the machine in Appendix 1 we get this ω*<sup>n</sup>* = 2.1511.

Using equation 2.28 we can define 3 modes of operation for SynRM[14]. We can draw voltage, current and torque loci using the equations derived earlier and then use equation 2.28 to find operating points. Figure [2.6](#page-31-0) shows field weakening operation of SynRM.

<span id="page-31-0"></span>![](_page_31_Figure_2.jpeg)

Figure 2.6: Field weakening operation of SynRM .

**Mode-1:** Maximum torque region: This is the region of low speeds where machine operates at maximum torque while current is at its limit. In the figure point A represents that operatig point. For point A, θ*<sup>i</sup>* = 45*<sup>o</sup>*and is discussed under MTPA section.

**Mode-2:** Current limited region: From point A to B the speed increases however the size of constant voltage ellipse decreases.

**Mode-3:** Voltage limited region: If the voltage is kept constant then in order to increase speed we must reduce the current that is we move towards point C. This mode with constant power operation sets the limit at speed given by equation 2.31

### <span id="page-32-0"></span>**2.2.5 Power Factor**

The equations derivied in previous sections is suitable to define MTPA operating points. In practical scenarios our machine terminal voltage is limited by DC-link voltage of the inverter. Therefore to avoid oversizing of the inverter or to define the maximum power factor operating point, we must establish a relation between power factor and machine parameteres. Under steady state, Figure [2.7](#page-32-1) shows the phasor relation between voltage, current and flux linkage while neglecting the effect of stator resistance.

<span id="page-32-1"></span>![](_page_32_Figure_2.jpeg)

Figure 2.7: Phasor diagram for SynRM.

From the figure the power factor is given as cos φ and is derived as shown below:

$$\phi = 90 - \beta + \tan^{-1}(\frac{v_d}{v_q})$$
 (2.32)

or

$$\phi = \tan^{-1}(\frac{i_d}{i_q}) + \tan^{-1}(\frac{\psi_q}{\psi_d})$$

therefore we have power factor as:

$$PowerFactor = \cos(\tan^{-1}(\frac{i_d}{i_q}) + \tan^{-1}(\frac{\psi_q}{\psi_d}))$$
 (2.33)

we can further solve equation 2.32 to get power factor in terms of saliency ratio and current angle as follows.

$$\phi = \tan^{-1}(\frac{\frac{i_d}{i_q} + \frac{L_q i_q}{L_d i_d}}{1 - \frac{i_d}{i_q} \frac{L_q i_q}{L_d i_d}})$$

on simplifying we get

$$\tan \phi = \frac{\zeta + \tan^2 \beta}{(\zeta - 1) \tan \beta}$$

therefore we get power factor as:

$$\cos \phi = \frac{\zeta - 1}{\sqrt{\frac{\zeta^2}{\tan^2 \beta} + \tan^2 \beta + \zeta^2 + 1}}$$
 (2.34)

From equation 2.34 it is clear that power factor only depends on saliency ratio ζ and current angle β. If we consider saliency ratio as constant then we can find maximum power factor by minimizing the denominator of equation 2.34 with respect to β.

Therefore we want to minimize ζ 2 cot<sup>2</sup> β+tan<sup>2</sup> β. On differentiating and equating to zero we get minima at

$$\tan \beta = \sqrt{\zeta} \tag{2.35}$$

Equation 2.35 can be used to find the operating point to get maximum power factor given that the saliency ratio remains constant.

On substituting equation 2.35 in 2.34 we get maximum power factor as

$$pf_{max} = \frac{\zeta - 1}{\zeta + 1}$$

## <span id="page-34-0"></span>**2.3 Simulation Results and Inferences**

In this section we will discuss about the simulation results for the control strategy discussed in the previous sections. Parameters of the machine selected for this study is given in Apendix 1. The simulation for the machine is performed on MATLAB/Simulink. The simulation study is performed using a machine model in Simulink, where we have used SPWM inverter (switching frequency of 10 kHz) to excite the machine. We choose current loop bandwidth as 10ms and speed loop badwidth as 1s. Since speed loop bandwidth is much higher than the current loop bandwidth, the proportional and integral coefficients calculated using symmetrical pole placement are similar to the values found using the equations derived earlier.

The control parameters were calculated based on the previous chapter.

```
• Speed Loop: using equations 2.16 to 2.18
     – Bandwidth = 1s; kp = 10.33; ki = 0.206
```

- Current Loop: using equations 2.12 to 2.14
  - **–** d-axis: bandwidth = 10 ms; *k<sup>p</sup>* = 4.818; *k<sup>i</sup>* = 20
  - **–** q-axis: bandwidth = 10 ms; *k<sup>p</sup>* = 1.188; *k<sup>i</sup>* = 20

The machine is operated under following conditions:

- 1. Reference speed of 400 RPM is given at 0.5 seconds.
- 2. Load torque is changed to 10 Nm at 1.5 seconds

### <span id="page-35-0"></span>**2.3.1 Below Base Speed Operation**

Figure [2.8](#page-35-1) shows reference speed vs measured speed. The response observed is that of first order and the choice of bandwidth for speed loop is justified as evident from the graph.

<span id="page-35-1"></span>![](_page_35_Figure_2.jpeg)

Figure 2.8: Reference speed vs Measured speed .

Figure [2.9.](#page-36-1) shows developed torque vs load torque. At 0.5 seconds when the speed reference changes from 0 to 400 rpm the torque produced is maximum and is nearly equal to the rated value. This value of torque is maintained until the speed of the rotor equals the reference speed. On closer inspection one can observe that the developed torque is slightly more than load torque. This behaviour is expected because of the presence of losses (∵ *B* , 0). At t = 1.5s, load torque is changed to 10Nm which causes a slight dip in speed and developed torque tracks load torque while compensating for losses.

<span id="page-36-1"></span>![](_page_36_Figure_0.jpeg)

Figure 2.9: Developed torque vs Load torque .

Figure [2.10.](#page-36-2) shows 3-phase inverter current waveforms. The current waveform is shown for the part when load changes to 10Nm at 1.5s. We can observe that current rises and touches a peak of 15A before settling down.

<span id="page-36-2"></span>![](_page_36_Figure_3.jpeg)

Figure 2.10: Inverter current waveforms .

### <span id="page-36-0"></span>**2.3.2 Beyond Base Speed Operation**

Using equation 2.31, if we want to operate our machine at constant power in beyond base speed we get ω*<sup>n</sup>* = 2.1511 as speed limit. For our 22kW SynRM machine this translates to 3226.6 rpm.

Figure [2.11.](#page-37-0) shows the variation of normalized torque with normalized speed above rated speed for the machine given in Appendix 1. As expected the torque <span id="page-37-0"></span>reduces as speed increases. This happens as an inverse relation till we reach ω*n*= 2.1511, beyond this constant power operation is not possible. However speeed further increases while torque reduces till the generated torque is equal to the losses.

![](_page_37_Figure_1.jpeg)

Figure 2.11: Normalized torque vs Normalized speed above rated speed.

<span id="page-37-1"></span>Figure [2.12](#page-37-1) shows the scatter plot of normalized id vs iq in the field weakening region for the machine given in Appendix 1. From the figure it is clear that *i<sup>d</sup>* decreases and *i<sup>q</sup>* increases resulting in field weakening as speed is increased.

![](_page_37_Figure_4.jpeg)

Figure 2.12: Normalized id vs iq in field weakening region .

### <span id="page-38-0"></span>**2.3.3 Inferences**

The results from the simulation of sensored vector control for the 22kW SynRM were presented in this chapter. The results were found to be in agreement with the theory discussed in chapter-2. The results for the field weakening region are in accordance with the voltage limited region operation of the SynRM presented in the previous chapter.

## <span id="page-38-1"></span>**2.4 Conclusion**

In this chapter we derived equations 2.5, 2.6 and 2.8 which models the SynRM voltage and torque in d-q reference frame. This formulation was then used to arrive at sensored vector control where using signal flow graph we decopuled the d and q-axis machine equations. This in conjunction with MTPA facilitated allowed us to compute PI compensators gain and bandwidth. In order to express machine performance independant of ratings, we formulated normalised machine equations. These normalized equations helped us to establish fundamentals of field weakening operation in SynRMs. The model developed here is used for the simulation of a 22kW SynRM whose parameters are given in Appendix 1.

### **CHAPTER 3**

# <span id="page-39-0"></span>**SATURATION EFFECT & FINITE ELEMENT ANALYSIS**

We derived our operating points based on the equations developed in chapter 2. However, we derived our conclusions based on the assumption that d and q-axis inductances remain constant for a given machine. This is true if we look at our machine at a particular instant in time. We can also say that these inductances remain constant when the current excitation is low such that rotor saturation is not present. For PMSM this assumption does not significantly affect the operating points. But due to highly anisotropic nature of SynRM rotor, the magnetic saturation onsets at far lower values than the rated current.

This chapter tries to explain the effect of saturation, such that can we relate it to the equations derived in chapter 2. Ansys MAXWELL is used to perform the Finite Element Analysis(FEA) to understand the machine behaviour under saturation. Also, there is a brief discussion on the simulation in the Ansys environment and how it was utilised to get d and q axis inductances which vary with stator current and current angle. Appendix 2 discusses briefly the procedure followed to perform the FEA.

## <span id="page-39-1"></span>**3.1 E**ff**ect of Saturation**

We know that the torque produced by SynRM depends on d and q-axis inductances as well as currents, as seen in the equation 2.8. Later in chapter 2, we derived the operating points of the machine on the assumption that *L<sup>d</sup>* and *L<sup>q</sup>* remain constant. This assumption is true only if the material's permeability remains unchanged throughout the operating region. Since inductance solely depends on the geometry and material's property, a non linear B-H curve will result in variable *L<sup>d</sup>* and *Lq*. Therefore, at different values of *I<sup>s</sup>* and β these inductances may change depending on the material's property. Also due to rotor geometry, we can not physically separate the d and q-axis flux. This causes some of the flux flowing through the d-axis to leak to the q-axis and vice versa. This effect causes a change in the inductance values and is known as the cross-coupling effect in literature [16][17].

While considering all these effect we can re-write equation 2.8 as:

$$m_d = \frac{2p}{3} \frac{p}{2} [L_d(I_s, \beta) - L_q(I_s, \beta)] \frac{I_s^2 \sin 2\beta}{2}$$
 (3.1)

where  $L_d(I_s, \beta)$  and  $L_q(I_s, \beta)$  are the d and q-axes inductance as functions of  $I_s$  and  $\beta$ .

In order to validate above equation, we first need to formalize a way in which we compute our  $L_d$  and  $L_q$ .

#### <span id="page-40-0"></span>**3.1.1** Estimation of $L_d$ and $L_q$

We define  $L_d$  and  $L_q$  as the flux linkages per unit current along d and q-axis respectively.

i.e 
$$L_d = \psi_d/i_d$$
 and  $L_a = \psi_a/i_a$ 

There are numerous ways in literature where  $L_d$  and  $L_q$  are estimated [16][18].

In first method the d-axis of the rotor is aligned with a-phase winding's magnetic axis, and then current excitation is given. The resulting flux linkage of a-phase winding is  $\psi_d$  and the a-phase current is  $i_d$ . Similarly  $L_q$  is found by aligning q-axis with a-phase axis. This method gives the inductances values at a particular value of  $I_s$ . In this method the effect of  $\beta$  is not considered and only inductances are given for saturated and unsaturated condition.

Another way is, for a given  $I_s$ , the rotor is kept at a contant position ( $\theta$ ). The 3-phase currents are found using transformation from rotor aligned d-q frame to stator aligned abc frame of reference as shown in figure 3.1 and using the transformation given in equation 3.2.

$$\begin{bmatrix} d \\ q \end{bmatrix} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix}$$
(3.2)

<span id="page-41-1"></span>![](_page_41_Picture_0.jpeg)

Figure 3.1: Rotor Reference frame(dq) at  $\theta$  w.r.t Stator reference frame(abc).

Since Ansys MAXWELL gives flux linkages in the stator reference frame we will use equation 3.2 to find  $\psi_d$  and  $\psi_q$  and then find  $L_d$  and  $L_q$  at every value of  $\beta$  for a given  $I_s$ 

#### <span id="page-41-0"></span>3.1.2 Power Factor

Power factor of the machine can be estimated in several ways. The machine parameter dependent method is described by the equation 2.34, however this method may not give correct results since saliency ratio will change with saturation which depends on both  $I_s$  and  $\beta$ . The other method uses power balance equation given as:

$$m_d\omega = \frac{2}{3}Re\{\overrightarrow{V_s}\overrightarrow{I_s^*}\}$$

This equation can be used however it requires knowledge of speed and supply voltage. Since in ansys we give currents as inputs using it might lead to some errors due to assumptions made while simplifying above equation. The most important one being the effect of cross-coupling.

Therefore, direct use of the equation 2.33 will give us the power factor. This is suitable since from ansys we can get  $\psi_d$  and  $\psi_q$  directly by trasformation from abc to dq frame as discussed in the previous section. This makes sure that we don't need to worry about the cross-coupling in d and q-axis inductances. Thus, we used the following equation to evaluate the power factor:

$$PowerFactor = \cos(\tan^{-1}(\frac{i_d}{i_q}) + \tan^{-1}(\frac{\psi_q}{\psi_d}))$$

#### <span id="page-42-0"></span>**3.1.3 Torque**

Ansys gives us directly the torque developed by the motor. In order to analytically estimate the developed torque we need to accurately determine the *L<sup>d</sup>* and *Lq*. If we use the method discussed in section 4.2.1, we will get inductance values. However, FEA torque value and the value of torque we get if equation 3.1 is used might differ. This difference is there because we didn't consider the cross-coupling effect in *L<sup>d</sup>* and *Lq*. However, if we are able to get the shape of the torque curve similar to the FEA torque curves, that would mean that we can define operating points. As we see from the results this is the case and thus for defining MTPA we can use the torque curves generated by the FEA and our estimation of power factor curves would also be similar to what we get if cross-coupling is considered.

If we see the torque generated at various rotor positions for the same *I<sup>s</sup>* and β, we should observe a torque ripple. This ripple is mainly due to winding distribution and slots. Since the slots are periodic from the rotor frame of reference, we should see a sinusoidal ripple in the torque.

## <span id="page-42-1"></span>**3.2 FEA Simulation and Results**

In FEA the region is divided into elements and then fields are numerically computed using maxwell's equations. For this study, the ANSYS Maxwell-2D software package is used to perform FEA. In Ansys one can use voltages or currents for the excitation of the windings. In our case, we used currents and performed our simulation in the magnetostatic domain. From the FEA we were able to get the torque generated and the flux linkages for the windings for a given *I<sup>s</sup>* and β. The flux linkages are obtained in abc reference frame which are then converted to dq reference frame with the help of transformation equation 3.2. In the same way using inverse transformation *i<sup>a</sup>* , *i<sup>b</sup>* and *i<sup>c</sup>* are calculated from the given values of *I<sup>s</sup>* and β. To reduce the computation time FEA was performed on 1/4 model of the machine as discussed in Appendix 2.

In this section we will discuss the results obtained from the FEA of 22kW SynRM, whose specifications are given in Appendix 1. The results obtained are then used to define the optimum operating point which can be integrated in control using look-up tables or curve fitting.

Figure [3.2](#page-43-1) shows the magnetic field density in the machine under unsaturated

and highly saturated condition. We can observe that the onset of saturation along q-xis is much earlier than that of d-axis. Moreover, we can also see high saturation along ribs, which explains the lower cross-coupling effect along q-axis at higher currents.

<span id="page-43-1"></span>![](_page_43_Figure_1.jpeg)

Figure 3.2: Unsaturated (left) Saturated(right).

### <span id="page-43-0"></span>**3.2.1 Inductance Estimation**

Figure [3.3](#page-43-2) shows the variation of d-axis inductance with β for different values of *I<sup>s</sup>* . It can be observed that, with increase in current, saturation increases which results in increased reluctance thus reduction of inductance. However it is also seen that with increasing β the *L<sup>d</sup>* remains constant for unsaturated case but increases for saturated rotor i.e higher currents. Another observation is that with increasing β, *i<sup>d</sup>* decreases which reduces the flux linkage along d-axis. Since we can not define *L<sup>d</sup>* at β = 90° we can look for the behaviour when β approaches 90°. Ideally, the d-axis flux linkage should go to zero if β approaches 90° But this is not the case as we can see that there is still a difference in the values of inductances, which is a representation of flux linkage. This is observed because of the cross-coupling effect.

<span id="page-43-2"></span>![](_page_43_Figure_5.jpeg)

Figure 3.3: Variation of *L<sup>d</sup>* with β at different *I<sup>s</sup>* .

Similarly, figure [3.4](#page-44-0) presents the *L<sup>q</sup>* depenedence on β for different values of *I<sup>s</sup>* . A similar argument can be made here, i.e. with increase in β the saturation along q-axis increases thus reducing the inductance. We can also see that this effect is prominant only in the lower values of current. Since the effective air-gap is very large along q-axis we can not see any drastic effect of saturation on *L<sup>q</sup>* at higher values of current.

<span id="page-44-0"></span>![](_page_44_Figure_1.jpeg)

Figure 3.4: Variation of *L<sup>d</sup>* with β at different *I<sup>s</sup>* .

Figure [3.5](#page-44-1) shows effect of β on the saliency ratio for increasing values of *I<sup>s</sup>* . Around β = 60° we can observe that saliency ratio is nearly same for higher values of current. Also from the figure [3.11](#page-48-0) we can see that power factor remains is same for higher values of current at β = 60°. This further strengthen the argument about the relation found in equation 2.33 and 2.34, even though cross coupling effect is not considered.

<span id="page-44-1"></span>![](_page_44_Figure_4.jpeg)

Figure 3.5: Saliency Ratio with β at different *I<sup>s</sup>* .

#### <span id="page-45-0"></span>**3.2.2 Torque**

Figure [3.6](#page-45-1) shows the variation of torque with rotor positon θ. Here the current is maintained at rated value and β is taken as . Here the coice of β is arbitrary, and it was choosen based on MTPA condition derived in section 2.2.1. The choice of β does not affect the torque ripple observed here. This ripple is due to slots and winding arrangements.

<span id="page-45-1"></span>![](_page_45_Figure_2.jpeg)

Figure 3.6: Ripple in Torque due to rotor position.

There are two components of torque ripple low frequency and high frequency [19]. Lower frequency torque ripple is due to winding distribution. And Higher frequency torque ripple is due to slots in the stator. Since our machine is 48 pole this gives us a slot pitch of 7.5°. On closer look one can confirm that the higher frequency component has period of nearly 7.5° mechanical which translate to the slot pitch of the stator.

This torque ripple will always be there and it would not effect the choice of *I<sup>s</sup>* and β for MTPA operation. Figure [3.7](#page-46-0) gives variation of torque with beta for different values of stator current. Due to increase in saturation with higher *I<sup>s</sup>* , the MTPA point is no longer at β = 45°. It shifts towards right for higher values of current.

<span id="page-46-0"></span>![](_page_46_Figure_0.jpeg)

Figure 3.7: Torque variation due to *I<sup>s</sup>* and β.

One can explain this shift in MTPA based on the equation 3.1. From the equation it is clear that torque depends on the difference of *L<sup>d</sup>* and *Lq*. At higher values of current q-axis inductance remains nearly constant since this axis is already saturated owning to its higher air gap. Thus if we rotate current vector towards q-axis the saturation in d-axis will reduce resulting in increase in *Ld*. This together with the product of *i<sup>d</sup>* and *i<sup>q</sup>* results in shifted maxima for torque curves.

Figure [3.8](#page-46-1) and figure [3.9](#page-47-1) gives the comparison between calculated torque and FEA torque. From the figure it is clear that the FEA torque and the calculated torque have similar shape. The difference is of a scaling factor which arises from the fact that we did not consider the cross-coupling effect. Neglecting cross-coupling effect in estimation of inductances gives us a reduced torque. However, from control perspective it is a good estimate since we are getting higher torque for the same value of *I<sup>s</sup>* and β as it is confirmed by the FEA torque.

<span id="page-46-1"></span>![](_page_46_Figure_4.jpeg)

Figure 3.8: Calculated Torque vs FEA Torque when the rotor is unsaturated.

<span id="page-47-1"></span>![](_page_47_Figure_0.jpeg)

Figure 3.9: Calculated Torque vs FEA Torque when the rotor is saturated.

#### <span id="page-47-0"></span>**3.2.3 Power Factor**

Figure [3.10](#page-47-2) shows p.u torque with power factor at the rated condition. This curve can be used to determine the β for which we have optimum torque and power factor.

<span id="page-47-2"></span>![](_page_47_Figure_4.jpeg)

Figure 3.10: Torque(p.u) and Power Factor curves with β at rated *I<sup>s</sup>* .

Figure [3.11](#page-48-0) gives the variation of power factor with current angle. It can be observed that the power factor also increases with β but increasing *I<sup>s</sup>* does not improve power factor when machine saturates. One can conclude that the machine performance is better under saturation. But this conclusion is valid with some constraints. The first constraint being the limited DC-link voltage availabel at inverter. And second is with increase in saturation losses also increases. But when we overload the drive for example in an EV, we can achieve higher torque value at better power factor for a short duration. Thus increasing the utilisation of the inverter while increasing performance.

<span id="page-48-0"></span>![](_page_48_Figure_0.jpeg)

Figure 3.11: Power factor variation with current angle.

Figure [3.12](#page-48-1) shows the p.u voltage required and torque produced by the SynRM at rated conditions. One can see that by operating the machine at higher value of β we can achive more than the rated torque at rated current while our voltage just hits it limit.

<span id="page-48-1"></span>![](_page_48_Figure_3.jpeg)

Figure 3.12: Torque, Voltage(p.u) and power factor at rated operating point.

From the machine parameters listed in Appendix 1 we see that under rated conditions the torque is 123Nm. However, from FEA we find that it is possible to get 144Nm torque from the machine by changing the β from 45° to 65°. This is a 17% increase in rated torque. Based on these curves we can form a look-up table and use these values to modify the MTPA control implemented in the controller.

## <span id="page-49-0"></span>**3.3 Conclusion**

In this chapter effect of saturation was studied with the help of FEA. The torque depends on rotor position, stator current and current angle. Rotor position contributes to the ripple in torque whereas stator current and current angle are responsible for the average torque produced. We also observed that the MTPA position is shifted from 45° to some higher angle depending on the magnitude of *I<sup>s</sup>* . The data obtained from the figure [3.7](#page-46-0) can be used to get a look-up table based MTPA control which is similar to the vector control shown in figure [2.3.](#page-22-1) The only modification that needs to be done is to remove 1/*k<sup>t</sup>* gain block and replace it with look-up table which directly generates references for *i<sup>d</sup>* and *iq*.

We also found the variation of power factor with increasing saturation. This information was then used to determine the excess torque that can be produced by the given machine. The calculations performed based on the estimated inductances also show similar trends to that of FEA results. These justify the method chosen for inductance estimation and can be used to develop control for practical applications since the shape of the curves will remain the same and the only difference would be a small scaling factor representing the effect of cross-coupling.

### **CHAPTER 4**

### <span id="page-50-0"></span>**HARDWARE ORGANISATION**

<span id="page-50-3"></span>A back to back converter with common DC-bus with schematic as shown in figure [4.1](#page-50-3) was assembled in the lab. This converter can also be used to run a multiphase motor or it can be used such that one converter acts as active front end and another as inverter.

![](_page_50_Figure_3.jpeg)

Figure 4.1: Schematic of back to back converter.

## <span id="page-50-1"></span>**4.1 Brief overview of Major Components**

## <span id="page-50-2"></span>**4.1.1 IGBT Module SKM200GB12E4 & Gate Driver SKYPER-32- PRO R**

The module SKM200GB12E4 has IGBTs in a half-bridge configuration and can have switching frequencies of up to 20KHz. The collector current is 313A at ambient temperature and its breakdown voltage is 1.2kV.

The IGBT gate driver SKYPER-32-PRO R can drive two IGBT's in the halfbridge configuration of our module. It provides automatic fault protection against short circuit by interrupting gate signals to the module. It also generates a small dead time if the input complementary signals don't have one in order to avoid a short circuit.

### <span id="page-51-0"></span>**4.1.2 PD-Card**

A Protection and Delay card (PD-Card) is mainly used for providing dead time between complimentary gate signals and protection against faults. The gate signals generated are directly given to the gate driver. This card has provision to sense a total of 8 signals and generate fault signals accordingly. The upper and lower references to trigger the fault signal is set with the help of potentiometers present on the board which are then fed to op-amp LM139 present on board to generate the fault signal. This card is programmed using Quartus. The FPGA is programmed schematically to generate dead band and fault protection logic. This PD-Card is based on Altera-MaxII-EPM1270T144C5N.

### <span id="page-51-1"></span>**4.1.3 Controller-TMS320F28335**

The controller uses a DSP TMS320F28335 by Texas Instruments. This is a 32-bit processor based on modified Harward Architecture and includes IEEE 754 singleprecision FPU. TMS320F28335 has six ePWM modules and each has two output channels ePWMxA and ePWMxB which can be used to generate complementary gate signals. It also includes 12-bit 16-channel ADC module whose reference is 3V. This functionality provides sensing on the controller itself. However suitable burden resistors must be selected to ensure proper sensing since our voltage and current sensors give current as the output signal.

### <span id="page-51-2"></span>**4.2 Hardware Setup**

Below are the images of the assembled inverter and the SynRM that is being manufactured. Suitable tests were performed to ensure that the inverter was working properly.

<span id="page-52-1"></span>![](_page_52_Picture_0.jpeg)

Figure 4.2: Assembeled Inverter.

<span id="page-52-2"></span>![](_page_52_Picture_2.jpeg)

Figure 4.3: SynRM .

### <span id="page-52-0"></span>**4.3 Conclusion**

This chapter briefly discussed some of the components used in the inverter. The inverter was tested by running a simple v/f control for the induction motor under unloaded condition.

Due to the unavailability of SynRM at the time of writing this thesis, the proposed control scheme under saturated conditions could not be implemented on hardware.

### **CHAPTER 5**

### **CONCLUSION**

## <span id="page-53-1"></span><span id="page-53-0"></span>**5.1 Summary of the Present Work**

In order to formulate a good control scheme for the SynRM, a detailed understanding of the influence of machine parameters on the output must be known. To fully understand the operating regions of the motor, a detailed mathematical model was derived in chapter-2. This model was later used to derive the MTPA based control and we also found an expression for the power factor. Later the mathematical model was normalized, in order to get motor performance characteristics depending only on the saliency ratio. Based on this normalized model various operating regimes under field weakening were discussed. Particular focus was given to the case when the machine operates at constant power beyond base speed and an expression for the speed limit was found. In order to validate the theory, a simulation of 22kW SynRM was done in MATLAB. Sensored vector control response was designed for first-order response while keeping non-idealities in the motor. Later, field weakening was studied in conjunction with the constant power operation of the machine, and its operating points were plotted for beyond base speed operation. However, the discussion was restricted to the case where machine was not saturated.

In chapter-3 the FEA was used for the SynRM. The FEA gave some unique insight of the machine operation. It was observed that the effect of rotor saturation was significant even at normal operation. First we found a suitable method to estimate values of d and q-axis inductances, while neglecting the cross-coupling effect, such that it is consistent with the theory given in chapter-2. Then based on the observations and existing literature, the notion of inductances being a function of current and current angle was put forth. This formulation was observed to validate the torque equation given in chapter-2 but with some error. This error is due to the cross-coupling effect and does not affect the formulation of control scheme. Based on the torque obtained from FEA it was observed that MTPA point was shifted to higher values of current angle. This saturation effect also changes the power factor trajectory of the machine. However, it was observed that saturation increases the torque output while improving the power factor at a given speed when compared to conventional MTPA. This study helps us to understand the impact of current space vector on the machine parameters. With the use of FEA we can derive suitable operating points which extract more performance from the same SynRM using conventional control strategies.

### <span id="page-54-0"></span>**5.2 Future Scope of Work**

Based on the FEA a better understanding of the machine is possible. Hardware realisation of the control scheme can be done in future. There is a lot of scope to implement the control points derived based on FEA in more advanced model predictive control (MPC) [20]. One can also derive simpler models based on curve fitting to implement control strategies. Also a better analytical model can be developed while considering the cross-coupling effect. There can also be a better definition for the rated parameters based on the machine model under saturated conditions. The model may not be an analytical one but a good approximation based on FEA can also serve the purpose of design optimization of the rotor. The rotor design process can also get benefit from the direct relation that could be found between optimum operating point and rotor geometry [21][22]. Finally, it is possible to make use of Ansys Simplorer in conjunction with Simulink to develop and test control algorithms virtually before deploying on hardware.

### **APPENDIX A**

### **Machine Parameters**

<span id="page-55-1"></span><span id="page-55-0"></span>Table A.1 shows the parameters for 22kW SynRM.

Table A.1: Machine Parameters.

| Machine Parameter    | Values      |
|----------------------|-------------|
| Rated Power          | 22 kW       |
| Phases               | 3           |
| Connection           | Delta       |
| Number of Poles      | 4           |
| Rated Speed          | 1500 RPM    |
| Rated Frequency      | 50 Hz       |
| Max torque output    | 123 Nm      |
| DC bus voltage       | 500 V       |
| Resistance per Phase | 0.2<br>Ω    |
| d-axis inductance    | 48.18 mH    |
| q-axis inductance    | 11.88 mH    |
| J                    | kgm2<br>0.5 |

<span id="page-55-2"></span>Table A.2 shows the coil winding details.

Table A.2: Winding Details.

| Winding Parameter | Values                 |
|-------------------|------------------------|
| Pitch             | 1-14, 2-13, 3-12, 4-11 |
| Turns/coil        | 10                     |
| Type              | Double layer           |
| Slot fill factor  | 41%                    |
| Parallel Path     | 2                      |
| Turns/slot        | 20                     |
| Turns/phase       | 80                     |
| Chorded by        | 2                      |

### **APPENDIX B**

### <span id="page-56-0"></span>**FEA modelling in Ansys MAXWELL-2D**

The software package used is Maxwell 2-D by Ansys. This appendix gives a brief overview of modelling procedure followed to get results with better accuracy with comparitively lesses computation time.

<span id="page-56-1"></span>Figure [B.1](#page-56-1) shows the model of the aboveSynRM in Maxwell-2D .

![](_page_56_Picture_4.jpeg)

Figure B.1: Maxwell-2D model of 22kW SynRM .

In FEA the region is divided into elements and then fields are numeriaclly computed using maxwell's equations. For this study ANSYS Maxwell-2D software package is used to perform FEA. Here we will briefly discuss the process and considerations required to perform a fairly accurate FEA while reducing the computation time.

The first step was to draw the machine and assign materials to the objects. The cross section of the machine can be drawn in the Ansys environment itself or it can be imported from other CAD softwares such as AutoCAD. In our case we used Ansys to draw stator core and winding. The rotor was drawn on AutoCAD and then imported to Ansys. The selected material for the rotor and stator was M36 grade steel. Figure [B.1](#page-56-1) shows the simulated model.

Since in FEA the computation time depends on the number of elements in the mesh generated, thus one has to compromise between the accuracy and time. In our case the rotor geometry is complex and requires high density mesh near rotor flux barrier, slots and air gap. Since our machine is 4-pole we can reduce our model size based on the symmetry and properly defining boundary conditions on the reduced model. Figure [B.3](#page-57-1) shows the quarter symmetry of machine and the boundary conditions are applied along x and y axis such that the magnetic potential along x- axis is same as that of y-axis but in opposite direction.

<span id="page-57-0"></span>![](_page_57_Picture_2.jpeg)

Figure B.2: Per Pole model for FEA .

<span id="page-57-1"></span>![](_page_57_Picture_4.jpeg)

Figure B.3: Master-slave Boundary .

The mesh generated is shown in figur[eB.4.](#page-58-0)

<span id="page-58-0"></span>![](_page_58_Picture_0.jpeg)

Figure B.4: Mesh used for the FEA .

In Ansys one can use voltages or currents for the excitation of the windings. In our case we used currents and performed our simulation in magnetostatic domain. From the FEA we were able to get the torque generated and the flux linkages for the windings for a given *I<sup>s</sup>* and β.

### **References**

- 1. NASA 2021, Accessed: 5 Nov 2021, <https://www.nasa.gov/press-release/2020 tied-for-warmest-year-on-record-nasa-analysis-shows>
- 2. Waide,P. and C. Brunner (2011), "Energy-Efficiency Policy Opportunities for Electric Motor-Driven Systems", IEA Energy Papers, No. 2011/07, OECD Publishing, Paris.
- 3. P. J. Lawrenson, "Theory & Performance of Polyphase Reluctance Machines", Proceedings of the IEE, 1964-August.
- 4. T. J. E. Miller, A. Hutton, C. Cossar and D. A. Staton, "Design of a synchronous reluctance motor drive," in IEEE Transactions on Industry Applications, vol. 27, no. 4, pp. 741-749, July-Aug. 1991, doi: 10.1109/28.85491.
- 5. J. K. Kostko, "Polyphase reaction synchronous motors," in Journal of the American Institute of Electrical Engineers, vol. 42, no. 11, pp. 1162-1168, Nov. 1923, doi: 10.1109/JoAIEE.1923.6591529
- 6. I. Boldea, "Reluctance Synchronous Machines and Drives", Oxford University Press, 2002
- 7. J. A. Santisteban and R. M. Stephan, "Vector control methods for induction machines: an overview," in IEEE Transactions on Education, vol. 44, no. 2, pp. 170-175, May 2001, doi: 10.1109/13.925828.
- 8. "Vector control of a synchronous reluctance motor including saturation and ironVector Control Methods for Induction Machines: An Overview loss," IEEE Trans. Ind. Applicut., vol. 27, no. 5, Sept./Oct. 1991.
- 9. R. Lagerquist, I. Boldea and T. J. E. Miller, "Sensorless-control of the synchronous reluctance motor," in IEEE Transactions on Industry Applications, vol. 30, no. 3, pp. 673-682, May-June 1994, doi: 10.1109/28.293716.
- 10. R.E Betz, "Theoretical aspects of the control of synchronous reluctance machines," in IEE Proc.-B, vol. 139, no. 4, July 1992.
- 11. A. Chiba and T. Fukao, "A closed-loop operation of super high-speed reluctance motor for quick torque response," in IEEE Transactions on Industry Applications, vol. 28, no. 3, pp. 600-606, May-June 1992, doi: 10.1109/28.137445
- 12. R. E. Betz, R. Lagerquist, M. Jovanovic, T. J. E. Miller and R. H. Middleton, "Control of synchronous reluctance machines," in IEEE Transactions on Industry Applications, vol. 29, no. 6, pp. 1110-1122, Nov.-Dec. 1993, doi: 10.1109/28.259721.

- 13. Ahn, J., Lim, S. B., Kim, K. C., Lee, J., Choi, J. H., Kim, S., & Hong, J. P. (2007). "Field weakening control of synchronous reluctance motor for electric power steering". IET Electric Power Applications, 1(4), 565-570. https://doi.org/10.1049/iet-epa:20060212
- 14. B. J. Chalmers and L. Musaba, "Design and field-weakening performance of a synchronous reluctance motor with axially-laminated rotor," pp. 271-278 vol.1, doi: 10.1109/IAS.1997.643038.
- 15. D. A. Staton, T. J. E. Miller and S. E. Wood, "Maximising the saliency ratio of the synchronous reluctance motor", Proc. Inst. Elect. Eng.—Elect. Power Appl., vol. 140, no. 4, pp. 249-259, Jul. 1993.
- 16. A. Colotti and K. S. Stadler, "Magnetic cross-coupling effects on the performance of the synchronous reluctance machine," 2014 16th European Conference on Power Electronics and Applications, 2014, pp. 1-10, EPE.2014.6910730.
- 17. Knebl, L.; Bacco, G.; Bianchi, N.; Ondrusek, C. Synchronous Reluctance Motor Analytical Model Cross-Saturation and Magnetization Analysis. Prz. Elektrotech. 2020, 1, 110–114
- 18. R. R. Moghaddam, F. Magnussen and C. Sadarangani, "Theoretical and Experimental Reevaluation of Synchronous Reluctance Machine," in IEEE Transactions on Industrial Electronics, vol. 57, no. 1, pp. 6-13, Jan. 2010, doi: 10.1109/TIE.2009.2025286.
- 19. A. Fratta, G. P. Troglia, A. Vagati and F. Villata, "Evaluation of torque ripple in high performance synchronous reluctance machines," Conference Record of the 1993 IEEE Industry Applications Conference Twenty-Eighth IAS Annual Meeting, 1993, pp. 163-170 vol.1, doi: 10.1109/IAS.1993.298919.
- 20. H. Hadla and S. Cruz, "Predictive Stator Flux and Load Angle Control of Synchronous Reluctance Motor Drives Operating in a Wide Speed Range," in IEEE Transactions on Industrial Electronics, vol. 64, no. 9, pp. 6950-6959, Sept. 2017, doi: 10.1109/TIE.2017.2688971.
- 21. G. Pellegrino, F. Cupertino and C. Gerada, "Automatic Design of Synchronous Reluctance Motors Focusing on Barrier Shape Optimization," in IEEE Transactions on Industry Applications, vol. 51, no. 2, pp. 1465-1474, March-April 2015, doi: 10.1109/TIA.2014.2345953.
- 22. W. Kim et al., "Optimal PM Design of PMA-SynRM for Wide Constant-Power Operation and Torque Ripple Reduction," in IEEE Transactions on Magnetics, vol. 45, no. 10, pp. 4660-4663, Oct. 2009, doi: 10.1109/TMAG.2009.2021847.