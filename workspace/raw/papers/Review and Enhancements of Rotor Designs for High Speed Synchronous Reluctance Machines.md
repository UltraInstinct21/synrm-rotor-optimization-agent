# Review and Enhancements of Rotor Designs for High Speed Synchronous Reluctance Machines

Ludwig Hausmann *wbk Institute of Production Science Karlsruhe Institute of Technology (KIT)* Karlsruhe, Germany ludwig.hausmann@kit.edu

Markus Heim *wbk Institute of Production Science Karlsruhe Institute of Technology (KIT)* Karlsruhe, Germany markus.heim@kit.edu

Marcel Waldhof, Julian Fischer *Institute of Electrical Energy Conversion (iew) University of Stuttgart*  Stuttgart, Germany marcel.waldhof@iew.uni-stuttgart.de julian.fischer@iew.uni-stuttgart.de

Prof. Dr.-Ing. Jürgen Fleischer *wbk Institute of Production Science Karlsruhe Institute of Technology (KIT)* Karlsruhe, Germany juergen.fleischer@kit.edu

Wilken Wößner, Max Oliveira Flammer *wbk Institute of Production Science Karlsruhe Institute of Technology (KIT)* Karlsruhe, Germany wilken.woessner@kit.edu

Prof. Dr.-Ing. Nejila Parspour *Institute of Electrical Energy Conversion (iew) University of Stuttgart*  Stuttgart, Germany nejila.parspour@iew.uni-stuttgart.de

*Abstract***—Rare earth metals are particularly required as a basic component of permanent magnets in modern traction drives for electric vehicles. Due to the limited global resources of raw materials, the environmental impact of mining and the challenges of recycling, the development of resource-saving alternatives is an important research topic. One option is the use of a synchronous reluctance machine (SynRM), whose rotor does not require magnetic materials, aluminum or copper due to its operating principle. Besides the cost-effective manufacturing, the robust and resource-saving rotor design and high efficiency of SynRM, this machine type suffers from a low power factor, poor torque and power density and earlier power drop in the field weakening range in comparison to permanentmagnet synchronous motors. These disadvantages result from the fragile design of the rotor lamination stack and the resulting limited maximum permissible operating speed of current industrial motors, which are therefore not yet suitable for traction drive applications.** 

**This paper gives an overview of new rotor concepts and designs which aim to increase the maximum operation speed of SynRM by optimizing the structural design. Subsequently, a new rotor topology is discussed and evaluated, especially regarding its mechanic and electromagnetic properties as well as the suitability for series production.**

*Keywords—Synchronous Reluctance Machine, Rotor Design, High Speed Application, Saliency Ratio, Fiber Reinforced Plastics* 

# I. INTRODUCTION

In order to reach high power densities within electric traction drives, permanently excited synchronous machine (PMSM) are mainly chosen as the suited motor topology [1]. However, the advantages of PMSM only take effect by using costly and resource intensive NdFeB and SmCo magnets from the rare earth materials neodymium and samarium. In addition, a volatile price development for rare earth materials and makes future market prices difficult to predict [2, 3]. Solely relying on the development and application of PMSM is therefore related to a significant economic risk.

For the above mentioned reasons, approaches are currently increasingly being pursued to reduce the required amount of rare earth materials per rotor, to enable the re-use and recycling of rare earth materials or to develop new magnetic materials. Another alternative is the use of a rotor design, which does not require any application of permanent magnets. As the synchronous reluctance machine (SynRM) does neither require permanent magnets, nor aluminum or copper, it can be seen as a suitable alternative (Fig. 1). Due to its relatively simple structure and the small amount of different materials needed, a conventional synchronous reluctance rotor can be manufactured with relatively low effort and offers high thermal endurance. Furthermore, due to generally low rotor losses, efficiencies of up to 95 % can be reached. In return, this offers relatively low heat generation within the machine, leading to lower thermal load on the ball bearings and the stator windings [4, 5]. Despite these advantages, SynRMs have so for only been developed for use as traction drives in isolated cases: Compared to PMSM, the power factor and power density as well as an early power drop in the field weakening range offers room for improvement of SynRMs. These disadvantages are mainly caused by the mechanical restrictions leading to limited maximum achievable rotor speeds. However, an increase of the rotor's maximum speed is seen as a significant potential to increase the power density of SynRMs. Multiple investigations were therefore carried out to either redefine mechanic and electromagnetic limitations or to bypass these limitations through the development of novel rotor concepts [6]. A broad overview and summary of existing investigations and concepts in the field of high speed synchronous reluctance machines is presented in the following chapter.

![](_page_0_Figure_15.jpeg)

Fig. 1. Structure of synchronous reluctance machines (SynRM) in comparison with asynchronous machines (ASM), permanent magnet synchronous machines (PMSM) and externally excited synchronous machines (EESM)

# II. STATE OF THE ART

#### *A. Analysis of existing concepts*

In order to carry out a systematic analysis of existing rotor concepts, the following questions were defined and are aimed to be answered within the following sections:

- How many different materials are applied within the rotor core?
- Is one of these materials applied as a structural reinforcement of the rotor core?
- If a structural reinforcement is applied, how is it arranged within/on the rotor?
- Which production process is used or is suggested?

## *B. Conventional approaches*

Several design concepts for rotor cores focus on the optimization of size, amount and position of structural ribs in a conventional electric sheet design. For instance, the approaches presented in [7], [8], [9] and [10] carry out a topology optimization to identify a trade-off between achievable maximum rotating speed and amount of iron losses within the rotor core. In these investigations, the transversally laminated rotor core is kept to one material and no additional support structure is being applied. Since these concepts offer a simple structure of the rotor core, they show a good suitability for cost-effective series production. However, a pure optimization of size, amount and position of structural ribs leads to a limited achievable output power. Specifically in [11] no further increase of the achievable maximum output power is found at 37.500 rpm. Also, higher rib thickness is seen to have a negative effect on the anisotropy and therefore also the power factor of the rotor core.

#### *C. Segmentation of the rotor core*

An alternative approach that doesn't solely focus on increasing the maximum speed but also on optimizing the magnetic properties of the rotor is a segmentation of the rotor core. This allows the use of cold-rolled grain-oriented steel, which aims to reduce core loss and increase saliency, efficiency as well as torque density [12]. However, additional assembly effort must be put into the secure fixation of the rotor segments. In [12], this is carried out through the use of PEEK reinforcement studs that are inserted axially through the rotor core. Filling the flux barriers with epoxy resin can also be necessary to increase the rotor stiffness. In addition, compared to non-segmented rotors, the segmentation of the rotor core can lead to an increase of torque ripple [8] and therefore undesired vibration during operation.

#### *D. Use of two different metal alloys*

To overcome the dependency on radial ribs used within the transversal plane of the rotor core, concepts with axially laminated rotor cores where developed and presented in [13] and [14]. In both investigations, a combination of magnetic and non-magnetic sheet metals was applied. While sheets of S355J0 and Inconel 718 [13] are connected by hot isostatic pressing [13], a laminate of 4140 and Nitronic 50 is obtained by brazing in [14]. The brazing process is distinguished by being relatively easy to automate even in delicate applications and preserving metallurgic characteristics due to low operating temperatures. On the downside brazing does not generate the strongest of all connections, which can lead to challenges in high speed applications. The same intention of combining magnetic and non-magnetic materials was implemented in [15], however, applying a different manufacturing process. The rotor that consists of iron rod arrays, which are radially integrated into a Cu-Al alloy tube, is manufactured using a casting process. This manufacturing process comes with cooling time that might affect the production productivity and requires an additional machining step for surface finish. Nonetheless, casting allows great freedom in design and casted parts withstand high compressive strengths. Another approach applying dual-phase magnetic materials is presented in [16]. This involves a nitrating process at high temperature and a material composition that enables higher absorption of nitrogen. Given that, the dual-phase feature of this material enables nonmagnetic bridges and posts, eliminating one of the key limitations of the SynRM designs in terms of torque density and flux weakening by improving the saliency. This concept's very good electromagnetic properties and suitability for high speed applications are opposed by a very complex and challenging manufacturing process [16].

## *E. Insertion of bolts*

Another possibility to increase the load capacity of the rotor core is the insertion of axial bolts. A concept for a switched reluctance motor using a flywheel shaped transversally laminated rotor core supported by axial bolts is presented in [17]. A high stiffness of the rotor can be achieved, leading to the fact that no shaft is needed. However, the cheek plates applied in these concepts require additional axial installation space. In addition, since a high amount of steel is used, high iron losses are expected at the designed maximum speed of 60.000 rpm, leading to high demands for the cooling of the rotor. Due to the comparably structurally weak rotor core caused by the flux barriers of the SynRM, the advantages of the design cannot be directly transferred from switched reluctance machines to SynRM.

# *F. Use of a rotor sleeve*

Instead of inserting the support structure within the rotor core an alternative is mounting an additional on the circumference of the rotor. An approach developed and applied on different rotor topologies is the application of a fiber reinforced rotor sleeve [11], [18]. Given the high load capacity of carbon fiber sleeves under tensile stress, the maximum achievable rotor speed can be significantly increased. Mounting the rotor sleeve through heat shrinking or direct winding leaves the inner shape of the rotor with a high design freedom. However, as the sleeve has to be placed on the circumference of the rotor core, it increases the air-gap between the rotor and the stator and therefore decreases the machine's efficiency [11]. In addition a non-uniform stress within the rotor can cause undesired deformation and hence a bursting of the rotor below designed maximum speed [18].

#### *G. Application of epoxy resin*

A frequently investigated concept is the use of epoxy resin within the flux barriers of the rotor core. While in [19] the resin is applied for additional mechanical integrity and rigidness in addition to a conventional rib structure, a variety of investigations focus on the application of epoxy resin as a substitute for structural ribs [18], [20], [21], [22] and [23]. The flux barriers are axially filled with epoxy resin and thereby form a non-magnetic connection to enhance the mechanical stability. In [23] additional cutouts in the rotor design create a form-fit, which further improves structural stability. Another unusual design feature is presented in [22] where in parts of the structure the centrifugal tensile stress is geometrically converted into a compressive stress. In these areas the dominant force on the support structure is compressive, enabling antiadhesive filler materials to be used. Although resulting in good electromagnetic properties, the maximum achievable rotor speed is highly dependent on the mechanic properties of the interface between the epoxy resin and the laminations. Furthermore, the thermal behavior of the epoxy resin has to be taken into account [18] and excessive epoxy resin may require an additional machining of the rotor's circumference [21].

#### H. 3D printing

With its characteristically high degree of freedom in design and manufacturing, additive manufacturing techniques pose an interesting option for rotor concepts. One approach that was studied in [24] is the axial insertion of a 3D-printed support structure. Several polymers as for example ABS, PC or PEI are presented as possible materials for a structure that distributes the force more evenly and thus increases the load capacity of the rotor. Enhancements of this approach are presented in [25] and [26] where concepts are developed in which the whole rotor structure is 3D-printed using the selective laser melting method with powdered metallic materials like Fe-30%Ni [26]. Subsequently, the structure is filled with a solidified aluminum paste for additional mechanical stability [25]. However, it should be noted that overall these concepts are only suitable for lower temperatures up to 100°C [24] and speeds up to 2000 rpm [24, 25]. While enabling a much higher degree of freedom in designing flux barriers, 3D-printing leads to an increase in manufacturing time and cost and is hence currently rather not applicable for mass production [24].

Another approach to a flexible production of laminations is presented in [12]. This process enables the production of stress and burr free laminations with relatively low tooling effort and a high amount of degrees of freedom for material choice and geometry of the laminations. However, several manufacturing steps such as exposing to ultraviolet light, developing and photo-etching are required to obtain the finished parts and therefore increase production effort. [20]

#### I. Summary

As described in the previous sections, a wide variety of concepts have already been analyzed and tested in various studies. To summarize the distinct approaches the references were assigned to different cells within a morphological box (TABLE I.). The row headers of the morphological box were chosen to represent key distinctive features between different design and production concepts: On the one hand, this is particularly evident in the quantity and type of different materials used for the rotor core and the supporting structure for structural reinforcement of the rotor core. On the other hand, distinctive features in the assembly process, the type of closure and the spatial arrangement of the support structure are shown.

# J. Challenges during testing of novel concepts for SynRM

Even though the presented concepts follow different approaches, common challenges could be identified during analysis and testing of novel rotor concepts.

Firstly, as expected, a reduction of layers thickness in laminated cores leads to a reduction of iron losses [13]. However, thinner layers lead to higher efforts in the production of the rotor core. Besides the challenging handling of thin layers (<0.2mm), thinner layers increase the amount of sheets needed per motor and therefore also increase the wear of a stamping tool used to produce the laminations [27]. Furthermore, a high sensitivity of the SynRM towards geometric errors caused by manufacturing and assembly deviations has been observed. Special attention to the respective production processes is therefore required to avoid the need for additional machining of the rotor assembly [21] [17]. Especially an increase of the air-gap due to geometric errors or the use of a rotor retaining sleeve is found to be very sensitive to motor's efficiency [7]. Even though no permanent magnet material is applied in a SvnRM, a detailed analysis of the rotor's thermal properties has to be carried out. This is the case when materials with different thermal expansion coefficients and highly temperature-dependent mechanic properties (e.g. polymers) are applied [18, 20]. Cooling strategies have also not been investigated in detail so far, although cooling and a reduction of core losses in high-speed applications is a general challenge. [10, 17]. In addition, the balancing process of the rotors as well as the consistency of the rotor unbalance during operation has only been focused on in isolated cases but is seen to be crucial to a silent and reliable operation of the rotor [12, 17].

TABLE I. SUMMARY OF PRESENTED CONCEPTS BY MEANS OF A MORPHOLOGICAL BOX

| Material composition                  | Mono-material structure [7–11, 17]            |            |                      |                                   |                                               | Multi-material structure [12–16, 18–25]   |                                           |                                                |    |                                        |                  |                                                |                             |
|---------------------------------------|-----------------------------------------------|------------|----------------------|-----------------------------------|-----------------------------------------------|-------------------------------------------|-------------------------------------------|------------------------------------------------|----|----------------------------------------|------------------|------------------------------------------------|-----------------------------|
| Material of support structure         | Metal [14–16, 25]                             |            | Polymers [12, 19–24] |                                   | 1                                             | Fiber reinforced plastic (continuous)[18] |                                           | Fiber reinforced<br>plastic (short or<br>long) |    | Combination                            |                  | No additional support structure [7–11, 13, 17] |                             |
| Assembly process of support structure | No joining process [7–11]                     | Screw [17] | -                    | Pressing [13, 24]                 | Joining by original forming [15, 16]          | Joining by<br>shaping<br>[18]             | Filling<br>[18–23]                        | Weldin                                         | ng | Soldering [14]                         |                  | Gluing                                         | Combinati<br>on<br>[12, 25] |
| Type of closure<br>for radial load    | Form-fit [17, 19, 23, 24]                     |            |                      |                                   | Force-fit [17, 22]                            |                                           | Material closure<br>[7–11, 14–16, 20, 21] |                                                |    |                                        | Combination [25] |                                                |                             |
| Arrangement of support structure      | Parallel to axis of wrotation [12, 13, 16–25] |            |                      | n transversal<br>plane<br>14, 15] |                                               | nferential [18]                           |                                           | Combination                                    |    | No additional support structure [7–11] |                  |                                                |                             |
| Additional end plates                 | Applied [12, 17, 18, 21]                      |            |                      |                                   | Not applied [7–11, 13–16, 19, 20, 22, 24, 25] |                                           |                                           |                                                |    |                                        |                  |                                                |                             |

One approach that has received little attention in previous investigations is the insertion of a fiber reinforced support structure into the rotor core. This field of improvement (also depicted by the morphological box in TABLE I. ) has led to the development of a new concept for the design and production of a high speed synchronous reluctance rotor.

# III. APPROACH

The new design presented in this paper focuses on a combination of good mechanic and electromagnetic properties with suitability for series production. Therefore, standard electrical sheets are chosen as the flux leading material. To ensure high mechanic load capacity especially towards centrifugal forces in high speed applications, continuous fiber reinforced structural struts are inserted within the rotor core. In order to realize the force transmission into the continuous fibers, bone-shaped struts created by a double loop connection around two support wires are proposed, which transfer the forces via form-fit between flux conducting sections. The concept opens up new design possibilities for optimizing the mechanical stability and safety of the rotor with lower impact on the electromagnetic properties than additional steel ribs. In order to evaluate the potential advantages of the structural rotor reinforcement, a comparison with a conventional design of a synchronous reluctance rotor was carried out by simulation. The concept study is based on a generic rotor topology that is not oriented towards a specific performance class or application, with the geometric dimensions given in TABLE II. In this case the outer diameter is set considerably high, to neglect the saturation effects in the stator yoke. The results of the structural and electromagnetic analysis as well as an overview of the developed manufacturing concepts are presented in the following chapter.

TABLE II. ANALYSZED GEOMETRY

| Description           | Value  |  |  |
|-----------------------|--------|--|--|
| Outer stator diameter | 250 mm |  |  |
| Bore diameter         | 130 mm |  |  |
| Active length         | 180 mm |  |  |
| Air-gap               | 0,5 mm |  |  |
| Number of slots       | 36     |  |  |
| Number of poles       | 4      |  |  |

# IV. RESULTS

# *A. Structural Analysis*

To verify the structural integrity of the new rotor concept against centrifugal forces and under thermal load, an analysis of the rotor topology was performed in the commercial software Abaqus FEA. The results were compared with a conventional rotor design of the same topology where the radial support ribs were cut out of the electric sheet. An ordinary unidirectional glass fiber composite was chosen as the material for the fiber reinforcement of the support structure. The material properties for the electric sheet as well as the support structure are summarized in TABLE III.

The fiber reinforced support structure was modeled using the two different approaches shown in Fig. 2. The modelling of the structure with only one integral part, to which several material sections are assigned, is simple and leads to robust contact simulation, but does not completely reflect the real structure due to the erroneously additional fibers in the middle section. On the other hand, modeling the support structure with separate parts and additional contact areas is more realistic, but the overall model is much more sensitive to contact related convergence problems. The comparison of both approaches results in a similar overall deformation and a difference of the maximum equivalent stress of about 15– 20 MPa in the electric sheet. Knowing that the middle section is actually filled with resin, the use of the simplified model seems legitimate without introducing critical errors due to the modeling.

TABLE III. MATERIAL PROPERTIES

| Electric Sheet                                        |               |
|-------------------------------------------------------|---------------|
| Density ρe                                            | 7,65 g/cm3    |
| Young's modulus E                                     | 185.000 N/mm2 |
| Poisson ratio ν                                       | 0.3           |
| Yield strength Rp0.2                                  | 390 N/mm2     |
| Tensile strength Rm                                   | 550 N/mm2     |
| Thermal expansion coefficient α                       | 12ꞏ10-6/K     |
| Unidirectional Glass Fiber Composite                  |               |
| Density ρg                                            | 1,9 g/cm3     |
| Longitudinal modulus E11                              | 40.000 N/mm2  |
| Transversal modulus E22                               | 11.000 N/mm2  |
| In-plane shear modulus G12                            | 4300 N/mm2    |
| Major Poisson ratio ν12                               | 0.28          |
| Minor Poisson ratio ν23                               | 0.07          |
| Longitudinal thermal expansion coefficient α1 [28]    | 4.5ꞏ10-6/K    |
| Transversal thermal expansion coefficient α2, α3 [28] | 50ꞏ10-6/K     |

![](_page_3_Figure_12.jpeg)

Fig. 2. a) Multi-material-section modeling, b) multi-part modeling.

The conventional and the new rotor design were both subjected to a centrifugal load corresponding to a speed of 15.000 rpm. Furthermore the impact of a maximal thermal load of 150 K temperature difference was analyzed. Both rotor designs show similar maximum equivalent stresses of the electric sheet (cf. Fig. 3 and Fig. 4), whereby the fiber composite material is in general only moderately stressed. For the new rotor design, the peak value of the radial expansion of the rotor near the air-gap under centrifugal and thermal loads is 161 μm and is thus slightly lower than the conventional design with 170 μm. The additional support structure becomes advantageous when the centrifugal load is increased to 20.000 rpm (cf. Fig. 5 and Fig. 6). While the maximum tensile strength of the electrical steel sheet is quickly exceeded in the conventional design due to the plastic strain concentration, the new design withstands the overspeed with maximum equivalent stress below 410 MPa. In addition, there are many ways to increase overall structural performance, such as optimizing or adding support elements, applying preload during assembly, embedding the support elements in axial end plates, using a more performant composite material (e.g. basalt or carbon fiber) or additionally filling the lateral air-gaps with adhesive resins. Finally, the structural behavior of a rotor with substituted central ribs was analyzed with the aim of improving the electromagnetic properties, as shown in Fig. 7. While the structural stability is higher than in the conventional design,

the compromise between mechanical and electromagnetic properties must be investigated in a more detailed analysis to derive an optimal design.

![](_page_4_Figure_1.jpeg)

Fig. 3. Conventional rotor design simulated at 15000 rpm, and 150 K thermal load. The color-map shows the Von Mises stress in MPa.

![](_page_4_Figure_3.jpeg)

Fig. 4. Novel rotor design simulated at 15000 rpm and 150 K thermal load. The color-map shows the Von Mises stress in MPa.

![](_page_4_Figure_5.jpeg)

Fig. 5. Conventional rotor design simulated at 20000 rpm and 150 K thermal load. The color-map shows the Von Mises stress in MPa.

![](_page_4_Figure_7.jpeg)

Fig. 6. Novel rotor design simulated at 20000 rpm and 150 K thermal load. The color-map shows the Von Mises stress in MPa.

![](_page_4_Figure_9.jpeg)

Fig. 7. Novel rotor design with substituted ribs, simulated at 20000 rpm and 150 K thermal load. . The color-map shows the Von Mises stress in MPa.

# *B. Electromagnetic Analysis*

In this section an electromagnetic study of the novel rotor is discussed to evaluate the electromagnetic influence of the modified rotor geometry. Therefore a preliminary stator design is conducted. The geometric parameters are listed in TABLE II. The number of slots per pole per phase is chosen to *q* = 3 and the number of turns per phase is calculated for a maximum DC-Link Voltage of UDC = 650 V at *n*base ≈ 5000 rpm. To verify the electromagnetic performance of the novel rotor, the introduced stator is used for both rotor geometries. Besides, no further optimizations are done for either of the topologies.

For stator and rotor electrical steel TKES M270-35A is assumed. The glass fiber support structure is neglected in the first attempt, because of the non-electromagnetic behavior of the glass fiber material [29]. The FEA is set up with the software COMSOL Multiphysics (cf. Fig. 8). A non-linear stationary FEA is done for different rotor positions within a half electrical period. To analyze the power range performance a complete torque speed map is calculated. Therefore, a hybrid numerical and analytical model is implemented, comparable to [30]. The optimal current vector is calculated by using the maximum torque per ampere (MTPA), maximum ampere (MA) and maximum torque per volt (MTPV) algorithms. The suitability of the novel rotor design is rated by the field orientated inductance ratio *x = Ld/Lq* and inductance difference *l* = *Ld – Lq*. According to the torque equation (1) the difference between these inductances is directly proportional to the average torque.

$$T \propto L_d - L_q \tag{1}$$

Furthermore, the ratio *x* has a large impact on the constant power range behavior in field weakening operation [31].

![](_page_4_Figure_16.jpeg)

Fig. 8. FEA simulation results of both rotor geometries for one pole. The color-map shows the flux density distribution.

In Fig. 9 the ratio between the inductance ratio of the initial rotor (IR) and the novel rotor (NR) is shown. It is noticeable that the inductance ratio of the NR is slightly smaller to the IR. The additional electrical steel for the bone holders decreases the magnetic resistance of the q-axis. This leads to a higher quadrature inductance Lq. This reduces the average torque by 4 % compared to the initial geometry. More detailed results are listed in TABLE IV.

Through small adjustments of the novel rotor design, here especially the substitution of rotor ribs by additional support elements as shown in Fig. 7, it is possible to improve the inductance ratio (cf. Fig. 9). As a result, improvements of the novel rotor can be seen, especially in the field weakening operation region. The higher power factor leads to a wider constant power range, which is beneficial for many applications, e.g. electric vehicles. The novel rotor design shows high potential for future optimization. Overall, the novel rotor designs an electromagnetic comparable to the initial geometry.

![](_page_5_Figure_1.jpeg)

Fig. 9. FEA simulation data of the torque ratio (TR) and power factor (PF) and the inductance ratio (InR) over the Speed.

TABLE IV. ELECTRICAL AND ELECTROMAGNETIC PARAMETERS IN ONE OPERATION POINT

| Parameter       | Unit | IR    | NR            | abs. dev.   |
|-----------------|------|-------|---------------|-------------|
| DC-Link Voltage | V    |       | 650           | -           |
| Nom. Current    | A    |       | 42            | -           |
| Torque          | Nm   | 36.54 | 32.26 (35.93) | 0.96 (0.98) |
| d-Inductance    | mH   | 8.87  | 8.77 (8.76)   | 0.99 (0.99) |
| q-Inductance    | mH   | 1.37  | 1.53 (1.39)   | 1.15 (1.01) |
| Power Factor    | -    | 0.68  | 0.66 (0.68)   | 0.97 (1.00) |
| Base speed      | rpm  | 5477  | 5488 (5532)   | 1.00 (1.01) |

## *C. Production concept*

After the potential of the new fiber reinforced rotor concept has been analyzed by simulation, a possible manufacturing process for the support structure and the assembly into the rotor core is described, as shown Fig. 10 a).

For the production of the axial support structure e.g. two austenite steel wires are entwined by a semi-finished fiber product. Independent of the fiber material either a unidirectional fiber tape or a woven fabric can be used, which theoretically allows for endless production of the support structure similar to a pultrusion process. Another possibility is to insert pieces of the axial support wire in a pre-woven fiber tube. In any case for finishing the support structure the fiber material is optionally impregnated and then consolidated in several rolling stages into its characteristics bone-shape and cut to the desired length. For the assembly of the final rotor, the supporting struts are axially press fitted into the sheet metal stack. As the negative shapes of the boneshaped struts (previously referred to as bone holder) are incorporated in the cross section of the sheet metal stack, a form closure is obtained.

As an alternative to single support elements with continuous fibers, a more cost-effective integral structure made of long-fiber reinforced plastics produced by injection molding or impact extrusion could be applied (Fig. 10 b). This concept also uses a force closure to ensure high reliability in the transmission of mechanical stresses, but aims to distribute the applied mechanical load along the entire cavities within the sheet metal stack. Cylindrical bores are inserted into the integral structure to reduce overall rotor mass and allow a flow of air cooling in axial direction. The structures can be axially fitted into the sheet metal stack with presumably low effort, since their curved shape allow a high safety against buckling under compressive stress.

![](_page_5_Picture_10.jpeg)

Fig. 10. a) Manufacturing concept of the support structure with continuous fibres, b) alternative long-fiber reinforced integral structure.

# V. CONCLUSION AND OUTLOOK

By means of a literature research, a morphological box classifying different approaches for high speed synchronous reluctance machines was developed. While many concepts have been developed using topology optimization of structural ribs and an application of resin within flux barriers, only few approaches have considered the use of fiber reinforced plastics as a support structure within the rotor core. A new concept inserting continuous fiber reinforced structural struts within the rotor core has therefore been presented.

A concept study by numerical simulation has shown that the structural performance of the rotor can be improved with fiber reinforced support structures to withstand higher centrifugal forces and to enable new design possibilities to adapt the electromagnetic behavior. In order to develop an optimal design for any test application, more detailed optimizations are necessary, which will be targeted in future research. Furthermore, in order to validate the simulations, the next step is the manufacturing of prototype rotor discs with fiber reinforced supporting struts, which have to be tested by burst tests. After a proof of concept for this novel rotor concept, it is planned to increase the maximum output power.

#### ACKNOWLEDGMENT

The authors wish to thank the coordinators of the project "Innovation Campus Future Mobility". As part of the "Strategiedialog Automobilwirtschaft (SDA)" it is generously funded by the Ministry of Economic Affairs, Labour and Housing of Baden-Württemberg for the generous financial funding of the FerRoMob project, in which context the published content has been generated.

# REFERENCES

- [1] H. Helms, J. Jöhrens, C. Kämper, J. Giegrich, A. Liebich, "Weiterentwicklung und vertiefte Analyse der Umweltbilanz von Elektrofahrzeugen," ifeu – Institut für Energie- und Umweltforschung Heidelberg GmbH, Heidelberg, Dessau-Roßlau, 2016.
- [2] S. Braun and I. Knüttgen, "Datenmonitor e-mobil BW 2019," 2019.
- [3] D. Schüler, M. Buchert, R. Liu, S. Degreif, and C. Merz, "Study on Rare Earths and Their Recycling.: Final Report for The Greens/EFA Group in the European Parliament," Darmstadt, 2011. Accessed: Jul. 31 2020.
- [4] E. Jorge and A.J.M. Cardoso, "Super Premium Synchronous Reluctance Motor Evaluation," in *IEEE International Conference on Industrial Technology (ICIT), 2013: 25 - 28 Feb. 2013, Pavilion - Clock Tower Conference Centre, Cape Town, South Africa ; proceedings*, 2013.
- [5] A. Boglietti, A. Cavagnino, M. Pastorelli, D. Staton, and A. Vagati, "Thermal analysis of induction and synchronous reluctance motors," pp. 675–680.
- [6] S. Günther, Ed., *Hochausgenutzte synchrone Reluktanzmaschinen für den Einsatz als elektrische Fahrmotoren,* 1st ed. Düren: Shaker, 2019.
- [7] A. Credo, G. Fabri, M. Villani, and M. Popescu, "High Speed Synchronous Reluctance Motors for Electric Vehicles: a Focus on Rotor Mechanical Design," in *2019 IEEE International Electric Machines & Drives Conference (IEMDC): May 12-15, 2019, Westin San Diego, San Diego, CA*, 2019, pp. 165–171.
- [8] A. Dziechciarz, C. Oprea, and C. Martis, "Multiphysics design of synchronous reluctance machine for high speed applications," in *IECON 2016 - 42nd Annual Conference of the IEEE Industrial Electronics Society*, Florence, Italy, Oct. 2016 - Oct. 2016, pp. 1704–1709.
- [9] M. Palmieri, F. Cupertino, and G. L. Cascella, "Mechanical Refinements for the Stress Reduction of High-Speed Synchronous Reluctance Machines," in *2018 XIII International Conference on Electrical Machines (ICEM)*, Alexandroupoli, Sep. 2018 - Sep. 2018, pp. 826–832.
- [10] F. Cupertino, M. Palmieri, and G. Pellegrino, "Design of high-speed synchronous reluctance machines," in *2015 IEEE Energy Conversion Congress and Exposition (ECCE)*, Montreal, QC, Canada, Sep. 2015 - Sep. 2015, pp. 4828–4834.
- [11] C. Babetto, G. Bacco, and N. Bianchi, "Synchronous Reluctance Machine Optimization for High-Speed Applications," *IEEE Trans. Energy Convers.*, vol. 33, no. 3, pp. 1266–1273, 2018, doi: 10.1109/TEC.2018.2800536.

- [12] C. Desai, H. R. Mehta, and P. Pillay, "Fabrication and Assembly Method for Synchronous Reluctance Machines," *IEEE Trans. on Ind. Applicat.*, vol. 54, no. 5, pp. 4227–4235, 2018, doi: 10.1109/TIA.2018.2836975.
- [13] V. Abramenko, J. Nerg, I. Petrov, and J. Pyrhonen, "Influence of Magnetic and Nonmagnetic Layers in an Axially Laminated Anisotropic Rotor of a High-Speed Synchronous Reluctance Motor Including Manufacturing Aspects," *IEEE Access*, vol. 8, pp. 117377–117389, 2020, doi: 10.1109/ACCESS.2020.3004705.
- [14] H. Hofmann and S. R. Sanders, "High-speed synchronous reluctance machine with minimized rotor losses," *IEEE Trans. on Ind. Applicat.*, vol. 36, no. 2, pp. 531–539, 2000, doi: 10.1109/28.833771.
- [15] J. Ikaheimo, J. Kolehmainen, T. Kansakangas, V. Kivela, and R. R. Moghaddam, "Synchronous High-Speed Reluctance Machine With Novel Rotor Construction," *IEEE Trans. Ind. Electron.*, vol. 61, no. 6, pp. 2969–2975, 2014, doi: 10.1109/TIE.2013.2253077.
- [16] P. B. Reddy *et al.,* "Performance Testing and Analysis of Synchronous Reluctance Motor Utilizing Dual-Phase Magnetic Material," *IEEE Trans. on Ind. Applicat.*, vol. 54, no. 3, pp. 2193–2201, 2018, doi: 10.1109/TIA.2018.2801264.
- [17] M. Besharati, J. Widmer, G. Atkinson, V. Pickert, and J. Washington, "Super-high-speed switched reluctance motor for automotive traction," in *2015 IEEE Energy Conversion Congress and Exposition (ECCE)*, Montreal, QC, Canada, Sep. 2015 - Sep. 2015, pp. 5241–5248.
- [18] K. Grace, S. Galioto, K. Bodla, and A. M. El-Refaie, "Design and Testing of a Carbon-Fiber-Wrapped Synchronous Reluctance Traction Motor," *IEEE Trans. on Ind. Applicat.*, vol. 54, no. 5, pp. 4207–4217, 2018, doi: 10.1109/TIA.2018.2836966.
- [19] S. M. Taghavi and P. Pillay, "A Mechanically Robust Rotor With Transverse Laminations for a Wide-Speed-Range Synchronous Reluctance Traction Motor," *IEEE Trans. on Ind. Applicat.*, vol. 51, no. 6, pp. 4404–4414, 2015, doi: 10.1109/TIA.2015.2445819.
- [20] A. Credo, M. Villani, M. Popescu, and N. Riviere, "Synchronous reluctance motors with asymmetric rotor shapes and epoxy resin for electric vehicles," in *ECCE 2019: IEEE Energy Conversion Congress & Expo : Baltimore MD, Sept. 29 - Oct. 3*, Baltimore, MD, USA, 2019, pp. 4463–4469.
- [21] Y. Bao *et al.,* "A Novel Concept of Ribless Synchronous Reluctance Motor for Enhanced Torque Capability," *IEEE Trans. Ind. Electron.*, vol. 67, no. 4, pp. 2553–2563, 2020, doi: 10.1109/TIE.2019.2914616.
- [22] J. Kolehmainen, "Synchronous Reluctance Motor With Form Blocked Rotor," *IEEE Trans. Energy Convers.*, vol. 25, no. 2, pp. 450–456, 2010, doi: 10.1109/TEC.2009.2038579.
- [23] W. T. Villet and M. J. Kamper, "Design of a reluctance synchronous machine for saliency based position sensorless control at zero reference current: 25 - 28 Feb. 2013, Pavilion - Clock Tower Conference Centre, Cape Town, South Africa ; proceedings," in *IEEE*

- *International Conference on Industrial Technology (ICIT), 2013: 25 - 28 Feb. 2013, Pavilion - Clock Tower Conference Centre, Cape Town, South Africa ; proceedings*, 2013, pp. 301–306.
- [24] H.-S. Hong, H.-C. Liu, S.-Y. Cho, J. Lee, and C.-S. Jin, "Design of High-End Synchronous Reluctance Motor Using 3-D Printing Technology," *IEEE Trans. Magn.*, vol. 53, no. 6, pp. 1–5, 2017, doi: 10.1109/TMAG.2017.2659782.
- [25] P.-W. Huang, M.-C. Tsai, and I.-H. Jiang, "3-D Structure Line-Start Synchronous Reluctance Motor Design Based on Selective Laser Melting of 3-D Printing," *IEEE Trans. Magn.*, vol. 54, no. 11, pp. 1–4, 2018, doi: 10.1109/TMAG.2018.2849710.
- [26] Z.-Y. Zhang, K. J. Jhong, C.-W. Cheng, P.-W. Huang, M.-C. Tsai, and W.-H. Lee, "Metal 3D printing of synchronous reluctance motor," in *2016 IEEE International Conference on Industrial Technology (ICIT)*, Taipei, Taiwan, Mar. 2016 - Mar. 2016, pp. 1125–1128.
- [27] A. Kraemer, J. Stoll, D. Blickle, G. Lanza, and B. Boeker, "Analysis of wear behavior of stamping tools

- in the production of electrical steel sheets," in *2015 5th International Electric Drives Production Conference (EDPC)*, 2015, pp. 1–7.
- [28] M. Hagenbeek, *Characterisation of Fibre Metal Laminates in Thermomechanical Loadings*. Saarbrücken: VDM Verlag Dr. Müller, 2010.
- [29] Tobias Mayr, "Multiphysikalische Auslegung induktiver Ladeeinheiten in Faserverbundkonzepten für die Elektromobilität," Dissertation, Institut für Leichtbau, Universität der Bundeswehr München, München, 2019.
- [30] J. Fischer, M. Schmid, and N. Parspour, ""Investigation of Maximum Torque per Ampere and Maximum Efficiency Control Strategies of a Transverse Flux Machine: in press," in *ICEM 2020*, 2020.
- [31] I. Boldea and L. Tutelea, *Reluctance Electric Machines*. Boca Raton : Taylor & Francis, a CRC title, part of the Taylor & Francis imprint, a member of the Taylor & Francis Group, the academic division of T&F Informa, plc, 2018.: CRC Press, 2018.