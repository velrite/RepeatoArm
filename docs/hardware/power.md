Power budget
Status labels used in this repository: MEASURED (author, engineering ruler), CODE (read from the firmware), DATASHEET (manufacturer typical value), CALCULATED, ASSUMPTION, NOT PROVIDED, NOT VERIFIED, IMPLEMENTED / NOT VERIFIED. Pick and drop positions are reconstructed from video (about plus or minus 3 cm), not measured.
Values are typical figures. MG996R: operating voltage 4.8-7.2 V, running current 0.5-0.9 A, stall current 2.5 A at 6 V, mass 55 g (manufacturer datasheet). SG90 figures (running 0.1-0.25 A, stall 0.65 A) are typical hobby-servo values and were not checked against the exact parts used. Script: calculations/payload_power_check.py.
Per-supply loads
Supply
Load
Running (A)
With 30% margin (A)
All stalled (A)
5 V / 3 A charger
Arm Arduino + 2 MG996R + 2 SG90
1.26 - 2.36
3.07
6.36
Second charger (rated 2 A)
Security Arduino + 1 MG996R + sensor, LEDs, buzzer
0.61 - 1.01
1.31
2.61
Whole system, five servos
3 MG996R + 2 SG90

11.4
8.8
The 5 V / 3 A charger runs close to its rating at the top of the range (2.36 A against 3 A). This matches the builder's report that the arrangement ran smoothly in normal motion.
A stalled servo can far exceed any of these chargers. The claw servos hold an object by pressing against it, which is a mild stall (up to about 1.3 A for both), so the claw is the load to watch.
Why one supply per group matters
An Arduino pin is rated at 40 mA absolute maximum, and the on-board regulator is meant for logic, not servos. Servo current must come from the charger rail, not through the board.
If a board is fed 12 V on VIN and also supplies servos from its 5 V pin, the regulator dissipates (12 - 5) V x current. At 0.35 A that is 2.4 W, and while gripping (1.45 A) about 10 W, far above what the regulator can shed. The author reports that the claw servos shared the first charger's 5 V rail, possibly tapped at an Arduino 5 V pin; which pin or rail was used was not verified, and if it was an Arduino 5 V pin fed from VIN the regulator concern above applies.
Early in the build the servos and boards were "fighting for power", which led to separating the supplies and adding two switches.
Open points
The thesis records the third MG996R on the 12 V charger. The MG996R is rated to 7.2 V, so a voltage-reduction stage would have been needed; what was used was not recorded.
The role of the second 5 V charger was not recorded.
No fuses are documented.
The loss of the first Nano was caused by a wire placed in the wrong hole during troubleshooting, not by overload.
