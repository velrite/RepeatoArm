# RepeatoArm: Pick-and-Drop Kinematics, Three-Method Verification

> **Status labels used in this repository:** MEASURED (author, engineering ruler), CODE (read from the firmware), DATASHEET (manufacturer typical value), CALCULATED, ASSUMPTION, NOT PROVIDED, NOT VERIFIED, IMPLEMENTED / NOT VERIFIED. Pick and drop positions are reconstructed from video (about plus or minus 3 cm), not measured.


*Calculation appendix. Every number below is printed by `kinematics_check.py` (same folder). Re-run it to reproduce.*

## 1. What this appendix shows

The arm's pick and drop poses were checked with **three independent inverse-kinematics methods**, and each answer was then put back through a **forward-kinematics check built from 4x4 homogeneous transforms**. All methods agree. The pick and drop positions themselves were estimated from the demo-video frames (the physical arm was dismantled after submission), so they are given with their uncertainty, not as measured values.

## 2. Arm model and inputs

| Quantity | Value | Basis |
|---|---|---|
| Workspace board | 60 x 60 cm | measured by the builder |
| Shoulder axis height H | 13.5 cm | measured by the builder |
| Upper arm L1 (shoulder to elbow) | 15 cm | measured by the builder |
| Forearm + closed claw L2 (elbow to gripper tip) | 15 cm | measured by the builder |
| Maximum reach from shoulder axis | L1 + L2 = 30 cm | calculated |
| Arm base position on board | (10, 18) cm | estimated from demo-video frames, about +/-2.5 cm |
| Pick height (gripper tip, tower top) | 22 cm | estimated from demo-video frames, about +/-4 cm |
| Drop height (gripper tip, stand) | 10 cm | estimated from demo-video frames, about +/-4 cm |

**Angle definitions.** q1 = base bearing measured from the board's +X axis. q2 = upper-arm elevation above horizontal. q3 = forearm angle relative to the upper arm (negative = forearm bent downward, the 'elbow-up' solution). These are geometric joint angles, not the 10-170 degree servo commands, which depend on how each servo horn was mounted.

**Plane reduction.** The base turns the arm about the vertical axis, so the problem splits into (a) a bearing in the floor plane and (b) a two-link problem in the vertical plane, with floor distance r and height z measured from the base axis.

## 3. Test cases

The pick is near the edge of the arm's reach, and its position is only known to about +/-3 cm, so it is tested at four floor distances (24, 26, 28 cm and the exact full-stretch distance) along the bearing read from the video. The first reading taken from the video is also included.

| # | Case | Board x, y (cm) | z (cm) |
|---|---|---|---|
| 1 | Drop (stand) | 31.00, 13.00 | 10.0 |
| 2 | Pick - near | 31.13, 29.38 | 22.0 |
| 3 | Pick - mid | 32.89, 30.33 | 22.0 |
| 4 | Pick - far | 34.65, 31.27 | 22.0 |
| 5 | Pick - full stretch | 35.33, 31.64 | 22.0 |
| 6 | Pick as first read from video | 36.00, 32.00 | 22.0 |

## 4. Step-by-step working

### Formulas used

- **Floor plane:** dx = x - 10, dy = y - 18, r = sqrt(dx^2 + dy^2). Bearing three ways: atan2(dy, dx); sign(dy)*acos(dx/r); asin(dy/r).
- **Height and reach test:** dz = z - 13.5, D = sqrt(r^2 + dz^2). Reachable only if D <= 30.
- **Method 1, law of cosines:** cos q3 = (D^2 - L1^2 - L2^2) / (2 L1 L2); q3 = -acos(cos q3); q2 = atan2(dz, r) - atan2(L2 sin q3, L1 + L2 cos q3).
- **Method 2, circle intersection:** a = (L1^2 - L2^2 + D^2) / (2D); h = sqrt(L1^2 - a^2). The elbow is where the circle of radius L1 about the shoulder meets the circle of radius L2 about the target; take the higher intersection. Then q2 = atan2(Ez - 13.5, Er) and q3 = atan2(z - Ez, r - Er) - q2.
- **Method 3, numerical:** damped least-squares (Jacobian) iteration from an arbitrary start of (45, -30) degrees, with no closed-form formula used. Stops when the position residual is below 1e-6 cm.
- **Check, forward kinematics:** T = Rz(q1) . Trans(0,0,13.5) . Ry(-q2) . Trans(15,0,0) . Ry(-q3) . Trans(15,0,0). The translation part of T must equal the target.

### Case 1: Drop (stand)

**Step 1, floor plane.** dx = 31.00 - 10 = 21.000; dy = 13.00 - 18 = -5.000; r = sqrt(21.000^2 + -5.000^2) = 21.587 cm. Bearing: atan2 = -13.392, acos form = -13.392, asin form = -13.392 degrees.

**Step 2, reach test.** dz = 10.0 - 13.5 = -3.500 cm; D = sqrt(21.587^2 + -3.500^2) = 21.869 cm; limit 30 cm.

**Method 1 (law of cosines).** cos q3 = (21.869^2 - 15^2 - 15^2) / (2*15*15) = 0.06278; q3 = -86.401. alpha = atan2(-3.500, 21.587) = -9.209; beta = atan2(15 sin q3, 15 + 15 cos q3) = -43.200; q2 = alpha - beta = 33.991 degrees.

**Method 2 (circle intersection).** a = 10.934, h = 10.268; elbow E = (12.437, 21.886) cm in (r, z). q2 = atan2(21.886 - 13.5, 12.437) = 33.991; forearm direction = -52.410; q3 = -52.410 - 33.991 = -86.401 degrees.

**Method 3 (numerical).** Converged in 8 iterations, residual 1.7e-11 cm: q2 = 33.991, q3 = -86.401 degrees.

| Method | q1 base | q2 shoulder | q3 elbow | FK lands at (dx, dy, z) cm | FK error (mm) |
|---|---|---|---|---|---|
| 1 Law of cosines | -13.392 | 33.991 | -86.401 | (21.000, -5.000, 10.000) | 0.00000 |
| 2 Circle intersection | -13.392 | 33.991 | -86.401 | (21.000, -5.000, 10.000) | 0.00000 |
| 3 Numerical | -13.392 | 33.991 | -86.401 | (21.000, -5.000, 10.000) | 0.00000 |

Largest disagreement between the three methods: 0.000000 degrees. Target was (21.000, -5.000, 10.0).

### Case 2: Pick - near

**Step 1, floor plane.** dx = 31.13 - 10 = 21.131; dy = 29.38 - 18 = 11.378; r = sqrt(21.131^2 + 11.378^2) = 24.000 cm. Bearing: atan2 = 28.301, acos form = 28.301, asin form = 28.301 degrees.

**Step 2, reach test.** dz = 22.0 - 13.5 = 8.500 cm; D = sqrt(24.000^2 + 8.500^2) = 25.461 cm; limit 30 cm.

**Method 1 (law of cosines).** cos q3 = (25.461^2 - 15^2 - 15^2) / (2*15*15) = 0.44056; q3 = -63.861. alpha = atan2(8.500, 24.000) = 19.502; beta = atan2(15 sin q3, 15 + 15 cos q3) = -31.930; q2 = alpha - beta = 51.433 degrees.

**Method 2 (circle intersection).** a = 12.730, h = 7.933; elbow E = (9.351, 25.228) cm in (r, z). q2 = atan2(25.228 - 13.5, 9.351) = 51.433; forearm direction = -12.428; q3 = -12.428 - 51.433 = -63.861 degrees.

**Method 3 (numerical).** Converged in 6 iterations, residual 6.8e-12 cm: q2 = 51.433, q3 = -63.861 degrees.

| Method | q1 base | q2 shoulder | q3 elbow | FK lands at (dx, dy, z) cm | FK error (mm) |
|---|---|---|---|---|---|
| 1 Law of cosines | 28.301 | 51.433 | -63.861 | (21.131, 11.378, 22.000) | 0.00000 |
| 2 Circle intersection | 28.301 | 51.433 | -63.861 | (21.131, 11.378, 22.000) | 0.00000 |
| 3 Numerical | 28.301 | 51.433 | -63.861 | (21.131, 11.378, 22.000) | 0.00000 |

Largest disagreement between the three methods: 0.000000 degrees. Target was (21.131, 11.378, 22.0).

### Case 3: Pick - mid

**Step 1, floor plane.** dx = 32.89 - 10 = 22.892; dy = 30.33 - 18 = 12.327; r = sqrt(22.892^2 + 12.327^2) = 26.000 cm. Bearing: atan2 = 28.301, acos form = 28.301, asin form = 28.301 degrees.

**Step 2, reach test.** dz = 22.0 - 13.5 = 8.500 cm; D = sqrt(26.000^2 + 8.500^2) = 27.354 cm; limit 30 cm.

**Method 1 (law of cosines).** cos q3 = (27.354^2 - 15^2 - 15^2) / (2*15*15) = 0.66278; q3 = -48.488. alpha = atan2(8.500, 26.000) = 18.104; beta = atan2(15 sin q3, 15 + 15 cos q3) = -24.244; q2 = alpha - beta = 42.348 degrees.

**Method 2 (circle intersection).** a = 13.677, h = 6.159; elbow E = (11.086, 23.604) cm in (r, z). q2 = atan2(23.604 - 13.5, 11.086) = 42.348; forearm direction = -6.140; q3 = -6.140 - 42.348 = -48.488 degrees.

**Method 3 (numerical).** Converged in 5 iterations, residual 4.6e-07 cm: q2 = 42.348, q3 = -48.488 degrees.

| Method | q1 base | q2 shoulder | q3 elbow | FK lands at (dx, dy, z) cm | FK error (mm) |
|---|---|---|---|---|---|
| 1 Law of cosines | 28.301 | 42.348 | -48.488 | (22.892, 12.327, 22.000) | 0.00000 |
| 2 Circle intersection | 28.301 | 42.348 | -48.488 | (22.892, 12.327, 22.000) | 0.00000 |
| 3 Numerical | 28.301 | 42.348 | -48.488 | (22.892, 12.327, 22.000) | 0.00000 |

Largest disagreement between the three methods: 0.000004 degrees. Target was (22.892, 12.327, 22.0).

### Case 4: Pick - far

**Step 1, floor plane.** dx = 34.65 - 10 = 24.653; dy = 31.27 - 18 = 13.275; r = sqrt(24.653^2 + 13.275^2) = 28.000 cm. Bearing: atan2 = 28.301, acos form = 28.301, asin form = 28.301 degrees.

**Step 2, reach test.** dz = 22.0 - 13.5 = 8.500 cm; D = sqrt(28.000^2 + 8.500^2) = 29.262 cm; limit 30 cm.

**Method 1 (law of cosines).** cos q3 = (29.262^2 - 15^2 - 15^2) / (2*15*15) = 0.90278; q3 = -25.474. alpha = atan2(8.500, 28.000) = 16.887; beta = atan2(15 sin q3, 15 + 15 cos q3) = -12.737; q2 = alpha - beta = 29.624 degrees.

**Method 2 (circle intersection).** a = 14.631, h = 3.307; elbow E = (13.039, 20.915) cm in (r, z). q2 = atan2(20.915 - 13.5, 13.039) = 29.624; forearm direction = 4.150; q3 = 4.150 - 29.624 = -25.474 degrees.

**Method 3 (numerical).** Converged in 6 iterations, residual 4.5e-11 cm: q2 = 29.624, q3 = -25.474 degrees.

| Method | q1 base | q2 shoulder | q3 elbow | FK lands at (dx, dy, z) cm | FK error (mm) |
|---|---|---|---|---|---|
| 1 Law of cosines | 28.301 | 29.624 | -25.474 | (24.653, 13.275, 22.000) | 0.00000 |
| 2 Circle intersection | 28.301 | 29.624 | -25.474 | (24.653, 13.275, 22.000) | 0.00000 |
| 3 Numerical | 28.301 | 29.624 | -25.474 | (24.653, 13.275, 22.000) | 0.00000 |

Largest disagreement between the three methods: 0.000000 degrees. Target was (24.653, 13.275, 22.0).

### Case 5: Pick - full stretch

**Step 1, floor plane.** dx = 35.33 - 10 = 25.332; dy = 31.64 - 18 = 13.640; r = sqrt(25.332^2 + 13.640^2) = 28.771 cm. Bearing: atan2 = 28.301, acos form = 28.301, asin form = 28.301 degrees.

**Step 2, reach test.** dz = 22.0 - 13.5 = 8.500 cm; D = sqrt(28.771^2 + 8.500^2) = 30.000 cm; limit 30 cm.

**Method 1 (law of cosines).** cos q3 = (30.000^2 - 15^2 - 15^2) / (2*15*15) = 1.00000; q3 = -0.000. alpha = atan2(8.500, 28.771) = 16.459; beta = atan2(15 sin q3, 15 + 15 cos q3) = -0.000; q2 = alpha - beta = 16.459 degrees.

**Method 2 (circle intersection).** a = 15.000, h = 0.000; elbow E = (14.385, 17.750) cm in (r, z). q2 = atan2(17.750 - 13.5, 14.385) = 16.459; forearm direction = 16.459; q3 = 16.459 - 16.459 = 0.000 degrees.

**Method 3 (numerical).** Converged in 19 iterations, residual 9.9e-07 cm: q2 = 16.474, q3 = -0.029 degrees.

| Method | q1 base | q2 shoulder | q3 elbow | FK lands at (dx, dy, z) cm | FK error (mm) |
|---|---|---|---|---|---|
| 1 Law of cosines | 28.301 | 16.459 | -0.000 | (25.332, 13.640, 22.000) | 0.00000 |
| 2 Circle intersection | 28.301 | 16.459 | 0.000 | (25.332, 13.640, 22.000) | 0.00000 |
| 3 Numerical | 28.301 | 16.474 | -0.029 | (25.332, 13.640, 22.000) | 0.00001 |

Largest disagreement between the three methods: 0.029467 degrees. Target was (25.332, 13.640, 22.0).

### Case 6: Pick as first read from video

**Step 1, floor plane.** dx = 36.00 - 10 = 26.000; dy = 32.00 - 18 = 14.000; r = sqrt(26.000^2 + 14.000^2) = 29.530 cm. Bearing: atan2 = 28.301, acos form = 28.301, asin form = 28.301 degrees.

**Step 2, reach test.** dz = 22.0 - 13.5 = 8.500 cm; D = sqrt(29.530^2 + 8.500^2) = 30.729 cm; limit 30 cm.

**Result: NOT REACHABLE.** D exceeds the limit by 0.73 cm. Methods 1 and 2 report no solution. Method 3 does not converge: it stalls with 0.76 cm of position error left, about the same as the shortfall. This point lies within the reading error of the video estimate, so it shows the pick is at or very near full stretch.

## 5. Summary of results

| Case | Reachable | q1 (deg) | q2 (deg) | q3 (deg) | Method spread (deg) | Worst FK error (mm) |
|---|---|---|---|---|---|---|
| Drop (stand) | yes | -13.39 | 33.99 | -86.40 | 0.000000 | 0.00000 |
| Pick - near | yes | 28.30 | 51.43 | -63.86 | 0.000000 | 0.00000 |
| Pick - mid | yes | 28.30 | 42.35 | -48.49 | 0.000004 | 0.00000 |
| Pick - far | yes | 28.30 | 29.62 | -25.47 | 0.000000 | 0.00000 |
| Pick - full stretch | yes | 28.30 | 16.46 | -0.00 | 0.029467 | 0.00001 |
| Pick as first read from video | no (short by 0.73 cm) | 28.30 | n/a | n/a | n/a | n/a |

In the full-stretch case the arm is at a singularity (elbow straight), where a tiny position tolerance corresponds to a larger angle change; that is why Method 3 differs by a few hundredths of a degree there while still landing within 0.00001 mm of the target.

## 6. Uncertainty

The pick and drop positions are estimates (about +/-3 cm, base position about +/-2.5 cm, tip height about +/-4 cm). Because the joint angles depend on floor distance and height, not on the absolute board position, the results are given as ranges over that uncertainty:

| | Pick (tower) | Drop (stand) |
|---|---|---|
| Base bearing | 15 to 44 deg | -34 to 2 deg |
| Shoulder elevation | 16 to 53 deg | 14 to 53 deg |
| Elbow bend | 0 to 71 deg | 62 to 103 deg |
| Reachable cases in the grid | 81 of 90 | 90 of 90 |

The unreachable pick cases are the far and high corner of the grid, where the elbow would need to be past straight. The pick therefore sits near the arm's reach limit, and the drop sits comfortably inside it.

**Physical error budget.** The 0.00 mm residuals above show that the mathematics is self-consistent. They do not describe the physical arm, which is foam board with servo backlash and link flex. For a pick-like pose at 28 cm reach, 1 degree of error at one joint moves the gripper tip by: base 0.49 cm, shoulder 0.51 cm, elbow 0.26 cm; 1 degree at all three combined (root-sum-square) gives 0.75 cm. A positional accuracy of 1% of a 28 cm reach (0.28 cm) would need each joint to hold within about 0.4 degrees, so any accuracy figure should come from a repeatability test, not from this calculation.

## 7. What this does and does not establish

**Established:** the inverse-kinematics solution is mathematically correct (three independent methods agree and the forward-kinematics check closes); the drop pose is comfortably within reach; the pick pose is reachable only near full stretch, and the first video reading of the pick position lies 0.73 cm beyond the 30 cm limit, which is within the estimate's uncertainty.

**Not established:** exact pick and drop coordinates (estimated from video), the servo command values used in the demonstration, and the physical positioning accuracy of the foam-board arm.

## 8. Reproduce

```
pip install numpy
python kinematics_check.py
```
