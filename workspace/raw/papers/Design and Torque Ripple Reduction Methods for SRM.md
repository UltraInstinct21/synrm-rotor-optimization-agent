# Design and Torque Ripple Reduction Methods for Synchronous Reluctance Machine applied in Electric Power Take-off actuation

Branko Ban, Andreas Andersson, and Stjepan Stipetic,´ *Senior member, IEEE*

*Abstract*—A synchronous reluctance machine has been selected and optimized for commercial vehicle power take-off application. The meta-modeling optimization process has been covered in detail. To reduce execution time, skewing has not been included in the optimization workflow. The penalty is elevated torque ripple of unskewed design (13.9%), which has been mitigated in the post-optimization process with the use of asymmetric rotor poles (7.5%), equal length segment skewing (6.2%), variable-length segment skewing (4.2%), and continuous rotor skewing (2.8%). Due to the increased production cost mostly related to winding insertion, stator skewing has not been considered as an option. A detailed comparative study has been conducted to illustrate the benefits and drawbacks of each rotor skewing alternative. The novel contribution presented in the paper is a new variable-length rotor segment skewing. This solution merges the qualities of continuous skewing (minimal torque ripple) and segmented skewing (reduced production cost).

*Index Terms*—synchronous reluctance; optimization; torque ripple.

## I. INTRODUCTION

D ue to green transition agenda, commercial vehicle manufacturers are investing considerable efforts in electric vehicle (EV) production. Examples of commercial vehicles suitable for electrification are multi-purpose vehicles (eMPV) are refuse, hook loader, or vacuum trucks [1]. Apart from vehicle traction eMPV must actuate additional body systems (usually through some type of hydraulic pump). The actuation is commonly done by a diesel engine or a gearbox-mounted output shaft referred to as power take-off (PTO, Fig. 1a). In the case of electric trucks, the additional, chassis-mounted electric machine (ePTO) can be the interface to the external attachments (Fig. 1b).

The proposed ePTO actuator machine is a synchronous reluctance machine (SyRM) [1], [2]. SyRM relies on high reluctance torque, thus theoretically needing no PM material in the rotor structure (Fig. 2).

They have relatively low material costs, higher overload capacity (no demagnetization issues), low rotor losses and are considered to be robust [3]–[5]. On the other hand, the lack

Branko Ban and Stjepan Stipetic are affiliated with the University of ´ Zagreb, Faculty of electrical engineering and computing (FER), Department of Electric Machines, Drives and Automation (e-mail: branko.ban@fer.hr, stjepan.stipetic@fer.hr). Additionally, Branko Ban is affiliated with Torquery Consulting. Andreas Andersson is affiliated with China Euro Vehicle Technology (CEVT), (e-mail: andreas.andersson@cevt.se). This work was partially supported by China Euro Vehicle Technology (CEVT).

![](_page_0_Picture_10.jpeg)

Fig. 1: a) Diesel engine PTO shaft with mounted hydraulic pump; b) ePTO powering hydraulic pump

![](_page_0_Figure_12.jpeg)

Fig. 2: SyRM rotor nomenclature

of a permanent magnetic field in the rotor is penalized with reduced torque density and power factor, and higher torque ripple if no skewing is applied [6], [7].

Most vehicle manufacturers have a strategy of reusing components whenever possible. The presumption is that ePTO inverter will have the same current rating as the traction inverter. The obvious conclusion is that the inverter will be oversized for ePTO application which effectively eliminates the low power factor issue.

As mentioned, increased torque ripple is one of the inherent disadvantages of the SyRM. The issue can be mitigated with the use of asymmetric rotor poles [8], [9] or with rotor or stator skewing [10], [11]. In contrast to skewing, asymmetric rotor poles are interesting as a cost reduction method. Typically, SyRM torque ripple is minimized by continuous rotor skewing [10]. The alternatives are segmented rotor skewing or continuous stator skewing. Stator skewing is usually out of scope due to higher production complexity. Adding one slot pitch step skew with several equal rotor segments is common practice in the design of interior permanent magnet machines (IPM). However, skew angle and the step skew length can be optimized to get better torque quality. This study proposes a novel segmented skewing technique with variable length segment pieces applied on SyRM.

The proposed solution is applicable to all kinds of electric

machines that allow stepped skew. To the best of the author's knowledge, similar solutions applied to SyRM's can not be found in the available literature. This paper will concentrate on the SyRM optimization for eMPV ePTO application and post-optimization rotor modification methods for torque ripple reduction. A detailed comparative study has been conducted to illustrate the benefits and drawbacks of each rotor skewing alternative. The baseline machine design has been derived through metamodel-based optimization.

## II. EPTO DESIGN

## *A. Typical optimization procedure*

Most of the electric machine design goals are in conflict with each other and thus form a multi-objective problem (e.g. reduction of volume and mass while increasing the efficiency). When used in EVs, increased machine weight contributes to the driving range reduction, while larger volume creates issues with mechanical integration within the drivetrain. Obviously, an optimal trade-off between conflicting requirements is a design imperative. Considering a large number of coupled parameters that affect the final design, manual design is usually not an option. Nowadays, mathematical optimization is a standard method for obtaining better designs [12] .

Optimization algorithms (OAs) can be divided into gradient-based methods and stochastic (metaheuristic) methods. Gradient methods converge fast but have difficulties with global optima because they require a feasible starting point if cost function non-convexity applies [13].

Stochastic methods are heavily used in electrical machine optimization [13]. The drawback is that the convergence can last for days, and the global optimum cannot be mathematically proven. Additionally, some popular metaheuristic methods are based on natural behavior (Genetic algorithm, Differential evolution [14], [15], Particle swarm [16]), but they can also be iterative [17], or based on approximation [18]. From an engineering standpoint, both approaches can find a satisfying result.

SyRM design is highly affected by the saturation within the rotor structure, which implies the use of computationally intensive finite element analysis (FEA).

The optimization system used for calculation of baseline ePTO machine consists of FEA tool (Ansys Motor-CAD), optimization tool (Ansys OptiSlang) which incorporates sensitivity analysis, meta-modeling and optimization algorithm, and external software (Matlab), which handles model building and FEA tool communication. Cross-section parametrization and automated design generation were implemented according to [19]. Optimization workflow is illustrated on Fig. 3 with color coding according to the used tool. Default OptiSLang genetic optimization algorithm has been selected. The main benefit of using a meta-modeling-based setup (also refereed as surrogate modeling by Bramerdorfer et. al. [20]) is the reduction of optimization time (typical optimization time is 2-3 days). The presented workflow is widely adopted in the e-machine design in automotive applications [21], [22].

### *B. Performance requirements*

The requirements for the ePTO machine in this paper are derived and carried over from [2]. For simplicity, the requirements are listed in Table I.

TABLE I: Peak operation requirements

| Description          | Symbol | Value | Unit |
|----------------------|--------|-------|------|
| Base speed           | nb     | 1700  | rpm  |
| Max. operating speed | nmax   | 2500  | rpm  |
| Max. torque          | Tmax   | ≥ 200 | Nm   |
| Battery voltage      | UDC    | 610   | V    |
| Max. phase current   | Is max | 300   | Arms |

## *C. Optimization objectives and inequality constraints*

Inequality constraints usually arise from various electromagnetic, thermal, mechanical, manufacturing, economic or normative limits such as maximum winding temperature, maximum rotor stress, minimum magnet dimensions, maximum active material cost, maximum noise, etc.

Inequality constraints (Table II) are taken into consideration in the optimization algorithm box in Fig. 3. The constraint function g<sup>1</sup> checks rotor structural factor of safety at maximum over-speed (1.2·nmax). Next, the design evaluation procedure contains several subfunctions designed according to ultra-fast scaling laws [23]. Multiple magnetostatic FEA calculations are performed to find the optimal maximum torque-per-ampere (MTPA) control angle. The number of turns per coil and the number of parallel paths of the machine is then matched to the required base speed. Constraint g<sup>2</sup> checks the losses are within limits. g<sup>3</sup> and g<sup>4</sup> check that maximum stator yoke and tooth flux density are below empirical limits provided by the machine manufacturers. Constraint g<sup>5</sup> is related to thermal loading coefficient (THL)

![](_page_1_Figure_16.jpeg)

Fig. 3: Optimization workflow with Matlab scripting and Motor-CAD FEA tool within OptiSlang environment.

which is equal to current density multiplied by electrical loading (THL =  $J \cdot A$ ). THL indicates if the machine can be cooled down at specified peak performance. The empirical values indicate that water cooling is possible if THL  $\leq 1.9$  MA<sup>2</sup>/m<sup>3</sup>.

Finally, a transient FEA calculation is performed at base speed. The transient is performed for the machine without skewing. To fulfill  $g_6$ , the calculated TPV must be higher than the limit. If the torque ripple  $(T_{\rm ripp})$  is higher than the limit, the machine does not satisfy the constraint  $g_7$ .

TABLE II: Inequality constraints and optimization goals

| No:              | Constraint description                            | Symbol              | Limit                              |
|------------------|---------------------------------------------------|---------------------|------------------------------------|
| $g_1$            | Stress yield factor at $1.2 \cdot n_{\text{max}}$ | FOS                 | $\geq 2$                           |
| $g_2$            | Total loss                                        | $P_{\mathrm{loss}}$ | ≤ 6000 W                           |
| $g_3$            | Flux density in stator yoke                       | $B_{\rm sy,max}$    | ≤ 1.6 T                            |
| $g_4$            | Flux density in stator tooth                      | $B_{\rm st,max}$    | ≤ 1.9 T                            |
| $g_5$            | Thermal loading $J \cdot A$                       | THL                 | $\leq 1.9 \text{ MA}^2/\text{m}^3$ |
| $g_6$            | Torque per volume                                 | TPV                 | $\geq 25 \text{ Nm/dm}^3$          |
| $g_7$            | Torque ripple without skewing                     | $T_{\mathrm{ripp}}$ | $\leq$ 15 %                        |
| No:              | Optimization goals                                | Symbol              | Unit                               |
| $\overline{f_1}$ | Min. total loss                                   | $P_{\mathrm{loss}}$ | W                                  |
| $f_2$            | Max. torque per rotor volume                      | TPV                 | Nm/dm <sup>3</sup>                 |

The optimization algorithm generates the designs, and the variants which fulfill all inequality constraints populate the estimated Pareto front (optimization goals according to Table II). The final step is the validation of the estimated Pareto front which completes the optimization process.

#### D. Preset model

Although 4 poles are a usual choice due to the higher power factor, we have selected a 6-pole machine. The reason is the higher theoretical torque density and lower torque ripple. In ePTO applications, the lower power factor is not an issue due to the use of an oversized inverter. The number of slots is 54 with 4 rotor flux barriers, resulting in a two-layer integer slot distributed winding. This combination provides a good compromise between the inherent ability to mitigate torque pulsations, susceptibility to noise, and the ability to use multiple parallel paths. The ideal number of turns per coil  $(N_c)$  and parallel paths  $(a_p)$  for matching the base speed is automatically calculated based on winding feasibility and ultra-fast scaling laws [23].

## III. OPTIMIZATION OF BASELINE DESIGN

Fig. 4 contains the **validated** Pareto front with  $N_{\rm pareto}$  = 89 members which fulfil all inequality constraints. The design marked with red arrow has been selected as optimal and it will be considered a baseline design in the continuation of the paper (Fig. 4). Major features are listed in Table III and cross-section on Fig. 5a.

## IV. TORQUE RIPPLE REDUCTION

Average torque should always be considered together with torque ripple. Both are obtained by running a transient

TABLE III: Major parameters of the baseline machine

| Description     | Symbol          | Value/Boundarie | Unit              |
|-----------------|-----------------|-----------------|-------------------|
| Stator diameter | $D_s$           | 214             | mm                |
| Shaft diameter  | $D_{\rm sh}$    | 54              | mm                |
| Phase number    | $N_{\rm ph}$    | 3               | -                 |
| No. of turns    | $\dot{N_c}$     | 21              | -                 |
| Parallel paths  | $a_p$           | 6               | -                 |
| Coil throw      | $y_c$           | 9               | -                 |
| Barrier number  | k               | 4               | -                 |
| Pole pairs      | p               | 3               | -                 |
| Slot number     | $N_s$           | 54              | -                 |
| Airgap          | $\delta$        | 0.7             | mm                |
| Stator bore     | $D_b$           | 128.4           | mm                |
| Fill factor     | -               | 0.43            | -                 |
| Rotor diameter  | $D_{\rm rotor}$ | 127             | mm                |
| Current density | J               | 17              | A/mm <sup>2</sup> |
| DC voltage      | $U_{\rm DC}$    | 610             | V                 |
| Split ratio     | $D_b/D_s$       | 0.6             | -                 |
| Barrier bridge  | $w_{\rm bb}$    | 0.3             | mm                |
| Active length   | $l_{\rm s}$     | 180             | mm                |

![](_page_2_Figure_13.jpeg)

Fig. 4: Validated Pareto front within constraints  $g_2$  and  $g_6$ .

calculation which is a standard time-stepping simulation where the position of the rotor changes place synchronously in time with stator magnetomotive force.

One of the inherent disadvantages of the SyRM is the increased torque ripple. The issue can be mitigated with the use of asymmetric rotor poles [8], [9] or with rotor or stator skewing [10], [11]. The drawback of using skewing in optimization is a prolonged transient calculation (it has to be done for each of the rotor segments, e.g. 5 segment rotor skew will have 5 times longer transient simulation). Transient simulation is a computationally expensive part of the design evaluation and depending on required details can take several minutes. Additionally, the Diesel engine PTO shaft has a quite large ripple [1], [2], so the decision was made to optimize the ePTO machine without skewing.

![](_page_3_Figure_0.jpeg)

Fig. 5: Possible rotor adjustments for torque ripple reduction. No skew (a,c); Equal length segment skew (a,d); Continuous skew (a,e); Variable length segment skew (a,f); Asymmetric poles (b). The skew arc length (lskew) is used only for illustration.

To compare the each rotor skewing method, postoptimization transient simulation have been performed for:

- 1) No skew, baseline design (Fig. 5a,c)
- 2) Equal length 3 segment skew (Fig. 5a,d)
- 3) Continuous rotor skew (Fig. 5a,e)
- 4) Variable length 3 segment skew (Fig. 5a,f)
- 5) Asymmetric poles, positive rotation direction (Fig. 5b)
- 6) Asymmetric poles, negative rotation direction (Fig. 5b)

Keys and keyways are typically used for circumferential positioning and connection of the rotor laminates and the shaft. Keyways are typically part of the shaft (Fig. 7a) while keys can be embedded within the rotor laminate (Fig. 7bc) or inserted as an extra component within the shaft (Fig. 7d). For a reliable connection, two or four key structures are commonly used. The number of the keyways should be designed carefully because keyways are cut out on the shaft, which will reduce shaft strength and increase the cost.

In theory, continuous skewing is the best option and should yield the minimal torque ripple [24]. On the other hand, it is potentially the most complex solution which can result in either increased shaft production cost (e.g. shaft keyway must be skewed, Fig. 7a, blue), or a more expensive stamping tool (e.g. each stamped laminate key must have slight angular offset). Obviously, there are many possible solutions to mitigate the mentioned production issues, but those details are out of the scope of this paper.

![](_page_3_Figure_12.jpeg)

Fig. 7: (a) Tesla Model S 60 tranction machine shaft [25]; Rotor and shaft keys: (b) two-key laminate, (c) four-key laminate, (d) insertion key as an additional component.

Equal length segment skewing is typically used in IPM machines with the purpose of reducing the cost and electromagnetic losses of the permanent magnet material. Rotor segmentation is simpler than continuous skewing (shaft keyway is straight, Fig. 7a, red) but still requires an angular laminate stamping variation.

![](_page_4_Figure_0.jpeg)

Fig. 6: Segment variation impact on torque ripple reduction. (a) Equal length segment torque components; (b) Variable length segment torque components; Total torque of equal (c) and variable (d) length segment skew.

Considering that SyRM does not have any magnets, the use of variable segment length skewing is proposed, where lengths can be freely varied with the goal to minimize torque ripple (Fig. 5f). Because the torque waveform amplitude of each segment is proportional to its length, it is possible to reduce the total ripple by varying individual segment lengths. The only requirement is that lseg 1 + ... + lseg <sup>N</sup>seg = ls. The approach is illustrated on Fig. 6.

The optimal segment lengths are achieved via torque ripple minimization function based on a proportional variation of individual segment torque waveforms (obtained from equal segment skewing). The details are planned to be published in the extended version of the paper.

According to [24], skewing variants 2-4 use skewing angle calculated by (1) where ϑskew is expressed in mechanical degrees, p is the number of pole pairs, and h is the highest amplitude torque harmonic of an unskewed rotor (h > 0). In this case, highest order harmonic is 18 (Fig. 9) resulting in <sup>ϑ</sup>skew = 360/(3 · 18) = 6.66◦ mechanical (Fig. 5d-f).

$$\vartheta_{\text{skew}} = \frac{360}{ph}$$
 (1)  $\vartheta_{\text{FBS}} = \frac{360}{2ph}$  (2)

The asymmetric pole approach is potentially the most affordable variant because it does not need any stamping tool variation and uses a straight keyway shaft (Fig. 7a, red). Due to the polar anisotropy, torque transient will differ based on the rotor rotational direction. To illustrate the issue, we have simulated the machine for positive (n = 1700 rpm) and negative (n = −1700 rpm) speed references.

Polar assymetricity has been achieved via flux barrier shift approach (FBS) by Ferrari et.al. [26]. The flux barrier shift angle is determined via (2). ϑFBS is expressed in mechanical degrees and as before, h is the highest amplitude torque harmonic of a unskewed rotor. <sup>ϑ</sup>FBS = 360/(2·3·18) = 3.33◦ mechanical (Fig. 5b).

## V. RESULTS

Table IV summarizes the performance at base speed for each skewing alternative. All responses have been simulated at base speed with equal phase currents amplitude under individual MTPA phase advance angles. The results are ordered by torque ripple, from highest (left) to smallest (right). Fig. 8 contains torque waveforms.

Torque ripple of a baseline design is less than 15% which is a good feature for a non-skewed SyRM. As expected, average torque is the highest of all alternatives, with relatively high power factor (Tavg = 242.3 Nm, Tripp. = 13.99%, cos φ = 0.68). Asymmetric poles with positive rotation reduce the ripple in relation to baseline with the same power factor (Tavg = 240.6 Nm, Tripp. = 7.64%, cos φ = 0.68). On the other hand, negative rotation direction provides additional ripple reduction (Tavg = 239.5 Nm, Tripp. = 7.22%, cos φ =

![](_page_5_Figure_0.jpeg)

Fig. 8: Transient torque for each skewing alternative

0.68). Equal length segment skewing further reduces torque ripple with penalty of lowest power factor (Tavg = 231.1 Nm, Tripp. = 6.24%, cos φ = 0.65). This variant has the smallest average torque. Better results are achieved by applying variable length segment skewing (Tavg = 233.5 Nm, Tripp. = 4.21%, cos φ = 0.66). Finally, as expected, continuous skewing yields the best results (Tavg = 235.7 Nm, Tripp. = 2.79%, cos φ = 0.66).

Note that in relation to baseline, skewing reduces both the average torque by approx. 2-5%, and torque ripple to approx. 3-8% depending on the skewing strategy. Performance-wise, all approaches yield similar average torque resulting in mechanical power of Pmech = 41 − 43 kW.

TABLE IV: Result comparison

| Name   | Unit | (baseline)<br>skew<br>No | 0<br>><br>n<br>poles<br>Asymmetric | 0<br><<br>n<br>poles<br>Asymmetric | segments<br>length<br>Equal | segments<br>length<br>Variable | skew<br>Continous |
|--------|------|--------------------------|------------------------------------|------------------------------------|-----------------------------|--------------------------------|-------------------|
| Tavg   | Nm   | 242.3                    | 240.6                              | 239.5                              | 231.1                       | 233.5                          | 235.7             |
| n      | rpm  | 1700                     | 1700                               | 1700                               | 1700                        | 1700                           | 1700              |
| γ      | ◦    | 63.00                    | 68.10                              | 57.60                              | 59.70                       | 62.60                          | 61.00             |
| Tripp. | %    | 13.99                    | 7.64                               | 7.22                               | 6.24                        | 4.21                           | 2.79              |
| cos φ  | -    | 0.68                     | 0.68                               | 0.68                               | 0.65                        | 0.66                           | 0.66              |
| Irms   | Arms | 95.7                     | 95.7                               | 95.7                               | 95.7                        | 95.7                           | 95.7              |
| ls     | mm   | 180                      | 180                                | 180                                | 180                         | 180                            | 180               |
| Pmech  | kW   | 43.1                     | 42.8                               | 42.6                               | 41.1                        | 41.6                           | 42.0              |
| m      | kg   | 44.1                     | 44.1                               | 44.1                               | 44.1                        | 44.1                           | 44.1              |

## VI. CONCLUSION

Considering robustness, price, and reliability, a synchronous reluctance machine (SyRM) has been selected as

![](_page_5_Figure_8.jpeg)

Fig. 9: Torque transient spectrum

the target ePTO technology. Baseline ePTO SyRM has been designed using meta-model-based optimization.

In this specific case, when compared with other skewing alternatives, the use of asymmetric poles results in a higher torque ripple. Considering that ePTO hydraulic pumps operate unidirectionally, asymmetric poles are a viable solution. The main benefit of asymmetric skewing is the minimal manufacturing complexity compared to either alternative. Equal length segments yield lower torque ripple with a penalty of lowest average torque. On the other hand, considering higher average torque and lower ripple, variable-length segmentation is a better alternative. In theory, the production cost of equal and variable-length segments should be the same. Continuous skewing is the best, but also the most complex variant. The production complexity comparisons are based on our professional experience and they should be considered in the context of ePTO SyRM.

We emphasize that the skewing approach economics are case-dependent and should take into account the manufacturing process details and the commercial decisions of a

## REFERENCES

- [1] B. Ban and S. Stipetic, "Electric Multipurpose Vehicle Power Take- ´ Off: Overview, Load Cycles and Actuation via Synchronous Reluctance Machine," *ACEMP-OPTIM*, 2019.
- [2] B. Ban and S. Stipetic, "Design and optimization of synchronous reluctance machine for actuation of electric multi-purpose vehicle power take-off," *Proceedings - 2020 International Conference on Electrical Machines, ICEM 2020*, pp. 1750–1757, 2020.
- [3] J. J. Germishuizen, F. S. Van der Merwe, K. Van der Westhuizen, and M. J. Kamper, "Performance comparison of reluctance synchronous and induction traction drives for electrical multiple units," *Conference Record - IAS Annual Meeting (IEEE Industry Applications Society)*, 2000.
- [4] J. R. Riba, C. López-Torres, L. Romeral, and A. Garcia, "Rare-earthfree propulsion motors for electric vehicles: A technology review," *Renewable and Sustainable Energy Reviews*, vol. 57, pp. 367–379, 2016.
- [5] S. Estenlund, M. Alaküla, and A. Reinap, "PM-less machine topologies for EV traction: A literature review," *2016 International Conference on Electrical Systems for Aircraft, Railway, Ship Propulsion and Road Vehicles and International Transportation Electrification Conference, ESARS-ITEC 2016*, 2016.
- [6] G. Pellegrino, T. M. Jahns, N. Bianchi, W. L. Soong, and F. Cupertino, *The Rediscovery of Synchronous Reluctance and Ferrite Permanent Magnet Motors Tutorial Course Notes*. Springer, 2016.
- [7] P. Duck, J. Jurgens, and B. Ponick, "Calculation of Synchronous Reluctance Machines Used as Traction Drives," *2015 IEEE Vehicle Power and Propulsion Conference, VPPC 2015 - Proceedings*, pp. 0– 4, 2015.
- [8] A. S. Kafadar, A. Tap, and L. T. Ergene, "Torque ripple reduction of SynRM using machaon type lamination," *2018 6th International Conference on Control Engineering and Information Technology, CEIT 2018*, no. October, pp. 25–27, 2018.
- [9] M. Ferrari, N. Bianchi, A. Doria, and E. Fornasiero, "Design of Synchronous Reluctance Motor for Hybrid Electric Vehicles," *IEEE Transactions on Industry Applications*, vol. 51, no. 4, pp. 21–36, 2015.
- [10] X. B. Bomela and M. J. Kamper, "Effect of stator chording and rotor skewing on performance of reluctance synchronous machine," in *IEEE Transactions on Industry Applications*, vol. 38, no. 1, 2002, pp. 91– 100.
- [11] T. Hubert, M. Reinlein, A. Kremser, and H.-G. Herzog, "Torque ripple minimization of reluctance synchronous machines by continuous and discrete rotor skewing," in *2015 5th International Conference on Electric Drives Production, EDPC 2015 - Proceedings*, 2015.
- [12] C. Lee, J. Lee, and I. G. Jang, "Shape optimization-based design investigation of the switched reluctance motors regarding the target torque and current limitation," *Structural and Multidisciplinary Optimization*, vol. 64, no. 2, pp. 859–870, 2021.
- [13] M. J. Kamper, F. S. Van Der Merwe, and S. Williamson, "Direct Finite Element Design Optimisation of the Cageless Reluctance Synchronous Machine," *IEEE Transactions on Energy Conversion*, vol. 11, no. 3, pp. 547–553, 1996.
- [14] J. Lampinen, "Multi-Constrained Nonlinear Optimization by the Differential Evolution Algorithm," in *Soft Computing and Industry*. Springer-Verlag London, 2002.
- [15] B. Ban, S. Stipetic, and T. Jercic, "Minimum set of rotor parameters for synchronous reluctance machine and improved optimization convergence via forced rotor barrier feasibility," *Energies*, vol. 14, no. 10, p. 16, 2021. [Online]. Available: https://www.mdpi.com/1996-1073/14/10/2744
- [16] G. Bramerdorfer, A. C. Zavoianu, S. Silber, E. Lughofer, and W. Amrhein, "Possibilities for Speeding Up the FE-Based Optimization of Electrical Machines-A Case Study," *IEEE Transactions on Industry Applications*, 2016.
- [17] J. Lee, J. H. Seo, and N. Kikuchi, "Topology optimization of switched reluctance motors for the desired torque profile," *Structural and Multidisciplinary Optimization*, vol. 42, no. 5, pp. 783–796, 2010.
- [18] C. Lee and I. G. Jang, "Topology optimization of multiple-barrier synchronous reluctance motors with initial random hollow circles," *Structural and Multidisciplinary Optimization*, vol. 64, no. 4, pp. 2213– 2224, 2021.

- [19] B. Ban and S. Stipetic, "Absolutely Feasible Synchronous Reluctance Machine Rotor Barrier Topologies with Minimal Parametric Complexity," *Machines*, vol. 10, no. 3, pp. 1–22, 2022. [Online]. Available: https://www.mdpi.com/2075-1702/10/3/206
- [20] G. Bramerdorfer and A. C. Zavoianu, "Surrogate-Based Multi- ˇ Objective Optimization of Electrical Machine Designs Facilitating Tolerance Analysis," *IEEE Transactions on Magnetics*, vol. 53, no. 8, pp. 1–11, 2017.
- [21] N. Riviere, G. Volpe, M. Villani, G. Fabri, L. Di Leonardo, and M. Popescu, "Design analysis of a high speed copper rotor induction motor for a traction application," in *2019 IEEE International Electric Machines and Drives Conference, IEMDC 2019*, 2019.
- [22] N. Riviere, M. Stokmaier, and J. Goss, "An innovative multi-objective optimization approach for the multiphysics design of electrical machines," in *2020 IEEE Transportation Electrification Conference and Expo, ITEC 2020*, 2020, pp. 691–696.
- [23] S. Stipetic, D. Zarko, and M. Popescu, "Ultra-fast axial and radial scaling of synchronous permanent magnet machines," *IET Electric Power Applications*, vol. 10, no. 7, pp. 658–666, 2016.
- [24] X. B. Bomela and M. J. Kamper, "Effect of stator chording and rotor skewing on average torque and torque ripple of reluctance synchronous machine," in *IEEE AFRICON Conference*, vol. 2, 1999, pp. 687–690.
- [25] J. Liang, J. W. Jiang, B. Bilgin, and A. Emadi, "Shaft Design for Electric Traction Motors," *IEEE Transactions on Transportation Electrification*, 2018.
- [26] S. Ferrari, G. Pellegrino, M. Davoli, and C. Bianchini, "Reduction of Torque Ripple in Synchronous Reluctance Machines through Flux Barrier Shift," *Proceedings - 2018 23rd International Conference on Electrical Machines, ICEM 2018*, pp. 2290–2296, 2018.

Branko Ban was born in Šibenik (Croatia) in 1991. He completed Bachelor (2012.) and Master (2015.) studies in Electrical Engineering at the University of Zagreb (Faculty of electrical engineering and computing) and Chalmers University of Technology. Since 2015. he is working in the automotive sector in areas related to electric machine R&D and quality assurance. Branko is a founder of Torquery Consulting, a company specialized in electric machine design and optimization. He is currently enrolled in the University of Zagreb PhD program covering next-generation electric machines.

Andreas Andersson was born in Göteborg, Sweden, in 1988. He received his M.Sc and Ph.D at Chalmers University of Technology in 2013 and 2018, respectively. He is currently working as technical expert at the department of Electric Drive Propulsion, China Euro Vehicle Technologies (CEVT), Göteborg, Sweden. His fields of research interest are electric machine design, electric drives and controls for automotive applications.

Stjepan Stipetic´ was born in Ogulin (Croatia) in 1985. He received Dipl.Eng. and PhD degrees in electrical engineering from the University of Zagreb, Croatia, in 2008 and 2014, respectively. Currently, he is an Assistant Professor at the University of Zagreb Faculty of Electrical Engineering and Computing, Department of Electrical Machines Drives and Automation, Croatia where his research activities are related to design, modelling, analysis and optimization of electrical machines.