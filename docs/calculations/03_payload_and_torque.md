# Calculation 03: payload and joint torque

**Evidence class legend:** MEASURED = taken by the builder with an engineering ruler; CODE = read from the submitted code; DATASHEET = manufacturer typical value; RECONSTRUCTED FROM VIDEO = estimated from demonstration-video frames (about +/-3 cm), not measured; ASSUMPTION = engineering assumption; CALCULATED = result of the equations below; NOT VERIFIED = no physical test supports it.

**Question.** Can the shoulder and elbow servos hold the 27 g PET bottle at full stretch, and what is the largest load they could carry?

**Given.** MG996R stall torque 9.4 kgf.cm at 4.8 V and 11 kgf.cm at 6.0 V, mass 55 g (DATASHEET, typical). SG90 claw servos 9 g each (thesis). Bottle mass 27 g (builder). L1 = L2 = 15 cm (MEASURED).

**Assumptions.** (1) Worst case: arm horizontal and fully stretched. (2) The elbow servo (55 g) sits at the elbow and the two claw servos (18 g total) at the tip. (3) The mass of the foam links is excluded because it is NOT PROVIDED. (4) "Smooth" load is taken as 50% of stall torque, a common engineering derating rule (ASSUMPTION). (5) Static torque only; no acceleration.

**Equations.** Torque at a joint = sum of (mass x distance). Maximum payload m = (T_available - T_fixed) / distance.
- Shoulder: T_fixed = m_elbow x L1 + m_claw x (L1 + L2); payload distance = L1 + L2
- Elbow: T_fixed = m_claw x L2; payload distance = L2

**Substitution.**
- Shoulder T_fixed = 0.055 x 15 + 0.018 x 30 = 0.825 + 0.540 = 1.365 kgf.cm
- Elbow T_fixed = 0.018 x 15 = 0.270 kgf.cm
- Bottle torque at the shoulder = 0.027 x 30 = 0.810 kgf.cm

**Result.**

| Supply | Case | Torque available (kgf.cm) | Shoulder limit (g) | Elbow limit (g) | Governing limit (g) |
|---|---|---|---|---|---|
| 4.8 V | stall limit | 9.40 | 268 | 609 | 268 |
| 4.8 V | smooth load (50%) | 4.70 | 111 | 295 | 111 |
| 6.0 V | stall limit | 11.00 | 321 | 715 | 321 |
| 6.0 V | smooth load (50%) | 5.50 | 138 | 349 | 138 |

At 4.8 V and 50% of stall, the 27 g bottle uses 24% of the governing limit, a safety factor of 4.1. Each 10 g of foam in the forearm (centred 22.5 cm out) removes about 7.5 g of payload; each 10 g in the upper arm (7.5 cm out) about 2.5 g. With 25 g in each link the smooth limit becomes 86 g.

**Interpretation.** The shoulder governs. The thesis's 280 g and 300 g figures are close to the stall limits, which are not sustained working loads.

**Design consequence.** Quote about 110 g (4.8 V) to 138 g (6.0 V) as the smooth working load before foam mass, and state the 27 g bottle as the demonstrated load.

**Verification status.** CALCULATED. NOT VERIFIED: no payload test was recorded. The thesis's printed torque calculation mixes units and adds arm weight to payload (ENGINEERING REVIEW REQUIRED).
