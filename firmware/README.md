# Firmware

Two Arduino sketches, one for each Arduino Uno in the build.

| Folder | Board | What it does |
|---|---|---|
| [arm_controller](arm_controller/arm_controller.ino) | Arduino Uno | Moves three MG996R joints from potentiometers, works the SG90 claw, records up to 10 poses and replays them |
| [security_alarm](security_alarm/security_alarm.ino) | Arduino Uno | Reads an HC-SR04 and sounds a buzzer and lights 4 LEDs when something is closer than 50 cm |

## Uploading a sketch
1. Install the Arduino IDE.
2. Open the `.ino` file. The `Servo` library comes with the IDE, so nothing else is needed.
3. Choose **Tools, Board, Arduino Uno** and select the port.
4. Click Upload.

## Notes
- The pin for every connection is in [docs/hardware/wiring-and-pins.md](../docs/hardware/wiring-and-pins.md).
- The arm sketch reads its buttons as plain inputs, so each button needs an external pull-down resistor.
- Both files were transcribed from the listings in my thesis, with formatting restored and the logic unchanged. They were not compiled again for this repository, and whether they match the files that were flashed byte for byte is not verified.
- How the code behaves, function by function, is in [docs/firmware.md](../docs/firmware.md).
