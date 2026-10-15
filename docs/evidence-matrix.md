# Evidence matrix

Status words: DEMONSTRATED (owner observation plus visual evidence), IMPLEMENTED / NOT VERIFIED (code or build exists, no test data), CALCULATED, NOT FOUND (no code or evidence), NOT VERIFIED.

| Claim | Evidence | Status | Location |
|---|---|---|---|
| The arm records up to 10 poses and replays them | Code; owner testing with about 8-9 poses; demo frames | DEMONSTRATED (qualitative) | firmware/arm_controller, testing.md T-01 |
| Replay loops continuously until power-off or reprogramming | Code; owner statement; about 6 cycles counted in the video (owner-stated) | DEMONSTRATED (qualitative), cycle log NOT PROVIDED | testing.md |
| The arm carried a 27 g PET bottle from pick to drop | Owner statement; frames | DEMONSTRATED (qualitative); mass is a manufacturer figure, not weighed | testing.md |
| Reach is 30 cm from the shoulder axis | Measured link lengths plus calculation | CALCULATED | calculations/01 |
| Pick and drop are reachable | Calculation on positions reconstructed from video | CALCULATED; positions not measured | calculations/02 |
| Inverse-kinematics method is correct | Three independent methods plus forward-kinematics check | CALCULATED, method verified | calculations/02, kinematics_appendix.md |
| Smooth payload about 111-138 g, stall limit 268-321 g | Datasheet torque plus calculation | CALCULATED; foam mass excluded; no payload test | calculations/03 |
| Positional error under 1% (thesis) | None | NOT VERIFIED | calculations/04 |
| Alarm triggers inside 50 cm | Code | IMPLEMENTED / NOT VERIFIED | firmware/security_alarm |
| Machine learning (thesis) | No algorithm in code; author says it meant storing and replaying moves | NOT FOUND as machine learning | change-log.md C-06 |
| Inverse kinematics in the Arduino code (thesis) | None in code | NOT FOUND | change-log.md C-07 |
| Interchangeable grippers: suction, magnetic (thesis) | Only the SG90 claw in code and parts list | NOT FOUND | change-log.md C-08 |
| Emergency stop; collision detection pausing the arm (thesis) | None in code | NOT FOUND | change-log.md C-08 |
| Foam structure showed no deformation (thesis) | No data | NOT VERIFIED | technical-debt.md |
| Power layout | Thesis 3.3.2 and three differing author accounts | CONFLICT, NOT VERIFIED | hardware/power.md |
