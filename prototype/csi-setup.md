# CSI Equipment Setup and Compatibility Notes

**Issue:** #39  
**Parent story:** #8 (Objective 1.1 – Set up a Wi-Fi transmitter/receiver pair and demonstrate CSI frame capture)  
**Status:** Initial verification notes (hardware on hand / to be confirmed by team)

## 1. Equipment roles

| Role | Device | Notes |
|------|--------|-------|
| Transmitter (AP / signal source) | GL.iNet GL-MT3000 (Beryl AX) | Wi-Fi 6 travel router. Acts as the access point that generates the Wi-Fi signals we will sense. |
| Receiver (CSI capture device) | ALFA AWUS036AXM | USB Wi-Fi 6E adapter. Used to receive and attempt to extract Channel State Information. |
| Host computer | Laptop or desktop running Linux (recommended: Ubuntu 22.04+ or Kali) | Runs capture software and stores recordings. USB 3.0 port required. |

## 2. Device specifications (from manufacturer / public sources)

### ALFA AWUS036AXM
- Chipset: MediaTek MT7921AUN
- Standards: 802.11 a/b/g/n/ac/ax (Wi-Fi 6 / 6E)
- Bands: 2.4 GHz / 5 GHz / 6 GHz
- Interface: USB 3.2 Gen 1 Type-A
- Antennas: 2× RP-SMA (detachable)
- Linux driver: `mt7921u` (in-kernel since Linux 5.18)
- Monitor mode: Supported on recent Linux kernels
- Official page: https://www.alfa.com.tw/products/awus036axm

### GL.iNet GL-MT3000
- SoC: MediaTek MT7981
- Wi-Fi: Wi-Fi 6 (AX3000), dual-band (2.4 / 5 GHz)
- Firmware: OpenWrt-based
- Ports: 2.5G WAN, 1G LAN, USB 3.0
- Useful as a controllable access point for experiments

## 3. Compatibility findings

### What works today
- The ALFA AWUS036AXM is recognized on modern Linux (kernel ≥ 5.18) with the in-kernel `mt7921u` driver. No out-of-tree driver compilation is required on recent Ubuntu/Kali.
- Monitor mode can be enabled with standard `iw` / `airmon-ng` tools.
- The GL-MT3000 can be configured as a normal access point (or in repeater mode) and is suitable as the transmitter.

### CSI capture limitations (important)
True fine-grained CSI (complex I/Q values per subcarrier, similar to the classic Intel 5300 or Atheros CSI Tool) is **not** available out-of-the-box on the ALFA AWUS036AXM. The `mt7921u` driver supports monitor mode and packet capture, but does not expose the vendor CSI reports that research tools rely on.

Practical options for this project:
1. **ESP32-based CSI (recommended starting point)** – Use one or more ESP32 boards with the [ESP32-CSI-Tool](https://github.com/StevenMHernandez/ESP32-CSI-Tool) or similar. Cheap, well-documented, and proven for Wi-Fi sensing.
2. **OpenWrt + MediaTek CSI patches** – Projects such as [ekstra-csi](https://github.com/imxdemetri/ekstra-csi) or MtkCSIdump target mt76-based OpenWrt routers (the GL-MT3000 family is a candidate). Requires custom firmware.
3. **Continue with ALFA + monitor mode** – Capture raw packets for RSSI / timing analysis only. This is weaker than true CSI but can still show motion effects.

**Current recommendation:** Treat the ALFA as a flexible receiver for packet-level experiments and evaluate an ESP32 or patched OpenWrt path for full CSI.

## 4. Required software and configuration (Linux host)

### Host OS
- Ubuntu 22.04+ or Kali Linux (kernel ≥ 5.18)
- USB 3.0 port

### Packages
```bash
sudo apt update
sudo apt install -y iw wireless-tools aircrack-ng tcpdump python3 python3-pip

Add CSI equipment setup notes
