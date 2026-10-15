# Repeatability test procedure (to be run on a rebuilt or similar arm)

> **Status labels used in this repository:** MEASURED (author, engineering ruler), CODE (read from the firmware), DATASHEET (manufacturer typical value), CALCULATED, ASSUMPTION, NOT PROVIDED, NOT VERIFIED, IMPLEMENTED / NOT VERIFIED. Pick and drop positions are reconstructed from video (about plus or minus 3 cm), not measured.


The submitted project reports replay as accurate but does not include a measured repeatability figure. Use this procedure to produce one. Report only numbers you have measured.

## Equipment
Graph paper or a printed 1 mm grid, tape, a fine marker or a pointer attached to the claw, a ruler or calipers, a phone camera on a fixed stand.

## Procedure
1. Fix the arm and the grid to the board so neither moves. Mark the grid origin and the arm base position.
2. Record three poses with the arm: a near point, a mid point and a far point (about 24, 26 and 28 cm from the base axis), each at a height you can mark.
3. For each pose, replay the saved sequence **20 times**. After each replay, wait for the arm to stop and mark where the pointer touches the grid, labelled with the trial number.
4. Repeat step 3 on a second day, or after powering the arm off and on, to include start-up effects.
5. Run once with the claw empty and once holding the 27 g bottle.

## Calculation
For each pose, read the (x, y) of each mark in millimetres, then:
- mean position = average of x and average of y
- error of trial i = distance from mark i to the mean position
- repeatability = mean error, and also report the largest error and the standard deviation
- percent of reach = repeatability / reach x 100, with reach measured from the base axis to the mark

```python
import numpy as np
pts = np.array([[x1, y1], [x2, y2]])   # replace with your measured marks (mm)
mean = pts.mean(axis=0)
err = np.linalg.norm(pts - mean, axis=1)
print(err.mean(), err.max(), err.std(ddof=1))
```

## Expected size of the numbers
One degree of servo error at 28 cm reach moves the tip about 0.5 cm, so a repeatability under 1% of reach (0.28 cm) would need each joint to return within about 0.4 degrees. Whatever you measure is the figure to quote.

## Data sheet

| Pose | Trial | x (mm) | y (mm) | Load |
|---|---|---|---|---|
| Near | 1 | | | |
