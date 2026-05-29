# MolEcule Chemistry Simulator

A Python/Pygame chemistry simulator that lets you spawn elements from the periodic table and watch them react with each other in real time.

![Simulator screenshot](Screenshot%202023-02-17%20011030.png)

> **Download (Windows .exe):** [Google Drive](https://drive.google.com/file/d/1zk_iCjAuCVrXg2edj_4g1DQ3IH-HSuxB/view?usp=sharing)

---

## Features

- Simulates chemical reactions between elements and molecules
- Reactions only occur when temperature conditions are met
- Change the state of matter (solid/liquid/gas) by adjusting temperature
- Pressure is fixed at 1 atm to keep things simple

**Visual conventions:**
| Visual | Meaning |
|--------|---------|
| Dot size | Molar volume |
| Dot text | Chemical formula |
| Clear dot with solid ring | Gas |
| Solid colored dot with ring | Liquid |
| Solid colored dot, no ring | Solid |
| Element color | CPK standard |
| Compound color | Color at STP |

---

## Screenshots

![Screenshot 1](Screenshot%202023-02-17%20010712.png)
![Screenshot 2](Screenshot%202023-02-17%20011131.png)

---

## Installation

**Requirements:** Python 3.8+

```bash
git clone https://github.com/adamivar/MolEcule-Chemistry-Simulator.git
cd MolEcule-Chemistry-Simulator
pip install -r requirements.txt
python main.py
```

---

## How to Use

| Action | Control |
|--------|---------|
| Spawn a mol of the current element | Left-click |
| Add more to a dot | Hold left-click |
| Switch to the next element | Right-click (cycles by atomic number) |
| Change temperature | Drag the slider (top-left corner) |

Temperature is displayed in K, °C, and °F. Setting it to absolute zero (0 K) effectively pauses all reactions.

---

## Purpose

MolEcule is designed as a fun educational toy for anyone curious about chemistry. It lets you explore basic reactions, see at what temperatures they occur, and observe how molar volume and states of matter behave — all interactively.

---

## Acknowledgments

Created by Adam Dobbins.
