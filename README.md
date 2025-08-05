# Bluetooth Proximity Lock for Linux (RSSI-based)

This is a simple Python script that **automatically locks your Linux screen** when your Bluetooth-connected phone moves too far away, based on the **RSSI (signal strength)** of the connection.

Inspired by Windows' "Dynamic Lock" feature, but designed for **Linux Mint (Cinnamon)** or any Linux distro with `cinnamon-screensaver`.

---

## 🔧 Features

- Locks your session when your phone is out of Bluetooth range.
- Uses Bluetooth RSSI signal strength (not just connection presence).
- Includes a **grace period** to prevent false positives.
- Fully local, no third-party dependencies beyond system tools.

---

## 🚀 Installation

### 1. Install system dependencies

Make sure `bluez` and `cinnamon-screensaver` tools are installed:

```bash
sudo apt update
sudo apt install bluez cinnamon-screensaver
```

On other desktop environments, replace `cinnamon-screensaver-command -l` with your DE's lock command (e.g. `gnome-screensaver-command -l` or `loginctl lock-session`).

---

### 2. Clone the repo

```bash
git clone https://github.com/yourusername/bluetooth-proximity-lock.git
cd blue-lock
```

---

### 3. Install Python requirements (optional)

```bash
pip install -r requirements.txt
```

> ⚠️ Note: This script uses only the Python standard library, so `requirements.txt` is empty by default unless extended.

---

## 🔧 Configuration

Edit the script and set your phone’s MAC address:

```python
DEVICE_MAC = "XX:XX:XX:XX:XX:XX"  # Replace with your phone's MAC
```

You can find your device MAC with:

```bash
bluetoothctl devices
```

Then:
- Connect and trust your phone:
  ```bash
  bluetoothctl
  connect XX:XX:XX:XX:XX:XX
  trust XX:XX:XX:XX:XX:XX
  ```

---

## 📈 Calibrating RSSI Distance

RSSI values are negative numbers — the closer to 0, the stronger the signal.

Example:
- `-45`: very close
- `-70`: a few meters away
- `-80`: out of the room

Set a safe threshold like:

```python
RSSI_THRESHOLD = -73  # Adjust based on your environment
ABSENCE_THRESHOLD = 3  # Number of weak checks before locking
CHECK_INTERVAL = 5     # Seconds between checks
```

---

## ▶️ Running the script

```bash
python3 rssi-lock.py
```

Or make it executable:

```bash
chmod +x rssi-lock.py
./rssi-lock.py
```

---

## 🔐 Security Note

This script **only locks the screen**. It does not unlock when the phone returns — this is intentional for security. You must type your password to log back in.

---

## 🛠 Optional: Auto-start on login

To run the script at login:
1. Open *Startup Applications* in your DE.
2. Add a new entry pointing to the full path of `rssi-lock.py`.

Or use a `systemd` user service (ask if you want help with this setup).

---

## 📄 License

MIT License

---

## 🤝 Contributing

Feel free to fork, improve and submit PRs!
