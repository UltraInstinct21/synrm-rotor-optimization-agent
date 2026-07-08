![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

*Article*

# **Design of a PM-Assisted Synchronous Reluctance Motor with Enhanced Performance and Lower Cost for Household Appliances**

**Yuli Bao \* and Chenyang Xia**

School of Electrical Engineering, China University of Mining and Technology, Xuzhou 221116, China; chyxia@cumt.edu.cn

**\*** Correspondence: yulibao1990@gmail.com

#### **Abstract**

Conventional permanent magnet-assisted synchronous reluctance machine (PMaSynRM) suffers from limited power factor and efficiency. To boost these, the use of sintered rare earth permanent magnets (PMs) is an option, with respect to sintered ferrite, resulting in a high-performance PMaSynRM (HP-PMaSynRM). However, the increasing price of rare earth PM can lead to an overall increase in machine cost. To overcome this issue, a novel HP-PMaSynRM is presented in this paper. Structurally, the proposed four-pole HP-PMaSynRM rotor is characterized by two fluid-shaped flux barriers filled with sintered ferrite, as well as a cut-off region. Based on the finite element analysis (FEA) results, the proposed HP-PMaSynRM exhibits higher performance compared with the conventional HP-PMaSynRM with rare earth PMs. It is shown that the proposed HP-PMaSynRM has higher power factor, efficiency, and better torque quality over a wide range of operating conditions. Moreover, the HP-PMaSynRM presented incurs lower cost. Finally, the proposed HP-PMaSynRM is manufactured, tested, and compared with the conventional benchmark HP-PMaSynRM, proving its advantages, including higher power factor, higher efficiency, lower torque oscillation, and lower cost.

**Keywords:** permanent magnet-assisted synchronous reluctance machine (PMaSynRM); rare earth; ferrite; permanent magnet (PM)

![](_page_0_Picture_10.jpeg)

Academic Editor: Payam Shams Ghahfarokhi

Received: 11 September 2025 Revised: 3 October 2025 Accepted: 14 October 2025 Published: 16 October 2025

**Citation:** Bao, Y.; Xia, C. Design of a PM-Assisted Synchronous Reluctance Motor with Enhanced Performance and Lower Cost for Household Appliances. *Machines* **2025**, *13*, 954. [https://doi.org/10.3390/machines](https://doi.org/10.3390/machines13100954) [13100954](https://doi.org/10.3390/machines13100954)

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(https://creativecommons.org/](https://creativecommons.org/licenses/by/4.0/) [licenses/by/4.0/\)](https://creativecommons.org/licenses/by/4.0/).

# **1. Introduction**

Electrical motors are widely used in various applications such as aerospace, automotive, industry, and household appliances [\[1](#page-16-0)[–4\]](#page-16-1). These motors have different topologies, depending on the corresponding application cases [\[5–](#page-16-2)[9\]](#page-16-3). In household applications, the motor cost is one of the key performance indicators, in addition to the efficiency and torque requirements. Thus, synchronous reluctance motors (SynRMs) have gained increasing interest in this application, thanks to their lower cost and higher efficiency compared with traditional induction motors (IMs) [\[10\]](#page-16-4).

Generally, rotors of SynRMs are characterized by multilayer flux barriers. SynRMs exhibit only reluctance torque owing to the absence of PMs, which limits the power factor, torque density, and efficiency level of the motor [\[11\]](#page-16-5). Various methods have been researched in the literature in order to enhance the anisotropy for better performance of such motor topology [\[12–](#page-16-6)[14\]](#page-16-7). A common solution is to use regular-shaped rectangular sintered PM in the center part of each flux barrier layer. Normally, sintered ferrite PMs are utilized

*Machines* **2025**, *13*, 954 2 of 18

for economic considerations [\[15\]](#page-16-8). In this paper, a PMaSynRM with only regular-shaped rectangular sintered ferrite is referred to as a conventional PMaSynRM.

Conventional PMaSynRMs exhibit higher efficiency and power factor compared with SynRMs since the existence of ferrite PMs not only assists the saturation of the rotor ribs, but also contributes a small amount of torque production [\[16\]](#page-16-9). In [\[17\]](#page-16-10), a number of studies investigating to enhance the performance of conventional PMaSynRM are reviewed in the literature. It is demonstrated that torque ripple can be significantly reduced by adopting an optimal rotor design or skewing techniques [\[18](#page-17-0)[–20\]](#page-17-1). Research in [\[21\]](#page-17-2) indicates that torque ripple resulting from the reluctance can be reduced while maintaining the average torque by designing a rotor with sinusoidal lamination. However, the rotor lamination disparity requires additional manufacturing cost, and the rotor complexity can be an impediment in assembly. Another strategy implemented to minimize the torque ripple is by optimizing the flux barrier angles and insulation ratio [\[22\]](#page-17-3). It is also illustrated that, by combining rotor asymmetry with rotor parameter optimization, torque ripple in conventional PMaSynRM can be limited within a small value [\[23\]](#page-17-4). Apart from the torque ripple, limited power factor and efficiency are also considered as downsides of conventional PMaSynRMs when directly compared with permanent magnet synchronous motors (PMSMs) with rare earth PMs [\[24\]](#page-17-5). In recent literature, some alternative solutions using asymmetrical topologies with the magnet-axis-shift (MAS) effect are proposed in order to maximize the average torque capacity, power factor, and efficiency [\[25\]](#page-17-6). However, the improvement from the MAS effect is limited. The electromagnetic performance of conventional PMaSynRMs is still not competitive against PMSMs owing to the disparity between ferrite and rare earth PMs [\[26\]](#page-17-7). Therefore, in conventional HP-PMaSynRMs, regular-shaped rectangular sintered rare earth PMs (e.g., NdFeB) are partially or completely used instead of only sintered ferrite PMs in conventional PMaSynRMs to satisfy the higher efficiency, power, and torque density demands [\[27\]](#page-17-8). In [\[28\]](#page-17-9), a PMaSynRM with NdFeB bonded magnets in U shape is designed and tested, showing its enhanced power factor and torque capability over traditional SynRM. However, the remanence of the bonded NdFeB is even lower than some sintered ferrites. As a result, it is not a cost-effective method from the electromagnetic point of view.

Conventional HP-PMaSynRMs possess excellent performance since the high remanence and coercivity of the sintered rare earth PMs provide strong rotor field excitation [\[29\]](#page-17-10), whereas their limited availability and harmful environmental impact increase the final motor cost [\[30\]](#page-17-11). This issue is critical in applications that need mass production and strict cost constraints such as household appliances [\[31\]](#page-17-12).

In this paper, a complete rare earth free novel HP-PMaSynRM is proposed aiming to demonstrate that PMaSynRM with only ferrite PMs is possible to have better performance than conventional HP-PMaSynRMs with rare earth PMs in terms of power factor, efficiency, and torque quality. Moreover, the cost advantage of the proposed motor is highlighted. Such HP-PMaSynRM is designed and manufactured with two fluid-shaped flux barriers filled with sintered ferrite PMs and a cut-off region. The proposed HP-PMaSynRM introduces a novelty with respect to the state of the art for this machine class.

This paper is organized as follows: In Section [2,](#page-2-0) the conventional benchmark HP-PMaSynRM (M1) is introduced. In Section [3,](#page-3-0) the proposed novel HP-PMaSynRM (M2) is characterized, and a detailed comparison with M1 is performed via FEA, indicating the advantages of M2 in terms of higher electromagnetic performance including higher average torque capability, lower torque ripple, higher power factor, and higher efficiency over a wide range of operating conditions. Moreover, the cost advantage of M2 is highlighted. A structural FEA of M2 is also carried out in this section in order to ensure the structural

Machines **2025**, 13, 954 3 of 18

robustness of M2. In Section 4, the experimental results are shown to prove the reliability of the FEA analysis. Finally, the conclusion of the paper is presented in Section 5.

#### <span id="page-2-0"></span>2. Reference Conventional HP-PMaSynRM

Figure 1 shows one pole of the conventional three-phase four-pole HP-PMaSynRM motor (M1). A single-layer integral slot distributed winding (ISDW) is used in the stator winding configuration in order to guarantee the highest saliency ratio to exhibit the highest reluctance torque [32].

<span id="page-2-1"></span>![](_page_2_Picture_4.jpeg)

Figure 1. Conventional benchmark HP-PMaSynRM (M1) sketch.

As shown in Figure 1, the rotor of the conventional HP-PMaSynRM is characterized by three flux barrier layers. PMs are inserted in the middle part of each barrier layer mainly to saturate the flux leakage in the q-axis for higher rotor anisotropy and to contribute a portion of magnetic torque. Consequently, the overall torque of the HP-PMaSynRM motor is the sum of both magnetic torque and reluctance torque, as shown in the following Equation (1):

<span id="page-2-2"></span>
$$T_e = \frac{3}{2}p(\lambda_{pm}i_d + (L_d - L_q)i_di_q) \tag{1}$$

where  $T_e$  is the total electromagnetic torque; p is the number of pole pairs;  $\lambda_{pm}$  is the flux linkage of the magnet;  $L_d$  and  $L_q$  are the d-axis and q-axis inductance, respectively; and  $i_d$  and  $i_q$  are the d-axis and q-axis current, respectively.

A sketch of one pole of the M1 rotor is shown in Figure 2 with geometrical identifications. Both the center ribs and the tangential ribs in Figure 2 exist to guarantee the mechanical property of the iron lamination within the maximum operating speed 7200 rpm for the required safety margin. Table 1 reports M1 parameters, including rotor geometry and performance.

<span id="page-2-3"></span>![](_page_2_Picture_10.jpeg)

Figure 2. M1 rotor sketch.

*Machines* **2025**, *13*, 954 4 of 18

<span id="page-3-1"></span>**Table 1.** M1 parameters.

| Rotor Geometry              | Label   | Value  | Unit  |
|-----------------------------|---------|--------|-------|
| Rotor outer diameter        | Dre     | 53.3   | mm    |
| Rotor inner diameter        | Dri     | 12.96  | mm    |
| Pole pairs                  | p       | 2      | -     |
| Radial rib thickness        | Wrad    | 0.45   | mm    |
| Tangential rib thickness    | Wtan    | 0.45   | mm    |
| First layer PM width        | Wpm1    | 5.4    | mm    |
| First layer PM height       | hpm1    | 1.8    | mm    |
| Second layer PM width       | Wpm2    | 10.8   | mm    |
| Second layer PM height      | hpm2    | 2.4    | mm    |
| Third layer PM width        | Wpm3    | 10.8   | mm    |
| Third layer PM height       | hpm3    | 2.4    | mm    |
| Rated Condition Performance | Label   | Value  | Unit  |
| Rated torque                | Tav     | 1.9    | Nm    |
| Rated speed                 | ω       | 5400   | r/min |
| Rated power                 | Pout    | 1074.4 | W     |
| DC-link voltage             | Vdc     | 310    | V     |
| Rated phase current         | Iph     | 3.4    | Arms  |
| Rated phase voltage         | Vph     | 118.6  | Vrms  |
| Power factor                | λ       | 0.925  | -     |
| Copper loss                 | Pcopper | 37.89  | W     |
| Iron loss                   | Piron   | 30.2   | W     |
| Efficiency                  | η       | 94.04  | %     |
| Torque ripple percentage    | Tripple | 14.57  | %     |

## <span id="page-3-0"></span>**3. HP-PMaSynRM with Enhanced Performance**

To further improve the motor performance such as power factor and efficiency, the option is either to increase the magnetic torque component or to enhance the reluctance torque component in Equation [\(1\)](#page-2-2) so that the motor can exhibit higher overall torque. However, the simple additional insertion of N30H would increase the motor cost. Thus, ferrite is introduced to replace the role of the rare earth PM N30H.

In this section, a ferrite-assisted HP-PMaSynRM M2 is presented, and the exact optimal shape of ferrite to produce the best torque capability is investigated. The motor output results are compared with the conventional M1 in the previous section in order to show the unique advantage of the proposed new HP-PMaSynRM.

### *3.1. Motor Characterization*

In general, M2 shares the same stator, winding configuration, stack length, rotor outer and inner diameters, and iron material with M1. The only difference is ferrite Y-40 is inserted in the rotor barrier in M2 instead of using rare earth PM material N30H in M1.

Figure [3](#page-4-0) shows half a pole of the M2 rotor. It is characterized by two fluid-shaped flux barriers filled with ferrite magnets. In addition, the M2 rotor also has a cut-off region at the q-axis.

Ferrite in M2 shares the same magnetic flux direction in q-axis. At each flux barrier end of the rotor, there is a small region with air instead of ferrite, which is highlighted in Figure [3.](#page-4-0) This is mainly for the purpose of avoiding ferrite demagnetization owing to the high saturation level over the tangential rib region. As shown in Figure [4,](#page-4-1) the flux density of the ferrite on the barrier end would be below the demagnetization knee value if the air region highlighted in Figure [3](#page-4-0) is not added. However, as illustrated in Figure [5,](#page-4-2) the flux density of the ferrite on the barrier end would be safely above the demagnetization *Machines* **2025**, *13*, 954 5 of 18

knee value according to Table [2,](#page-4-3) thanks to the air region. A detailed flux density behavior analysis on the ferrite end during a full electrical cycle is recorded in Figure [6,](#page-5-0) showing the minimum value of 0.1789 T, which is above the demagnetization knee value 0.12 T.

<span id="page-4-0"></span>![](_page_4_Picture_2.jpeg)

**Figure 3.** M2 rotor sketch.

<span id="page-4-1"></span>![](_page_4_Picture_4.jpeg)

**Figure 4.** Flux density of the ferrite without air region on barrier end.

<span id="page-4-2"></span>![](_page_4_Picture_6.jpeg)

**Figure 5.** Flux density of the ferrite with air region on barrier end.

<span id="page-4-3"></span>**Table 2.** Ferrite Y-40 property.

| Property Item        | Label | Value  | Unit |
|----------------------|-------|--------|------|
| Coercivity           | Hcb   | 342.4  | kA/m |
| Intrinsic coercivity | Hcj   | 357.26 | kA/m |
| Remanence            | Br    | 0.45   | T    |
| Demagnetization knee | Bmd   | 0.12   | T    |

*Machines* **2025**, *13*, 954 6 of 18

<span id="page-5-0"></span>![](_page_5_Figure_1.jpeg)

**Figure 6.** Minimum flux density on the ferrite end with air region on barrier end case.

The main geometrical parameters considered in Figure [3](#page-4-0) can be summarized below:

- *Dre* and *Dri* are rotor outer and inner diameters;
- *ϑb*<sup>1</sup> and *ϑb*<sup>2</sup> are barrier angles;
- *Wtan* is tangential rib thickness;
- ∆*b*1 and ∆*b*2 are flux barrier end opening angles;
- *Lf errite* and *Liron* are ferrite and iron length in q-axis correspondingly, *Ltotal* is the total length in q-axis, *Lair* is the air length in q-axis;
- *Ccut* is the length from the center of the cut-off region to the rotor center in q-axis and *ϑcut* is the cut-off region angle.

The geometrical dimensions of the M2 rotor in Figure [3](#page-4-0) are summarized in Table [3,](#page-5-1) where the parameters with \* are optimized values through a MOGA-II genetic algorithm optimization via ModeFrontier [\[33\]](#page-17-14). The method has been well established in [\[15\]](#page-16-8). The two objectives are to minimize the torque ripple and to maximize the average torque in order to have the best torque quality. Since PMaSynRM is originally derived from SynRM, it is logical to define a *k f errite* representing the insulation level in the q-axis since ferrite has nearly the same permeability as air [\[34\]](#page-17-15). *k f errite* in Table [3](#page-5-1) is defined in Equation [\(2\)](#page-5-2) as

<span id="page-5-2"></span>
$$k_{ferrite} = \frac{L_{ferrite}}{L_{total}} \tag{2}$$

<span id="page-5-1"></span>

| Table 3. M2 rotor geometrical dimension parameters. |  |  |
|-----------------------------------------------------|--|--|
|-----------------------------------------------------|--|--|

| Rotor Parameters | M2      | Unit   |
|------------------|---------|--------|
| Dre              | 53.3    | mm     |
| Dri              | 12.96   | mm     |
| Wtan             | 0.45    | mm     |
| r                | 1.15    | mm     |
| ϑb1              | 29.1 *  | degree |
| ϑb2              | 42 *    | degree |
| ∆b1              | 1       | degree |
| ∆b2              | 1       | degree |
| k f errite       | 0.42 *  | -      |
| Ccut             | 26.65 * | mm     |
| ϑcut             | 11.15 * | degree |

<sup>\*</sup> Optimized parameters.

As shown in the M2 rotor in Figure [3,](#page-4-0) the edges of the two ferrite filled flux barriers are drawn on the basis of the N. E. Joukowski air potential function [\[35\]](#page-17-16), which is an applied mathematical model to describe 'natural flux'. The method was first proposed in [\[36\]](#page-17-17), indicating that by applying 'natural flux'-shaped barriers, reluctance torque could be produced to the maximum extent. The center of each arc lies on the q-axis due to rotor *Machines* **2025**, *13*, 954 7 of 18

symmetry. Moreover, a cut-off region is introduced in M2. The cut-off curve is modified by a cubic function dominated by two the independent parameters *ϑcut* and *Ccut*. The purpose of setting this cut-off region is to acquire a desired saturation level in the iron region around the cut-off, in which way the motor would produce a minimized torque ripple. The Pareto front solutions of M2 are shown in Figure [7.](#page-6-0) The solutions are all recorded under MTPA (Maximum Torque Per Ampere) mode with the same rated phase current of 3.26 Arms. Among the Pareto front solutions, the final solution is selected, as marked in Figure [7.](#page-6-0)

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Figure 7.** Pareto front from M2 optimization.

Figures [8](#page-6-1) and [9](#page-7-0) elaborate the sensitivity analysis of torque ripple from the cut-off region constant *Ccut* and the cut-off region angle *ϑcut*. As shown in Figure [8,](#page-6-1) the variations of *Ccut* and *ϑcut* give different effects on the torque ripple. Starting from the selected optimized point with *Ccut* 26.6 mm and *ϑcut* 11.15 degrees, further decrease in *Ccut* would increase the torque ripple from the optimized 12.34% to around 18% and further decrease or increase in *ϑcut* would increase the torque ripple. It is worth noticing that the maximum torque ripple over 40% occurs with *Ccut* at around 25.5 mm and *ϑcut* at around 14 degrees, which is over three times larger than the optimized torque ripple value at 12.34%. The influence of *Ccut* and *ϑcut* on average torque is presented in Figure [9.](#page-7-0) It can be seen that the average torque is not as sensitive to *Ccut* and *ϑcut* as torque ripple. Although further decrease in *ϑcut* from the optimized 11.15 degrees to 9 degrees would increase the average torque value from 1.907 Nm to 1.915 Nm, it results in an over 17% torque ripple, which is not preferred. To conclude, the above analysis confirms the importance of selecting suitable cut-off region parameters in order to reduce the torque ripple.

In the next section, the M2 solution is compared and analyzed in detail with respect to the reference M1 regarding average torque, torque ripple, efficiency, etc.

<span id="page-6-1"></span>![](_page_6_Figure_6.jpeg)

**Figure 8.** M2 Torque ripple percentage as a function of *ϑcut* and *Ccut*.

*Machines* **2025**, *13*, 954 8 of 18

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

**Figure 9.** M2 Average torque as a function of *ϑcut* and *Ccut*.

#### *3.2. M1 and M2 Performance and Cost Comparison*

In this section, M1 and M2 mentioned in the previous sections are selected for comparison. Both motors are simulated under the same phase current at 3.26 Arms by means of FE software MagNet (version 2019.1.0.33). The torque results under MTPA mode are shown in Figure [10.](#page-7-1) It can be noted that M2 with the insertion of ferrite in a particular flux barrier shape can contribute more average torque compared with M1 with rare earth PM.

<span id="page-7-1"></span>![](_page_7_Figure_5.jpeg)

**Figure 10.** Torque comparison of M1 and M2 under 3.26 Arms current loading in MTPA mode.

The exact torque component values are reported in Table [4.](#page-8-0) As shown in Table [4,](#page-8-0) the magnetic torque component is increased by 13.15% in M2 compared with M1. Even though the reluctance torque component is decreased very little by 0.56% in M2, the total average torque is improved from 1.815 Nm in M1 by 5.07% to 1.907 Nm in M2, thanks to the increase in the magnetic torque component. It is interesting to notice that both reluctance torque and magnetic torque contribute in relatively the same order of magnitude in M1 and M2.

It has been clearly shown in Figure [10](#page-7-1) and Table [4](#page-8-0) that M2 with ferrite in fluid barrier shape can produce more average torque due to the additional magnetic torque component. Therefore, it is necessary to conclude the exact motor performance of the two motors at a rated condition considering other evaluations such as efficiency and power factor. The performance results of M1 and M2 at a rated condition are summarized in Table [5,](#page-8-1) and rotor material cost results are listed in Table [6.](#page-8-2) It can be noticed from Table [5](#page-8-1) that iron loss in M1 and M2 has insignificant difference, and the total loss is mainly determined by the copper loss. To summarize, it is clearly indicated that M2 presents the following benefits:

• The phase current is reduced by about 4.12% in M2 compared with 3.4 Arms in M1.

*Machines* **2025**, *13*, 954 9 of 18

• The power factor is improved from the original 0.925 in M1 to 0.944 in M2. The increase is about 2.05%.

- Copper loss in M2 is reduced compared with M1, thanks to the lower current, which contributes to the eventual efficiency improvement from 94.04% in M1, by 0.23% to 94.27% in M2.
- M2 has the lower torque pulsation of 12.34% compared with 14.57% in M1.
- The PM cost of M2 is reduced to only 35.6% of M1, thanks to the remarkably cheaper price of ferrite Y-40 compared with rare earth PM N30H. Meanwhile, rotor iron cost is decreased by about 14.7% in M2. Generally, the rotor material cost of M2 is reduced by 59.6% compared with M1, which is an obvious price advantage.

<span id="page-8-0"></span>**Table 4.** Torque component data under phase current at 3.26 Arms in MTPA.

| Torque                       | M1    | M2     | Unit |
|------------------------------|-------|--------|------|
| Total average torque         | 1.815 | 1.907  | Nm   |
| Improvement                  | -     | +5.07  | %    |
| Reluctance torque            | 1.07  | 1.064  | Nm   |
| Improvement                  | -     | −0.56  | %    |
| Magnetic torque              | 0.745 | 0.843  | Nm   |
| Improvement                  | -     | +13.15 | %    |
| Reluctance torque proportion | 58.95 | 55.79  | %    |
| Magnetic torque proportion   | 41.05 | 44.21  | %    |

<span id="page-8-1"></span>**Table 5.** Motor performance comparison at rated condition.

| Rated Condition          | Label   | M1     | M2     | Unit |
|--------------------------|---------|--------|--------|------|
| Average torque           | Tav     | 1.9    | 1.9    | Nm   |
| Speed                    | ω       | 5400   | 5400   | rpm  |
| Power                    | Pout    | 1074.4 | 1074.4 | W    |
| Torque ripple percentage | Tripple | 14.57  | 12.34  | %    |
| MTPA phase current       | Iph     | 3.4    | 3.26   | Arms |
| Current reduction        | -       | -      | 4.12   | %    |
| Power factor             | λ       | 0.925  | 0.944  | -    |
| Power factor increase    | -       | -      | 2.05   | %    |
| Copper loss              | Pcopper | 37.89  | 35.01  | W    |
| Iron loss                | Piron   | 30.2   | 30.6   | W    |
| Efficiency               | η       | 94.04  | 94.27  | %    |
| Efficiency increase      | -       | -      | 0.23   | %    |

<span id="page-8-2"></span>**Table 6.** Rotor cost comparison.

| Rotor Material Cost           | M1       | M2       | Unit    |
|-------------------------------|----------|----------|---------|
| PM volume                     | 16,044   | 54,607   | mm3     |
| PM material                   | N30H     | Y-40     | -       |
| PM unit price 1               | 68.5     | 10.96    | US\$/kg |
| PM cost                       | 8.24     | 2.93     | US\$    |
| Rotor iron volume             | 93,925   | 80,275   | mm3     |
| Rotor iron material           | M235-35A | M235-35A | -       |
| Rotor iron cost               | 0.88     | 0.75     | US\$    |
| Rotor material cost           | 9.12     | 3.68     | US\$    |
| Rotor material cost reduction | -        | 59.6     | %       |

<sup>1</sup> Based on the quotes from manufacturers in 2022.

*Machines* **2025**, *13*, 954 10 of 18

Under a rated condition, M2 exhibits lower torque ripple at 12.34% compared with 14.57% in M1, as reported in Table [5.](#page-8-1) The instantaneous torque of the two motors over one electrical period is included in Figure [11,](#page-9-0) which clearly indicates the instantaneous torque differences. This is because M2 has generally lower torque ripple harmonic amplitudes compared with M1. As shown in Figure [12,](#page-9-1) the amplitude of the 6th harmonic order in M2 is only around 63% of that in M1. Compared with M1, M2 also has obviously smaller 12th and 18th harmonic order values. In general, M2 exhibits lower torque ripple harmonic order values compared with M1 apart from the 24th and 36th.

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

**Figure 11.** Torque comparison of M1 and M2 under rated condition in MTPA mode.

<span id="page-9-1"></span>![](_page_9_Figure_4.jpeg)

**Figure 12.** Torque ripple harmonics comparison of M1 and M2 under rated condition in MTPA mode.

To conclude, M2 exhibits higher efficiency, higher power factor, and lower torque ripple and costs less compared with M1. It is proved that the HP-PMaSynRM with fluidshaped ferrite PMs could be provided with higher performance and lower price compared with traditional HP-PMaSynRM with rectangular-shaped rare earth PMs. As a result, the following part is to include a deeper comparison study between M2 and M1 to verify the efficiency and power factor advantages of M2 regarding a wide operating speed range.

Figures [13](#page-10-0) and [14](#page-10-1) report the efficiency and power factor of M1 and M2 over the speed range from 100 rpm to rated 5400 rpm and torque range from 0.5 Nm to 2 Nm (rated 1.9 Nm included). As shown in Figure [13,](#page-10-0) M2 is provided with higher efficiency at every operating point within the scope. In M1, the highest efficiency is limited to below 94.2%, whereas in M2, the highest efficiency can reach over 94.4%. Moreover, M2 is provided with an obvious wider range of efficiency over 94% compared with M1. In Figure [14,](#page-10-1) it can be evidently indicated that M2 exhibits a higher power factor. Within the speed and torque range, the power factor in M2 is over 0.94 and can reach over 0.99 at torque load conditions below 1 Nm. However, in M1, the power factor is only 0.925 at a rated condition. Moreover, a *Machines* **2025**, *13*, 954 11 of 18

power factor over 0.96 occupies almost a 75% region in M2, whereas it is only around 50% in M1.

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Figure 13.** Efficiency map comparison between M1 and M2 from 100 rpm to rated speed.

<span id="page-10-1"></span>![](_page_10_Figure_4.jpeg)

**Figure 14.** Power factor map comparison between M1 and M2 from 100 rpm to rated speed.

Table [7](#page-10-2) reports the detailed values of efficiency and power factor on the marked operating point to show the obvious advantage of M2. As reported in Table [7,](#page-10-2) the efficiency and power factor of M2 are apparently higher at the six chosen operating points. The data of the rated operating point is also included in Table [7,](#page-10-2) which is also reported specifically in Table [5.](#page-8-1)

| Operating Point | Speed (rpm) | Average Torque (Nm) |  |  |
|-----------------|-------------|---------------------|--|--|

|                                |                     |     | Efficiency (%) |          |       | Power Factor (-) |          |       |
|--------------------------------|---------------------|-----|----------------|----------|-------|------------------|----------|-------|
| Operating Point<br>Speed (rpm) | Average Torque (Nm) | M1  | M2             | Increase | M1    | M2               | Increase |       |
| 1                              | 1200                | 1.0 | 88.38          | 88.71    | +0.33 | 0.971            | 0.991    | +0.02 |
| 2                              | 1800                | 1.2 | 90.65          | 91.07    | +0.42 | 0.955            | 0.981    | +0.03 |
| 3                              | 2400                | 1.4 | 91.80          | 92.27    | +0.47 | 0.940            | 0.970    | +0.03 |
| 4                              | 3600                | 1.5 | 93.25          | 93.66    | +0.41 | 0.931            | 0.964    | +0.03 |
| 5                              | 4200                | 1.8 | 93.49          | 93.86    | +0.37 | 0.928            | 0.950    | +0.02 |

6 (rated) 5400 1.9 94.04 94.27 +0.23 0.925 0.944 +0.02

<span id="page-10-2"></span>**Table 7.** Efficiency and power factor comparison between M1 and M2.

*Machines* **2025**, *13*, 954 12 of 18

#### *3.3. Structural Analysis*

A structural FEA is performed for M2 via ANSYS software 2024R2 in order to ensure the rotor mechanical integrity against centrifugal force at the designed 7200 rpm maximum rotating speed. The analysis is carried out by simulating one rotor pole to save computing time cost, thanks to the symmetry.

Table [8](#page-11-1) reports the mechanical properties that are fully considered in the mechanical simulation. All contact regions between the iron and ferrite are set as frictional, meaning that sliding and separation are taken into account in order to simulate the worst circumstances when the bondings lose effectiveness. The results at the 7200 rpm maximum rotor speed are presented in Figure [15.](#page-11-2) As shown in Figure [15,](#page-11-2) the maximum von Mises stress lies in the tangential rib region of the second-layer barrier end. The maximum von Mises stress value is around 92 Mpa, and it is purely safe compared with the 460 Mpa tensile strength capability included in Table [8;](#page-11-1) moreover, the maximum deformation at 7200 rpm is only 1.6 µm.

<span id="page-11-1"></span>**Table 8.** Rotor material properties.

| Property         | M235-35A | Y-40 | Unit  |  |
|------------------|----------|------|-------|--|
| Mass density     | 7600     | 4900 | kg/m3 |  |
| Young's modulus  | 185      | 180  | GPa   |  |
| Poisson's ratio  | 0.3      | 0.28 | -     |  |
| Tensile Strength | 460      | 35   | MPa   |  |

<span id="page-11-2"></span>![](_page_11_Figure_6.jpeg)

**Figure 15.** Equivalent (von Mises) stress and deformation analysis of M2 rotor at 7200 rpm maximum speed.

#### <span id="page-11-0"></span>**4. Experimental Validation**

In order to verify the FEA results of the proposed M2 and traditional M1, M1 and M2 have been manufactured and tested. The experimental measurements are collected from the platform shown in Figure [16.](#page-12-0) The test machine is coupled with a SUGAWARA rig. SUGAWARA is a precise dynamometer with a speed capability of 100–25,000 rpm and a torque capability of 0.06–2 Nm. The torque resolution of SUGAWARA can reach 0.001 Nm. The test motor is driven by a cheap STM32-based controller for economic consideration. Prototypes of M1 and M2 are shown in Figure [17.](#page-12-1)

Results of the six operating points in Table [7](#page-10-2) have been tested regarding both M1 and M2, including the actual speed, average torque, phase current, output power, power factor, and efficiency, as highlighted in Table [9.](#page-12-2) The experimental results regarding the power factor and efficiency show a good agreement with the ones from FEA in Table [7](#page-10-2) for both M1 and M2. It can be easily noticed that M2 exhibits reduced current with the same torque requirement. Considering the rated operating point 6 (5400 rpm, 1.9 Nm), the phase current

*Machines* **2025**, *13*, 954 13 of 18

in M2 is 3.357 Arms, which is 4.1% smaller than 3.498 Arms in M1. Additionally, the power factor and efficiency test results of M2 show an obvious advantage compared with M1.

<span id="page-12-0"></span>![](_page_12_Picture_2.jpeg)

**Figure 16.** SUGAWARA rig for motor performance testing.

<span id="page-12-1"></span>![](_page_12_Picture_4.jpeg)

**Figure 17.** M1 rotor lamination with N30H (**a**), M2 rotor lamination with Y-40 (**b**), and M1 and M2 stator lamination (**c**).

| Operating Point | Motor | Speed<br>(rpm) | Average Torque<br>(Nm) | Phase Current<br>(Arms) | Output Power<br>(W) | Power Factor<br>(-) | Efficiency<br>(%) |
|-----------------|-------|----------------|------------------------|-------------------------|---------------------|---------------------|-------------------|
| 1               | M1    | 1199           | 1.001                  | 2.096                   | 125.659             | 0.952               | 87.0              |
|                 | M2    | 1199           | 0.998                  | 2.071                   | 125.256             | 0.981               | 87.64             |
| 2               | M1    | 1799           | 1.200                  | 2.396                   | 226.050             | 0.931               | 90.15             |
|                 | M2    | 1798           | 1.200                  | 2.333                   | 225.842             | 0.991               | 90.62             |
| 3               | M1    | 2401           | 1.400                  | 2.748                   | 351.955             | 0.921               | 91.32             |
|                 | M2    | 2401           | 1.402                  | 2.658                   | 352.384             | 0.975               | 91.72             |
| 4               | M1    | 3601           | 1.500                  | 2.839                   | 565.568             | 0.919               | 92.98             |
|                 | M2    | 3601           | 1.500                  | 2.717                   | 565.521             | 0.967               | 93.48             |
| 5               | M1    | 4200           | 1.800                  | 3.301                   | 791.857             | 0.911               | 93.19             |
|                 | M2    | 4200           | 1.802                  | 3.174                   | 792.519             | 0.952               | 93.48             |
| 6 (rated)       | M1    | 5401           | 1.902                  | 3.498                   | 1075.925            | 0.915               | 93.48             |
|                 | M2    | 5401           | 1.905                  | 3.357                   | 1077.751            | 0.939               | 93.85             |

<span id="page-12-2"></span>**Table 9.** Experimental results comparison between M1 and M2.

Figures [18](#page-13-0) and [19](#page-13-1) present the efficiency and power factor maps comparisons of M1 between experimental and FEA results. It can be seen that the experimental results align closely with the FEA results in both efficiency and power factor cases. Even though the efficiency of M1 could not reach 94% experimentally within the tested speed and torque range as shown in Figure [18,](#page-13-0) the difference is minor. At a rated condition, M1's efficiency is 93.48%, which is only 0.56% lower than the FEA value of 94.04%. The experimental power factor values of M1 are slightly lower than the FEA ones, as shown in Figure [19,](#page-13-1) with a difference of less than 0.02, which is acceptable. Similarly, Figures [20](#page-13-2) and [21](#page-14-0) show that the efficiency and power factor maps of M2 also agree well between experimental and FEA Machines 2025, 13, 954 14 of 18

results. Moreover, it is evident that M2 performs better than M1 in terms of both efficiency and power factor at a wide range of operating conditions experimentally by comparing Figure 20 with Figure 18 and Figure 21 with Figure 19 correspondingly.

<span id="page-13-0"></span>![](_page_13_Figure_2.jpeg)

Figure 18. M1 efficiency maps comparison between experimental and FEA results.

<span id="page-13-1"></span>![](_page_13_Figure_4.jpeg)

Figure 19. M1 power factor maps comparison between experimental and FEA results.

<span id="page-13-2"></span>![](_page_13_Figure_6.jpeg)

Figure 20. M2 efficiency maps comparison between experimental and FEA results.

*Machines* **2025**, *13*, 954 15 of 18

<span id="page-14-0"></span>![](_page_14_Figure_1.jpeg)

**Figure 21.** M2 power factor maps comparison between experimental and FEA results.

The torque ripple validation is characterized on a test rig presented in Figure [22.](#page-14-1) The tested M1 and M2 are performed at a very low speed of 10 rpm/min so that the nature of torque oscillations can be captured. As shown in Figure [22,](#page-14-1) the tested motor is connected through a torque transducer to a master commercial servo motor. An irreversible gear box with a 1:50 ratio is coupled between the master motor and the torque transducer in order to reduce the actual speed on the tested motor side. The control of the tested motor is driven by a STM32-based controller, which has already been shown in Figure [16.](#page-12-0) Current values of M1 and M2 are controlled under the rated condition referring to Table [5.](#page-8-1) The torque ripple results of both M1 and M2 have been collected and are shown in Figures [23](#page-15-1) and [24](#page-15-2) correspondingly.

<span id="page-14-1"></span>![](_page_14_Picture_4.jpeg)

**Figure 22.** Test rig for torque ripple measurements.

It can be observed that the torque ripple waveform from FEA matches quite well with the experimental results. As shown in Figure [23,](#page-15-1) the M1 measured torque ripple is 15.25% with an average torque of 1.855 Nm, whereas the FEA simulation gives a 14.57% torque ripple with an average torque of 1.9 Nm. The difference in average torque is around 2.4%, and the difference value in torque ripple is only 0.68%. As shown in Figure [24,](#page-15-2) the measured torque ripple of M2 is 13.1% with an average torque of 1.856 Nm, and it is 12.34% and 1.9 Nm in FEA simulation. The difference in average torque is around 2.3%, and the

*Machines* **2025**, *13*, 954 16 of 18

difference value in torque ripple is only 0.76%. Moreover, it is obvious that the oscillation trends of the FEA and experimental results are quite similar in both M1 and M2 cases.

Based on the results presented in this section, it is proved that the FEA simulation results predict the performance of M1 and M2 quite accurately.

<span id="page-15-1"></span>![](_page_15_Figure_3.jpeg)

**Figure 23.** M1 torque ripple comparison between experimental and FEA results under 3.4 Arms phase current and an MTPA current angle of 47 electrical degrees.

<span id="page-15-2"></span>![](_page_15_Figure_5.jpeg)

**Figure 24.** M2 torque ripple comparison between experimental and FEA results under 3.26 Arms phase current and an MTPA current angle of 44 electrical degrees.

# <span id="page-15-0"></span>**5. Conclusions**

This paper has proposed a complete rare earth free novel HP-PMaSynRM (M2). The proposed M2 is characterized by two fluid-shaped flux barriers filled with sintered ferrite PMs and one cut-off region. A comprehensive comparison between M2 and the benchmark conventional HP-PMaSynRM with rare earth PMs (M1) on torque, power factor, and efficiency via FEA is made, indicating that M2, even with only ferrite PMs and without rare earth PMs, can exhibit 5.07% higher average torque capability at the same current of 3.26 Arms and reduce torque ripple value by 15.3% at a rated condition. M2 can provide a 2% higher power factor and a 0.23% increase in efficiency at a rated condition. Moreover, the power factor and efficiency advantages of M2 exist within a wide speed operating range. Apart from the electromagnetic advantages, the cost of the M2 rotor is 59.6% lower than that of the M1 rotor, thanks to the significantly cheaper price of ferrite Y40 (10.96 USD/kg) compared with rare earth PM N30H (68.5 USD/kg).

The experimental results of M1 and M2 match the ones from FEA, including average torque, power factor, efficiency, and torque ripple, which validates the reliability of the FEA results. It is proved that the proposed rare earth free HP-PMaSynRM, with only ferrite PMs, *Machines* **2025**, *13*, 954 17 of 18

can be designed to be better than rare earth HP-PMaSynRM, enabling better performance at lower cost.

**Author Contributions:** Conceptualization, Y.B.; methodology, Y.B.; formal analysis, Y.B.; investigation, Y.B.; resources, Y.B. and C.X.; writing—original draft preparation, Y.B.; writing—review and editing, Y.B. and C.X.; supervision, C.X. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was funded by China University of Mining and Technology, Xuzhou.

**Data Availability Statement:** The original contributions presented in this study are included in the article. Further inquiries can be directed to the corresponding author.

**Conflicts of Interest:** The authors declare no conflicts of interest.

#### **References**

- <span id="page-16-0"></span>1. Ma, K.; Sun, Y.; Gao, Y.; Tang, X.; Jiang, X. Design and Optimization of High-Speed Five-Phase Fault-Tolerant Permanent Magnet Motor for Aerospace Applications. In Proceedings of the 26th International Conference on Electrical Machines and Systems (ICEMS), Zhuhai, China, 5–8 November 2023; pp. 253–257.
- 2. Nasiri-Zarandi, R.; Karami-Shahnani, A.; Toulabi, M.S.; Tessarolo, A. Design and Experimental Performance Assessment of an Outer Rotor PM-Assisted SynRM for the Electric Bike Propulsion. *IEEE Trans. Transp. Electrif.* **2023**, *9*, 727–736. [\[CrossRef\]](http://doi.org/10.1109/TTE.2022.3202819)
- 3. Karthika, N.; Manogna, R.; Ravali, R.; Niharika, S. IoT-Based Speed Sensing and Fault Monitoring of Induction Motor Using GSM Technique for Industrial Application. *Int. J. Recent Dev. Sci. Technol.* **2024**, *8*, 187–191.
- <span id="page-16-1"></span>4. Mirzaei, A.; Rad, N.A.; Torkaman, H.; Zarghani, A. Comparison Study and Performance Enhancement of Induction Motor Using Optimized SynRM for Household Applications. In Proceedings of the 3rd International Conference on Electrical Machines and Drives (ICEMD), Tehran, Iran, 20–21 December 2023; pp. 1–5.
- <span id="page-16-2"></span>5. Pellegrino, G.; Vagati, A.; Guglielmi, P.; Boazzo, B. Performance Comparison Between Surface-Mounted and Interior PM Motor Drives for Electric Vehicle Application. *IEEE Trans. Ind. Electron.* **2012**, *59*, 803–811. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2011.2151825)
- 6. Cao, R.; Lu, M.; Jiang, N.; Cheng, M. Comparison Between Linear Induction Motor and Linear Flux-Switching Permanent-Magnet Motor for Railway Transportation. *IEEE Trans. Ind. Electron.* **2019**, *66*, 9394–9405. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2019.2892676)
- 7. Guglielmi, P.; Pastorelli, M.; Carrer, A.; Beato, A.; D'Antonio, D.; Fagnano, L. An IPM-PMASR Motor for Home Appliance Washing Machines. In Proceedings of the IECON 2013–39th Annual Conference of the IEEE Industrial Electronics Society, Vienna, Austria, 10–13 November 2013; pp. 2608–2613.
- 8. Kakosimos, P.E.; Sarigiannidis, A.G.; Beniakar, M.E.; Kladas, A.G.; Gerada, C. Induction Motors Versus Permanent-Magnet Actuators for Aerospace Applications. *IEEE Trans. Ind. Electron.* **2014**, *61*, 4315–4325. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2013.2274425)
- <span id="page-16-3"></span>9. Sakunthala, S.; Kiranmayi, R.; Mandadi, P.N. A Study on Industrial Motor Drives: Comparison and Applications of PMSM and BLDC Motor Drives. In Proceedings of the 2017 International Conference on Energy, Communication, Data Analytics and Soft Computing (ICECDS), Chennai, India, 1–2 August 2017; pp. 537–540.
- <span id="page-16-4"></span>10. de Almeida, A.T.; Ferreira, F.J.T.E.; Baoming, G. Beyond Induction Motors–Technology Trends to Move Up Efficiency. *IEEE Trans. Ind. Appl.* **2014**, *50*, 2103–2114. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2013.2288425)
- <span id="page-16-5"></span>11. Degano, M. Analysis, Design and Optimization of Innovative Electrical Machines Using Analytical and Finite Element Analysis Methods. Ph.D. Thesis, University of Padova, Padova, Italy, 2014.
- <span id="page-16-6"></span>12. Bao, Y.; Degano, M.; Wang, S.; Chuan, L.; Zhang, H.; Xu, Z.; Gerada, C. A Novel Concept of Ribless Synchronous Reluctance Motor for Enhanced Torque Capability. *IEEE Trans. Ind. Electron.* **2020**, *67*, 2553–2563. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2019.2914616)
- 13. Donaghy-Spargo, C.M. Electromagnetic Mechanical Design of Synchronous Reluctance Rotors with Fine Features. *IEEE Trans. Magn.* **2017**, *53*, 8206308. [\[CrossRef\]](http://dx.doi.org/10.1109/tmag.2017.2700892)
- <span id="page-16-7"></span>14. Babetto, C.; Bacco, G.; Bianchi, N. Synchronous Reluctance Machine Optimization for High Speed Applications. *IEEE Trans. Energy Convers.* **2018**, *33*, 1266–1273. [\[CrossRef\]](http://dx.doi.org/10.1109/TEC.2018.2800536)
- <span id="page-16-8"></span>15. Degano, M.; Carraro, E.; Bianchi, N. Selection Criteria and Robust Optimization of a Traction PM-Assisted Synchronous Reluctance Motor. *IEEE Trans. Ind. Appl.* **2015**, *51*, 4383–4391. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2015.2443091)
- <span id="page-16-9"></span>16. Ge, L.; Zhu, X.; Wu, W.; Liu, F.; Xiang, Z. Design and Comparison of Two Non-Rare-Earth Permanent Magnet Synchronous Reluctance Motors for EV Applications. In Proceedings of the 20th International Conference on Electrical Machines and Systems (ICEMS), Sydney, Australia, 11–14 August 2017; pp. 1–5.
- <span id="page-16-10"></span>17. Tawfiq, K.B.; Ibrahim, M.N.; El-Kholy, E.E.; Sergeant, P. Performance Improvement of Synchronous Reluctance Machines—A Review Research. *IEEE Trans. Magn.* **2021**, *57*, 8107811. [\[CrossRef\]](http://dx.doi.org/10.1109/tmag.2021.3108634)

*Machines* **2025**, *13*, 954 18 of 18

<span id="page-17-0"></span>18. Bianchi, N.; Degano, M.; Fornasiero, E. Sensitivity Analysis of Torque Ripple Reduction of Synchronous Reluctance and Interior PM Motors. *IEEE Trans. Ind. Appl.* **2015**, *51*, 187–195. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2014.2327143)

- 19. Vagati, A.; Pastorelli, M.; Franceschini, G.; Petrache, S.C. Design of Low-Torque-Ripple Synchronous Reluctance Motors. *IEEE Trans. Ind. Appl.* **1998**, *34*, 758–765. [\[CrossRef\]](http://dx.doi.org/10.1109/28.703969)
- <span id="page-17-1"></span>20. Gallardo, C.; Madariaga, C.; Tapia, J.A.; Degano, M. Impact of Rotor Step Skew on the Performance of Synchronous Reluctance Machines. In Proceedings of the 2023 IEEE CHILECON, Valdivia, Chile, 5–7 December 2023; pp. 1–5.
- <span id="page-17-2"></span>21. Muteba, M.; Twala, B.; Nicolae, D.V. Torque Ripple Minimization in Synchronous Reluctance Motor Using a Sinusoidal Rotor Lamination Shape. In Proceedings of the 2016 XXII International Conference on Electrical Machines (ICEM), Lausanne, Switzerland, 4–7 September 2016; pp. 606–611.
- <span id="page-17-3"></span>22. Degano, M.; Murataliyev, M.; Shuo, W.; Barater, D.; Buticchi, G.; Jara, W.; Bianchi, N.; Galea, M.; Gerada, C. Optimised Design of Permanent Magnet Assisted Synchronous Reluctance Machines for Household Appliances. *IEEE Trans. Energy Convers.* **2021**, *36*, 3084–3095. [\[CrossRef\]](http://dx.doi.org/10.1109/TEC.2021.3076675)
- <span id="page-17-4"></span>23. Bianchi, N.; Bolognani, S.; Bon, D.; Dai Pre, M. Rotor Flux-Barrier Design for Torque Ripple Reduction in Synchronous Reluctance and PM-Assisted Synchronous Reluctance Motors. *IEEE Trans. Ind. Appl.* **2009**, *45*, 921–928. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2009.2018960)
- <span id="page-17-5"></span>24. Carraro, E.; Degano, M.; Morandin, M.; Bianchi, N. PM Synchronous Machine Comparison for Light Electric Vehicles. In Proceedings of the 2014 IEEE International Electric Vehicle Conference (IEVC), Florence, Italy, 17–19 December 2014; pp. 1–8.
- <span id="page-17-6"></span>25. Zhao, W.; Chen, D.; Lipo, T.A.; Kwon, B.-I. Performance Improvement of Ferrite-Assisted Synchronous Reluctance Machines Using Asymmetrical Rotor Configurations. *IEEE Trans. Magn.* **2015**, *51*, 8108504. [\[CrossRef\]](http://dx.doi.org/10.1109/TMAG.2015.2436414)
- <span id="page-17-7"></span>26. Al-Ani, M.; Walker, A.; Vakil, G.; Gerada, D.; Gerada, C.; Paciura, K. Modifications to PM-Assisted Synchronous Reluctance Machine to Achieve Rare-Earth-Free Heavy-Duty Traction. *IEEE J. Emerg. Sel. Top. Power Electron.* **2023**, *11*, 2029–2038. [\[CrossRef\]](http://dx.doi.org/10.1109/JESTPE.2022.3203184)
- <span id="page-17-8"></span>27. Du, Z.S.; Lipo, T.A. Cost-Effective High Torque Density Bi-Magnet Machines Utilizing Rare Earth and Ferrite Permanent Magnets. *IEEE Trans. Energy Convers.* **2020**, *35*, 1577–1584. [\[CrossRef\]](http://dx.doi.org/10.1109/TEC.2020.2978256)
- <span id="page-17-9"></span>28. Poskovic, E.; Babetto, C.; Bianchi, N.; Ferraris, L. Bonded Magnets in PM-Assisted Synchronous Reluctance Machines: Performance Dependence on the Production Technology. In Proceedings of the 2019 IEEE International Electric Machines & Drives Conference (IEMDC), San Diego, CA, USA, 12–15 May 2019; pp. 442–448.
- <span id="page-17-10"></span>29. Poskovic, E.; Ferraris, L.; Bianchi, N.; Franchini, F. Study of the Adoption of Different Bonded Magnets in Assisted Reluctance Machines. In Proceedings of the 2020 International Conference on Electrical Machines (ICEM), Gothenburg, Sweden, 23–26 August 2020; pp. 1676–1682.
- <span id="page-17-11"></span>30. Krishnan, R. *Permanent Magnet Synchronous and Brushless DC Motor Drives*; CRC Press: Boca Raton, FL, USA, 2017.
- <span id="page-17-12"></span>31. Boldea, I.; Tutelea, L.N.; Parsa, L.; Dorrell, D. Automotive Electric Propulsion Systems with Reduced or No Permanent Magnets: An Overview. *IEEE Trans. Ind. Electron.* **2014**, *61*, 5696–5711. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2014.2301754)
- <span id="page-17-13"></span>32. Tangudu, J.K.; Jahns, T.M. Comparison of Interior PM Machines with Concentrated and Distributed Stator Windings for Traction Applications. In Proceedings of the 2011 IEEE Vehicle Power and Propulsion Conference (VPPC), Chicago, IL, USA, 6–9 September 2011; pp. 1–8.
- <span id="page-17-14"></span>33. Poles, S. *MOGA-II: An Improved Multi-Objective Genetic Algorithm*; Technical Report 2003-006; Esteco: Trieste, Italy, 2003.
- <span id="page-17-15"></span>34. Degano, M.; Di Nardo, M.; Galea, M.; Gerada, C.; Gerada, D. Global Design Optimization Strategy of a Synchronous Reluctance Machine for Light Electric Vehicles. In Proceedings of the 8th IET International Conference on Power Electronics, Machines and Drives (PEMD 2016), Glasgow, UK, 19–21 April 2016; pp. 1–5.
- <span id="page-17-16"></span>35. Mathews, J.H.; Howell, R.W. *Complex Analysis for Mathematics and Engineering*, 4th ed.; Jones and Bartlett Publishers: Sudbury, MA, USA, 2001; ISBN 0-7637-1425-9.
- <span id="page-17-17"></span>36. Rajabi Moghaddam, R. Synchronous Reluctance Machine (SynRM) in Variable Speed Drives (VSD) Applications. Ph.D. Thesis, KTH Royal Institute of Technology, Stockholm, Sweden, 2011.

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.