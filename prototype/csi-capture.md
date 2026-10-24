# CSI / Frame Capture Demonstration

**Issue:** #8  
**Depends on:** #39 (equipment setup notes)  
**Goal:** Show that we can capture Wi-Fi frames (and, where possible, CSI) from a known transmitter.

## 1. Setup used

- **Transmitter:** GL.iNet GL-MT3000 (configured as an access point on a fixed channel)
- **Receiver:** ALFA AWUS036AXM in monitor mode on a Linux host
- **Host:** Ubuntu/Kali (kernel ≥ 5.18) with `mt7921u` driver

## 2. Steps to reproduce the capture

### Transmitter
1. Power on the GL-MT3000 and set a known SSID (example: `CSI-Lab`).
2. Fix the channel (example: 2.4 GHz channel 6) so the receiver can stay on one channel.
3. Note the distance and orientation between the router and the adapter for later experiments.

### Receiver (ALFA)
```bash
# Confirm adapter is present
lsusb | grep -i -E 'alfa|mediatek|0e8d'

# Enable monitor mode (replace wlan1 with the actual interface name)
sudo airmon-ng check kill
sudo ip link set wlan1 down
sudo iw dev wlan1 set type monitor
sudo ip link set wlan1 up

# Confirm
iwconfig

# Option A: tcpdump
sudo tcpdump -i wlan1 -w csi-lab-capture.pcap

# Option B: airodump-ng (shows beacons and stations live)
sudo airodump-ng wlan1
