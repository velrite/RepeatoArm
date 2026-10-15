# System overview

> **Status labels used in this repository:** MEASURED (author, engineering ruler), CODE (read from the firmware), DATASHEET (manufacturer typical value), CALCULATED, ASSUMPTION, NOT PROVIDED, NOT VERIFIED, IMPLEMENTED / NOT VERIFIED. Pick and drop positions are reconstructed from video (about plus or minus 3 cm), not measured.


RepeatoArm has two independent Arduino subsystems: a **record-and-replay arm controller** and a **proximity security alarm**. They share a workspace and a common ground, but the firmware does not link them.

## Block diagram

```mermaid
flowchart LR
  subgraph PWR["Power (as the builder describes it)"]
    C1["5 V / 3 A charger"]
    C2["12 V / 2 A charger"]
  end

  subgraph ARM["Arm controller (Arduino Uno)"]
    POT["3 potentiometers<br/>A0, A1, A2"]
    BTN["5 push buttons<br/>D7 to D11"]
    LEDA["2 status LEDs<br/>D12 play, D13 record"]
    MCU1["Arduino Uno<br/>manual control, record, replay"]
  end

  subgraph SERVOS["Actuators"]
    J12["2 x MG996R<br/>joints 1 and 2<br/>D2, D3"]
    J3["1 x MG996R<br/>joint 3<br/>D4"]
    CL["2 x SG90 claw<br/>D5, D6"]
  end

  subgraph SEC["Security alarm (Arduino Uno)"]
    US["HC-SR04<br/>trig D9, echo D10"]
    MCU2["Arduino Uno<br/>50 cm threshold, 5 s auto-reset"]
    LEDS["4 LEDs D2 to D5<br/>1 kohm each"]
    BZ["Buzzer D6"]
    RST["Reset button D7"]
  end

  POT --> MCU1
  BTN --> MCU1
  MCU1 --> LEDA
  MCU1 -->|signal| J12
  MCU1 -->|signal| J3
  MCU1 -->|signal| CL
  US --> MCU2
  RST --> MCU2
  MCU2 --> LEDS
  MCU2 --> BZ
  C1 -->|power| ARM
  C1 -->|power| J12
  C1 -->|power| CL
  C2 -->|power| SEC
  C2 -->|"power (how it was reduced to servo voltage: not recorded)"| J3
Record-and-replay flow
flowchart TD
  A["Manual mode: pots set joints 1 to 3, buttons open or close claw"] --> B{"D9 pressed?"}
  B -->|"yes: start recording, LED D13 on"| C["Move arm to a pose with the pots"]
  C --> D{"D10 pressed?"}
  D -->|"yes: save pose<br/>(3 joint angles + claw state, up to 10)"| C
  D -->|"D9 again: stop recording"| A
  A --> E{"D11 pressed?"}
  E -->|"yes: play, LED D12 on"| F["Ramp 1 degree per 30 ms through each saved pose,<br/>one joint after another"]
  F --> G["Return to first pose, wait 1 s"]
  G --> H{"D10 pressed?"}
  H -->|"no: repeat"| F
  H -->|"yes: stop"| A
Notes
The second 5 V charger in the bill of materials has no role recorded in the thesis text.
How the third MG996R was supplied from the 12 V charger was not recorded; see power.md.
The first build used an Arduino Nano for the arm (Fig 3.3 of the thesis); after the board was lost during troubleshooting, the final build used Unos for both subsystems.
