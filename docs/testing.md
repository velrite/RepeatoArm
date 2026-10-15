# Testing

## Strategy
- **Unit and integration tests:** none exist (NOT PROVIDED). The firmware was exercised on hardware.
- **System test:** record a pick-and-drop sequence with the arm and replay it (T-01).
- **Experimental tests:** repeatability, payload, accuracy. None were measured (see the procedure in `repeatability-test.md`).
- **Failure tests:** none were planned; two incidents are in `failures.md`.

## Test records

| ID | Objective | Configuration | Observed | Result | Evidence status |
|---|---|---|---|---|---|
| T-01 | Teach and replay a pick-and-drop of a PET bottle | Arduino Uno arm controller, pots, five servos, tray 60 x 60 cm, tall tower (pick) and short stand (drop). About 8-9 poses saved, repeated testing (owner-stated). Claw approached from above. | Arm replayed the sequence and carried the bottle to the stand. The bottle was not dropped; the grip felt marginal but the cap flange rested on the jaws. Replay looped until power-off or reprogramming. About 6 cycles counted in the demonstration video (owner-stated). | Worked as intended in the demonstration | Owner observation and my walkthrough video. Cycle log and measurements NOT PROVIDED. |
| T-02 | Alarm triggers inside 50 cm | Uno, HC-SR04, LEDs, buzzer, reset button | Thesis says detection was tested at different distances; no readings are given. | Not assessable | IMPLEMENTED / NOT VERIFIED. Data NOT PROVIDED. |
| T-03 | Positional repeatability | None | None | None | NOT PROVIDED. The thesis claim of "<1%" has no data. |

## Metrics that can and cannot be reported
- **Cycle time:** NOT PROVIDED. The code bounds it: 1 degree per 30 ms per joint, one joint at a time.
- **Success rate:** only "carried without dropping in the demonstration" is supported; no counts.
- **Position error, standard deviation, failure rate:** no data.
