# Titan Security — CSI Data Flow Design

**Project:** Radar over WiFi  
**Group:** G19 — Titan Security  
**Owner:** 23jdo5  
**Epic:** #2 — Wi-Fi CSI Sensing  
**Related User Stories:** #8, #13  
**Task:** #47 — Create CSI Data Flow Diagram  
**Sprint:** Sprint 2  
**Status:** Proposed Design  
**Specification:** [Wi-Fi CSI Sensing Specification — PR #46](https://github.com/sopper75/CPSC490-G19-TitanSecurity/pull/46)

## 1. Overview

This document describes the planned data flow for Titan Security's Wi-Fi CSI sensing system.

The system aims to capture wireless channel measurements, associate them with timestamps, store the recordings, and validate their quality before using them for drone detection.

The diagrams represent the proposed system design. Full CSI acquisition and drone detection have not yet been demonstrated.

## 2. Level 0 — CSI Data Flow Diagram

The Level 0 diagram illustrates how the Wi-Fi CSI sensing system interacts with external components.

```mermaid
flowchart LR
    OP["Experiment Operator"]
    TX["GL.iNet Wi-Fi Transmitter"]
    ENV["Wireless Test Environment"]
    SYS["0.0 Wi-Fi CSI Sensing System"]
    DET["Future Drone Detection Pipeline"]

    OP -->|"Capture settings and session information"| SYS
    TX -->|"Wi-Fi transmissions"| ENV
    ENV -->|"Received wireless signals"| SYS
    SYS -->|"Recording files and quality reports"| OP
    SYS -.->|"Validated CSI recordings — planned"| DET
```

![Level 0 data flow showing the Wi-Fi transmitter, wireless environment, CSI sensing system, experiment operator, and future drone detection pipeline](diagrams/csi-dfd-level0.png)

**Figure 1 — Level 0 CSI Data Flow Diagram.**

Figure 1 shows the external inputs and outputs of the planned Wi-Fi CSI sensing system. Wireless transmissions pass through the experimental environment, where physical objects and interference may affect the channel. The sensing system will capture measurements, record experimental information, and produce quality reports. Validated recordings will later support the drone detection pipeline.

Dashed arrows represent future integrations.

## 3. Level 1 — CSI Data Flow Diagram

Figure 2 expands the Wi-Fi CSI sensing system from Figure 1 into three proposed processes: measurement capture, timestamping and recording, and data-quality validation.

```mermaid
flowchart TD
    OP["Experiment Operator"]
    ENV["Wireless Test Environment"]

    P1["1.0 Capture CSI Measurements"]
    P2["2.0 Add Timestamps and Metadata"]
    P3["3.0 Validate Data Quality"]

    D1[("D1 Raw CSI Recordings")]
    D2[("D2 Validated CSI Dataset")]
    D3[("D3 Quality Reports")]

    DET["Future Drone Detection Pipeline"]

    OP -->|"Capture settings"| P1
    OP -->|"Experiment information"| P2
    ENV -->|"Received Wi-Fi signals"| P1

    P1 -->|"CSI measurements"| P2
    P2 -->|"Timestamped records"| D1
    D1 -->|"Recorded measurements"| P3

    P3 -->|"Accepted records"| D2
    P3 -->|"Validation results"| D3

    D3 -->|"Quality report"| OP
    D2 -.->|"Future classifier input"| DET
```

![Level 1 data flow showing CSI measurement capture, timestamping, raw recordings, data validation, validated datasets, and quality reports](diagrams/csi-dfd-level1.png)

**Figure 2 — Level 1 CSI Data Flow Diagram.**

Figure 2 shows the proposed internal data flow of the CSI sensing system. Measurements will be captured through compatible receiver hardware, associated with timestamps and experiment information, and stored in raw recording files. The data-quality process will then produce validated records and quality reports.

All numbered processes and data stores represent planned functionality. The final CSI-compatible receiver and capture method are still to be confirmed.
