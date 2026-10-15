Wiring and pin table
Status labels used in this repository: MEASURED (author, engineering ruler), CODE (read from the firmware), DATASHEET (manufacturer typical value), CALCULATED, ASSUMPTION, NOT PROVIDED, NOT VERIFIED, IMPLEMENTED / NOT VERIFIED. Pick and drop positions are reconstructed from video (about plus or minus 3 cm), not measured.
All pin assignments below are taken from the submitted code. Where the thesis text differs from the code, the code is followed (see the change log).
Arm controller (Arduino Uno in the final build)
Pin
Connected to
Direction
Function in code
D2
Servo 1 (MG996R) signal
Output
Joint 1, driven from pot A0
D3
Servo 2 (MG996R) signal
Output
Joint 2, driven from pot A1
D4
Servo 3 (MG996R) signal
Output
Joint 3, driven from pot A2
D5
Servo 4 (SG90) signal
Output
Claw jaw A: open 100, closed 20 degrees
D6
Servo 5 (SG90) signal
Output
Claw jaw B: open 80, closed 160 degrees
D7
Push button
Input
Claw open
D8
Push button
Input
Claw close
D9
Push button
Input
Start / stop recording
D10
Push button
Input
Save current pose; also stops replay
D11
Push button
Input
Play recorded poses
D12
LED
Output
Playback indicator
D13
LED
Output
Recording indicator
A0, A1, A2
Potentiometers
Analog input
Joint 1, 2, 3 angle, mapped 0-1023 to 10-170 degrees
Notes
Buttons read HIGH when pressed (INPUT, no internal pull-up), so each needs an external pull-down resistor to ground. The resistor values were not recorded.
Which physical joint (base, shoulder, elbow) is servo 1, 2 or 3 was not recorded.
Recording uses servo.read(), which returns the last angle commanded, not a measured position.
Security alarm (Arduino Uno)
Pin
Connected to
Direction
Function in code
D9
HC-SR04 trigger
Output
10 microsecond trigger pulse
D10
HC-SR04 echo
Input
Echo pulse width, distance = duration x 0.034 / 2 cm
D2, D3, D4, D5
LEDs, 1 kohm series resistor each
Output
All on when alarm is active
D6
Buzzer
Output
1 kHz tone when alarm is active
D7
Reset push button to ground
Input, internal pull-up
Press (LOW) to clear the alarm
Behaviour: alarm starts when distance is below 50 cm, clears after 5 s or on the reset button, loop delay 100 ms.
LED current with 1 kohm resistors at 5 V and about 2 V LED drop: about 3 mA each, well inside the 20 mA per pin recommendation.
Power wiring (from thesis section 3.3.2 and the builder's account)
Supply
Feeds
5 V / 3 A charger
Arm Arduino, servos 1 and 2, claw servos
12 V / 2 A charger
Security Arduino (VIN), servo 3
Second 5 V charger
Role not recorded
All grounds are joined into one common ground (thesis section 3.3.2).
Two switches (a control switch and a power switch) were added to manage power sharing; which one does what was not recorded.
The first arm build mounted a Nano on veroboard through female header pins, with extra wires drawn out for VIN, 5 V and ground so nothing was soldered to the Nano.
