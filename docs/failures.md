# Failures and incidents

## F-01: arm controller board destroyed
- **Component:** arm controller (Arduino Nano on veroboard).
- **Expected:** board survives troubleshooting.
- **Observed:** the Nano was rendered unusable (author's account).
- **Detection:** NOT PROVIDED.
- **Root cause:** a wire was placed in the wrong hole during troubleshooting (author's account).
- **Contributing factors:** deadline pressure; troubleshooting a hand-wired veroboard; no spare Nano.
- **Correction:** the arm controller was rebuilt on an Arduino Uno, so the final system used two Unos instead of a Nano and a Uno.
- **Verification after correction:** the final system ran the demonstration (author's account).
- **Remaining risk:** no reverse-polarity or fuse protection is documented, so the same mistake could destroy another board.
- **Design choice that helped:** the Nano was mounted in header pins with wires drawn out for VIN, 5 V and ground, so nothing was soldered to the Nano itself. The author says this was to avoid flux and heat damage.

## F-02: power sharing between servos and boards
- **Component:** power distribution.
- **Observed:** after the circuit was built, the loads were "fighting for power" (author's account).
- **Root cause:** shared supply for servos and logic (author's account); measurements NOT PROVIDED.
- **Correction:** separate supplies for groups of loads and two added switches (a control switch and a power switch).
- **Verification:** the author reports the arrangement ran very smoothly. No current measurements NOT PROVIDED.
- **Remaining risk:** the exact supply split, which switch does what, and how servo 3 was supplied from 12 V are NOT PROVIDED. See [power.md](hardware/power.md).

## F-03: replay cannot be stopped with a button press
- **Component:** arm firmware.
- **Expected:** D10 stops replay.
- **Observed:** replay continued until power-off, reprogramming or the Arduino reset button.
- **Root cause (from code):** replay is a blocking routine and the button is read once per cycle.
- **Correction:** none implemented.
- **Remaining risk:** no software or hardware emergency stop. See [technical-debt.md](technical-debt.md).
