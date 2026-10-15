# Calculations

Python scripts that reproduce the numbers in [docs/calculations](../docs/calculations/). They need Python 3 and NumPy (`pip install numpy`).

| File | What it does |
|---|---|
| `kinematics_check.py` | Solves the pick and drop poses three independent ways and checks each with forward kinematics. Run: `python3 kinematics_check.py` |
| `payload_power_check.py` | Payload at full stretch, power budget for each charger, and replay time. Run: `python3 payload_power_check.py` |
| `payload_power_output.txt` | The output of `payload_power_check.py` when it was run for this repository |
| `kinematics_appendix.md` | Step-by-step working for every case, with every substitution |

Inputs: link lengths are my engineering-ruler measurements; MG996R figures are from its datasheet; pick and drop positions are reconstructed from my demo video (about plus or minus 3 cm). See the status labels in each calculation.
