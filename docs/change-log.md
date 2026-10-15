# Change log and thesis-versus-evidence review

The submitted thesis was **not edited**. This log records every place where the repository differs from the thesis, what was found, and why.

| ID | Where in thesis | Before (thesis) | Finding | After (repository) |
|---|---|---|---|---|
| C-01 | 3.1 DH table, forward and inverse kinematics examples | Example forward kinematics returns (-15, -15, 34.5) cm; pick angles (26.57, -2.13, 125.74) deg for target (33.96, -0.24, 37.07); drop angles (56.31, 6.29, 135.64) deg for (5.15, 10.19, 31.35) | With the printed DH table the example returned (41.4, 1.9, 5.6) cm; the printed pick and drop angles landed 275-534 mm and 314-331 mm from their targets; the 34.5 equals 13.5 + 9 + 12, the sum of offsets. ENGINEERING REVIEW REQUIRED. The author's 13 pages of hand working were not provided. | Recomputed with three methods: [01](calculations/01_reach_and_workspace.md) and [02](calculations/02_inverse_kinematics_pick_drop.md). |
| C-02 | 4.1 workspace "60 cm by 60 cm" | Read as the workspace | It is the board size. Reach radius is about 27-30 cm. | [01](calculations/01_reach_and_workspace.md) |
| C-03 | 4.x payload / torque calculation | Mixed units, arm weight added to payload, 0.0188 vs 0.170 kg, 9.49 vs 9.4, joint 1 torque 13.31 vs datasheet 11 | Not dimensionally consistent. ENGINEERING REVIEW REQUIRED. | [03](calculations/03_payload_and_torque.md) |
| C-04 | 3.2 alarm pins | LEDs D3/D4, buzzer D5 | Code uses LEDs D2-D5, buzzer D6 | hardware/wiring-and-pins.md follows the code |
| C-05 | 3.1 arm board | Uno (text) vs Nano (Figs 3.2, 3.3) | Nano in design and first build, Uno in the final build | ADR-01, F-01 |
| C-06 | Abstract, 4.1.4, 5.1 "machine learning" | Learned and optimised the task | No learning algorithm in the code. The author says it meant storing and replaying moves. | Described as teach-and-repeat |
| C-07 | 3.1, 4.1.5 inverse kinematics "in Arduino code" | Implemented, handles out-of-reach targets | No IK in the code; the arm is pot-driven. Analysis is offline. | Not claimed |
| C-08 | 3.1, 4.1.2, 4.3, 1.4 | Interchangeable suction/magnetic grippers; emergency stop; collision detection pausing the arm; fuses, bearings, bushings | Not found in code or parts list | Not claimed; listed as future work |
| C-09 | 4.1.3 "<1% positional error" | Stated as a result | No data | NOT VERIFIED; [04](calculations/04_resolution_and_tip_error.md) |
| C-10 | 3.3.2 power | 5 V 3 A for servos 1-2; 12 V for servo 3 and VIN | Author gave differing accounts later; servo 3 on 12 V exceeds the 4.8-7.2 V rating | Conflict recorded in hardware/power.md |
| C-11 | Figs 3.3, 3.6 resistors | All "0R1" | Placeholder. Author reports 1 kohm on alarm LEDs. | 1 kohm per author; pull-down values NOT PROVIDED |
| C-12 | Fig 3.6 | Four LEDs, two buzzer symbols, no button | Code: four LED pins, one buzzer pin, a reset button; author recalls three lights | Code followed; fitted count NOT RECONCILED |
| C-13 | Alarm code comment | "5 microsecond pulse" | Code sends 10 microseconds | Noted, code unchanged |
| C-14 | 4.1.2 object | "PET preform" (earlier account) | Author now says PET bottle, 27 g, 70-73 mm, figures from the seller's website | Bottle; figures labelled manufacturer data |
| C-15 | Repository calculations | Pick point (34.7, 31.3, 22) shifted to fit reach | Retracted; shifting a measured point to fit the maths is not acceptable | Four test distances plus ranges; first reading (36, 32, 22) reported as 0.73 cm out of reach |
| C-16 | Earlier conversation | Blown board linked to regulator overload | Retracted: cause was a wrong wire | F-01 |
| C-17 | Reference list | Includes unrelated health and water-carrying papers; years differ | NOT VERIFIED | references.md |
