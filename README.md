🛡️ Zero Stroke - Keylogger Analysis & Countermeasure

**Table of Contents**
* [Overview](#overview)
* [🔥 Key Features](#key-features)
* [🚀 Quick Start](#quick-start)
* [🛠️ Roadmap](#roadmap)
* [⚙️ Usage](#usage)
* [📝 Sample Log Output](#sample-log-output)
* [🧰 Tools](#tools)
* [👨‍💻 About the Author](#about-the-author)
* [📜 License](#license)
* [⚠️ Disclaimer](#disclaimer)

## Overview <a name="overview"></a>

This project started with a tactical deep dive into keyloggers through simulation and the strategic engineering of a custom keylogger, StrokeCap v2.0. The primary objective has now shifted towards building "Zero stroke," a robust countermeasure tool designed to detect and potentially mitigate keylogging activities. This lab serves as an offensive and defensive security-oriented exploration.

## 🔥 Key Features <a name="key-features"></a>

* **Hands-on Keylogger Simulation:** Conducted a practical simulation using an external Python keylogger to gain a foundational understanding of keylogging techniques.
* **Custom Keylogger Development (StrokeCap v2.0):** Engineered a Python-based keylogger (StrokeCap v2.0) with advanced features including comprehensive JSON logging and basic parsing.
* **JSON Logging:** Utilizes a structured JSON format for log entries, facilitating easy data parsing and potential future analysis.
* **Basic JSON Parsing:** Implements a basic parsing mechanism to read the `stroke_cap_log.txt` file and display the captured keystrokes.
* **Zero stroke Countermeasure (Planned):** Development of a tool to identify keylogging activities through various methods:
    * Detecting known keylogger file names and types.
    * Monitoring for suspicious file creation and modification.
    * Analyzing running processes for known keylogger names and suspicious behavior.
    * Detection of processes hooking keyboard or mouse events.
    * (Future) Registry analysis and network activity monitoring.
* **Alert Mechanism:** "Zero stroke" will feature a hybrid alert system, providing pop-up notifications for immediate user awareness and detailed logging to a separate file.
* Modular Design: The project is designed with a modular approach to enable the integration of diverse detection and response strategies for "Zero stroke."
* Cross-Platform Exploration: Primarily developed and tested on a Linux environment (Backbox VM), with consideration for future adaptation to Android (Termux/UserLAnd).

## 🚀 Quick Start <a name="quick-start"></a>

1.  Gained initial experience by simulating a keylogger attack using an existing tool.
2.  Successfully developed StrokeCap v2.0, a custom keylogger with JSON logging and basic parsing capabilities.
3.  The subsequent step is to commence the development of "Zero stroke," the keylogger countermeasure.

## 🛠️ Roadmap <a name="roadmap"></a>

**Phase 1: Keylogger Simulation & Insight Gathering (Computer)**
* **Goal:** To acquire practical knowledge of keylogger behavior through direct simulation.
* **Tasks:** Utilize an external keylogger to simulate and analyze keystroke capture.

**Phase 2: Custom Keylogger Engineering (StrokeCap v2.0) (Computer/Phone)**
* **Goal:** To build a feature-rich keylogger for in-depth understanding of its mechanisms.
* **Tasks:** Develop StrokeCap v1.0, v1.1, and v2.0 with comprehensive JSON logging and basic parsing.

**Phase 3: Countermeasure Development ("Zero stroke") - Core Detection (Computer/Phone)**
* **Goal:** To build the initial detection capabilities of "Zero stroke."
* **Tasks:** Implement file system analysis (detecting `stroke_cap_log.txt`, known file types, suspicious creation), and basic process monitoring (detecting Python processes). Integrate a basic alert mechanism (console print).

**Phase 4: Expanding Zero stroke Detection (Computer/Phone)**
* **Goal:** To enhance the detection capabilities of "Zero stroke."
* **Tasks:** Implement more advanced process monitoring (hooking detection), and potentially begin exploring registry analysis (Windows) and network activity monitoring.

**Phase 5: Alert System Enhancement and Containerization (Computer/Phone)**
* **Goal:** To refine the alert system and containerize "Zero stroke" with Docker.
* **Tasks:** Implement pop-up notifications and separate log file writing for alerts. Create a Dockerfile for "Zero stroke."

**Phase 6: Porting and Cross-Platform Adaptation (Phone)**
* **Goal:** To adapt and test "Zero stroke" on mobile environments.
* **Tasks:** Port the codebase to Android (Termux/UserLAnd), optimize for mobile, conduct thorough testing.

**Phase 7: Enhancement and Refinement (Phone/Computer)**
* **Goal:** To improve the effectiveness and robustness of "Zero stroke."
* **Tasks:** Implement advanced detection methods, enhance response capabilities, conduct extensive testing and debugging.

**Phase 8: Documentation and Finalization (Phone/Computer)**
* **Goal:** To complete comprehensive documentation for the entire project.
* **Tasks:** Write detailed README, provide code comments, finalize project documentation.

## ⚙️ Usage <a name="usage"></a>

To run the StrokeCap v2.0 keylogger, navigate to the directory where you have saved the `StrokeCap.py` file in your terminal and execute the following command:

```bash
python3 StrokeCap.py
The script will start logging keystrokes in JSON format to a file named stroke_cap_log.txt in the same directory. After you press the ESC key to stop the logging, the script will then attempt to parse the log file and display the captured keystrokes in the terminal.

📝 Sample Log Output
Platform Information (Appears at the beginning of stroke_cap_log.txt and in the console):

StrokeCap v2.0 logging started on: Linux
Sample JSON Log Entries in stroke_cap_log.txt:

JSON

{"event_type": "PRESS", "timestamp": "2025-07-14 12:56:14.872897", "key": "'i'"}
{"event_type": "RELEASE", "timestamp": "2025-07-14 12:56:14.946059", "key": "'i'"}
{"event_type": "PRESS", "timestamp": "2025-07-14 12:56:15.391241", "key": "[SPACE]"}
{"event_type": "RELEASE", "timestamp": "2025-07-14 12:56:15.478748", "key": "[SPACE]"}
{"event_type": "PRESS", "timestamp": "2025-07-14 12:56:19.738519", "key": "[ENTER]"}
{"event_type": "RELEASE", "timestamp": "2025-07-14 12:56:19.812195", "key": "[ENTER]"}
{"event_type": "PRESS", "timestamp": "2025-07-14 12:56:24.495657", "key": "[ESC]"}
{"event_type": "RELEASE", "timestamp": "2025-07-14 12:56:24.619442", "key": "[ESC]"}
Sample Parsed Keystrokes Output (Displayed in the terminal after stopping logging):

--- Parsed Keystrokes ---
i b a a t u n d e   i d r i s [ENTER]
🧰 Tools
Virtualization Software (VirtualBox, VMware)

Backbox Linux VM

Existing Python-based Keylogger

Python Programming Language

pynput library

datetime module

platform module

json module

Development Environment (VS Code, Sublime Text)

Git

Termux or Kali via UserLAnd (on Android)

Text Editor (on phone)

👨‍💻 About the Author
🔖 Built with ❤️ by Sanni Idris
GitHub: github.com/Specia-cipher/defenseops-lab
LinkedIn: linkedin.com/in/sanni-idris-89917a262
📧 Gmail: sannifreelancer6779@gmail.com

📜 License
MIT License

⚠️ Disclaimer
This keylogger (StrokeCap) is intended for educational and ethical testing purposes only within a controlled environment. Use of this tool for any malicious or unauthorized activity is strictly prohibited and may be illegal. The author(s) are not responsible for any misuse of this software
