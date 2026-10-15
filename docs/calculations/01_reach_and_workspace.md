# Calculation 01: reach and workspace

**Evidence class legend:** MEASURED = taken by the builder with an engineering ruler; CODE = read from the submitted code; DATASHEET = manufacturer typical value; RECONSTRUCTED FROM VIDEO = estimated from demonstration-video frames (about +/-3 cm), not measured; ASSUMPTION = engineering assumption; CALCULATED = result of the equations below; NOT VERIFIED = no physical test supports it.

**Question.** How far can the gripper tip reach, at the pick height, the drop height and table level?

**Given.** Shoulder axis height H = 13.5 cm, upper arm L1 = 15 cm, forearm plus closed claw to tip L2 = 15 cm (MEASURED, engineering ruler). Pick tip height 22 cm and drop tip height 10 cm (RECONSTRUCTED FROM VIDEO).

**Assumptions.** (1) The arm is a planar two-link chain in the vertical plane, rotated about the vertical base axis. (2) Links are rigid. (3) The claw tip is the end point. (4) Mechanical joint limits are not applied (NOT PROVIDED).

**Equation.** Maximum 3D reach from the shoulder axis: R = L1 + L2. Maximum horizontal distance at tip height z: r_max(z) = sqrt(R^2 - (z - H)^2).

**Substitution.**
- R = 15 + 15 = 30 cm
- z = 22 cm: r_max = sqrt(900 - (8.5)^2) = sqrt(900 - 72.25) = 28.77 cm
- z = 10 cm: r_max = sqrt(900 - (-3.5)^2) = 29.80 cm
- z = 0 cm (table): r_max = sqrt(900 - (-13.5)^2) = 26.79 cm
- Minimum reach: |L1 - L2| = 0 cm geometrically (practical minimum depends on joint limits, NOT PROVIDED).

**Result.** Maximum 3D reach 30 cm; horizontal reach 28.8 cm at 22 cm height, 29.8 cm at 10 cm, 26.8 cm at table level. Units: cm.

**Interpretation.** The 60 x 60 cm figure is the board, not the arm's reach. The tip can cover a half-disc of radius about 27-30 cm about the base axis.

**Design consequence.** A pick target more than 28.8 cm from the base axis (at 22 cm height) cannot be reached. The first video reading of the pick (36, 32, 22 from base (10, 18)) is 29.53 cm away horizontally, which is 0.73 cm beyond reach in 3D (see calculation 02).

**Verification status.** CALCULATED. NOT VERIFIED: no physical reach measurement exists.
