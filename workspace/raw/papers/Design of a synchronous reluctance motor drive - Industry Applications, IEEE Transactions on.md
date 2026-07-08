# Design of a Synchronous Reluctance Motor Drive

T. J. E. Miller, Senior Member, IEEE, Alan Hutton, Calum Cossar, and David A. Staton

Abstract—A segmental-rotor synchronous reluctance motor is used in a variable-speed drive with current-regulated PWM control. The low-speed torque capability is compared with those of an induction motor, a switched reluctance motor, and a brushless dc PM motor of identical size and copper weight. The results suggest that many of the desirable properties of the switched reluctance motor can be realized with the synchronous reluctance motor but using standard ac motor and control components. The torque capability is lower, but so is the noise level.

#### I. Introduction

THE POLYPHASE synchronous reluctance motor was developed particularly in the 1960's as a line-start (cage-type) synchronous ac motor [1]-[4] for applications where several motors are operated synchronously from a single voltage-source inverter. In some cases, it has been replaced by cage-type ac permanent-magnet (PM) motors that, although more expensive, have better performance and permit more motors to run from the same inverter [17].

More recently, there has been increasing use of variable-frequency ac induction motor drives with one motor per inverter. At first, the six-step inverter was used, usually with constant voltage/frequency ratio and often without speed feedback. The development of pulse-width-modulated (PWM) inverters followed with slip-control, and today, field-oriented or "vector" control is the most advanced form of ac drive, with performance characteristics that match those of the best dc drives. Although the induction motor is the most common in ac drives, synchronous PM motors are also used. With one motor per inverter, there is no need for a rotor cage because the motor does not have to start across the line.

It is perhaps surprising that there has been so little development of the cageless synchronous reluctance motor instead of the induction motor or PM ac motor for variable-frequency operation [6]-[8], [13], [14]. One reason is probably its reputation for poor efficiency and low power factor, but the removal of the rotor cage and the use of field-oriented control

Paper IPCSD 91-17, approved by the Electric Machines Committee of the IEEE Industry Applications Society for presentation at the 1989 Industry Applications Society Annual Meeting, San Diego, CA, October 1-5. Manuscript released for publication February 5, 1991. This work was supported by the UK Science and Engineering Research Council, a grant from the General Electric Company, and the member companies of the Scottish Power Electronics and Electrical Drives (SPEED) Consortium.

T. J. E. Miller, C. Cossar, and D. A. Staton are with the Department of Electronics and Electrical Engineering, University of Glasgow, Glasgow, Scotland.

A. J. Hutton is with Micro Marketing, Motorola Ltd., Glasgow, Scotland. IEEE Log Number 9100935.

provide the designer with two new degrees of design freedom that do not appear to have been fully explored.

The main features of the synchronous reluctance motor are as follows:

- The rotor is potentially less expensive than the PM rotor. Because it requires no cage winding, it is lighter and possibly cheaper than an induction-motor rotor.
- The torque per ampere is independent of rotor temperature, unlike that of the PM or induction motors.
- The stator and the inverter power circuit are identical to those of the induction motor or PM synchronous motor drives.
- The control is simpler than that of the field-oriented induction motor drive, although shaft position feedback is necessary.
- Because of scaling effects, the poor efficiency and high slip of small induction motors prevent the extension of ac drive technology down to low power levels. The PM ac motor or brushless dc motor can be used instead, but PM motors are more expensive. They are temperature sensitive, susceptible to demagnetization, and may require additional inverter protection. The synchronous reluctance motor offers an alternative means of obtaining the advantages of a synchronous motor but at lower cost.

The synchronous reluctance motor's smoothly rotating field distinguishes it from the *switched* reluctance motor [9], [11]. It therefore fits in the "family of ac drives," which is represented by the motors along the diagonal of Fig. 1. This family enjoys a high degree of uniformity of motor and controller component parts while offering a wide range of performance characteristics [9] obtained by changing only the motor rotor and the control strategy. The rotating field permits smooth torque and good operation down to low speeds, both of which are difficult to achieve in the switched reluctance motor. Unlike the switched reluctance motor, the synchronous motor is completely compatible with the stators and controllers of other ac motor drives.

To provide a shorter name and to distinguish it from the switched reluctance motor, the term SYNCHREL is used in this paper [12]. The design of a small SYNCHREL motor drive is described, and the performance is compared with those of a switched reluctance drive, an induction motor drive, and a brushless dc (BLDC) PM motor drive. The results presented are confined to the preliminary experimental findings of a study whose scope includes larger drives than the ones

<span id="page-1-0"></span>![](_page_1_Figure_2.jpeg)

Fig. 1. Family of motor types showing ac motors along the diagonal; the SYNCHREL motor is the center motor with magnets removed [9].

described here, as well as the optimization of lamination geometry and control parameters. It is planned that those results will be published later. Particular points of interest in the present paper are the comparison of motors of different types, all with essentially the same frame size and tested under identical conditions.

## II. BASIC THEORY

The inverter-fed SYNCHREL motor is freed from the old constraints of the line-start version as follows:

- No starting cage is necessary. The rotor can therefore be designed purely for synchronous performance.
- Electronic control makes the motor autosynchronous.
   Therefore, the torque angle can be set to maximize torque per ampere at all loads and speeds without concern for pullout.
- There is no need for amortisseur currents to prevent rotor oscillations. This makes it possible to design for the highest possible ratio of the synchronous reactances X<sub>a</sub> and X<sub>d</sub> without concern for stability.

Because the SYNCHREL motor is a classical synchronous machine, its electromagnetic torque is given by (1), where  $I_d$  and  $I_q$  are components of the rms phase current I resolved along the d and q axes of the phasor diagram; they correspond to the space-vector components of stator mmf along

![](_page_1_Picture_11.jpeg)

Fig. 2. Phasor diagram of SYNCHREL motor.

the d and q axes of the rotor:

$$T = \frac{m}{2} p I_d I_q (L_q - L_d). \tag{1}$$

Here, m is the number of phases, p is the number of pole-pairs, and  $L_d$  and  $L_q$  are the direct- and quadrature-axis synchronous inductances, respectively. Note that  $X_d =$  $2\pi f L_d$  and  $X_q = 2\pi f L_q$ , where f is the frequency. The torque is independent of speed, provided that the voltage is boosted above the constant volts per Hertz level to compensate for resistive voltage drop at low speed. The torque per ampere is maximized if the phase current is oriented at 45° to the q axis so that  $I_d$  and  $I_q$  are equal in magnitude. Since  $L_d < L_a$ ,  $I_d$  must be negative, and therefore, the current leads the q axis in the phasor diagram (Fig. 2). Note that the convention adopted here, in which the q axis is the highinductance axis, is contrary to the convention used in the literature on the line-start reluctance motor. This is because the particular motors in this paper are related to the interiormagnet hybrid motor in which the magnet axis is the lowinductance axis; it is more consistent with classical synchronous machine theory to make this the d axis.

Equation (1) is the starting point for designing the rotor lamination. Evidently the saliency (i.e., the difference  $L_a$  $L_d$  or the ratio  $L_a/L_d$ ) must be maximized but within constraints set by manufacturability. It is interesting to consider the theoretical limits to the saliency. For a four-pole motor with sinusoidally distributed windings, if the rotor is removed, the rotating magnetic field has the form of Fig. 3. By suitable choice of time origin, the q axes can be aligned with the reference axes of the flux so that all the flux is q-axis flux, and the d-axis flux is zero. The saliency in this flux pattern is therefore infinite. Now, the objective is to design a rotor that can be introduced into this field without disturbing its shape. Since the rotor must be ferromagnetic, it must present infinite permeance to q-axis flux and zero permeance to d-axis flux. The obvious way to achieve this is to make an axially laminated rotor in the fashion described by Cruickshank [2] in which the laminations are shaped to follow the flux lines in Fig. 3 and are separated by flux barriers that inhibit the d-axis flux in such a way that if the rotor were rotated 90 electrical degrees relative to the stator mmf the flux would fall to zero. This construction (Fig. 3) is perhaps the natural way to attempt to construct a reluctance rotor with infinite saliency, but in practice, the flux-barriers are not impermeable, and the saliency is finite.

Assume that the laminations and flux barriers are everywhere very thin, and let t be the average ratio of flux-barrier thickness to the combined thickness of lamination and flux barrier. Then, 1/(1-t) is a measure of the flux concentra-

<span id="page-2-0"></span>![](_page_2_Picture_2.jpeg)

**Fig. 3. "Natural" four-pole field of sine-distributed current sheet representing the stator winding, aligned with the** *q* **axis. The shaded sections represent flux guides interspersed with flux barriers whose surfaces follow the natural flux lines of the field. This structure was used by Cruickshank** *et al.* **[2] in their line-start reluctance motor. Because of symmetry, only one octant is shown.** 

tion that occurs in the laminations owing to the loss of cross section to the flux barriers. For a peak airgap flux density of 0.8 T and a saturation density of around 1.7 T, *t* must be limited to the order of 0.5. Now, the synchronous reactance *X,* is inversely proportional to the airgap length *g,* and by the methods of **[9],** it can be shown that *Xd* is inversely proportional to the *sum* of g and the combined thickness of the flux barriers, which is very roughly equal to *tR,* where *R* is the rotor radius. Therefore, the saliency is given approximately by

$$\frac{X_q}{X_d} = \frac{(tR+g)}{g} = \frac{tR}{g} + 1. \tag{2}$$

With *t* = 0.5 and *R /g* typically about *50,* this indicates a maximum saliency of about 25. Values achieved in practice are usually much smaller (generally no more than 10-15), partly because of leakage inductance, which effectively adds a "swamping term" to both the numerator and denominator of (2) and partly because of saturation. Nevertheless, this simple line of reasoning indicates some fundamental bounds to the achievement of high saliency and illustrates some of the factors that are important.

The axially laminated rotor is not easy to manufacture. **A**  transverse lamination with the pattern of flux barriers shown in Fig. **3** would also be difficult to make by punching; individual laminations would be flimsy and difficult to handle. The geometry of Fig. 4 is a compromise. It can be regarded as having just one flux barrier. If this is rectangular, it can accommodate a permanent magnet, providing a simple means for enhancing the performance of a small motor when necessary. With the magnets, the motor is an *interior magnet* or *buried magnet* motor, which is sometimes also called a *hybrid* PM/reluctance motor (PMH motor). The **SYN-CHREL** motors in this paper are all of this type.

In evaluating a series of rotor designs, **the** linear magnetic theory developed in **[9]** was used to calculate values of *Ld*  and *L,* in terms of dimensions, turns, etc. The values were checked against finite-element calculations and both ac and dc measurements [ **121.** 

## 111. **EVOLUTION** OF **THE DESIGN**

Three rotors have been built, and the cross sections of two of these are shown in Fig. 4. The pole pieces are held by two

![](_page_2_Picture_11.jpeg)

![](_page_2_Picture_12.jpeg)

**(b) 1; (b) rotor 2. Fig. 4. Transversely laminated single-barrier SYNCHREL rotors: (a) Rotor** 

**Rotor2** 

![](_page_2_Picture_14.jpeg)

**Fig 5. Components of hybrid synchronous reluctance/PM motor showing optional permanent magnets.** 

thin ribs that attach to the *q* axis webs in the same way as in the interior magnet motor described by Jahns, *et al. [5].* Fig. *5* shows the components of the disassembled motor.

To minimize *Ld,* the ribs (Fig. 4) must saturate at a low level of current. This requires them to be radially thin. *L,* is not sensitive to the airgap length because of the large reluctance in the flux barrier. *L,* must be maximized; therefore, saturation is undesirable in any part of the q-axis flux path. Therefore, the pole piece needs to have adequate radial

TABLE I

| Parameter                                       | Rotor 1   | Rotor 2   |
|-------------------------------------------------|-----------|-----------|
| Pole arc (°)                                    | 68.0      | 62.3      |
| Rotor Diameter (mm)                             | 40.5      | 41.1      |
| Airgap length (mm)                              | 0.45      | 0.15      |
| Rib width (mm)                                  | 0.5       | 0.5       |
| Web width (mm)                                  | 1.0       | 2.5       |
| Flux-barrier thickness (mm)                     | 5.4       | 5.4       |
| Rotor material                                  | Losil 800 | Losil 800 |
| L <sub>d</sub> [measured] (mH)                  | 10.8      | 10.3      |
| L <sub>d</sub> [finite-element] (mH)            | 10.2      | 11.3      |
| L <sub>q</sub> [measured] (mH)                  | 28.3      | 41.0      |
| L <sub>a</sub> [finite-element] (mH)            | 27.7      | 50.3      |
| Ratio L <sub>a</sub> /L <sub>d</sub> [measured] | 2.6       | 4.0       |

depth, and the web needs to be sufficiently wide as well. Rotor 1 (Fig. 4(a)) was designed to accommodate 5.4-mmthick magnets, and for operation as a SYNCHREL motor, the webs are too narrow; therefore, they were widened in rotor 2. With 16 slots, this ensures that the web does not saturate when aligned with the axis of the phase winding. The parameters of the two rotors are summarized in Table I and [12]. The inductances quoted in Table I were measured and calculated at 3.0 A.

The synchronous inductance ratios quoted in Table I are all well below the theoretical limit of 25 mentioned earlier. This is because saturation decreases the q-axis inductance, whereas leakage through the ribs increases the d-axis inductance. It is the price paid for the convenience of a lamination that has a simple punching geometry and the ability to accommodate magnets when required. However, as stated earlier, an object of the investigation is to determine whether acceptable performance is obtainable while retaining these features.

Fig. 6(a) and (b) show typical d- and q-axis finite-element flux plots. The calculation of magnetization curves is a straightforward exercise of the finite-element method [18] once the magnetization characteristics of the core steel are accurately known. Fig. 7 shows measured magnetization curves for rotor 1, clearly showing the effect of saturation on the inductance ratio. Fig. 8 shows the running torque of both rotors as a function of rms phase current. The calculated curves were obtained from equation (1) and  $L_d$  and  $L_g$  taken from the appropriate magnetization curves at the appropriate current level. This calculation is approximate, but it reflects the general trend and underlines the superiority of rotor 2 with its higher inductance ratio. The torques in Fig. 8 were measured at a low speed in order to minimize the effects of windage and core losses and provide data for the comparison described in Section V.

## IV. ELECTRONIC CONTROL

The configuration of the electronic control for two-phase motor is shown in Fig. 9. A 360-pulse magnetoresistive encoder mounted on the motor shaft generates an indexed pulse count representing the rotor position. This count is used to address two EPROM's: one for the d axis and one for the q axis. The EPROM's contain sine and cosine values multiplied in MDAC's by the reference or command value of the phase current. These analog signals are used as references for

![](_page_3_Picture_9.jpeg)

![](_page_3_Picture_10.jpeg)

Fig. 6. (a) D-axis flux plot showing operation of flux barrier and leakage through the ribs that hold the pole pieces in position. D-axis current = 3.0 A; (b) Q-axis flux plot. Q-axis current = 3.0 A.

![](_page_3_Figure_12.jpeg)

Fig. 7. Phase flux linkage versus current over a range of rotor positions between the d axis and the q axis; rotor 2.

two full H-bridge hysteresis-type current-regulators, one for each phase. Power integrated circuits operating at 40 V are used for the H bridges. In the simplest mode of operation, the current phase angle is set at a fixed value of 45 electrical degrees, and the motor is controlled entirely by its current reference with torque approximately proportional to current

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

Fig. 8. Running torque versus phase current. The points are measured; the lines are calculated (by (1), with inductances read from Fig. 6).

![](_page_4_Figure_4.jpeg)

Fig. 9. Electronic controller block diagram.

squared (Fig. 8). A speed loop can be added outside the feedforward torque regulator. A more sophisticated strategy is to control the orientation of the stator mmf vector according to the operating requirements, and provision is made in Fig. 9 for the addition of a phase-shift to vary the orientation.

## V. COMPARISON WITH INDUCTION, PM, AND SWITCHED RELUCTANCE MOTORS

Tests were performed to compare the SYNCHREL motor with several other brushless motors of different types. The dimensions and performance comparisons are summarized in Table II

So many different types of brushless motors are possible in this size range that it was not possible to test every one of the different types. In particular, no tests were performed on the classical brushless dc PM motor. However, it would be unfortunate to omit this machine because of its commercial importance, its simplicity, and its close theoretical relationship to the dc commutator motor, and therefore, a column of calculated results has been included in Table II for this machine (labelled BLDC). In a sense, these figures are 'purer' than measured results taken on a particular model because they are exactly defined and totally reproducible, and since this motor conforms well with relatively simple design calculations [9], [19], it is used here as the benchmark or per-unit base to which the parameters of all the other motors are normalized. The design equations used for this motor are given in full in [9], and Appendix I contains details of the design. Fig. 10 shows the cross section of this motor. Note that the slots are rectangular, whereas all the ac motors in Table II have round-bottom slots, as is shown in Fig. 4.

## A. Description of Motors Tested

Column 1 contains the calculated "base" values for the brushless dc PM motor BLDC, which is assumed to have 180° magnet arcs, 120° rectangular phase current waveforms, and a wye-connected three-phase stator (Appendix I). Column 2 is the permanent-magnet hybrid (PMH-1) motor or "interior magnet" motor based on the SYNCHREL lamination (rotor 1) with NdFeB magnets of remanent flux density 1.1 T. This motor is labelled PMH-1. The dimensions of the magnets are identical to those in Column 3 (PMH-2), which is the PMH motor obtained by fitting *ceramic* magnets of remanent flux density 0.4 T to rotor 1 of Fig. 4(a). The BLDC motor in column 1 has the same magnet weight and the same ceramic magnet material as PMH-2.

Columns 4-7 are induction motors with airgaps ranging from 0.1 to 0.4 mm in steps of 0.1 mm to show the sensitivity of the performance to the airgap length, which is an important parameter in the cost of manufacture. For motors of this size and length/diameter ratio, 0.2 mm is a normal value for the airgap length.

Columns 8-10 are switched reluctance motors with airgaps ranging from 0.2 to 0.4 mm in steps of 0.1 mm to show the sensitivity of the performance to the airgap length. The controller for these machines is based on an integrated-circuit switched-reluctance drive control described in [20].

Column 11 is the SYNCHREL motor with rotor 1 (Fig. 4(a)). This is not the best of the SYNCHREL rotors, but it shows the effect of removing the magnets from the PMH-1 and PMH-2 interior-magnet motors in columns 2 and 3. Column 12 is the best of the SYNCHREL motors described in this paper, with rotor 2 (Fig. 4(b)). Both SYNCHREL motors, both PMH motors, and all the induction motors have exactly the same stator and windings.

All of the motors have four rotor poles, but the induction and SYNCHREL motors have two phases instead of three. This does not affect the performance. The SYNCHREL, PMH, and induction motors were operated with the current-regulated field-oriented PWM inverter described in Section IV. In the case of the two synchronous machines, the torque angle was adjusted experimentally to give maximum torque per ampere.

## B. Test Conditions

Because of differences in voltage, speed range, and lamination material between the motors, it was not considered meaningful to compare efficiencies directly. Instead, the performance parameter used for comparison was the torque at low speed, under conditions of equal *stator* copper loss in all the motors. The results have been normalized by calculation to the same copper weight (0.29 kg) in the stator windings. Results are summarized in Table II. Comparisons are made at a copper loss of about 14 W, which represents about two thirds of the dissipation capability of the (nonventilated, totally enclosed) frame for continuous rated operation with a temperature rise by resistance of about 55°C. Assuming that the copper losses are of the order of 2/3 of the total losses at maximum power, this also gives a rough idea of the performance comparison at maximum power.

Even minor differences in frame size, length/diameter

<span id="page-5-0"></span>![](_page_5_Picture_2.jpeg)

Fig. 10. Cross section of BLDC motor (see also Appendix I).

TABLE **I1**  MOTOR PERFORMANCE COMPARISON

| PARAMETER                                                                              | Un    | 1<br>BLDC | 2<br>PMH-1 | 3<br>PMH-2    | 4<br>IM-1        | 5<br>IM-2 | 6<br>IM-3   | 7<br>IM-4 | 8<br>SR-1 | 9<br>SR-2 | 10<br>SR-3 | 11<br>REL-1 | 12<br>REL-2 |
|----------------------------------------------------------------------------------------|-------|-----------|------------|---------------|------------------|-----------|-------------|-----------|-----------|-----------|------------|-------------|-------------|
|                                                                                        |       |           |            |               |                  |           |             |           |           |           |            |             |             |
| Phases<br>Poles                                                                        |       | 3<br>4    | 2<br>4     | 2<br>4        | 2<br>4           | 2<br>4    | 2<br>4      | 2<br>4    | 3         | 3         | 3          | 2<br>4      | 2           |
|                                                                                        |       |           |            |               |                  |           |             |           | 614       | 614       | 614        |             | 4           |
| Stator OD                                                                              | mm    | 77.0      | 77.8       | 77.8          | 77.8             | 77.8      | 77.8        | 77.8      | 73.7      | 73.7      | 73.7       | 77.8        | 77.8        |
| Rotor OD                                                                               | mm    | 40.6      | 40.6       | 40.6          | 40.6             | 40.6      | 40.6        | 40.6      | 35.5      | 35.3      | 35.1       | 40.5        | 40.0        |
| Stack Lgth                                                                             | mm    | 50.0      | 50.0       | 50.0          | 50.0             | 50.0      | 50.0        | 50.0      | 44.5      | 44.5      | 44.5       | 50.0        | 50.0        |
| O/A Length                                                                             | mm    | 86.0      | 90.0       | 90.0          | 90.0             | 90.0      | 90.0        | 90.0      | 74.0      | 74.0      | 74.0       | 90.0        | 90.0        |
| Airgap                                                                                 | mm/lO | 4.0       | 4.5        | 4.5           | 1.0              | 2.0       | 3.0         | 4.0       | 2.0       | 3.0       | 4.0        | 4.5         | 2.0         |
| Stator Cu                                                                              | kg    | 0.29      | 0.29       | 0.29          | 0.29             | 0.29      | 0.29        | 0.29      | 0.29      | 0.29      | 0.29       | 0.29        | 0.29        |
| Magnet                                                                                 | kg    | 0.11      | 0.16       | 0.11          |                  |           |             |           |           |           |            |             |             |
| Steel                                                                                  | kg    | 0.80      | 1.28       | 0.98          | 1.25             | 1.25      | 1.24        | 1.24      | 0.94      | 0.94      | 0.94       | 1.28        | 1.28        |
| Total wt.                                                                              | kg    | 1.20      | 1.73       | 1.38          | 1.54             | 1.54      | 1.53        | 1.53      | 1.23      | 1.23      | 1.23       | 1.57        | 1.57        |
| Mat'l cost                                                                             |       | 2.0       | 13.3       | 2.1           | 2.0              | 2.0       | 2.0         | 2.0       | 1.6       | 1.6       | 1.6        | 1.8         | 1.8         |
| Inertia                                                                                | %     | 100       | 134        | 119           | 134              | 134       | 134         | 134       | 25        | 25        | 26         | 109         | 109         |
| Ohms/ph                                                                                | Ohm   | 2.9       | 1.9        | 1.9           | 1.9              | 1.9       | 1.9         | 1.9       | 2.9       | 2.0       | 2.9        | 1.9         | 1.9         |
| Current                                                                                | Arms  | 1.3       | 1.9        | 1.9           | 1.9              | 1.9       | 1.9         | 1.9       | 1.3       | 1.3       | 1.3        | 1.9         | 1.9         |
| P cu (st)                                                                              | W     | 14.1      | 13.6       | 13.7          | 13.7             | 13.7      | 13.7        | 13.7      | 14.3      | 14.3      | 14.3       | 13.7        | 13.7        |
| P Cu (ro)                                                                              | W     |           |            |               | 7.1              | 5.8       | 4.2         | 4.1       |           |           |            |             |             |
| Torque                                                                                 | mNm   | 329       | 702        | 295           | 280              | 250       | 180         | 150       | 346       | 256       | 188        | 109         | 250         |
| Torque                                                                                 | %     | 100       | 213        | 90            | 85               | 76        | 55          | 46        | 105       | 78        | 57         | 33          | 76          |
| T/Vr                                                                                   | %     | 100       | 213        | 90            | 85               | 76        | 55          | 46        | 155       | 116       | 86         | 33          | 78          |
| T/Vs                                                                                   | %     | 100       | 209        | 88            | 83               | 74        | 54          | 45        | 129       | 95        | 70         | 32          | 74          |
| T/Vtot                                                                                 | %     | 100       | 200        | 84            | 80               | 71        | 51          | 43        | 133       | 99        | 72         | 31          | 71          |
| T/J                                                                                    | %     | 100       | 159        | 75            | 63               | 57        | 41          | 34        | 414       | 307       | 220        | 30          | 70          |
| T/Weight                                                                               | %     | 100       | 147        | 78            | 66               | 59        | 43          | 36        | 102       | 76        | 56         | 25          | 58          |
| T/f Mat'l                                                                              | %     | 100       | 32         | 85            | 85               | 76        | 55          | 46        | 128       | 94        | 69         | 36          | 83          |
|                                                                                        |       |           |            |               |                  |           | Copper f/kg |           |           | > 4.0     |            |             |             |
| Note: PMH-1 has NdIGT-30H magnets (interior)<br>PMH-2 has Ceramic-8 magnets (interior) |       |           | Steel f/kg |               |                  | f0.5      |             |           |           |           |            |             |             |
|                                                                                        |       |           |            | Aluminum f/kg |                  |           | f4.0        |           |           |           |            |             |             |
| BLDC motor has Ceramic 8 magnets (surface mounted)                                     |       |           |            |               | Ceram. Mag. f/kg |           |             | f4.0      |           |           |            |             |             |
|                                                                                        |       |           |            |               |                  |           |             |           |           |           |            |             |             |

ratio, copper weight, airgap length, and other key parameters can significantly affect performance. The test data in Table I1 is unusual in that all the motors are very close in physical size and shape, and all the ac motors have exactly the same stator. This eliminates the need for adjustments to take account **of** differences in dimensions. The main adjustment that had to be made was to the results for the switched reluctance **(SR)** motors, which were tested as built with only 0.155 **kg** of copper in the stator windings and a very low slot-fill factor. Since the comparisons in Table I1 are constructed on the basis of equal stator copper losses, the performance of these motors had to be recalculated with almost double the amount of copper in the windings. The adjustment was performed using the computer-program **PC-SRD** [SI, and a careful study of the accuracy of these results indicates that the calculated torque with 0.29 kg of winding copper may be as much as 16% low. Moreover, no correction was made for the fact that the stack length **of** the SR motors was only 89% of that of the other motors. The **SR**  motor torques in Table I1 are therefore underestimated by as much as 25%, but because these figures have not been directly verified by test, the conservative adjusted values are used in Table 11.

NdFeB Mag. f/kg E7 *.O* 30-Oct-90

The results are valid only for small motors similar in size

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Fig. 11. Continuous low-speed torque of 78-mm-diameter brushless motors at the same stator copper loss with equal stator copper weights.** 

![](_page_6_Figure_4.jpeg)

**Fig. 12. Torque/inertia ratio of 78-mm-diameter brushless motors at the same stator copper loss with equal stator copper weights, expressed as a percentage of the torque/inertia ratio of the BLDC motor in Column 1.** 

to the ones tested, i.e., in the 50-200-W range or so. Extrapolation up to larger powers is unlikely to be meaningful.

## *C. Performance Comparison*

**A** selection of results from [Table I1](#page-5-0) is plotted in Figs. 11-13.

*1)Torque:* Fig. 11 shows the continuous torque capability of each type **of** motor relative to the BLDC motor torque. The PMH-1 motor has the "unfair" advantage of high-energy magnets, which explains its high torque capability. When fitted with the same volume of the same ceramic magnet material, the interior-magnet motor (PMH-2) produces only about 90% of the BLDC motor torque and only 14% more than the **SYNCHREL** motor REL-2.

Even with an airgap of 0.1 mm, the induction motor produces only 85% of the BLDC motor torque, and it also has the penalty of 7.1 W of rotor losses that are not included in the "equal stator copper loss" criterion. When the airgap is increased to the more manufacturable value of 0.2 mm, the

![](_page_6_Figure_11.jpeg)

**Fig. 13. Torque per unit of material cost of 78-mm-diameter brushless motors at the same stator copper loss with equal stator copper weights, expressed as a percentage of the torque per unit material cost of the BLDC motor in Column 1.** 

torque is reduced to 76 % , and if the total losses were reduced to the same level as in the BLDC motor, the torque would be derated to only about 50%. This result is entirely expected: Small induction motors suffer seriously from excessive magnetizing current and slip losses, and the results merely highlight the known advantage of PM and synchronous motors. As the airgap is increased still further, the torque falls off rapidly. At 0.4 mm (the same airgap as used in the BLDC motor), the induction motor torque is only 46%, even before the derating due to rotor losses is applied.

The switched reluctance motor also suffers from this inverse relationship between torque (at constant copper loss) and airgap length, but in this case, there is no slip loss, and the degradation is due to increased excitation requirements as the airgap increases. With constant stator copper loss, the relative rate of degradation is very roughly the same as in the induction motor. The SR motor produces some 30% more torque than the induction motor with the same airgap but without any significant rotor losses. Torque parity with the BLDC motor is achieved only with a 0.2-mm airgap. The SR motor cannot tolerate the large airgap (0.4 mm) of the BLDC motor; with a 0.4-mm gap, its torque is only 57%. It was observed in testing that the SR motor was the noisiest motor, even at the preadjustment torque level (around 200 mNm for SR-1 with 0.155 kg of copper). If this motor is actually operated at 346 mNm, it is excessively noisy even though it is still operating far below its theoretical electromagnetic capability.

The **SYNCHREL** motor REL-1 in column 11 is included to show the effect of removing the magnets from PMH-1 or PMH-2; there is a marked reduction in torque to 33%, and again, the large airgap of the BLDC motor cannot be tolerated. The motor REL-2 (column 12, using rotor 2 of Fig. 4(b)) has much better performance (76%) and even outperforms the induction motor IM-2 with the same airgap length. Moreover, it does this with negligible rotor losses. Although the torque is lower than the 105% of SR-1 with the same airgap length, it **is** comparable with the 78% of the SR-2

motor, and if these motors had to be designed for the same noise level, the SYNCHREL motor REL-2 would be competitive. It has the further advantage of using a standard induction-motor stator.

- 2) Torque/Inertia Ratio (T/J): Fig. 12 shows the torque/inertia ratio based on the continuous torque capability. (Transient torque capability was not evaluated.) The high value for the SR motor is mainly due to its low inertia, which results from the small rotor diameter and the removal of material between the rotor poles. The SYNCHREL motor REL-2 has about 20% better T/J than the induction motor IM-2 but only 70% of that of the BLDC motor.
- 3) Torque / Material Cost Ratio: Fig. 13 shows the torque per unit of material cost based on the per-kilogram costs of materials given in Table II. These costs are approximate and somewhat variable, but they do give an additional insight. The PMH-1 motor is clearly penalized by the high cost of its magnet material. Otherwise, the only motor to excel the BLDC motor is the switched-reluctance SR-1 motor. The SYNCHREL motor REL-2 is a few percent more economical than the induction motor IM-2, but both are 15-20% less cost effective than the BLDC motor.

#### VI. CONCLUSION

A simple synchronous reluctance (SYNCHREL) motor using a 78-mm-diameter induction motor stator and fixed-phaseangle variable-frequency control produces an efficient synchronous motor drive with approximately 50% more torque than the induction motor in the same stator based on equal total motor losses. The low-speed torque is about 30% lower than that of a switched reluctance motor having the same framesize, airgap length, and copper weight; however, in other respects, the quieter SYNCHREL motor has many of the attractive features of the switched reluctance motor-freedom from permanent magnets, high-temperature and high-speed capability, freedom from parameter variations due to temperature, etc. It also uses standard ac motor parts and sinewave control. Calculations show that the SYNCHREL motor as described in this paper cannot equal the torque of the brushless dc motor with ferrite magnets in this size range, even on the basis of torque per unit material cost; neither can it tolerate the large airgap length of the BLDC motor. However, if manufacturing cost is taken into account, the syn-CHREL motor is quite competitive because of its simple rotor and the common induction motor stator.

These results have been achieved with a single flux-barrier design capable of accommodating permanent magnets. The inductance ratio is much smaller than theoretically possible in a pure synchrel motor, and much better results would be expected with an axially laminated construction or equivalent.

The comparison of motor types underlines the superiority of the PM brushless dc motor in raw torque production at low speed and its ability to tolerate a large airgap length. The comparison also highlights the weakness of the induction motor in this small size range. The advantage of the syn-CHREL motor is that it uses a standard induction-motor stator and provides a synchronous, efficient drive with parameters

independent of temperature and freedom from demagnetization and other magnet-related problems. Although the performance is exceeded by the switched reluctance (SR) motor, the SR motor has the disadvantage of a higher noise level and higher torque ripple, and it cannot use a standard ac motor

These conclusions cannot be extrapolated to larger motors because the effects of scale are too nonlinear. Future plans include the extension to integral-horsepower motors [16] and the investigation of small motors with much higher inductance ratios.

#### APPENDIX

#### PARAMETERS OF BLDC MOTOR DESIGN

| Stator/rotor diameters       | 77/50 mm              |
|------------------------------|-----------------------|
| Airgap length                | 0.4 mm                |
| Stack length                 | 50 mm                 |
| Magnet thickness/pole arc    | 3.8 mm/180° elec      |
| Magnet/remanent flux-density | ceramic/0.329T        |
| Coercive force               | 269 kA/m              |
| Poles/slots/phases           | 4/24/3                |
| Tooth width                  | 2.5 mm                |
| Slot area                    | $61.5 \text{ mm}^2$   |
| Winding type                 | Lap, single layer     |
| Coil throw (slot pitches)    | 5                     |
| Turns in series per phase    | 200/0.6 mm dia        |
| Self/mutual inductance       | 12.7/1.8 mH           |
| Airgap flux density          | 0.246T (open circuit) |

Torque constant 0.2 Nm/ASpeed at test point 200 r/min

### ACKNOWLEDGMENT

Thanks are due to R. S. Boughton (Sherman Electromech), S. E. Wood (Brook Crompton Parkinson), P. Ibbotson (Watson Marlow), A. J. Hutton (Motorola), K. Debebe, I. Young, and J. Kelly of the University of Glasgow.

#### REFERENCES

- [1] P. J. Lawrenson and L. A. Agu, "Theory and performance of polyphase reluctance machines," *Proc. Inst. Elec. Eng.*, vol. 111, pp. 1435-1445, 1964.
- A. J. O. Cruickshank, A. F. Anderson, and R. M. Menzies, "Axially laminated anisotropic rotors for reluctance motors," Proc. Inst.
- Elec. Eng., vol. 113, pp. 2058-2060, 1966.

  W. Fong, and J. S. C. Htsui, "New type of reluctance motor," Proc. Inst. Elec. Eng., vol. 117, pp. 545-551, 1970.
- V. B. Honsinger, "Steady-state performance of reluctance machines," IEEE Trans. Power App. Syst., vol. PAS-90, pp. 305-317, 1971.
- T. M. Jahns, G. B. Kliman, and T. W. Neumann, "Interior magnet synchronous motors for adjustable-speed drives," *IEEE Trans. In*dustry Applications, vol. IA-22, pp. 738-747, 1986.
- T. Fukao, "Principles and output characteristics of super high-speed reluctance generator system," *IEEE Trans. Industry Applications*, vol. IA-22, pp. 702-707, 1986.
- A. Frata and A. Vagati, "A reluctance motor for high dynamic performance applications," in Conf. Rec. 1987 IEEE Industry Applications Soc. Ann. Mtg., Part 1, pp. 295-302, Paper ID-87-24
- A. Chiba and T. Fukao, "A closed-loop control of super high-speed reluctance motor for quick torque response," in *Conf. Rec. 1987* IEEE Industry Applications Society Ann. Mtg., Part 1, pp. 289-294, Paper ID-87-23.
- T. J. E. Miller, Brushless Permanent-Magnet and Reluctance Motor Drives. Oxford: Oxford University Press, 1989
- [10] T. J. E. Miller and M. I. McGilp, "PC CAD for switched reluctance

- drives," in IEE Conf. Publ. 282, pp. 360-366, 1987.
- [11] P. J. Lawrence et al., "Variable-speed switched reluctance motors," Proc. Inst. Elec. Eng., vol. 127, pt. B, pp. 253-265, 1980.
  [12] T. J. E. Miller and K. Debebe, "Design of a synchronous reluctance
- [12] T. J. E. Miller and K. Debebe, "Design of a synchronous reluctance motor," in *PCIM MOTORCON Conf. Proc.* (Munich), June 6-8, 1989, pp. 69-83.
- [13] T. Lipo and L-Y Xu, "A novel converter-fed reluctance motor with high power density," in Symp. Electric Drives (Cagliari, Italy), June 1987, pp. 315-321.
- 1987, pp. 315-321.
  [14] L.-Y. Xu and T. Lipo, "Analysis of a variable speed singly-salient reluctance motor utilizing only two transistor switches," in Conf. Rec. 1988 IEEE Industry Applications Soc. Ann. Mtg., Part I, pp. 38-43.
- [15] T. J. E. Miller, P. G. Bower, R. C. Becerra, and M. Ehsani, "Four-quandrant brushless reluctance drive," in *Proc. IEE Conf. Power Electron. Variable-Speed Drives* (London), July 1988, pp. 273-276.
- [16] M. R. Harris and T. J. E. Miller, "Comparison of design and performance parameters in switched reluctance and induction motors," in *Proc. IEE Conf. Elect. Machines Drives* (London), Sept. 1989, pp. 303-307, CP310.
- [17] H. Jordan, Energy-Efficient Electric Motors and Their Application. New York: Van Nostrand Reinhold, 1983.
- [18] P. P. Silvester and D. Lowther, Computer-Aided Design in Magnetics. Springer-Verlag, 1986.
   [19] P. Pillay and R. Krishnan, "Modeling, simulation, and analysis of
- [19] P. Pillay and R. Krishnan, "Modeling, simulation, and analysis of permanent-magnet motor drives, Part II: The brushless DC motor drive," *IEEE Trans. Industry Applications*, vol. IA-25, pp. 274-279, Mar./Apr. 1989.
- [20] T. J. E. Miller, C. Cossar, and D. Anderson, "A new control IC for switched reluctance motor drives," in *Proc. IEE Conf. Power Electron. Variable Speed Drives* (London), July 17-19, 1990, pp. 331-335, CP324.

![](_page_8_Picture_13.jpeg)

T. J. E. Miller (SM'82) is a native of Wigan, UK. He was educated at Atlantic College and the Universities of Glasgow and Leeds, U.K.

He spent 20 years in industrial research and development, including eight years with General Electric Corporate Research and Development, Schenectady, NY, before becoming Titular Professor in Power Electronics at Glasgow University. He is author of two textbooks, numerous patents, and IEEE and IEE publications.

![](_page_8_Picture_16.jpeg)

**Alan Hutton** was born in Glasgow, Scotland, on April 29, 1966. He received the B.Eng. (Hons.) degree in electrical and electronic engineering from the University of Glasgow, Scotland, in 1987.

He has spent two years as a research assistant under the SPEED consortium at the University of Glasgow. He was engaged in the design of switched reluctance motors and drives and is about to submit for a Masters degree based on this work. He is presently working for Motorola in technical marketing.

Mr. Hutton is an associate member of the IEE.

![](_page_8_Picture_20.jpeg)

Calum Cossar was born in Hamilton, Scotland, on January 22, 1962. He received the B.Sc. (Hons.) degree in electrical and electronic engineering from the University of Glasgow, Scotland, in 1983.

He spent five years as a design engineer with Ferranti Defence Systems Ltd. and was involved in high-speed DSP in radar systems. For the last two years, he has been employed as a research technologist at the University of Glasgow. His field of interest is digital techniques in motor control.

![](_page_8_Picture_23.jpeg)

David A. Staton was born in Chesterfield, England, on July 29, 1961. He received the B.Sc. (Hons.) degree in electrical and electronic engineering from Trent Polytechnic, Nottingham, England, in 1983 and the Ph.D. degree from the University of Sheffield, England, in 1988.

From 1977 to 1984, he was employed by British Coal, who sponsored him while he was undertaking his B.Sc. degree. While at the University of Sheffield, he developed CAD software for permanent-magnet dc motors in collaboration with GEC

Electromotors Ltd. From 1988 to 1989, he was with the Thorn EMI Central Research Laboratories and was engaged in the design of motors for the Kenwood range of food processors. Over the last year, he has been employed as a research assistant at the University of Glasgow and is involved in optimizing the design of synchronous reluctance motors.

Dr. Staton is an associate member of the IEE.