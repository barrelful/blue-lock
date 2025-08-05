#!/usr/bin/env python3
import subprocess
import time

DEVICE_MAC = "XX:XX:XX:XX:XX:XX"  # Replace with your phone's MAC  
RSSI_THRESHOLD = -40             # Lock if signal is weaker (more negative)
ABSENCE_THRESHOLD = 3            # How many weak signals before locking
CHECK_INTERVAL = 5               # Seconds between checks

absence_counter = 0

def get_rssi(mac):
    try:
        output = subprocess.check_output(["hcitool", "rssi", mac], stderr=subprocess.STDOUT)
        # Example output: "RSSI return value: -60"
        rssi = int(output.decode().strip().split(":")[-1])
        return rssi
    except subprocess.CalledProcessError:
        return None

while True:
    rssi = get_rssi(DEVICE_MAC)
    if rssi is not None:
        print(f"RSSI: {rssi}")
        if rssi < RSSI_THRESHOLD:
            absence_counter += 1
            print(f"Too far ({absence_counter}/{ABSENCE_THRESHOLD})")
        else:
            absence_counter = 0
            print("Phone is close enough.")
    else:
        absence_counter += 1
        print(f"Could not get RSSI ({absence_counter}/{ABSENCE_THRESHOLD})")

    if absence_counter >= ABSENCE_THRESHOLD:
        print("Phone too far or disconnected. Locking screen.")
        subprocess.call(["cinnamon-screensaver-command", "-l"])
        absence_counter = 0  # Optional: reset or exit

    time.sleep(CHECK_INTERVAL)