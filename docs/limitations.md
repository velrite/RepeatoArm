# Limitations and future work

> **Status labels used in this repository:** MEASURED (author, engineering ruler), CODE (read from the firmware), DATASHEET (manufacturer typical value), CALCULATED, ASSUMPTION, NOT PROVIDED, NOT VERIFIED, IMPLEMENTED / NOT VERIFIED. Pick and drop positions are reconstructed from video (about plus or minus 3 cm), not measured.


## Scope of the firmware
The submitted firmware is a **teach-and-repeat controller**: joints follow potentiometers, up to 10 poses (with claw state) can be saved, and the arm replays them in a loop. The inverse-kinematics work in this repository is an offline analysis of the same arm, used to check reach and joint angles, not code running on the Arduino. The security alarm is a separate board and does not command the arm.

## Known limitations
1. **No position feedback.** Recording stores the last commanded angle, so replay repeats commands exactly, but the physical position depends on servo dead band, backlash and the flex of the foam links. A measured repeatability figure has not been taken; see the [test procedure](repeatability-test.md).
2. **Resolution is 1 degree per joint.** At about 28 cm reach that is about 0.5 cm of tip movement (rounding to the nearest degree gives about plus or minus 0.4 cm).
3. **Joints move one after another** (1 degree every 30 ms), so the path between poses is not a straight line, and a worst-case 10-pose replay can take over two minutes.
4. **Stop button is read only once per replay cycle** (CODE). Replay is a blocking routine, so a momentary press during movement is not seen. The builder reports that replay ran continuously until the machine was switched off or reprogrammed. There is no hardware emergency stop. In practice the builder stopped replay with the Arduino reset button (which also clears the saved poses) or by switching off. Status: IMPLEMENTED / NOT VERIFIED (button response was not tested).
5. **Pick is near the reach limit.** The two 15 cm links give a 30 cm reach from the shoulder axis (about 27-28 cm along the board at table level). The drop is comfortably inside.
6. **Payload.** Torque analysis gives about 110-140 g as a smooth working load at full stretch before the foam links are counted, and 268-321 g as the stall limit. The demonstration used a 27 g PET bottle. The claw jaw gap (smallest and largest object width) was not measured.
7. **Power.** Supplies are shared and unfused; the claw servos load their rail when gripping. The third MG996R was recorded on 12 V, above its 7.2 V rating, with the reduction method not recorded.
8. **Security alarm.** One HC-SR04 with a narrow detection cone, a fixed 50 cm threshold and no filtering. A timed-out reading returns 0 cm, which would trigger the alarm (untested).
9. **Pick and drop positions are estimates** taken from demonstration video frames (about plus or minus 3 cm) because the arm was dismantled after submission.
10. **Recorded poses are held in RAM** (CODE: the array is not written to EEPROM). Pressing reset or removing power erases the recording, so a sequence must be taught again after every restart. The demonstration used about 8-9 of the 10 available poses (owner-stated).
11. **Grip retention is partly geometric.** The bottle's wide cap or flange rested on the jaws, which the builder gives as the reason it was not dropped, while the clamping force alone felt marginal (owner-stated). The claw has no force limit or sensing, and slip testing was not done. Status: IMPLEMENTED / NOT VERIFIED.

What I would do about these is in [future-work.md](future-work.md).
