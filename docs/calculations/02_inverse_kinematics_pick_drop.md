# Calculation 02: inverse kinematics for the pick and drop poses

**Evidence class legend:** MEASURED = taken by the builder with an engineering ruler; CODE = read from the submitted code; DATASHEET = manufacturer typical value; RECONSTRUCTED FROM VIDEO = estimated from demonstration-video frames (about +/-3 cm), not measured; ASSUMPTION = engineering assumption; CALCULATED = result of the equations below; NOT VERIFIED = no physical test supports it.

**Question.** What joint angles place the gripper tip at the pick and drop positions, and are those positions reachable?

**Given.** H = 13.5 cm, L1 = 15 cm, L2 = 15 cm (MEASURED). Base at (10, 18) cm on the 60 x 60 cm board (board MEASURED; base position RECONSTRUCTED FROM VIDEO, +/-2.5 cm). Pick tip at tower top, 22 cm; drop tip at stand, 10 cm (RECONSTRUCTED FROM VIDEO, +/-4 cm). The pick is tested at four distances because its position is only known to about +/-3 cm.

**Assumptions.** Planar two-link model; elbow-up solution; angles are geometric (q1 base bearing from +X, q2 upper-arm elevation, q3 forearm angle relative to upper arm, negative = bent down). These are not the 10-170 degree servo commands, whose zero position and direction are NOT PROVIDED.

**Equations (three independent methods, then a forward-kinematics check).** Full step-by-step working for every case, with the substitutions, is in [kinematics_appendix.md](../../calculations/kinematics_appendix.md).
- Method 1, law of cosines: cos q3 = (D^2 - L1^2 - L2^2) / (2 L1 L2); q2 = atan2(dz, r) - atan2(L2 sin q3, L1 + L2 cos q3)
- Method 2, circle intersection of the L1 circle about the shoulder and the L2 circle about the target
- Method 3, numerical damped least squares from an arbitrary start
- Check: 4x4 homogeneous-transform forward kinematics must return the target

**Result.**

| Case | Board x, y, z (cm) | Floor distance (cm) | q1 (deg) | q2 (deg) | q3 (deg) | Method spread (deg) | FK error (mm) |
|---|---|---|---|---|---|---|---|
| Drop (stand) | 31.00, 13.00, 10 | 21.59 | -13.39 | 33.99 | -86.40 | 0.000000 | 0.00000 |
| Pick near (r=24) | 31.13, 29.38, 22 | 24.00 | 28.30 | 51.43 | -63.86 | 0.000000 | 0.00000 |
| Pick mid (r=26) | 32.89, 30.33, 22 | 26.00 | 28.30 | 42.35 | -48.49 | 0.000004 | 0.00000 |
| Pick far (r=28) | 34.65, 31.27, 22 | 28.00 | 28.30 | 29.62 | -25.47 | 0.000000 | 0.00000 |
| Pick full stretch | 35.33, 31.64, 22 | 28.77 | 28.30 | 16.46 | -0.00 | 0.029467 | 0.00001 |
| Pick, first video reading | 36.00, 32.00, 22 | 29.53 | 28.30 | not reachable | not reachable | n/a | n/a |

**Interpretation.** The three methods agree and the forward check closes, so the mathematics is correct. The drop is well inside reach. The pick is reachable only close to full stretch, and the first video reading of its position is 0.73 cm out of reach, which is inside the reading uncertainty.

**Design consequence.** The pick sits near the reach limit, so small positioning errors matter most there. Because the pick position is estimated, results are given as ranges (see the appendix, section 6).

**Verification status.** CALCULATED. The method is verified by agreement between independent calculations. The physical angles used in the demonstration are NOT PROVIDED. The thesis's own printed inverse-kinematics numbers could not be reproduced from its stated table (ENGINEERING REVIEW REQUIRED, see the project change log).
