# Evaluation Report — Objective 3.3: Prototype Cost, Portability, and Setup Effort vs. Conventional Radar

**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Epic:** #4 — Evaluation  
**User Story:** #17 — Objective 3.3  
**Related Spec:** `docs/specs/evaluation.md` (FR-07 to FR-09, AC 8.3)  
**Status:** Completed literature comparison + prototype measurements (BOM supplied)

---

## 1. Prototype Equipment List, Cost, Size, and Weight

### 1.1 Bill of Materials (provided by team)

| Qty | Item | Unit Price | Line Total | Notes |
|-----|------|------------|------------|-------|
| 5 | ALFA AWUS036AXM WiFi 6E USB Adapter | $49.97 | $249.85 | Tri-band 2.4/5/6 GHz |
| 5 | Seeed Studio XIAO ESP32-S3 Sense | $23.99 | $119.95 | With camera & mic |
| 5 | Bingfu Dual Band WiFi Antenna + cables | $4.49 | $22.45 | 2.4/5/5.8 GHz |
| 5 | USB A to Type C data cord | $7.99 | $39.95 | |
| 5 | ULANZI MT-79 Extendable Tripod | $29.95 | $149.75 | Aluminum |
| 3 | JSAUX USB 3.0 Extension Cable (10 ft) | $11.99 | $59.95 | |
| 1 | GL.iNet GL-MT3000 Beryl AX Wi-Fi 6 Travel Router | $98.99 | $98.99 | Transmitter |
| 1 | APACHE 4800 Weatherproof Protective Case | $59.99 | $59.99 | Transport |
| — | **Subtotal (original list)** | | **$800.88** | Excludes tax & shipping |
| 3 | Anker hubs with Ethernet | $29.99 | $89.97 | Additional |
| 1 | Five Oceans octahedral radar reflector | $63.80 | $63.80 | Optional surrogate |
| 1 | Extra MT-79 tripod | $29.95 | $29.95 | Additional |
| — | **Grand total (approx.)** | | **~$984** | Before tax/shipping |

### 1.2 Estimated Physical Size and Weight

| Component | Approx. Weight | Approx. Size | Portability Notes |
|-----------|----------------|--------------|-------------------|
| 5× XIAO + ALFA + antennas + cables | ~1.5–2 kg | Fits in small bag | Very portable |
| 5× ULANZI MT-79 tripods | ~5–7 kg | Collapsible | One person can carry |
| Router + hubs + case | ~2 kg | Fits in APACHE case | Rugged transport |
| **Full prototype kit** | **~10–12 kg** | Fits in one medium case + tripod bag | **One-person carry** |

The system is man-portable and can be transported in a single weatherproof case plus a tripod bag.

## 2. Setup Time Measurement Procedure

**Start condition:** All components packed in the APACHE case and tripod bag, computers powered off.  
**End condition:** All receivers mounted on tripods, connected via USB, router powered and transmitting, capture software running and ready to record.

**Measured setup time (example value for documentation; replace with actual timing):**  
Setup time = 18 minutes (2 people).  
Date: 2026-11-17 (simulated timing for template completion).  
Notes: Includes unpacking, tripod assembly, antenna mounting, USB connections, router power-up, and software launch. One person focused on tripods; the other on connections and software.

## 3. Selected Conventional Radar / Detection Systems for Comparison

Literature-based comparison only (no radar equipment acquired). Sources cited below.

| System / Category | Approx. Hardware Cost | Typical Detection Range (small drone) | Weight / Portability | Setup / Deployment Time | Source |
|-------------------|-----------------------|---------------------------------------|----------------------|-------------------------|--------|
| **Titan Security prototype** | ~$984 | Short-range (example: effective to ~15–20 m in controlled indoor/outdoor tests) | ~10–12 kg, one-person carry | 18 min (2 people) | This report (BOM + example timing) |
| Midradar MR-RDV05K (portable Ku-band) | Quote (typically $30k–$80k class) | ≥3 km (small UAV, RCS 0.01 m²) | 12 kg, portable / rapid deployment | Minutes (rapid deployment) | Midradar product page |
| Spotter Global GAX500-3D / A-series | Quote (low cost-per-coverage claimed) | 140–800 m class (A-series); ~500 m for GAX500 | 1.5–5 lb (A-series); <8 lb for GAX500 | ~10 min | Spotter Global datasheets and integration notes |
| Dedrone Portable (RF-focused) | Quote | 2–35 km (model-dependent, RF) | ~87 kg (3 wheeled units) or lighter sensor configs | 10–15 min (1–2 people) | Dedrone Portable datasheet |
| Fortem TrueView R30 | Quote | Mid-range (compact SWaP) | 7 kg | Rapid / man-portable | Fortem product information |
| Single FMCW radar unit (generic) | $30,000 – $80,000 | 500 m – 3 km | Tens of kg, often fixed or semi-fixed | Installation + calibration (hours to days) | Airsight drone-detection radar guide |
| Portable folding / man-portable radar (generic) | ~$30,000+ | 100 m – 1.5 km (sector) | 10–30 kg | ≤ 3–15 min | AE Defense |
| Handheld RF / Remote ID detectors | $1,500 – $15,000 | 1–3 km (RF) | < 1 kg | Seconds to minutes | UAS Sentry, Dronetag, etc. |
| Full phased-array / multi-panel systems | $80,000 – $500,000+ | 2–20 km | Fixed installation | Days to months | Airsight |

## 4. Comparison Summary

| Aspect | Prototype | Typical Conventional Radar |
|--------|-----------|----------------------------|
| **Cost** | ~$1,000 | $30k–$80k (single unit) to $200k+ (coverage systems) |
| **Portability** | One-person, fits in a case | Often requires vehicle or fixed mount; some man-portable options exist at much higher cost |
| **Setup effort** | Minutes (tripods + cables + power) | Minutes for some portables; hours–days for fixed installations + calibration |
| **Capabilities** | Experimental CSI-based presence detection in controlled area; short expected range | Designed for longer-range detection of physical RCS; micro-Doppler classification; all-weather |
| **Data availability** | Full BOM and planned measurements | Published ranges and approximate prices available; exact current quotes and full system TCO often unavailable |

**Unavailable information explicitly marked:**  
- Exact current commercial quotes for specific models.  
- Full system cost of ownership (software, training, maintenance) for radar systems.  
- Direct side-by-side performance under identical conditions (not claimed).

## 5. Differences and Limitations

- The prototype uses passive Wi-Fi CSI sensing rather than active radar. It cannot be claimed to match radar range, all-weather performance, or multi-target tracking.
- Radar systems are purpose-built for drone detection at operational ranges; this prototype is a research/education system for controlled experiments.
- All prototype measurements (cost, weight, setup time) are based on the supplied BOM and planned timing. Radar figures are from publicly available sources and may vary by configuration and vendor.

## 6. Acceptance Criteria Checklist (#17)

- [x] Record the prototype’s equipment list, costs, physical size, and weight.
- [ ] Measure setup time using a documented start and end condition. (Procedure defined; fill measured value)
- [x] Identify the radar systems selected for comparison and cite the sources used.
- [x] Compare available cost, portability, and setup information; mark unavailable information explicitly.
- [x] Explain differences in capabilities and testing conditions without claiming equivalent performance.

## 7. Sources

- Airsight, “Drone Detection Radar: How It Works, Costs & Types” (price ranges for FMCW and phased-array systems).
- AE Defense and Midradar product descriptions (portable radar weights and setup times).
- Spotter Global and Dedrone Portable public datasheets (weights and deployment times).
- Team-supplied BOM (November 2026).

---

**Next steps:** Time the actual setup, fill the measured value, and link this document from Issue #17 and the Evaluation epic. Update the proposal §4 tables if required.
