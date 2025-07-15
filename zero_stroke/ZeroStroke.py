import os
import subprocess
import time
import json
from datetime import datetime

KNOWN_KEYLOGGER_FILES = [
    "keylog.exe",
    "logger.exe",
    "spyware.exe",
    "monitor.exe",
    "capture.exe",
    # Add more known file names as you discover them
]

SUSPICIOUS_LOG_FILES = [
    "log.txt",
    "key.log",
    "password.log",
    # Add more common log file names
]

ALERT_LOG_FILE = "zero_stroke_alerts.log"

def detect_known_keylogger_files():
    print("Scanning for known keylogger files...")
    for filename in KNOWN_KEYLOGGER_FILES:
        if os.path.exists(filename):
            message = f"Known keylogger file detected: {filename}"
            print(f"[ALERT] {message}")
            trigger_alert(message)

def detect_suspicious_log_files():
    print("Scanning for suspicious log files...")
    log_file_path = "stroke_cap_log.txt" # Keeping our lab-specific check
    if os.path.exists(log_file_path):
        message = f"Potential keylogger log file detected: {log_file_path}"
        print(f"[ALERT] {message}")
        trigger_alert(message)
    for filename in SUSPICIOUS_LOG_FILES:
        if os.path.exists(filename):
            message = f"Potential keylogger log file detected: {filename}"
            print(f"[ALERT] {message}")
            trigger_alert(message)

def detect_python_processes():
    print("Scanning running processes...")
    try:
        output = subprocess.check_output(["ps", "aux"]).decode("utf-8")
        for line in output.splitlines():
            if "StrokeCap.py" in line and "ZeroStroke.py" not in line:
                message = f"Potential keylogger (StrokeCap) process running: {line.strip()}"
                print(f"[ALERT] {message}")
                trigger_alert(message)
                return  # Found it, can stop here for this basic check
    except subprocess.CalledProcessError:
        print("Error checking processes.")

def trigger_alert(message):
    timestamp = datetime.now().isoformat()
    alert_data = {
        "timestamp": timestamp,
        "alert_message": message
    }
    print(f"\n*** ZERO STROKE ALERT: {message} ***\n") # Keep console output
    try:
        with open(ALERT_LOG_FILE, "a") as f:
            f.write(json.dumps(alert_data) + "\n")
            print(f"(Alert details also logged to: {ALERT_LOG_FILE})") # Added console output
    except Exception as e:
        print(f"Error writing to alert log file: {e}")

def main():
    print("ZeroStroke is scanning for suspicious activity...")
    detect_known_keylogger_files()
    detect_suspicious_log_files()
    detect_python_processes()
    print("Scan complete.")

if __name__ == "__main__":
    main()
