# Future work

- Separate regulated 5-6 V rails for each servo group with fuses, and a hardware emergency stop.
- Position feedback (servo with feedback, or encoders) and a closed-loop check of replay accuracy.
- Move several joints at once with interpolated paths; store poses in EEPROM so they survive power loss.
- Run the inverse kinematics on the board so poses can be entered as board coordinates.
- Link the alarm to the arm so a detected intrusion pauses the replay.
- Stiffer links (acrylic or aluminium) and a gripper with force sensing and a measured jaw range.
- Learn from several demonstrations, for example averaging taught poses.

These follow from the limits listed in [limitations.md](limitations.md).
