# Design decision records

Only decisions with evidence are recorded. Reasons are the author's unless marked CODE. Alternatives not stated by the author are NOT PROVIDED.

**ADR-01: Controller change from Nano to Uno.** Context: the design and first build used a Nano for the arm and a Uno for the alarm. Event: the Nano was lost (F-01) and no Nano was available. Decision: use a Uno for both. Consequence: the thesis text says Uno while Figs 3.3 and 4.2 show a Nano.

**ADR-02: Mount the Nano in header pins on veroboard.** Reason: avoid soldering directly to the Nano and the flux or heat damage that can follow. Trade-off: more wiring to route and labels needed. Consequence: the board was easy to replace but the wiring was exposed to a mis-wire.

**ADR-03: Separate supplies and two switches.** Context: loads were contending for power (F-02). Decision: split loads across chargers and add a control switch and a power switch. Rejected alternatives: NOT PROVIDED. Consequence: smoother operation (author's account); layout and servo 3 voltage unresolved.

**ADR-04: Record and replay in RAM, one joint at a time.** Context: the arm is taught with potentiometers and replayed. Decision (CODE): store up to 10 poses of `servo.read()` values in an array and replay joints sequentially at 1 degree per 30 ms. Reason (author): joints are taught one at a time, so replay pauses naturally between steps. Trade-off: simple and predictable, but not simultaneous motion, slow, lost on reset, and the stop button is rarely seen. Rejected alternatives: NOT PROVIDED.

**ADR-05: Foam board structure.** Reason (thesis): light weight and strength-to-weight. Trade-off: low stiffness and no deflection data. Consequence: torque calculation excludes link mass because it is NOT PROVIDED.
