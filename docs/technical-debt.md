# Technical debt

**Known limitations.** See `limitations.md` (items 1-11).

**Missing tests.** No unit or integration tests; no repeatability, payload, accuracy, endurance or alarm-distance data.

**Hardware constraints.** MG996R operating range 4.8-7.2 V (datasheet); servo 3 recorded on 12 V. Foam links have unknown mass, stiffness and backlash. Gripper jaw gap and force NOT PROVIDED.

**Software limitations.** Blocking replay; poses in RAM; no stop during motion; Play with no recording drives joints toward 0 degrees; first cycle may jump; alarm can false-trigger on no echo. Details in `firmware.md`.

**Measurement uncertainty.** Link lengths measured with an engineering ruler (uncertainty NOT PROVIDED). Pick and drop positions reconstructed from video, about plus or minus 3 cm. Bottle mass and diameter are manufacturer figures.

**Unverified assumptions.** 50% derating for smooth load; SG90 current figures are typical values; elbow servo at the elbow in the torque model; foam link mass excluded.

**Safety limitations.** Implemented protections: none documented in hardware; the alarm is a separate board and does not act on the arm. Recommended: emergency stop cutting servo power, fuses on each supply, reverse-polarity protection, joint-limit clamping, guarding.

**Reproducibility limitations.** Servo-to-joint mapping, zero positions, supply layout, resistor values, jaw geometry and foam link dimensions are NOT PROVIDED, so the build cannot be reproduced exactly from this repository.

**Documentation debt.** The submitted thesis still contains claims not supported by the code, and a DH table and calculations that cannot be reproduced. They are listed in `change-log.md`.
