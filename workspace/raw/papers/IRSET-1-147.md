![](_page_0_Picture_0.jpeg)

# **DESIGN AND ANALYSIS OF SYNCHRONOUS RELUCTANCE MOTOR (SynRM) USING MATLAB SIMULINK**

Mohammed Ayad Alkhafaji1,\*, Yunus Uzun<sup>2</sup>

<sup>1</sup>Department of Electrical Electronics and Computer Engineering,

Graduate School Of Natural and Applied Sciences, Aksaray University, Aksaray, Turkey <sup>2</sup>Department of Electrical and Electronics Engineering, Faculty of Engineering, Aksaray University, Aksaray, Turkey

------------------------------------------------

\*Corresponding author

## **ABSTRACT**

In recent years, the synchronous reluctance motor SynRM has become an important part in many electrical and mechanical industries. The SynRM has several characteristics and features which made it different from other types of motor that previously used in many industries in the same field. This paper presents the modelling, analysing and simulation of synchronous reluctance motor (SynRM) drive system, and present a part of differences in feature and design between the SynRM and other reluctance motors. The SynRM mathematical fundamental has formed by using the dynamic equations of the motor. Technically, the d-q transformation strategy has been employed for the vector control method of the SynRM to convert the three-phase voltage into two-phase. Space Vector Pulse Width Modulation technology has used to modelling and simulation the SynRM model without rotors cage or magmatic material. The six sectors of mechanical SynRM have converted to six MOSFET transistors and electrical power supply to represent the fundamental of three-phase voltage source. Hence, the MATLAB Simulink environment has used to simulate and modify the SynRM model and represented the direct and quadratic axes voltages, and the feature of SynRM modelled to include speed and torque with different frequencies and load conditions.

**Keywords:** SynRM, SVPWM, Inverters, d-q transformation, Matlab simulink.

# **Introduction**

In the beginning, SynRM is one of several synchronous machines, and the SynRM rotor structure has manufactured without winding or magnet material. As a comparison between SynRM with

![](_page_1_Picture_0.jpeg)

other types of reluctance motors like IM, BLDC motor and switch reluctance motor SRM, the result shows that SynRM is precision in manufacturing, simple structure. In addition to, it has a distinctive properties like low torque average, larger torque pulsation and low power factor. In fact, the SynRM may give a high stable performance in contrast with other AC drives compared with IM. The SynRM is a three-phase motor operated by three-phase of space vector inverter. As mentioned earlier, the SynRM is a kind of synchronous machines that have no winding or permanent magnet on the rotor and salient poles, it has a fragmented rotor of the numerous barriers. The reason for made the reluctance motor rotor form laminated axially steel it has to dominate low torque response and unsuitable power factor, although older versions of reluctance motor have lacked this technology of manufacturing. The stator-winding layout of SynRM is quite similar to the IM. Whereas, the rotor structure of SynRM is quite different from IM, it is not caged rotor or twisting and does not have any magnetic material, it has only laminated obstacles which designed in complex manner, and an optimized to have a top quadrature axis compliments and non-direct axis jealousy, once the magnetic field flow in the stator winding and according to the rotor structure it is a low and high hesitation area and they signify practically the magnetic poles (Fellani&Abaid, 2010), (Fellani&Abaid, 2013), (Consoll et al., 1999). The rotor design in SynRM is rotated to reach the low reluctance areas and drifting away of the high reluctance areas in the same time of rotate, the reason of this work strategy to achieve the magnetic field synchronous speed. In fact, the stator formula to both of SynRM and IM are the same signal into the rotating frame. The SynRM does not need any magnetic or winding substance on the rotor structure which makes the motor rugged, construction simplicity, the cheapest cost of manufacturing, higher torque per unit quantity possibility, operating at most high speeds capability which makes the SynRM, and the rotor windings Failing to result a simple control procedures, and the decline's minimization create SynRM an appealing and famous choice for numerous industrial and automotive applications due to all of those significant and amazing characteristics (Mohdzeeshan, 2011) (Golten&Verwer, 1991) (Reddy et al., 2012). The earliest versions of SynRMs are used directly a caged rotor, the most important reason that pristine SynRMs do not have a beginning torque attributes, but now the modern SynRM and using the newest kinds of inverters, field orientation control (FOC) technology along with using pulse width modulation (PWM) technique supply a convenient technique for control, So without any rotor cage that the machine may will be initiated (Soltani&Abootorabi, 2004). The speed variable parameters have used in SynRM motor system design to correct the motor speed drive due to several elements like energy conservation, control situation, velocity, and enhancement the transient response characteristics. The aim of a motor speed controller is to take a signal representing the reference speed and to drive the motor at that reference speed (Fellani&Abaid, 2013). Although, control system consists of a speed that been feedback from the system, a SynRM, a voltage source space vector inverter, a controller, and a speed setting device. The major reason of using feedback in these systems is

![](_page_2_Picture_0.jpeg)

to be able to obtain a reference-point regardless of any variation or other concern in the characteristics the system back to the reference-point. Fig.1 is show SynRM rotor flux barrier and IM motor rotor cage. In addition to, the SynRM motor can be revealed from its d-q stationary axis equal circuits as in Fig.3.

Figure 1: The machineal design contants of relectunce motors, Induction motor (left) and SynRM (right) motor topologies

![](_page_2_Picture_3.jpeg)

(Donaghy-Spargo, 2016)

Figure 2: SynRM d-q axis equivalent circuit

![](_page_2_Picture_6.jpeg)

(Mostafa et al., 2013)

### **SynRM Mathematical Model**

As mentioned earlier, The SynRM version is quite similar to the induction motor IM. The difference is by neglecting the rotor losses from the IM equations. A SynRM's model is described by the following equations.

$$V_d = R_s I_d + \frac{d\lambda_d}{dt} - \omega_r \lambda_q \tag{1}$$

$$V_q = R_s I_q + \frac{d\lambda_q}{dt} + \omega_r \lambda_d \tag{2}$$

$$\lambda_{\rm d} = L_{\rm d} I_{\rm d} \tag{3}$$

![](_page_3_Picture_0.jpeg)

$$\lambda_{\mathbf{q}} = L_{\mathbf{q}} \mathbf{I}_{\mathbf{q}} \tag{4}$$

The direct and quadratic axis twisting self-inductance and measured at Henri unit (H), signify the stator winding resistance in an ohm ( $\Omega$ ) and is the rotor angular speed in radian per minute (rad/sec) . By both of each Eq.3 and Eq.4 the over shift speed could be acquired as will detect in Eq.5 and Eq.6 as following:

$$\frac{\mathrm{d}\lambda_d}{\mathrm{dt}} = V_\mathrm{d} - R_\mathrm{s}I_\mathrm{d} - \omega_\mathrm{r}\lambda_q \tag{5}$$

$$\frac{\mathrm{d}\lambda_{\mathrm{q}}}{\mathrm{d}t} = V_{\mathrm{q}} - R_{\mathrm{s}}I_{\mathrm{q}} - \omega_{\mathrm{r}}\lambda_{\mathrm{d}} \tag{6}$$

From Eq.5 the change-speed rate of the direct axis current could be gained in Eq.6

$$\frac{\mathrm{dI_d}}{\mathrm{dt}} = \frac{1}{L_d} (V_\mathrm{d} - R_\mathrm{s} I_\mathrm{d} + \omega_\mathrm{r} L_q I_q) \tag{7}$$

And with Eq.6 the change-speed rate of the quadratic axis current could be gained in Eq.8.

$$\frac{\mathrm{dI_q}}{\mathrm{dt}} = \frac{1}{L_a} (V_{\mathrm{q}} - R_{\mathrm{s}} I_{\mathrm{q}} + \omega_{\mathrm{r}} L_d I_d) \tag{8}$$

In addition to, obtain the torque equation for SynRM can as trace in Eq.9.

$$T = \frac{3}{4} \frac{P}{2} (L_{d} - L_{q}) I_{d} I_{q}$$
 (9)

Where T signifies the electromagnetic torque of this SynRM at Newton per meter N/m. The of speed rate can be acquired by the following equation.

$$\frac{d\omega_{\rm r}}{dt} = \frac{P}{I} (T_{\rm e} - T_{\rm L}) \tag{10}$$

Where P the amount of poles is pairs of this motor and load, J represents the moment of inertia coefficient of the motor in kilogram square meter (kgm²), and  $T_L$  is the load torque to the motor inside newton per meter N/m. The Laplace transformation to the torque equation is given below in Eq.11.

$$T = \frac{3}{2} P(L_d - L_q) i_d i_q - (B\omega_r + J \frac{d\omega r}{dt})$$
(11)

Where B is the viscous friction coefficient of the motor (Fellani&Abaid, 2013).

## **Mathematical Model of Stationary Field Transformation**

The transformation from the mechanical model has done by using the d-q transformation, which is used for vector control method of the synchronous motor machine. The based of the idea which is the windings of the stator are distributed a d-q version is an effective

![](_page_4_Picture_0.jpeg)

tool for simulation of all AC machines including the SynRM (Tran, 2012). When Three-phase balanced and adjusted windings and symmetry to two-phase equilibrium windings deliver rotating magnetic field speed  $\Phi$  and value are equality, the Three-phase windings are equal with the two-phase windings. The d-q transformation is well-balanced three-phase  $V_d$ ,  $V_b$  and  $V_c$  into balanced two-phase  $V_d$  and  $V_q$  as shown in Fig.3. The conversion matrix is explained in Eq.12 and the simulation is shown in Fig.9.

$$\begin{bmatrix} V_{d} \\ V_{q} \end{bmatrix} = \sqrt{\frac{2}{3}} \begin{bmatrix} 1 & \frac{-1}{2} & \frac{-1}{2} \\ 0 & \frac{\sqrt{3}}{2} & \frac{-\sqrt{3}}{2} \end{bmatrix} \begin{bmatrix} V_{a} \\ V_{b} \\ V_{c} \end{bmatrix}$$
(12)

Where  $V_a$ ,  $V_b$  and  $V_c$  are the three-phase balance voltages and  $V_d$  and  $V_q$  are the two-phase equivalent for three phase voltages. The zero axis voltage is neglected, and the power is the same in both the three phase and the two-phase transformation. In addition to, the d-q transformation matrix block simulate shown in Fig.9.

Figure 3: The Direct and Quadratic Voltage Transformation

![](_page_4_Figure_5.jpeg)

#### **Voltage Source Inverter Mathematical theory**

As a definition of an inverter, it is a power electronic circuit which converts the DC voltage source into AC voltage source, depending on the inverter work type the voltage transformation could be into a single phase, two phases or three phases. An inverter motors that are ingesting and utilized in frequency factor and voltage for variable rate application. The Pulse Width Modulation PWM method that is much popular to SVPWM technique that has utilized due to the DC bus voltage. Additionally, as compared to the SPWM it provides a greater performance and awareness can be achieved and which imply an output voltage can get. The amounts represented the output of inverter as distance phase or distance vectors are this SVPWM notion. A premise is the amounts of the three-phase are one quantity. The steady-state and transient states both may be suitable for distance vector representation this is among the benefits of this SVPWM technique once the steady state condition is the sole requirement for phasor representation. The Space

![](_page_5_Picture_0.jpeg)

Vector Modulation (SVM) technique has been evolved as a vector strategy to Pulse Width Modulation (PWM) for three-phase inverters. Therefore, Fig.4 shows the converter circuit includes six MOSFET transistors and electricity supply represent the fundamental Three-Phase Voltage-Source. The SVPWM inverter is a scheme for creating a wave, which generates a voltage to the total harmonic distortion, is reduced. Any modulation scheme's goal is to procure the output signal with a basic material with as much as harmonics that are minimal. This strategy restricts distance vectors to be implemented in line with the area. The calculation of switching instants has done by using SVM plot based upon the representation of shifting vectors in the plane of the frame. Fig.5 shows the six sectors of the distance vector and the distance vector stage voltages (Zheng, 2018). Among the PWM Approaches that are significant and famous is SVPWM method for VSI for the controlling of AC Machines, for example, IMs, PMSM, and SynRM.

*Figure 4: Three-Phase Voltage-Source inverter circuit connected to power supply (Zheng,2018)*

![](_page_5_Picture_3.jpeg)

*Figure 5: The six sectors of the SVPWM (Zheng,2018)*

![](_page_5_Figure_5.jpeg)

![](_page_6_Picture_0.jpeg)

SVPWM technique demonstrates that the distance vector modulation method create from DC bus voltage possess distortion once the voltage created and greater efficacy. The reference voltage and its own angle of this distance vector inverter are contingent on the d-q transformation as shown in Fig.3.

$$\| V_{\text{ref}} \| = \sqrt{V_{\text{d}}^2 + V_{\text{q}}^2} \tag{13}$$

$$\alpha = \tan^{-1} \left( \frac{V_d}{V_q} \right) = \omega_s t = 2\pi f_s t \tag{14}$$

$$V_{ref}T_s = (V_1T_a + V_2T_b + V_{0.7}T_o)$$
(15)

$$T_z = (T_a + T_b + T_o) \tag{16}$$

$$V_{ref} = V_{ref}e^{j\alpha} \tag{17}$$

$$V_1 = \frac{2}{3} V_d, V_{0,7} = 0, V_2 = \frac{2}{3} V_d e^{j\frac{\pi}{3}}$$
 (18)

The source space vector has been assumed to be constant during one switching cycle to get high switching frequency. The zero vectors refer to the start switching and each of switching period  $T_Z$  or full null per vectors per  $T_S$ , and each of nulls have duration width of  $\left(\frac{T_O}{2}\right)$ , so the space vector equations can be written as follows:

**Re:** 
$$V_{ref} \cos \alpha T_z = \frac{2}{3} V_{dc} T_a + \frac{1}{3} V_{dc} T_b$$
 (19)

Im: 
$$V_{ref} \sin \alpha T_z = \frac{1}{\sqrt{3}} V_{dc} T_b$$
 (20)

$$T_{a} = \frac{\sqrt{3} T_{z} V_{ref}}{V_{dc}} \sin(\frac{\pi}{3} - \alpha) = T_{z} * m_{a} * \sin(\frac{\pi}{3} - \alpha)$$
 (21)

$$T_{b} = \frac{\sqrt{3} T_{z} V_{ref}}{V_{dc}} \sin(\alpha) = T_{z} * m_{a} * \sin(\alpha)$$
 (22)

$$T_o = (T_z - T_a - T_b)$$
 (23)

Where  $m_a$  represents the modulation index of the SVPWM inverter, and  $V_{dc}$  is the DC source voltage in volt unite.

$$m_a = \frac{\sqrt{3} V_{ref}}{V_{dc}} \quad (0 \le \alpha \le 60) \tag{24}$$

$$T_{a} = \frac{\sqrt{3} T_{z} V_{ref}}{V_{dc}} \left( \sin(\frac{\pi}{3} - \alpha + \frac{n-1}{3}\pi) \right) = \frac{\sqrt{3} T_{z} V_{ref}}{V_{dc}} * \left( \sin(\frac{n\pi}{3} - \alpha) \right)$$
 (25)

![](_page_7_Picture_0.jpeg)

$$T_{b} = \frac{\sqrt{3} T_{z} V_{ref}}{V_{dc}} \left( \sin\left(\alpha - \frac{n-1}{3}\pi\right) \right)$$
 (26)

# **SynRM Block System Simulation**

The direct and quadratic axis voltages has framed to represent the SynRM model design. The voltages equations of SynRM which framed in Eq.1 and Eq.2 are implement in Matlab/Simulink environment block as in Fig.6. The direct and quadratic axis voltages are represented the input of SynRM block system, and the result of simulation that represent by both of speed and torque. The complete Simulink model of SynRM drive system is shown in Fig.7. It consists of three main blocks, the SynRM block, d-q transformation block, inverter block.Morever, the block current of the two axes direct and quadrature are shown in the Fig.12 and Fig.13.The parameters which has used in SynRM design shown in the Tab.1.

*Figure 6: SynRM Model Block Design*

![](_page_8_Picture_0.jpeg)

*Figure 7: SynRM Drive System Block*

*Figure 8: Simulink Block of two axis SynRM.*

![](_page_8_Figure_4.jpeg)

![](_page_9_Picture_0.jpeg)

*Figure 9: d-q Transformation Matrix Block.*

![](_page_9_Picture_2.jpeg)

*Figure10: The Direct Axis Current Block*

![](_page_9_Picture_4.jpeg)

*Figure 11: The Quadrature Axis Current Block.*

![](_page_9_Picture_6.jpeg)

*Table 1: SynRM parameters*

| Parameter | Parameter Value | Units |
|-----------|-----------------|-------|
| Ld        | 6.0645          | mH    |
| Lq        | 0.910           | mH    |

![](_page_10_Picture_0.jpeg)

| Rs | 0.0265    | Ohm              |
|----|-----------|------------------|
| J  | 0.245     | Kgm <sup>2</sup> |
| В  | 0.0000009 | N.m.s            |
| Р  | 2         | poles            |

## The Results of SynRM Model Simulation

The simulation results are explained in this section. The efficiecny of motor was measured 94.8%. The features for your SynRM which exited through providing two-phase voltages  $V_d$  and  $V_q$  as shown in Fig.8. in addition to, the effect of the machine free of load and 25 Hz frequency are given in Fig.12 to Fig.13, also in Fig.14 and Fig.15 shown the direct and quadratic axes current in the same frequancy and load. The characteristics for the SynRM which exited through providing two-phase voltages as in Fig.6. Therefore, the Effect of the machine free of load and 50 Hz frequency are given in Fig.16 and Fig.17. The motor speed and torque when loading the motor with 20 N. m load at 1.4 sec with no control action and frequency of 25 Hz operation frequency are shown in Fig.18 and Fig.19.

Figure 12: Motor Speed with 25 Hz Frequency at No Load Condition.

![](_page_10_Figure_5.jpeg)

Figure 13: Motor Torque with 25 Hz Frequency at No Load Condition.

![](_page_10_Figure_7.jpeg)

![](_page_11_Picture_0.jpeg)

Figure 14: Direct Axis Current with 25 Hz Frequency at No Load Condition.

![](_page_11_Figure_2.jpeg)

Figure 15: Quadratic Axis Current with 25 Hz Frequency at No Load Condition.

![](_page_11_Figure_4.jpeg)

Figure 16: Motor Speed with 50 Hz Frequency at No Load Condition.

![](_page_11_Figure_6.jpeg)

Figure 17: Motor Torque with 50 Hz Frequency at No Load Condition.

![](_page_11_Figure_8.jpeg)

![](_page_12_Picture_0.jpeg)

Figure 18: Motor Speed with 20 N Load Applied at 1.4 Sec

![](_page_12_Figure_2.jpeg)

Figure 19: Motor torque with 20 N load applied at 1.4 Sec.

![](_page_12_Figure_4.jpeg)

#### Conclusion

This part has examined SynRM's operation. The contribution from the model's version fed into the SynRM and will be to convert the voltage. By controlling the performance frequency, the motor speed will be controlled. The results reveal that since the SynRM has two ways this motor's rate is 3000 rpm. Due to the absence of control activity the SynRM speed decline when implementing the load. When connecting the motor into the static transformation that is d-q, the function of motor does not change because the conversion matrix provides the power. The results demonstrated that the SynRM version legitimate under different operation conditions.

![](_page_13_Picture_0.jpeg)

# **Refrences**

- [1] Fellani, M. A. and Abaid E. ( 2013), "Modeling and Simulation of Reluctance motor using digital computer," *International Journal of Computer Science and Electronics Engineering*, vol. 1, pp. 148- 152.
- [2] Consoll, A., Russo, F. And Testa, A. (1999). "Low- and Zero-Speed Control of Synchronous Reluctance Motor," *IEEE Trans. Ind. Appl.,* vol. 35, no. 5, pp. 1050-1057.
- [3] Fratta, A. and Vagati, A. ( 1992), "A Reluctance Motor Drive for High Dynamic Performance Applications," *IEEE Trans. Industry Appl.*, vol. 28, no. 4, pp. 873-879.
- [4] Fellani, M. A., and Abaid E. (2010) "Matlab/Simulink-Based Transient Stability Analysis of a Sensorless Synchronous Reluctance Motor," *World Academy of Science, Engineering and Technology*, vol. 4, no. 8, pp. 1364-1368.
- [5] Soltani, J. and Abootorabi Zarchi H. (2004). "Robust Optimal Speed Tracking Control of A Current Sensorless Synchronous Reluctance Motor Drive Using A New Sliding Mode Controller," *IJE Journal*, vol. 17, no. 2, pp. 155-170.
- [6] Mohdzeeshan H. ( 2011). Position Control of Permanent Magnet Brushless DC Motor using PID Controller Master Thesis in Electrical Engineering, Thapar University:Patiala.
- [7] Golten, J. and Verwer, A. (1991). *Control System Design And Simulation*, London, UK: McGraw-Hill.
- [8] Reddy M. B., Obulesh Y. P. and Raju S. S. (2012). "Particle Swarm Optimization Based Optimal Power Flow for Volt-Var Control," *ARPN J. Eng. Appl.Sci.*, vol. 7, pp. 20-25.
- [9] Zheng, J., Huang,S., Rong,F. And Lye,M. (2018). "Six-Phase Space Vector PWM under Stator One-Phase Open-Circuit Fault Condition," *Energies*, vol. 11, no. 7, 1796.
- [10]Tran, P.H. (2012). Matlab/simulink implementation and analysis of three pulse-width-modulation (PWM) Techniques, Master of Science in Electrical Engineering , Boise State University, United States: Boise.
- [11]Bianchi, N., Bolognani, S., Carraro, E. and Castiello, M. (2016). "Electric Vehicle Traction based On Synchronous Reluctance Motors," *IEEE Transactions on Industry Applications*, vol. 52, no. 6, pp. 4762-4769
- [12] Jha, A. (2016). European Training Network for the Design and Recycling of Rare-Earth Permanent Magnet Motors and Generators in Hybrid and Full Electric Vehicles,EU MSCA-ETN DEMETER .[Online]. Available:<https://etn-demeter.eu/lets-discuss-motors-in-electric-vehicles-continued>
- [13]Donaghy-Spargo, C. M. (2016). Synchronous reluctance motor technology : opportunities, challenges and future direction. *Engineering technology reference*, pp. 1-15.