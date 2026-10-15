# How I built RepeatoArm

*2023–2024 · Final-year Mechatronics Engineering project, Federal University Oye-Ekiti*

This is the story of the build, organised by stage, with the pictures I took along the way. Where I did not record something, I say so instead of guessing.

[← Back to the README](../README.md)

## Where it started

<p align="center">
  <img src="../media/photos/00-origin-fixing-the-first-arm.jpg" alt="Me building and fixing the first robotic arm, controlled by potentiometers and push buttons only" width="640"><br>
  <em>Me building and fixing the first robotic arm, controlled by potentiometers and push buttons only</em>
</p>

The project began with a robotic arm controlled only by potentiometers and push buttons. It had no recording and no security.

RepeatoArm keeps that control scheme and adds two things: **record-and-replay** of the arm's poses, and a **separate proximity alarm**.

## The materials

<p align="center">
  <img src="../media/photos/04-materials-components.jpg" alt="The materials I gathered for the build" width="640"><br>
  <em>The materials I gathered for the build</em>
</p>

The main parts are MG996R servos for the three joints, SG90 servos for the claw, Arduino boards, potentiometers, push buttons, an HC-SR04 ultrasonic sensor, LEDs, a buzzer, foam board, veroboard and chargers. The full list is in [hardware/bill_of_materials.md](../hardware/bill_of_materials.md).

## The arm

<p align="center">
  <img src="../media/photos/05-build-arm-servos-and-foam-board.jpg" alt="Servos mounted on foam board, an early stage of the arm" width="640"><br>
  <em>Servos mounted on foam board, an early stage of the arm</em>
</p>

The arm is foam board with the servos mounted directly on it. I measured the links with an engineering ruler: shoulder height 13.5 cm, upper arm 15 cm, forearm and closed claw 15 cm.

<p align="center">
  <img src="../media/photos/06-build-arm-assembly-with-control-buttons.jpg" alt="Assembling the arm with its control buttons" width="640"><br>
  <em>Assembling the arm with its control buttons</em>
</p>

## The controller and its circuit

<p align="center">
  <img src="../media/photos/07-build-arduino-uno-box.jpg" alt="A box I made for the Arduino Uno" width="640"><br>
  <em>A box I made for the Arduino Uno</em>
</p>

<p align="center">
  <img src="../media/diagrams/circuit-01-robotic-arm.png" alt="Circuit diagram of the robotic arm, drawn with a Nano" width="640"><br>
  <em>Circuit diagram of the robotic arm. It was drawn with a Nano; the final build used an Uno (see below).</em>
</p>

The first version of the arm's controller used an Arduino Nano. I built a veroboard with female header pins so the Nano could simply plug in. I did all the soldering on the board first, so I never had to apply heat to the Nano itself, and I brought out extra header pins for VIN, the 5 V output and ground, because the Nano has only a few of each.

<p align="center">
  <img src="../media/photos/11-electronics-veroboard-and-nano.jpg" alt="Veroboard with header pins and the Nano after I built the circuit" width="640"><br>
  <em>The veroboard with the Nano plugged in, after I built the circuit</em>
</p>

## The workspace and the alarm

I built the 60 × 60 cm workspace and the alarm system before I built the arm itself.

<p align="center">
  <img src="../media/photos/08-build-workspace-and-alarm-before-arm.jpg" alt="The workspace and the alarm system, finished before I built the arm" width="640"><br>
  <em>The workspace and the alarm system, finished before I built the arm</em>
</p>

<p align="center">
  <img src="../media/photos/09-build-alarm-stand-and-sensor.jpg" alt="The alarm stand and ultrasonic sensor, nearly done" width="640"><br>
  <em>The alarm stand and ultrasonic sensor, nearly done</em>
</p>

<p align="center">
  <img src="../media/diagrams/circuit-02-security-system.png" alt="Circuit diagram of the security alarm" width="640"><br>
  <em>Circuit diagram of the alarm. The resistor labels in the drawing are placeholders; the LEDs ran on 1 kΩ.</em>
</p>

The alarm is its own Arduino with an HC-SR04 sensor, four LEDs on 1 kΩ resistors, a buzzer and a reset button. It starts the alarm when something comes within 50 cm and clears it after 5 seconds or when the button is pressed.

## Wiring it together

<p align="center">
  <img src="../media/photos/10-build-wiring-after-assembly.jpg" alt="Wiring the connections after assembly" width="640"><br>
  <em>Wiring the connections after assembly</em>
</p>

## Testing and debugging

At one stage the arm was not picking things up. I tested whether the potentiometers were driving the servos. What I changed to fix it was not recorded, so I won't claim a cause.

<p align="center">
  <a href="https://youtube.com/shorts/gA7qPNep2mg?feature=share"><img src="https://img.youtube.com/vi/gA7qPNep2mg/hqdefault.jpg" alt="Testing that the potentiometers drive the servos" width="420"></a><br>
  <em>▶ Testing that the potentiometers drive the servos (the arm was not picking yet)</em>
</p>

Later I ran an all-round test, and everything worked.

<p align="center">
  <a href="https://youtube.com/shorts/4teszjtGUk8?feature=share"><img src="https://img.youtube.com/vi/4teszjtGUk8/hqdefault.jpg" alt="All-round test: everything working" width="420"></a><br>
  <em>▶ All-round test: everything working</em>
</p>

## The Nano I lost

While I was troubleshooting the arm's controller, a wire was put in the wrong hole and destroyed the Nano. I had no spare Nano, and the deadline was close. I rebuilt the arm's controller on an Arduino Uno while keeping my teammates calm.

I had planned a Nano for the arm and an Uno for the alarm. I ended with an Uno for each. The record is in [failures.md](failures.md).

## The power problem

After the circuits were built, I found a power distribution problem: the servos and the boards were competing for power. I studied it and split the loads across separate chargers, with a common ground, and added a control switch and a power switch.

I do not remember which switch controls what, and the exact split between chargers is not recorded, so I have left those open and documented them as open. They are listed in [hardware/power.md](hardware/power.md).

## The final build

<p align="center">
  <a href="https://youtu.be/JiwwPDpY4y4"><img src="https://img.youtube.com/vi/JiwwPDpY4y4/hqdefault.jpg" alt="Full walkthrough: introduction, live demo and Q&A" width="520"></a><br>
  <em>▶ Full walkthrough: me introducing the project, a live demo and Q&A</em>
</p>

The final build used an Uno for the arm and an Uno for the alarm. In the demonstration the arm carried a 27 g PET bottle (the manufacturer's figure) from a tall tower to a short stand, about 6 cycles on video, using 8–9 saved poses.

## What I would do differently

- Check every connection before applying power, and label the wires.
- Write down the power layout while building it, not afterwards.
- Keep test notes and measurements, so every claim can point to data.
- Give the arm a hardware emergency stop and a stop button that responds during movement.
