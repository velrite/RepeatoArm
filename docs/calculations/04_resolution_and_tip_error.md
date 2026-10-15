# Calculation 04: command resolution and tip error

**Evidence class legend:** MEASURED = taken by the builder with an engineering ruler; CODE = read from the submitted code; DATASHEET = manufacturer typical value; RECONSTRUCTED FROM VIDEO = estimated from demonstration-video frames (about +/-3 cm), not measured; ASSUMPTION = engineering assumption; CALCULATED = result of the equations below; NOT VERIFIED = no physical test supports it.

**Question.** How far does the gripper tip move for one degree of joint error, and what does that imply for the thesis's "<1% positional error" statement?

**Given.** The code writes integer degrees (1 degree steps) with the pots mapped from 0-1023 to 10-170 degrees (CODE). A pick-like pose at r = 28 cm, z = 22 cm, base bearing 28.3 degrees (RECONSTRUCTED FROM VIDEO). L1 = L2 = 15 cm, H = 13.5 cm (MEASURED).

**Assumptions.** Error from one joint at a time; effects combined by root-sum-square; no backlash or flex included (NOT PROVIDED).

**Equation.** Tip displacement from a 1 degree change at each joint, from the forward-kinematics model. Rounding to the nearest degree gives half of that.

**Substitution and result.**
- Base: 0.49 cm per degree; shoulder: 0.51 cm per degree; elbow: 0.26 cm per degree
- Combined (RSS): 0.75 cm per degree at all three joints
- Rounding to the nearest degree (+/-0.5 degree each): 0.38 cm, which is 1.3% of a 28 cm reach
- 1% of 28 cm = 0.28 cm, which is 0.57 degrees of base error alone, or about 0.37 degrees at each joint if all three contribute equally

**Interpretation.** Replay re-sends identical stored angles, so the commands repeat exactly. The physical position depends on servo dead band, backlash and link flex, none of which were measured.

**Design consequence.** A "<1%" claim needs measurement. The thesis gives no data for it, so it is NOT VERIFIED. A test procedure is in [repeatability-test.md](../repeatability-test.md).

**Verification status.** CALCULATED. NOT VERIFIED physically.
