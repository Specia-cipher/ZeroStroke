🛡️ Zero Stroke - Keylogger Analysis & Countermeasure

**SANNI-BABATUNDE-IDRIS  sannifreelancer6779@gmail.com  @Linkedin  https://www.linkedin.com/in/sanni-idris-89917a262?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app**

A project focused on understanding keylogger operation, starting with practical simulation using a third-party tool, followed by the development of a custom keylogger (StrokeCap) and a countermeasure (Zero Stroke).

**📑 Table of Contents**

* [Overview](#overview)
* [Initial Keylogger Simulation](#initial-keylogger-simulation)
* [StrokeCap v2.0](#strokecap-v20)
* [Zero Stroke](#zero-stroke)
* [🔥 Key Features](#key-features)
* [🛠️ Project Stages](#project-stages)
* [🧰 Tools Used](#tools-used)
* [Next Plan](#next-plan)
* [📜 License](#license)
* [⚠️ Disclaimer](#disclaimer)

---

## Overview <a name="overview"></a>

This project documents a comprehensive exploration into keylogger technology, encompassing initial simulation and analysis, the development of custom tools for offensive and defensive security learning, and future plans for enhancement and deployment.

---

## Initial Keylogger Simulation <a name="initial-keylogger-simulation"></a>

The project commenced with a hands-on simulation of a keylogger attack using an existing Python-based tool (`python-keylogger`). This crucial first step provided practical insights into how keyloggers operate, including their logging mechanisms and potential vulnerabilities. The analysis of the simulated keylogger's behavior informed the subsequent development of the custom tools.

---

## StrokeCap v2.0 <a name="strokecap-v20"></a>

A custom Python-based keylogger engineered to capture keystrokes and log them in JSON format, including timestamps, special key descriptions, and platform detection. It also includes basic parsing to display captured keystrokes after logging.

**Usage:**

```bash
# Navigate to the directory containing StrokeCap.py
cd ZeroStroke/
# Run the keylogger
python3 StrokeCap.py
Press ESC in the terminal where StrokeCap is running to stop the logging. Captured keystrokes will be saved in a file named stroke_cap_log.txt in the same directory, and a basic parsed output will be displayed in the terminal.

Author: Sanni Idris (Specia-cipher)

Zero Stroke
A basic Python-based countermeasure tool designed to detect potential keylogging activity by analyzing file systems and running processes for indicators associated with keyloggers, including StrokeCap. It provides alerts via console output and structured JSON logging to a file named zero_stroke_alerts.log.

Usage:

Bash

# Navigate to the directory containing ZeroStroke.py
cd ZeroStroke/
# Run the countermeasure tool
python3 ZeroStroke.py
Zero Stroke will scan for suspicious activity and output alerts to the console. Details of the alerts will also be logged in JSON format to zero_stroke_alerts.log in the same directory.

Author: Sanni Idris (Specia-cipher)

🔥 Key Features
Hands-on Keylogger Attack Simulation (Completed)

Custom Keylogger (StrokeCap v2.0) with JSON Logging and Parsing

Keylogger Detection Tool (Zero Stroke) with:

Known Keylogger File Detection

Suspicious Log File Detection (including StrokeCap's log)

Running StrokeCap Process Detection

Hybrid Alert System (Zero Stroke) with Console Output and JSON Log File

🛠️ Project Stages
Completed:

Phase 1: Initial Keylogger Simulation & Insight Gathering

Phase 2: Custom Keylogger Engineering (StrokeCap v2.0)

Phase 3: Countermeasure Development ("Zero stroke") - Core Detection

Next:

Phase 4: Alert System Enhancement and Containerization (Focus on Docker for both tools)

🧰 Tools Used
Virtualization Software (VirtualBox, VMware)

Backbox Linux VM

Existing Python-based Keylogger (python-keylogger)

Python Programming Language

pynput library (for StrokeCap)

datetime module (for both)

platform module (for StrokeCap)

json module (for both)

subprocess module (for Zero Stroke)

Next Plan
The immediate next step is to focus on containerizing both the StrokeCap and Zero Stroke tools using Docker.

📜 License
MIT License

⚠️ Disclaimer
This project is intended for educational and ethical testing purposes only. Use of these tools for any malicious or unauthorized activity is strictly prohibited. The author(s) are not responsible for any misuse of this software.

