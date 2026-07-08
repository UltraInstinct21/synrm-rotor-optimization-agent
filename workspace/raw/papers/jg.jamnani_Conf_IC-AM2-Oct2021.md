![](_page_0_Picture_1.jpeg)

## ScienceDirect

![](_page_0_Picture_3.jpeg)

[International Conference on Additive Manufacturing and Advanced Materials – 2021]

# Performance Analysis and Comparison of PM-Assisted Synchronous Reluctance Motor with Ferrites and Rare-earth Magnet Materials

Swapnil N. Jania,b,\*, Jitendra G. Jamnani<sup>b</sup>

*<sup>a</sup>Nirma University, Nr. Vaishnodevi Circle Sarkhej-Gandhinagar Highway, Ahmedabad, 382481, India <sup>b</sup>Pandit Deendayal Energy University, Knowledge Corridor Raisan Village Sector-7, Gandhinagar, 382007, India* 

#### **Abstract**

The aim of the paper is to provide appropriate design methodology for chosen suitable permanent magnet material to be applied in manufacturing the Permanent Magnet (PM) assisted synchronous reluctance motor (PMASyRM). Another purpose is to reduce the use of rare earth magnets in motor design and increase the use of ferrite magnets to achieve the best performance of motor. The performance analysis of motor is discussed with different PM materials volume or quantity. The tradeoff design is presented to achieve the best performance parameter i.e. high torque, efficiency and low torque ripple. The effect of combination of different PM materials on performance parameters of motor is analyzed.

#### [copyright information to be updated in production process]

*Keywords: Permanent Magnet (PM) assisted synchronous reluctance motor (PMASyRM), Rare earth magnets and Ferrites magnets, Performance parameters, Finite Element Analysis (FEA)*

## **1. Introduction**

Electric Vehicles in the recent times have gained lot of ground and attention over the Conventional IC engine driven vehicles. Electric motor is the most important part for any type of electric vehicles. High torque and power density are the prieme most requirements for any electric motor used for EVs. PM motors are exhibits these type of characteristics which are exactly matching with requirements of EVs. Non PM motors have less torque and power density, so not preferred for EVs and hence not popular. Now a days induction motor is becoming popular for EVS but still certain drawbacks are there. In PM motors, Permanent Magnet Synchronous Motor (PMSM) is the best choice for EVs from all aspects. Only drawback of PMSM is high cost and demagnetization of PMs at high temperature due to PM materials used in it. As PM materials rare-earth PM materials i.e. Neodymium Ferrite Boron (NdFeB) and Samarium Cobalt (SMCo2) are mainly used in PMSM. These materials have high flux density and coercive force with respect to ferrites based PM. Cost of these rare earth materials is very high and avalebility of these materials is very less all over the globe and also dependency on other country are major drawbacks which think researchers to find out the new alternate against it. Synchronous Reluctance Motor is the good option for the EVs but due to low power factor and torque density this motor is not the proper choice. In recent time the drawbacks of SyRM are overcome by adding the PM in flux barriers at proper place and motor is called PM assisted Synchronous Reluctance Motor. (PMASyRM) As PM material people are using hybrid material which is combination of rare earth and ferrites to add in flux barriers which are in very less volume. Ferrite materials have low flux density and lower demagnetization characteristics, which makes infeasible to use it alone in flux barriers. To achieve proper flux density and higher demagnetization few amount of rare earth PM material is added to improve performance of ferrites. So this is the cost effective solution with enhance performance of PMASyRM. [1,2]

#### 2. Permanent Magnet Material Technology

As discussed in previous section, for EV application PM motors are the best option due to its inherent advantages i.e. high power density, high torque. Although PM motors are costly and also problems associated (i.e. demagnetization and overloading) with it due to use of PMs in higher volume. So researchers have found the another option i.e. to use of PM material in less quantity to avoid problems associated with usage of PMS and also to achieve the good performance like PM motors. For this purpose PM assisted synchronous reluctance motor is the best candidate and emerging as cost effective solution. Although it has gain attention in last decade, but still not becoming popular in market but people are finding it as best option against PMSM and Induction motors. From design point of view, low amount of PM is added in flux barriers of PMASyRM or to enhance performance of motor against the conventional synchronous reluctance motor. Hybrid magnet is also one of the good option instead of rare-earth where cost is important concern and at a same time performance can be achieved similar like rare-earth type magnet. Selection of PM material for rotor flux barrier is also important criteria. For this one can know characteristics and behaviour of rare-earth materials and ferrite materials. Table I represents the characteristics of different PM materials which may help designer to select best suitable material to achieve high performance. Table II gives idea about the suitability of different PM material for Electric motor. [7]

Table-1 Properties of PM materials.

| Material                   | Ferrites    | AlniCo    | SmCo     | NdFeB      |
|----------------------------|-------------|-----------|----------|------------|
| Property                   | (Ceramic 8) | (AlNiCo5) | (REC-26) | (NMX-42BH) |
| Br (kG)                    | 4           | 12.5      | 10.5     | 13.1       |
| >(%aC)                     | -0.18       | -0.02     | -0.03    | -0.11      |
| (BH)max MGOe               | 3.8         | 5.5       | 26       | 42         |
| Hd (kOe)                   | 3.3         | 0.64      | 10+      | 14         |
| >(%βC)                     | 0.4         | -0.015    | -0.3     | -0.6       |
| Hs (kOe)                   | 10          | 3         | 30       | 25         |
| Tc (°C)                    | 450         | 890       | 825      | 310        |
| Electrical<br>Conductivity | Poor        | Good      | Good     | Good       |

In PM-assisted synchronous reluctance motor, in flux barriers PM are placed in the form of different shapes. By adding PMs in flux barriers, magnetizing flux is saturated at some extent and performance of reluctance motor is improved. Due to addition of PMs, magnet torque is added with reluctance torque, which increase torque density and power density. Also power factor of motor improves which reduces the kVA rating of inverter. As PM material in PMASyRM, rare-earth magnets are used due to its inherent properties but problem of cost and demagnetization is included. To make the cost effective solution in flux barriers as PM material hybrid PM material is the best choice to meet performance criteria as economic point of view. In hybrid PM material one difficulty is to achieve proper saliency ration with the minimum usage of PM material in rotor. There are different rotor topologies are available and would be designed to achieve best suitable rotor topology for motor. In this paper by selecting combination of PM materials i.e. rare earth and ferrites FE analysis is carried out in ANSYS software. Optimal design methodology is adopted to achieve proper performance i.e. low torque ripple, high power and high torque. Electromagnetic analysis is done of newly adopted design and different plots are taken. [10]

Table-2. Suitability of different PM materials.

| Material                             | Ferrites    | AlNiCo    | SmCo      | NdFeB      |
|--------------------------------------|-------------|-----------|-----------|------------|
|                                      | (Ceramic 8) | (AlNiCo5) | (REC-26)  | (NMX-42BH) |
| Adhesive Force                       | Excellent   | Good      | Medium    | Weak       |
| Cost                                 | Medium      | Weak      | Good      | Excellent  |
| Design Diversity                     | Excellent   | Excellent | Excellent | Excellent  |
| Resistance                           | Weak        | Weak      | Weak      | Weak       |
| Resistance against<br>temp influence | Weak        | Good      | Excellent | Medium     |
| Corrosion<br>Resistance              | Weak        | Excellent | Excellent | Excellent  |
| Magnetizing<br>direction             | Excellent   | Excellent | Excellent | Excellent  |
| Magnetic Stability                   | Excellent   | Excellent | Weak      | Medium     |

#### **3. Topology of Permanent Magnet Assisted Synchronous Reluctance Motor**

The basic construction and working principle of PM (Permanent magnet) assisted synchronous reluctance motor is explained. Then, its various features are discussed and are summarized along with some of its limitation. Also, a good analytical model is introduced to summarize the basic idea behind it. Permanent magnet (PM) assisted synchronous reluctance machine here is designed in which first of all geometry of the machine is designed to maximize the reluctance torque. To increase the Torque, Permanent Magnets are added in the flux barriers. Along with that rotor dimensions are obtained for the machine. Reason of trend for this motor in EVs is because of its robustness, reduced cost and high overloading capacity. Power factor, Power density and Torque density of synchronous reluctance motor are comparatively low and to overcome this disadvantage we add permanent magnet in Synchronous reluctance motor's rotor to improve its performance. Now the structure looks similar to an Interior Permanent Magnet motor, but here flux linkages of PM and the number of Permanent Magnets is smaller than conventional Interior Permanent Magnet motors.

PM assisted synchronous reluctance motor (SynRM) is the best option for automotive application in which high efficiency and variable speed is required which fulfills by this motor. , which belongs to the family of brushless synchronous AC motor drives. The construction of PMASynRM is Synchronous Reluctance Motor with Permeant Magnets. In this type motor, PM materials are added to the flux barriers for the performance improvement in the motor. The power factor of the motor is also increasing. PM assisted synchronous reluctance motor does not have an excitation in it which can be shown in below Fig.1.1 and rotor here is constructed using flux barriers as shown below.

![](_page_2_Picture_5.jpeg)

Fig.1 Construction of PMASynRM

#### 4. Analytical Design

#### 4.1. Rotor Geometry Design

Rotor geometry design is first step to design PM Assisted Synchronous Reluctance. This motor's rotor contains flux barriers and flux carriers so this type of rotor structure produces two different reluctance paths. In the q-axis there is high reluctance path and, in the d-axis there is low reluctance path. In the flux barriers Permanent magnet material inserted to improve the performance of the motor. The outer diameter of Rotor can be calculated by following equation. [2]

$$D = 2n_p \frac{\tau}{\pi}(1)$$

The Pole pitch  $(\tau)$  is the function of d-axis component of air-gap flux density, pole pairs, saturation factor and electromagnetic torque. The Rotor length can be calculated by using the stack aspect ratio and the air-gap length can be calculated from pole pitch to air-gap ratio. L=  $\lambda \tau$ 

#### 4.2. Flux barrier geometrical parameters

The sizing and positioning of the flux barriers in the rotor must be determined. In figure PMASynRM rotor with four barriers is shown. In this figure Tm represents the barrier's thickness along with the d-axis, Ts is the iron part's thickness along with the d-axis, Wm is the length of the flux barrier perpendicular to the d-axis, Wb represents the length parallel to the q-axis, Tb is the flux barrier's thickness along with the q-axis and  $\alpha m$  represents the barrier end point angle.

#### 4.3. Machine Parameters

To analyze the motor's performance, its electrical and magnetic parameters need to be identified. By using following equations leakage inductance, phase resistance and magnetizing inductance. The leakage inductance can be calculated from following equation:

![](_page_3_Picture_9.jpeg)

Fig. 2 Geometrical Parameters of flux barriers

Ls
$$\sigma = 2\mu_0 n_s^2 N_{spp} n_p (\lambda_s + \lambda_z + \lambda_f)$$
 (2)  
Where,  
 $\lambda_s \cong \frac{2h_{s2}}{3(b_{s1} + b_{s2})} + \frac{2h_{s1}}{b_{s1} + b_{s0}} + \frac{h_{s0}}{b_{s0}}$  (slot permeance) (3)

$$\lambda z = \frac{5g}{5b_{so}+4g} \quad (4)$$

$$\lambda f = \frac{0.34q}{L} \left( l_f - 0.64\tau \right) \quad (5)$$

$$l_f = \Pi_{\frac{7}{2}}^{\tau} \quad (\text{stator end winding length})$$

$$Lm = 6\mu_o \tau L \frac{\left( n_p N_{spp} K_{wi} n_s \right)^2}{\Pi^2 n_p g K_c (1+K_s)} \quad (\text{For motor with uniform air gap}) \quad (6)$$
The phase resistance can be calculated from the following equation.
$$Rs = \rho l_c n_p N_{spp} n_s^2 \frac{J}{n_s I} \quad (7)$$

$$Where, \ \rho = 2.3*10^{-8} \quad \Omega \text{m}$$

 $l_c = 2(l + l_f)$  where,  $l_f$  is Winding end connection length

## 4.4. Permanent Magnet Selection

There are many permanent magnet types available in the market. Some magnets have high remanent flux density but these magnets are very costly and limitation in operating temperature. Some magnets have capability to operate in a higher temperature but they have low energy product. Some of the permanent magnet are: Neodymium-Iron-Boron (NdFeB), Alnico, Ferrite and Samarium-Cobalt (SmCo). i.e. Table 1 & 2. [4] For Finite Element Analysis purpose NdFeB (1.2 T) magnet is selected as it has strong magnetic properties which are essential from the EV requirement point of view.

#### 5. Finite Element Analysis: Results and Discussion

FE design is carried out as per the mentioned parameters in Table 3 by using ANSYS MAXWEL software. Rotor is internal side and V-shaped buried structure is adopted. To improve the features related with poor performance of the conventional SyRM and also cost of the rare earth material is high and also issue of less availability, few design modifications are carried out with the purpose of to improve saliency ratio of motor to produce high power density by using the finite-Element Method (FEM). Due to absent of rotor conductors, there is no copper losses occurred in this motor as magnetic field is produced from permanent magnets. 2D and 3D models of the initial design are presented in figures. Transient analysis is also done. [6]

Table 3. Motor Specification and Design parameters.

| Parameter                      | PMASynRM                |  |  |
|--------------------------------|-------------------------|--|--|
| Peak/Continuous output power   | 200 kW/100 kW           |  |  |
| Base/Maximum speed             | 1500 RPM/6000 RPM       |  |  |
| Number of poles/slots          | 8/24                    |  |  |
| DC bus Voltage                 | 650 V                   |  |  |
| Outer diameter of Stator       | 355 mm                  |  |  |
| Outer diameter of Rotor        | 240 mm                  |  |  |
| Active stack length            | 125 mm                  |  |  |
| Air gap thickness              | 1 mm                    |  |  |
| RMS line current               | 375 A                   |  |  |
| Total number of turns          | 3                       |  |  |
| Parallel paths                 | 1                       |  |  |
| Length of winding turn         | 524 mm                  |  |  |
| Coil fill factor               | 55%                     |  |  |
| Stator phase resistance        | $7.99~\mathrm{m}\Omega$ |  |  |
| End winding resistance         | $4.17~\mathrm{m}\Omega$ |  |  |
| End winding inductance         | 13.01 mH                |  |  |
| Peak RMS current density       | 25.1 A/mm2              |  |  |
| Continuous RMS current density | 10.1 A/mm2              |  |  |

] From using motor specification, model of PM assisted synchronous Reluctance Motor is developed in Ansys Maxwell Software for analysis purpose.

![](_page_5_Figure_1.jpeg)

Fig. 3 Full Model of PMASynRM

![](_page_5_Figure_3.jpeg)

Fig.4 Isometric view and front view of PMASynRM

The materials used for different parts of permanent magnet assisted synchronous Reluctance Motor is for stator and Rotor core is M-19 29 Ga, for magnets N36Z\_20 and ferrites which is hybrid PM material, for conductors copper is used. Due to the addition of rare earth materials cogging torque is introduced although electromagnetic torque of motor is improved with respect to ferrite material PMs. Due to cogging torque, there is torque ripple in this torque waveform. By using torque ripple reduction techniques, torque ripples are minimized, but still the torque waveform is not smooth. In this area still work can be done. Flux density plot, field strength plot, input current waveform and torque waveform are displayed in figures. As per the excitation given, proper plots are achieved with proper value and directions. [6]

![](_page_6_Figure_0.jpeg)

Fig. 5 Flux density Plot and field strength plot

![](_page_6_Figure_2.jpeg)

Fig. 6 Input Current Waveform and Torque waveform

#### **6. Conclusion**

The major disadvantage of SyRM is low torque density. By adding rare earth material in combination with ferrites in flux barrier, the performance of the motor improves which is presented here. These Permanent magnets are placed such that it opposes the q-axis flux. So, saliency ratio of the motor increases. Thus, the torque performance of the motor improves. Power factor of the motor also improves. So, volt-ampere reactive (VAr) requirement decreases. So, inverter power rating reduces. Due to the presence of Permanent magnet, there is cogging torque which affects the average torque of the motor. Due to the present of rare-earth material in rotor, the price of this motor slightly increases but at same time it gives improved performance. The motor is free from demagnetizing problem due to less quantity of rare earth PM against majority of ferrite PM material.

### **References**

- [1] Taghavi S. Design of synchronous reluctance machines for automotive applications (Doctoral dissertation, Concordia University).
- [2] Khan KS. Design of a permanent-magnet assisted synchronous reluctance machine for a plug-in hybrid electric vehicle (Doctoral dissertation, KTH Royal Institute of Technology
- [3] Dulanto AO. Design of a synchronous reluctance motor assisted with permanent magnets for pump applications (Doctoral dissertation, KTH).
- [4] Villani M. High performance electrical motors for automotive applications–status and future of motors with low cost permanent magnets. In Proceedings of the 8th International Conference on Magnetism and Metallurgy, Dresden, Germany 2018 Jun (pp. 12-14).
- [5] Ramesh P, Lenin NC. High power density electrical machines for electric vehicles Comprehensive review based on material technology. IEEE Transactions on Magnetics. 2019 Aug 20;55(11):1-21.
- [6] Panda S, Keshri RK. Design and analysis of synchronous reluctance motor for light electric vehicle application. In IECON 2018-44th Annual Conference of the IEEE Industrial Electronics Society 2018 Oct 21 (pp. 2021- 2025). IEEE.

- [7] Villani, Marco, and Monteluco di Roio. "High Performance Electrical Motors for Automotive Applications– Status and Future of Motors with Low Cost Permanent Magnets." In Proceedings of the 8th International Conference on Magnetism and Metallurgy, Dresden, Germany, pp. 12-14. 2018.
- [8] Carraro, M. Morandin, and N. Bianchi, "Optimization of a Traction PMASR Motor According to a given Driving Cycle," IEEE ITEC, 2014, pp. 1–6.
- [9] Xing, Fuzhen, Wenliang Zhao, and Byung-Il Kwon, "Design and Optimisation of a Novel Asymmetric Rotor Structure for a PM-assisted Synchronous Reluctance Machine," IET Electric Power Applications, Vol. 13, Issue 5, 2018, pp. 573-580.
- [10] Barcaro, Massimo, Tomas Pradella, and Ivano Furlan, "Low-torque Ripple Design of a Ferrite-assisted Synchronous Reluctance Motor," IET Electric Power Applications, Vol. 10, Issue 5, 2016, pp. 319-329.
- [11] Ferrari, Marco, et al., "Design of Synchronous Reluctance Motor for Hybrid Electric Vehicles," IEEE Transactions on Industry Applications, Vol. 51, Issue 4, 2015, pp. 3030-3040.
- [12] Bianchi, Nicola, et al., "Electric Vehicle Traction based on Synchronous Reluctance Motors," IEEE Transactions on Industry Applications, Vol. 52, Issue 6, 2016, pp. 4762-4769.
- [13] Pellegrino G, Vagati A, et al., "Performance Comparison between Surface Mounted and Interior PM Motor Drives for Electric Vehicle Application," IEEE Transactions on Industrial Electronics, 2012, Vol. 59, pp. 803- 811.