# 🛡️ ZeroStroke - Keylogger Analysis & Countermeasure

![MIT License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Containerized](https://img.shields.io/badge/containerized-Podman-green)

**Author:** Sanni Babatunde Idris – [LinkedIn](https://www.linkedin.com/in/sanni-idris-89917a262?utmsource=share&utmcampaign=sharevia&utmcontent=profile&utmmedium=androidapp)  
📧 sannifreelancer6779@gmail.com  

---

## 📑 Table of Contents

- [Overview](#overview)
- [Initial Keylogger Simulation](#initial-keylogger-simulation)
- [StrokeCap v2.0](#strokecap-v20)
- [ZeroStroke](#zerostroke)
- [Containerization (Podman)](#containerization)
- [🔥 Key Features](#key-features)
- [🛠️ Project Stages](#project-stages)
- [🧰 Tools Used](#tools-used)
- [Next Plan](#next-plan)
- [📜 License](#license)
- [⚠️ Disclaimer](#disclaimer)

---

## 📖 Overview

ZeroStroke is a Python-based keylogger detection tool born out of curiosity-driven research into offensive and defensive security. The project simulates keylogger behavior, develops custom offensive tooling (StrokeCap), and builds a defensive countermeasure (ZeroStroke).  

---

## 🧪 Initial Keylogger Simulation

The journey started by cloning and testing an existing Python keylogger (*python-keylogger*). This step offered hands-on insights into:  

- Keystroke capture techniques
- Log file handling
- Process behavior analysis

These insights guided the engineering of custom tools.

---

## 🛠️ StrokeCap v2.0

A Python-based keylogger that captures keystrokes with:  

✅ JSON structured logging  
✅ Timestamps and special key handling  
✅ Platform detection  

**Usage:**
```bash
# Navigate to StrokeCap directory
cd ZeroStroke/

# Run StrokeCap
python3 StrokeCap.py

📝 Captured keystrokes are saved to strokecaplog.txt. Press ESC to stop logging.


---

🛡️ ZeroStroke

A countermeasure tool that scans for keylogging activity by detecting:

Known keylogger files

Suspicious logs (e.g., strokecaplog.txt)

Active keylogger processes


Usage:

# Navigate to ZeroStroke directory
cd ZeroStroke/

# Run ZeroStroke
python3 ZeroStroke.py

📦 Alerts are displayed in the console and logged to zerostrokealerts.log.


---

🐳 Containerization (Podman)

✅ Why ZeroStroke Was Containerized

ZeroStroke was containerized to ensure:

Isolation from host systems

Portability across environments

Easy deployment in testing labs


🛑 Why StrokeCap Wasn’t

StrokeCap, as an offensive tool, remains uncontainerized to discourage casual or unintended use. This reflects a deliberate ethical stance in releasing potentially dangerous tooling.

📦 Build & Run with Podman

# Build ZeroStroke container
podman build -t zerostroke .

# Run container
podman run --rm -it zerostroke

📸 Screenshot Example
(Replace this with your screenshot)



---

🔥 Key Features

Hands-on keylogger simulation

Custom keylogger engineering (StrokeCap)

Countermeasure with console + JSON logging

Podman containerization for safe deployment



---

🗺️ Project Stages

Stage	Status

Initial Keylogger Simulation	✅ Completed
StrokeCap v2.0 Development	✅ Completed
ZeroStroke Core Detection	✅ Completed
Podman Containerization	✅ Completed
StrokeCap Containerization	🛑 Deferred



---

🧰 Tools Used

Python 3

pynput, subprocess, datetime, platform

Backbox Linux VM (sandboxed testing)

Podman (containerization on Termux)

Termux for mobile lab operations



---

📌 Next Plan

Extend ZeroStroke’s detection heuristics

Build AttackOps-Lab for offensive simulations

Integrate both labs (DefenseOps + AttackOps) for full-spectrum coverage



---

📜 License

MIT License


---

⚠️ Disclaimer

This project is intended for educational purposes only. Misuse of these tools for unauthorized activity is strictly prohibited. The author assumes no responsibility for misuse.
