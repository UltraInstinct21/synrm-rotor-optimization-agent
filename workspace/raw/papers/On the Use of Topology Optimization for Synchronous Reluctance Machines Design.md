![](_page_0_Picture_0.jpeg)

*Article*

# **On the Use of Topology Optimization for Synchronous Reluctance Machines Design**

**O ˘guz Korman [\\*](https://orcid.org/0000-0003-0685-7964) , Mauro Di Nardo [,](https://orcid.org/0000-0003-0137-4920) Michele Degano and Chris Gerada**

Power Electronics, Machines and Control (PEMC) Research Group, University of Nottingham, Nottingham NG7 2RD, UK; mauro.dinardo4@nottingham.ac.uk (M.D.N.); michele.degano@nottingham.ac.uk (M.D.); chris.gerada@nottingham.ac.uk (C.G.)

**\*** Correspondence: oguz.korman@nottingham.ac.uk

**Abstract:** Synchronous reluctance (SynRel) machines are considered one of the promising and costeffective solutions to many industrial and mobility applications. Nonetheless, achieving an optimal design is challenging due to the complex correlation between geometry and magnetic characteristics. In order to expand the limits formed by template-based geometries, this work approaches the problem by using topology optimization (TO) through the density method (DM). Optimization settings and their effects on results, both in terms of performance and computation time, are studied extensively by performing optimizations on the rotor of a benchmark SynRel machine. In addition, DM-based TO is applied to an existing rotor geometry to assess its use and performance as a design refinement tool. The findings are presented, highlighting several insights into how to apply TO to SynRel machine design and its limitations, boundaries for performance improvements and related computational cost.

**Keywords:** synchronous reluctance machine; topology optimization; density method

![](_page_0_Picture_9.jpeg)

**Citation:** Korman, O.; Di Nardo, M.; Degano, M.; Gerada, C. On the Use of Topology Optimization for Synchronous Reluctance Machines Design. *Energies* **2022**, *15*, 3719. <https://doi.org/10.3390/en15103719>

Academic Editors: Nicola Bianchi, Ludovico Ortombina and Sheldon Williamson

Received: 12 April 2022 Accepted: 11 May 2022 Published: 19 May 2022

**Publisher's Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](_page_0_Picture_14.jpeg)

**Copyright:** © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(https://](https://creativecommons.org/licenses/by/4.0/) [creativecommons.org/licenses/by/](https://creativecommons.org/licenses/by/4.0/) 4.0/).

# **1. Introduction**

Electrical machines are of great interest thanks to their key role in systems electrification and their ever-increasing performance requirements for industrial and e-mobility applications. Among many types of electric machines, Synchronous Reluctance (SynRel) machines have been recently recognized to be a potential candidate for a number of applications, as they present cost-effective energy conversion without the use of permanent magnets, a wide speed range of operation and robust structure. Furthermore, Switched Reluctance Motors (SRM) present similar overall characteristics, but they do require a custom converter depending on the stator and rotor salient teeth combination and polarity. Considering their drive requirements, SynRel machines benefit from relatively cheaper converter topology and a more common control technique when compared to SRM, which is another popular motor type without permanent magnets that has been widely investigated.

Throughout the years, different methodologies have been adopted to design Syn-Rel machines, focusing mainly on the rotor geometry. Early studies used analytical approaches to form flux barriers for maximum torque production and minimum torque fluctuation [\[1–](#page-11-0)[3\]](#page-11-1). These works provided a strong basis for further research where the finite element method (FEM) is adapted and used with computational algorithms to effectively optimize the flux barrier shape.

Traditional optimization of SynRel machines aims to find optimum values of parameters describing a specific rotor shape. Different flux barrier topologies, most commonly circular [\[4\]](#page-11-2), fluid-shaped [\[5\]](#page-11-3) and straight-segmented barrier structures [\[6](#page-11-4)[,7\]](#page-11-5), are used in the literature to design SynRel machines. In [\[8\]](#page-11-6), these flux barrier topologies are compared in terms of performance and computation time, showing that each of them presents advantages and disadvantages.

Parametric optimization, as described above, is proven to be a very effective approach for reaching the objectives in a reasonable amount of computation time. However, *Energies* **2022**, *15*, 3719 2 of 13

parametric optimizations naturally limit the exploration of the research space of possible geometries. TO aims to find the optimal structure with a set of materials without imposed shapes (template-based geometries), as is the case with parametric optimization where degrees of freedom are naturally limited.

Starting with the work of Dyck [\[9\]](#page-11-7) in 1996, TO found its place in electromagnetic design. Since then, many methodologies have been developed and combined together to design electrical machines. Among the different methods, On/Off, density and levelset methods are the most popular. The On/Off method, thanks to its simple theory and implementation, has been widely applied to the design of electric machines. In [\[10](#page-11-8)[,11\]](#page-11-9), a surface permanent magnet machine and a SynRel machine are optimized using a heuristic and stochastic approach, respectively. A modified version of this method, incorporating normalized Gaussian networks, has been used to design SynRel machines and internal permanent magnet (IPM) machines in [\[12\]](#page-11-10). The same method is employed in [\[13\]](#page-11-11) for the optimization of rotor bars in a line-start IPM machine.

Another TO technique, the density method (DM), has also been investigated, as its implementation with sensitivity-based methods and gradient optimization algorithms lead to faster convergence. This method has been applied to wound field synchronous machines in [\[14\]](#page-11-12) and compared with the design achieved by parametric optimization. In a similar study presented in [\[15\]](#page-11-13), rotors of SynRel machines are optimized using a combined magneto-structural analysis. The same method is applied to two case studies in [\[16\]](#page-11-14), which include the minimization of the rotor mass for a surface permanent magnet machine and the minimization of torque ripple for a V-type IPM rotor.

Although in the literature there are a number of works using DM and exploring its adoption for the design of electric machines, there are just a few studies focusing on SynRel machines. Considering the complex anisotropy requirements to improve torque production of such machine type, an optimal design is even more challenging using TO compared to parametric optimization. Therefore, to better understand the potential advantages and drawbacks of using TO, for this type of electrical machine, a more detailed investigation is required. This paper aims to investigate the use of DM through the analysis of its optimization settings and their effects on the optimization results, which represents a novel aspect with respect to the state-of-the-art. The findings of this work are discussed in terms of the performance of the optimal solutions and computation time required for their achievement.

First, brief background information about DM is given in Section [2.](#page-1-0) In Section [3,](#page-3-0) design studies are shown with different optimization settings. Optimizations are performed on a benchmark machine to evaluate the effect of the mesh structure, initial density, penalization coefficient and optimization objectives. Results are then discussed in terms of performance, feasibility and computation time. Finally, TO is performed on an existing design to discuss its usage as a design refinement tool.

#### <span id="page-1-0"></span>**2. Literature Review on Density-Method-Based Topology Optimization**

#### *2.1. Background*

TO was first adopted for mechanical design purposes. Among the early works, a practical application based on the homogenization method (HM) is presented in [\[17\]](#page-12-0). Later, a modified version of this method was used for electromagnetic design in [\[9\]](#page-11-7). A design space is discretized into cells whose material properties can change between the available materials through an interpolation function. For example, if two materials, such as iron and air, are considered, each cell can be iron and air, and the intermediate material can be found by interpolation. In the study, a magnetic bearing is optimized by using the conjugate gradient algorithm to maximize force. This method is nowadays referred to as DM or solid isotropic material with penalization (SIMP).

*Energies* **2022**, *15*, 3719 3 of 13

# *2.2. Methodology*

The number of variables to be optimized using DM is high due to the fact that it represents the material properties of the cells that make up the design space. As a consequence, gradient-based algorithms are generally implemented for the optimization in order to benefit from their fast convergent nature. However, for each evolution step of the optimization, the sensitivities of variables need to be known. This is computationally expensive using the forward difference method and central difference method, as the objective function needs to be evaluated at least as much as the variables (in the case of the finite difference method, the number of evaluations is doubled). For this reason, the adjoint variable method (AVM) is frequently implemented to calculate sensitivities. Using AVM, it is possible to obtain sensitivities with a single evaluation of the objective function, greatly reducing the computational burden [\[18\]](#page-12-1).

# *2.3. Applications to Magnetic Systems and Electric Motors*

DM is applied to a C-core actuator in [\[19\]](#page-12-2), using multiple design spaces with different materials through a sequential linear programming (SLP) algorithm. Air, iron, magnet and coil properties are used to optimize material distribution for maximum force. The force of a magnetic coupler is optimized in [\[20\]](#page-12-3) by using element sensitivities obtained by the finite difference method. Different interpolation schemes between materials are considered by controlling the exponential term named the penalization coefficient *n* as in Equation [\(1\)](#page-2-0). Here, *ρ<sup>i</sup>* stands for normalized density, and *µ<sup>i</sup>* is the corresponding relative permeability. Permeability of air and iron are shown with *µ*<sup>0</sup> and *µ<sup>r</sup>* in order. For convenience, interpolation schemes with respect to increasing *n* are shown in Figure [1.](#page-2-1)

<span id="page-2-0"></span>
$$\mu_i = \mu_0 [1 + (\mu_r - 1)\rho_i^n] \tag{1}$$

A C-core actuator and a permanent magnet model are optimized as presented in [\[21\]](#page-12-4). In this study, TO problems are repeated with different starting points (initial density), and the results exhibit only a slight influence on the objective value and final geometries. The use of a penalization coefficient is analyzed for removing the intermediate (also called gray-scale) materials even though it leads to convergence problems.

<span id="page-2-1"></span>![](_page_2_Figure_7.jpeg)

**Figure 1.** Various interpolation schemes characterized by a penalization coefficient.

An SRM is optimized in [\[22\]](#page-12-5) by using the SLP algorithm where the sensitivities are analytically calculated. The optimization results showed a good improvement in terms of the torque ripple despite a decrease of about 8% in the average torque.

In [\[23\]](#page-12-6), a method of moving asymptotes (MMA) is used as the optimization algorithm, and AVM is used for obtaining the sensitivities to optimize a permanent magnet synchronous machine with two different magnet placements. A mesh-independent filtering is included in the objective function to remove intermediate materials. Another study [\[24\]](#page-12-7)

*Energies* **2022**, *15*, 3719 4 of 13

combines MMA with a smoothed heavyside function to design the rotor of a SynRel machine with different objective functions. With the aim of improving the sensitivity-based nature of DM and to obtain a more uniform material distribution for a SynRel rotor, the authors of [\[25\]](#page-12-8) start from a design space with random hollow circles.

In [\[26\]](#page-12-9), a different approach is followed for removing intermediate materials. A filtering function (called feasibility factor) is used and minimized with the main objective function(s). This strategy is used to optimize an electromagnet and the pole head of a salient pole synchronous generator.

A multi-material TO study presented in [\[14\]](#page-11-12) considers both magnetic and structural aspects for designing the pole and the winding region of a wound field synchronous machine's rotor. A similar method is applied to the design of SynRel machines in [\[15\]](#page-11-13), where the authors conducted magnetic TO with and without preformed rotor bridges. MMA and globally convergent MMA algorithms are used, and their capability of minimizing intermediate materials is shown.

# <span id="page-3-0"></span>**3. Investigation of Optimization Settings**

A commercial finite element software, JMAG Designer, was used in this study. Mesh elements are used as cells that make up the design space, and they are given material properties so that optimization variables are created. Since the focus is SynRel machines, only iron and air were considered. Interpolation between these two materials was performed by using Equation [\(1\)](#page-2-0).

# *3.1. Details of the Benchmark Machine*

A benchmark SynRel machine available and designed in former projects for light traction applications was considered. The specifications of this motor are summarized in Table [1.](#page-3-1) The maximum current density was limited to 10 A/mm<sup>2</sup> , and a distributed single layer winding was used. A water jacket cooling system with a flow rate of 3 L/min was implemented. The lamination material was M290-50A for both the stator and rotor.

| Parameter            | Benchmark Machine |
|----------------------|-------------------|
| Rated Speed (rpm)    | 2500              |
| Maximum Speed (rpm)  | 10,000            |
| DC Bus Voltage (V)   | 610               |
| Stator Diameter (mm) | 245               |
| Rotor Diameter (mm)  | 160               |
| Air gap length (mm)  | 0.7               |
| Stack Length (mm)    | 120               |
| Number of Slots      | 36                |
| Number of Poles      | 6                 |

<span id="page-3-1"></span>**Table 1.** Specifications of the benchmark machine.

The benchmark machine is the result of a parametric multi-objective optimization design using a genetic algorithm with the objectives of maximizing the average torque and minimizing the torque ripple. It was selected as one of the optimum machines having a good compromise between average torque and torque ripple. The details of this optimization study are given in [\[27\]](#page-12-10), while the benchmark machine is shown in Figure [2.](#page-4-0) The average torque of the optimal solution is 100.8 Nm with 7.3% ripple.

#### *3.2. Optimization Starting from an Empty Design Space*

In this part, TO was performed with different settings to optimize the material distribution in the rotor. An empty design space was used respecting the outer dimensions of the benchmark motor's rotor. During the analyses, symmetrical poles were considered. In order to prevent and reduce the number of unfeasible results, an outer layer surrounding the rotor was used with a 0.5 mm thickness. The stator, winding configuration and peak

*Energies* **2022**, *15*, 3719 5 of 13

current of the original machine was unchanged. The effect of the mesh resolution, starting material density, penalization factor and objective functions were investigated in terms of objective values and computation time. Later, an existing design space was used as the initial design space to perform a TO.

<span id="page-4-0"></span>![](_page_4_Picture_2.jpeg)

**Figure 2.** Stator and rotor of the benchmark machine.

# 3.2.1. Effect of Discretization

The discretization of the design space directly affects TO in terms of computation time. A higher resolution can be obtained by increasing the total number of cells in the design region; however, the computation time is adversely affected. The sides of the mesh elements are limited to maximum lengths of 0.25, 0.5, 1 and 2 mm. The minimum and maximum mesh densities are shown in Figure [3a](#page-4-1),b, respectively.

<span id="page-4-1"></span>![](_page_4_Picture_6.jpeg)

**Figure 3.** Maximum and minimum mesh densities used for optimization; maximum mesh length of: (**a**) 0.25 mm and (**b**) 2 mm.

TO was performed with the objective of maximizing the average torque with a penalization coefficient of 1 and initial density of 0.9. The number of iterations were limited to 300 for each model, even though the computation time was quite different due to the number of mesh elements. The optimization results are shown in Figure [4.](#page-5-0) The models with a maximum mesh length of 1 and 2 mm reach their knee points (around 30th iteration) faster than the models with 0.25 and 0.5 mm mesh lengths (around 40th iteration). This might be insignificant in terms of iteration number but the model with 0.25 mm mesh takes 4.4 h to reach the knee point, whereas the one with 2 mm takes 9 min.

*Energies* **2022**, *15*, 3719 6 of 13

<span id="page-5-0"></span>![](_page_5_Figure_1.jpeg)

**Figure 4.** Results of optimizations with different mesh densities.

The maximum objective values were obtained as 97.5, 97.2, 94.7 and 93.2 Nm for decreasing mesh intensity. This suggests that with the increased mesh resolution, it is possible to obtain slightly better average torque by compromising the computation time. Quantitatively speaking, between the two extreme cases, there is 31 h of difference in computation time and 4.5% difference in average torque.

The material and flux density distributions of the final designs are given in Figure [5](#page-6-0) to show the convergence to a reluctance-like structure. Even though a bounding outer frame is used, models with 0.5 and 2 mm mesh do not have a feasible mechanical connection to the frame. This points out the need to add further manufacturing feasibility constraints to the optimization process or the need for a final refinement stage in order to make the optimal solution feasible. Nevertheless, analyzing all the optimal solutions shown in Figure [5a](#page-6-0)–g, it is evident that there are negligible amounts of intermediate materials that do not represent any major challenges for shape definition.

# 3.2.2. Effect of Initial Density

The effect of initial density has been studied in [\[21\]](#page-12-4) for a magnetic shield, and only slight changes were observed in terms of objective value. Although the target problem is relatively complex in that case, similar results were obtained hereafter through optimizations conducted with initial densities of 0.2, 0.5 and 0.9 using the 1 mm mesh model. Slightly different average torque values of 94.3, 95.2 and 94.7 Nm were obtained for final designs with increasing starting density, as shown in Figure [6.](#page-7-0) Analyzing the results, it is clear that starting from a design space with more air, the time required for convergence is greatly increased. This can be justified by the low overall sensitivities obtained in the early iterations.

*Energies* **2022**, *15*, 3719 7 of 13

<span id="page-6-0"></span>![](_page_6_Figure_1.jpeg)

**Figure 5.** Density and flux density distributions for models with increasing maximum mesh lengths. (**a**) Density distribution 0.25 mm mesh; (**b**) flux density distribution 0.25 mm mesh; (**c**) density distribution 0.5 mm mesh; (**d**) flux density distribution 0.5 mm mesh; (**e**) density distribution 1 mm mesh; (**f**) flux density distribution 1 mm mesh; (**g**) density distribution 2 mm mesh; (**h**) flux density distribution 2 mm mesh.

The distribution of material densities is depicted in Figure [7.](#page-7-1) Investigating the material distributions, it is seen that two models with starting densities of 0.2 and 0.5 have more intermediate materials compared to the initial density of 0.9.

*Energies* **2022**, *15*, 3719 8 of 13

Based on the material distributions and objective values, it is clear that the initial starting point has only a little effect on the optimization results. Considering that the optimal material distribution is affected by the complexity and nature of the problem, this observation should not be considered general.

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

<span id="page-7-1"></span>**Figure 6.** Results of optimizations with different initial densities.

![](_page_7_Figure_4.jpeg)

**Figure 7.** Material density distributions, with initial density of: (**a**) 0.2, (**b**) 0.5, (**c**) 0.9.

# 3.2.3. Effect of Penalization Coefficient

Different types of interpolation schemes are used in the literature, and a summary can be found in [\[26\]](#page-12-9). The exponential term in Equation [\(1\)](#page-2-0) is usually referred to as a penalization coefficient because a steep interpolation drives the material property towards higher permeability. In other words, a sharper change in the material properties occur.

To assess the dependency of the optimization results on the penalization parameter, a number of optimizations has been performed on the 1 mm mesh model. The average torque versus the iteration number is given in Figure [8.](#page-8-0) The results indicate that the higher the penalization coefficient, the lower the convergence speed. In addition, there is a substantial drop in average torque when the penalization coefficient is higher than one.

When analyzing the material distributions, as shown in Figure [9,](#page-8-1) it is noticeable that the number of intermediate materials are increasing with the penalization coefficient. Although the intermediate materials shown between red and blue have magnetic properties closer to air, it is hard to differentiate between material borders. It might be possible to further decrease the number of intermediate materials by increasing the number of iterations; however, it is evident that increasing the penalization coefficient worsens the convergence rate.

*Energies* **2022**, *15*, 3719 9 of 13

<span id="page-8-0"></span>![](_page_8_Figure_1.jpeg)

**Figure 8.** Results of optimizations with different penalization coefficients.

<span id="page-8-1"></span>![](_page_8_Figure_3.jpeg)

**Figure 9.** Material density distributions obtained with different penalization coefficient: (**a**) *n* = 2, (**b**) *n* = 3, (**c**) *n* = 4, (**d**) *n* = 5, (**e**) *n* = 10, (**f**) *n* = 20.

*Energies* **2022**, *15*, 3719 10 of 13

# *3.3. Optimization of Torque Ripple*

The optimization of torque ripple is generally more challenging than optimizing average torque alone, as it actually requires a uniform distribution of flux in the air-gap. In DM, this requires the calculation of each cell's sensitivity with respect to rotor position. Taking into account this complexity, the number of iterations for this study is increased to 1000. Using models with maximum mesh lengths of 1 and 2 mm, two optimizations are run with the objectives of increasing average torque and decreasing torque ripple, starting with an initial density of 0.9 and penalization coefficient of 1.

The best of both optimizations, considered as the one with the highest average torque, is shown in Figure [10.](#page-9-0) The model with the 2 mm mesh has 92.3 Nm average torque with a 4.6% ripple, and the other model has 92.1 Nm average torque with a 6.3% ripple. One of the most important distinctions of torque ripple objectives is seen as the formation of an additional air segment, resembling a three barrier structure not seen in the previous sections. As a remark, despite the higher computational time, a more feasible magnetic structure is obtained.

<span id="page-9-0"></span>![](_page_9_Figure_4.jpeg)

**Figure 10.** Results of torque ripple optimization, and material density of (**a**) 2 mm mesh model and (**b**) 1 mm mesh model.

When material distributions of two models, as shown in Figure [10a](#page-9-0),b, are compared, the model with the 1 mm mesh exhibits more intermediate materials than the model with the 2 mm mesh. This can be explained by the fact that the model had a higher number of variables and increased complexity of the objective functions, leading to slow convergence.

#### *3.4. Optimization Starting from a Non-Empty Design Space*

In the previous subsections, various optimizations have been performed on the benchmark machine starting from an empty design space, and the effect of some critical optimization settings have been investigated. In this part, the TO is applied to a non-empty design space, i.e., starting from an already optimized rotor structure. For this purpose, the rotor of the benchmark machine is used with its three flux barrier geometry. A single objective optimization of maximizing average torque is used, limiting the maximum number of iterations to 300.

The obtained material distribution and corresponding flux density distribution are shown in Figure [11b](#page-10-0),c. Electromagnetic torque versus output position is shown in Figure [11a](#page-10-0) for both the original and optimized machine. The average torque of the optimized machine is slightly increased from 100.8 to 102.3 Nm (+1.5%), while the torque ripple reduces from 7.3% to 6.5%. From Figure [11b](#page-10-0), it can be clearly seen that the outermost and middle barriers have minor shape modifications while the innermost barrier is enlarged towards the shaft. This increase in the total ratio of air to iron thickness in the rotor is the reason for the torque increments due to better electromagnetic exploitation of the soft magnetic material. As a result, a minor performance increment is obtained by applying TO as a refinement tool. The underlying significance of this change in the performance is the fact that when using the parametric expression of the geometry, it is not possible to achieve

*Energies* **2022**, *15*, 3719 11 of 13

such a shape, unless certain modifications are made to increase the geometrical degrees of freedom.

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Figure 11.** Optimization results starting from a non-empty design space: (**a**) Electromagnetic torque of original and optimized model, (**b**) material distribution, (**c**) flux density distribution.

# **4. Conclusions**

In this work, TO is applied to a SynRel machine using DM with particular focus on the rotor design. Effect of design space resolution, starting point, penalization and objective functions are investigated by performing TO starting from an empty rotor design space. These critical parameters and their effects on the material distribution, performance and computation time are investigated in depth.

Based on the results, it is apparent that using a high penalization coefficient to reduce the number of intermediate materials causes convergence problems for material distribution, which makes it hard to distinguish boundaries of material areas. Furthermore, any of the designs with intermediate materials were not advantageous in terms of performance.

In addition, it is found that the inclusion of torque ripple within the objective function, despite increasing the computation burden, helps to obtain a more uniform material distribution. The results show the importance of structural consideration, as in its absence, mechanical integrity is not guaranteed. The effect of discretization and initial densities has more of an effect on computation time than the objective value when compared to the other optimization settings. Nevertheless, starting TO with a medium number of cells is considered to be good practice when time is a constraint.

*Energies* **2022**, *15*, 3719 12 of 13

In the case where TO was applied starting from an already optimized rotor structure, a minor improvement is reached. The final design shows improved saliency through better electromagnetic exploitation of the rotor material, which is not possible to obtain using parametric-based optimizations.

The results of the reported design exercise suggest that the use of topology optimization can be used as a refinement design tool once the machine geometry has been largely defined and optimized with standard parametric-based approaches.

**Author Contributions:** Conceptualization, O.K., M.D.N., M.D. and C.G.; methodology, O.K.; software, O.K.; validation, O.K. and M.D.N.; formal analysis, O.K.; investigation, O.K., M.D.N. and M.D.; resources, M.D.N. and M.D.; data curation, O.K., M.D.N. and M.D.; writing—original draft preparation, O.K.; writing—review and editing, M.D.N. and M.D.; visualization, O.K.; supervision, M.D.N. and M.D.; project administration, M.D.; funding acquisition, M.D. and C.G. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research received no external funding.

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** Not applicable.

**Conflicts of Interest:** The authors declare no conflict of interest.

# **References**

<span id="page-11-0"></span>1. Staton, D.; Miller, T.; Wood, S. Maximising the saliency ratio of the synchronous reluctance motor. *Electr. Power Appl. IEEE Proc.* **1993**, *140*, 249–259. [\[CrossRef\]](http://doi.org/10.1049/ip-b.1993.0031)

- 2. Lipo, T.; Vagati, A.; Society, I.A.; Committee, I.A.S.I.D. Synchronous Reluctance Motors and Drives: A New Alternative. In Proceedings of the IAS Annual Meeting, Denver, CO, USA, 2 October 1994.
- <span id="page-11-1"></span>3. Vagati, A.; Pastorelli, M.; Francheschini, G.; Petrache, S. Design of low-torque-ripple synchronous reluctance motors. *IEEE Trans. Ind. Appl.* **1998**, *34*, 758–765. [\[CrossRef\]](http://dx.doi.org/10.1109/28.703969)
- <span id="page-11-2"></span>4. Cupertino, F.; Pellegrino, G.; Gerada, C. Design of Synchronous Reluctance Motors With Multiobjective Optimization Algorithms. *IEEE Trans. Ind. Appl.* **2014**, *50*, 3617–3627. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2014.2312540)
- <span id="page-11-3"></span>5. Moghaddam, R.R.; Magnussen, F.; Sadarangani, C. Theoretical and Experimental Reevaluation of Synchronous Reluctance Machine. *IEEE Trans. Ind. Electron.* **2010**, *57*, 6–13. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2009.2025286)
- <span id="page-11-4"></span>6. Nardo, M.D.; Calzo, G.L.; Galea, M.; Gerada, C. Design Optimization of a High-Speed Synchronous Reluctance Machine. *IEEE Trans. Ind. Appl.* **2018**, *54*, 233–243. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2017.2758759)
- <span id="page-11-5"></span>7. Moghaddam, R.R.; Gyllensten, F. Novel High-Performance SynRM Design Method: An Easy Approach for A Complicated Rotor Topology. *IEEE Trans. Ind. Electron.* **2014**, *61*, 5058–5065. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2013.2271601)
- <span id="page-11-6"></span>8. Pellegrino, G.; Cupertino, F.; Gerada, C. Barriers shapes and minimum set of rotor parameters in the automated design of Synchronous Reluctance machines. In Proceedings of the 2013 International Electric Machines Drives Conference, Chicago, IL, USA, 12–15 May 2013; pp. 1204–1210. [\[CrossRef\]](http://dx.doi.org/10.1109/IEMDC.2013.6556286)
- <span id="page-11-7"></span>9. Dyck, D.; Lowther, D. Automated design of magnetic devices by optimizing material distribution. *IEEE Trans. Magn.* **1996**, *32*, 1188–1193. [\[CrossRef\]](http://dx.doi.org/10.1109/20.497456)
- <span id="page-11-8"></span>10. Hahn, I. Heuristic Structural Optimization of the Permanent Magnets Used in a Surface Mounted Permanent-Magnet Synchronous Machine. *IEEE Trans. Magn.* **2012**, *48*, 118–127. [\[CrossRef\]](http://dx.doi.org/10.1109/TMAG.2011.2167980)
- <span id="page-11-9"></span>11. Lee, T.H.; Lee, J.H.; Yi, K.P.; Lim, D.K. Optimal Design of a Synchronous Reluctance Motor Using a Genetic Topology Algorithm. *Processes* **2021**, *9*, 1778. [\[CrossRef\]](http://dx.doi.org/10.3390/pr9101778)
- <span id="page-11-10"></span>12. Sasaki, H.; Igarashi, H. Topology Optimization Using Basis Functions for Improvement of Rotating Machine Performances. *IEEE Trans. Magn.* **2018**, *54*, 1–4. [\[CrossRef\]](http://dx.doi.org/10.1109/TMAG.2017.2759784)
- <span id="page-11-11"></span>13. Lolova, I.; Barta, J.; Bramerdorfer, G.; Silber, S. Topology optimization of line-start synchronous reluctance machine. In Proceedings of the 2020 19th International Conference on Mechatronics-Mechatronika, (ME), Prague, Czech Republic, 2–4 December 2020; pp. 1–7. [\[CrossRef\]](http://dx.doi.org/10.1109/ME49197.2020.9286643)
- <span id="page-11-12"></span>14. Guo, F.; Salameh, M.; Krishnamurthy, M.; Brown, I.P. Multimaterial Magneto-Structural Topology Optimization of Wound Field Synchronous Machine Rotors. *IEEE Trans. Ind. Appl.* **2020**, *56*, 3656–3667. [\[CrossRef\]](http://dx.doi.org/10.1109/TIA.2020.2989682)
- <span id="page-11-13"></span>15. Guo, F.; Brown, I.P. Simultaneous Magnetic and Structural Topology Optimization of Synchronous Reluctance Machine Rotors. *IEEE Trans. Magn.* **2020**, *56*, 1–12. [\[CrossRef\]](http://dx.doi.org/10.1109/TMAG.2020.3014289)
- <span id="page-11-14"></span>16. Ma, B.; Zheng, J.; Lei, G.; Zhu, J.; Jin, P.; Guo, Y. Topology Optimization of Ferromagnetic Components in Electrical Machines. *IEEE Trans. Energy Convers.* **2020**, *35*, 786–798. [\[CrossRef\]](http://dx.doi.org/10.1109/TEC.2019.2960519)

*Energies* **2022**, *15*, 3719 13 of 13

<span id="page-12-0"></span>17. Bendsøe, M.P.; Kikuchi, N. Generating optimal topologies in structural design using a homogenization method. *Comput. Methods Appl. Mech. Eng.* **1988**, *71*, 197–224. [\[CrossRef\]](http://dx.doi.org/10.1016/0045-7825(88)90086-2)

- <span id="page-12-1"></span>18. Allaire, G. A review of adjoint methods for sensitivity analysis, uncertainty quantification and optimization in numerical codes. *IngÉNieurs L'Automobile* **2015**, *836*, 33–36.
- <span id="page-12-2"></span>19. Wang, S.; Park, S.; Kang, J. Multi-domain topology optimization of electromagnetic systems. *Compel.-Int. J. Comput. Math. Electr. Electron. Eng.* **2004**, *23*, 1036–1044. [\[CrossRef\]](http://dx.doi.org/10.1108/03321640410553463)
- <span id="page-12-3"></span>20. Yoo, J.; Yang, S.; Choi, J.S. Optimal Design of an Electromagnetic Coupler to Maximize Force to a Specific Direction. *IEEE Trans. Magn.* **2008**, *44*, 1737–1742.
- <span id="page-12-4"></span>21. Okamoto, Y.; Takahashi, N. Investigation of topology optimization of magnetic circuit using density method. *Electr. Eng. Jpn.* **2006**, *155*, 53–63. [\[CrossRef\]](http://dx.doi.org/10.1002/eej.20259)
- <span id="page-12-5"></span>22. Lee, J.; Seo, J.H.; Kikuchi, N. Topology optimization of switched reluctance motors for the desired torque profile. *Struct. Multidiscip. Optim.* **2010**, *42*, 783–796. [\[CrossRef\]](http://dx.doi.org/10.1007/s00158-010-0547-1)
- <span id="page-12-6"></span>23. Hermann, A.N.A.; Mijatovic, N.; Henriksen, M.L. Topology optimisation of PMSM rotor for pump application. In Proceedings of the 2016 XXII International Conference on Electrical Machines (ICEM), Lausanne, Switzerland, 4–7 September 2016; pp. 2119–2125. [\[CrossRef\]](http://dx.doi.org/10.1109/ICELMACH.2016.7732815)
- <span id="page-12-7"></span>24. Okamoto, Y.; Hoshino, R.; Wakao, S.; Tsuburaya, T. Improvement of Torque Characteristics For a Synchronous Reluctance Motor Using MMA-based Topology Optimization Method. *IEEE Trans. Magn.* **2018**, *54*, 1–4. [\[CrossRef\]](http://dx.doi.org/10.1109/TMAG.2017.2762000)
- <span id="page-12-8"></span>25. Lee, C.; Jang, I.G. Topology optimization of multiple-barrier synchronous reluctance motors with initial random hollow circles. *Struct. Multidiscip. Optim.* **2021**, *64*, 1–12. [\[CrossRef\]](http://dx.doi.org/10.1007/s00158-021-02976-2)
- <span id="page-12-9"></span>26. Mohamodhosen, B.S.B. Topology Optimisation of Electromagnetic Devices. Ph.D. Thesis, Ecole Centrale de Lille, Villeneuved'Ascq, France, 2017.
- <span id="page-12-10"></span>27. Korman, O.; Nardo, M.D.; Degano, M.; Gerada, C. A Novel Flux Barrier Parametrization for Synchronous Reluctance Machines. *IEEE Trans. Energy Convers.* **2022**, *37*, 675–684. [\[CrossRef\]](http://dx.doi.org/10.1109/TEC.2021.3099628)