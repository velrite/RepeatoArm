"""RepeatoArm: payload (torque), power budget and replay-time checks. Run: python payload_power_check.py
Inputs marked 'datasheet' are typical values; 'builder' values were measured or reported by the builder."""
import numpy as np
L1 = L2 = 15.0                                   # cm, builder measured
T_STALL = {"4.8 V": 9.4, "6.0 V": 11.0}          # MG996R stall torque, kgf.cm (datasheet, typical)
M_ELBOW_SERVO, M_CLAW, M_BOTTLE = 0.055, 0.018, 0.027   # kg: MG996R (datasheet 55 g), 2x SG90 (9 g each), PET bottle (builder, 27 g)

def capacity(T, derate, m1=0.0, m2=0.0):
    """Max payload (kg) at full horizontal stretch; m1, m2 = foam upper-arm / forearm mass (kg), centred on each link."""
    shoulder = M_ELBOW_SERVO*L1 + M_CLAW*(L1+L2) + m1*L1/2 + m2*(L1+L2/2)
    elbow = M_CLAW*L2 + m2*L2/2
    return min((T*derate - shoulder)/(L1+L2), (T*derate - elbow)/L2)

print("== Payload at full horizontal stretch (foam links excluded)")
for v, t in T_STALL.items():
    s, w = capacity(t, 1.0), capacity(t, 0.5)
    print(f"{v}: stall limit {1000*s:.0f} g | smooth working load (50% of stall) {1000*w:.0f} g | safety factor for 27 g bottle {w/M_BOTTLE:.1f}")
print("Foam link mass effect (4.8 V, 50%), each link 0/25/50 g:", [round(1000*capacity(9.4, .5, m, m)) for m in (0, .025, .05)], "g")

print("\n== Power budget (A). MG996R datasheet: run 0.5-0.9 A, stall 2.5 A at 6 V; SG90 typical: run 0.1-0.25 A, stall 0.65 A")
mg, sg = (0.5, 0.9, 2.5), (0.1, 0.25, 0.65)
arm_logic, sec_logic = 0.06, 0.05 + 0.015 + 4*0.003 + 0.03     # Uno, HC-SR04, 4 LEDs at 3 mA (1 kohm), buzzer ~30 mA
groups = {"Charger 1: arm Arduino + 2 big servos + 2 claw servos": [2*mg[i] + 2*sg[i] + arm_logic for i in range(3)],
          "Charger 2: security Arduino + 1 big servo + security circuit": [mg[i] + sec_logic for i in range(3)]}
for n, g in groups.items():
    print(f"{n}: running {g[0]:.2f}-{g[1]:.2f} A, +30% margin {1.3*g[1]:.2f} A, all stalled {g[2]:.2f} A")
print("Whole system, all five servos stalled:", round(3*mg[2] + 2*sg[2], 2), "A; +30% =", round(1.3*(3*mg[2] + 2*sg[2]), 1), "A")
print("LED current at 1 kohm, 5 V, 2 V drop:", (5-2.0)/1000*1000, "mA each")

print("\n== Replay time (code: 1 degree per 30 ms, joints move one after another)")
step_s = 0.030
print("Worst case, 10 saved poses, each joint sweeping 160 deg:", round(9*3*160*step_s, 1), "s, plus return to start up to", round(3*160*step_s, 1), "s")
print("Typical, 4 poses, 60 deg per joint per segment:", round(3*3*60*step_s, 1), "s")
print("Stop-button response: checked once per replay cycle, so up to the cycle time above")
