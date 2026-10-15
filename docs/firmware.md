# Firmware documentation

Files: `firmware/arm_controller/arm_controller.ino`, `firmware/security_alarm/security_alarm.ino`. Both were transcribed from the supplied listings with formatting restored. They have not been compiled or run by the documentation author. Observations below come from reading the code. None was executed on hardware, so each is IMPLEMENTED / NOT VERIFIED.

## Arm controller

**Purpose.** Manual joint control with potentiometers, and recording and replay of up to 10 poses.

**Inputs.** Potentiometers A0-A2. Push buttons D7 (claw open), D8 (claw close), D9 (start/stop recording), D10 (save pose, and stop replay), D11 (play).
**Outputs.** Servo signals D2-D4 (MG996R joints), D5-D6 (SG90 claw). LEDs D12 (play) and D13 (recording). Serial 9600 baud messages.
**Dependencies.** Arduino core and the `Servo` library.

**States.** Manual (pots drive joints), Recording, Playing.

| Event | Effect |
|---|---|
| D9 pressed, not recording | Start recording, clear stored poses, LED D13 on |
| D9 pressed, recording | Stop recording, LEDs off |
| D10 pressed, recording | Save pose: three `servo.read()` values plus claw state (1 if servo 4 = 100 and servo 5 = 80) |
| D11 pressed | Play: LED D12 on, LED D13 off |
| D10 pressed, playing | Stop playing (only read between cycles) |
| Arduino reset | Clears everything (poses are in RAM) |

**Algorithm.** Pot value mapped from 0-1023 to 10-170 degrees. Replay: for each pair of saved poses, joint 1 ramps, then joint 2, then joint 3 (1 degree per 30 ms), then the claw is commanded to the state of the next pose. After the last pose the arm ramps back to pose 1, waits 1 s and repeats.
**Timing.** Loop delay 5 ms; 300 ms delays after button actions; replay is blocking.
**Error handling.** Only a check for more than 10 poses, which prints "Max array".

**Observations (questionable design decisions, not changed).**
1. `servo.read()` returns the last commanded angle, not a measured position. Recorded poses are commands.
2. Buttons are read as `INPUT` with no internal pull-up, so each needs an external pull-down. Values NOT PROVIDED.
3. Replay is blocking and the stop button is read once per cycle, so a momentary press during movement is missed. The author stopped replay with the Arduino reset button or power-off.
4. Play with no saved poses: the array is zero-initialised, so the joints ramp toward 0 degrees, below the 10-degree pot minimum, and the claw closes.
5. First cycle: the first ramp starts from the recorded pose value, not the current position, so a first write may jump to that pose without ramping.
6. A claw state change is issued after the three joint moves of a segment, with no pause afterwards.
7. The 10-170 degree mapping is wider than the roughly 120 degrees of travel the MG996R datasheet text gives (vendor variants list 180). Endpoint behaviour NOT VERIFIED.
8. Servo objects are copied into an array and passed by value. This works in the demonstrated build.
9. Variable names are misleading: `buttonStopRecord` saves a pose, and `ledStopRecord` is the play LED.

## Security alarm

**Purpose.** Detect an object within 50 cm and signal it.
**Inputs.** HC-SR04 echo D10, reset button D7 (internal pull-up, pressed = LOW). **Outputs.** HC-SR04 trigger D9, LEDs D2-D5, buzzer D6 (1 kHz tone).
**Behaviour.** Measure every 100 ms. Distance below 50 cm turns all LEDs and the buzzer on for 5 s, or until reset is pressed.

**Observations (not changed).**
1. `pulseIn` has no timeout argument, so with no echo it waits up to its default and returns 0, giving a distance of 0 cm, which triggers the alarm.
2. If an object stays within 50 cm after reset or the 5 s expiry, the alarm re-triggers on the next pass.
3. A comment says "5 microsecond pulse" but the code sends 10 microseconds, which is the sensor's specified trigger length.
4. The threshold is fixed at 50 cm, with no filtering of readings.
5. The alarm does not signal the arm controller.
