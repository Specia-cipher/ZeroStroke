import os
import subprocess
import time

def detect_log_file():
    log_file_path = "stroke_cap_log.txt"  # Assuming it's in the same directory for now
    if os.path.exists(log_file_path):
        print(f"[ALERT] Suspicious file found: {log_file_path}")
        trigger_alert("Potential keylogger log file detected!")

def detect_python_processes():
    try:
        output = subprocess.check_output(["ps", "aux"]).decode("utf-8")
        for line in output.splitlines():
            if "StrokeCap.py" in line and "ZeroStroke.py" not in line:
                print(f"[ALERT] Running StrokeCap process found: {line.strip()}")
                trigger_alert("Potential keylogger (StrokeCap) process running!")
                return  # Found it, can stop here for this basic check
    except subprocess.CalledProcessError:
        print("Error checking processes.")

def trigger_alert(message):
    print(f"\n*** ZERO STROKE ALERT: {message} ***\n")
    # In the future, we can add more sophisticated alerting here (e.g., pop-ups, logging to a file)

def main():
    print("ZeroStroke is scanning for suspicious activity...")
    detect_log_file()
    detect_python_processes()
    print("Scan complete.")

if __name__ == "__main__":
    main()
