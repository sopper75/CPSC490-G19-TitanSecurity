# Wi-Fi CSI Sensing — Technical Specification

**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Sponsor:** Raytheon Applied Signal Technology (RTX-AST)  
**Epic:** #2 — Wi-Fi CSI Sensing  
**Related User Stories:** #8, #13  
**Task:** #45 — Write Wi-Fi CSI Sensing Specification  
**Sprint:** Sprint 2  
**Status:** Draft

---

## 1. Overview

The purpose of the Wi-Fi CSI sensing component is to establish a reliable and reproducible method of collecting wireless signal measurements for Titan Security's drone detection system.

Wi-Fi signals propagate through an environment and interact with objects through reflection, scattering, and multipath propagation. When an object, such as a drone, moves through the monitored area, it may alter the characteristics of the wireless channel.

Channel State Information (CSI) provides information about the wireless channel response, which can be analyzed to identify changes in the surrounding environment. These measurements will serve as the foundation for the drone detection and classification components developed in later stages of the project.

The sensing component will be responsible for configuring compatible wireless hardware, collecting channel measurements, recording data with timestamps, and verifying that the collected information is suitable for further processing.

The team has begun configuring its wireless equipment and performing preliminary Wi-Fi experiments. However, the complete CSI acquisition method has not yet been verified. This specification defines the intended functionality, technical requirements, acceptance criteria, and limitations of the sensing system.

## 2. Scope

### 2.1 In Scope

The Wi-Fi CSI sensing component will include the following capabilities:

- Configure a Wi-Fi transmitter and receiver for controlled experiments.
- Identify compatible hardware and software for CSI acquisition.
- Capture wireless channel measurements using supported devices.
- Record measurements with timestamps and relevant session information.
- Save collected data in a documented, machine-readable format.
- Verify recordings for missing, invalid, or inconsistent measurements.
- Maintain reproducible hardware and software configurations.
- Document the procedures required to repeat sensing experiments.
- Identify hardware limitations that may affect CSI acquisition.

### 2.2 Out of Scope

The following capabilities are outside the scope of the sensing component:

- Training the complete drone detection classifier.
- Performing final drone versus non-drone classification.
- Estimating the position or movement of detected drones.
- Measuring final detection accuracy and effective detection range.
- Comparing the completed system with conventional radar.
- Developing a production-ready drone surveillance system.

These capabilities will be addressed through the project's Drone Detection and Evaluation epics.

## 3. Related Epics and User Stories

### Epic #2 — Wi-Fi CSI Sensing

Establish a sensing platform capable of capturing and storing Wi-Fi channel measurements for future drone detection experiments.

### User Story #8 — Objective 1.1

**Set up a Wi-Fi transmitter and receiver pair and demonstrate CSI frame capture.**

The sensing platform must establish a repeatable wireless configuration and demonstrate acquisition of actual CSI measurements using compatible hardware and software.

### User Story #13 — Objective 1.2

**Save CSI measurements to timestamped files and verify their data quality.**

The system must preserve collected measurements and verify their integrity before they are used for training or evaluation.

These objectives define the requirements for the sensing platform. Their implementation is scheduled across multiple sprints.

## 4. Functional Requirements

Functional requirements describe the behavior the sensing system must provide.

| ID    | Functional Requirement                                                                                                                                 | Related Story |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| FR-01 | When a sensing session begins, the system shall identify the configured transmitter, receiver, wireless channel, and capture method.                   | #8            |
| FR-02 | When compatible hardware receives supported wireless traffic, the system shall acquire CSI measurements through the selected firmware or capture tool. | #8            |
| FR-03 | When a CSI frame is captured, the system shall preserve the available channel measurements without misrepresenting their format.                       | #8            |
| FR-04 | When hardware provides packet metadata instead of full CSI, the system shall identify the output as packet-level information.                          | #8            |
| FR-05 | When measurements are collected, the system shall associate them with timestamps and a recording session identifier.                                   | #13           |
| FR-06 | When a recording session ends, the system shall save collected measurements in a documented file format.                                               | #13           |
| FR-07 | When recorded measurements are validated, the system shall check for missing fields, malformed values, and timestamp inconsistencies.                  | #13           |
| FR-08 | When invalid measurements are identified, the system shall report the detected errors and affected records.                                            | #13           |
| FR-09 | When an experiment is documented, the system shall preserve the available hardware configuration and relevant environmental conditions.                | #8, #13       |

### 4.1 Requirements Traceability

**Objective 1.1 — Issue #8**

Requirements FR-01, FR-02, FR-03, FR-04, and FR-09 establish the sensing environment and define how successful CSI capture will be demonstrated.

**Objective 1.2 — Issue #13**

Requirements FR-05, FR-06, FR-07, FR-08, and FR-09 define the recording, storage, and validation functionality needed to prepare the collected measurements for further analysis.

## 5. Non-Functional Requirements

Non-functional requirements establish the quality and operational constraints of the sensing platform.

| ID     | Requirement                                                                                                                     | Purpose         |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| NFR-01 | Hardware and software configurations shall be documented sufficiently for another team member to reproduce the experiment.      | Reproducibility |
| NFR-02 | Recorded measurements shall retain timestamps and information identifying the capture session.                                  | Traceability    |
| NFR-03 | Validation procedures shall produce consistent results when executed repeatedly on the same unchanged recording.                | Reliability     |
| NFR-04 | Original measurement files shall be preserved when processed versions are generated.                                            | Data integrity  |
| NFR-05 | The system shall report configuration failures and invalid data through readable error messages.                                | Troubleshooting |
| NFR-06 | Configuration files committed to GitHub shall not expose authentication credentials or private secrets.                         | Security        |
| NFR-07 | A teammate shall be able to execute documented setup and validation procedures using the required dependencies and sample data. | Maintainability |

Specific performance targets, such as acceptable frame loss, capture frequency, and recording duration, will be determined after the selected CSI acquisition method has been verified.

## 6. Hardware and Software Environment

The proposed sensing environment uses commercially available wireless hardware to investigate changes in Wi-Fi channel measurements.

### 6.1 Hardware Components

| Component          | Hardware                                | Purpose                                                                                           | Status                                         |
| ------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Wi-Fi Transmitter  | GL.iNet GL-MT3000 (Beryl AX)            | Provides configurable Wi-Fi transmissions during experiments.                                     | Initial configuration completed                |
| Microcontroller    | Seeed Studio XIAO with Wi-Fi capability | Supports preliminary wireless experiments and investigation of compatible CSI collection methods. | Basic Wi-Fi scanning tested                    |
| External Antenna   | Dual-band Wi-Fi antenna                 | Supports wireless experiments when compatible with the selected device.                           | Connected during preliminary setup             |
| USB Wi-Fi Receiver | ALFA AWUS036AXM                         | Planned receiver for Linux wireless packet capture and compatibility testing.                     | Planned; not yet tested by the document owner  |
| Host Computer      | Laptop or desktop                       | Runs capture and processing software and stores recordings.                                       | Available; final capture configuration pending |

### 6.2 GL.iNet GL-MT3000 Router

The GL-MT3000 will serve as a configurable Wi-Fi access point during sensing experiments.

The router allows the team to control relevant wireless settings, including the network name, channel, security configuration, and channel bandwidth.

A repeatable configuration is important because changes to the transmitter's settings can influence the collected wireless measurements.

Initial router setup has been performed. The final experimental configuration will be documented after the team completes its hardware compatibility testing.

### 6.3 Seeed Studio XIAO

The team has begun experimenting with a Seeed Studio XIAO microcontroller.

Preliminary work has included connecting the device through USB, configuring the Arduino IDE, and executing basic Wi-Fi scanning operations.

These tests demonstrate basic wireless functionality but do not establish that the device can capture full CSI measurements.

The exact XIAO model, supported firmware, and CSI capabilities must be confirmed before selecting the device for the final sensing configuration.

### 6.4 ALFA AWUS036AXM

The ALFA AWUS036AXM is a USB Wi-Fi adapter included in the team's planned experimental configuration.

The adapter will be investigated as a wireless receiver connected to a compatible Linux computer.

Planned activities include:

- Connecting and identifying the adapter on the host computer.
- Verifying driver compatibility.
- Configuring wireless monitor mode.
- Receiving and recording Wi-Fi traffic.
- Examining captured frames and metadata.
- Evaluating the adapter's suitability for the sensing platform.

The adapter's standard Linux driver supports packet-level wireless capture but does not expose the detailed per-subcarrier CSI measurements required by typical Wi-Fi CSI sensing methods.

Therefore, the ALFA adapter may support preliminary packet capture experiments without being the final CSI acquisition device.

Additional hardware or firmware may be required to obtain full CSI.

### 6.5 Software Components

| Software                 | Intended Purpose                                             | Status         |
| ------------------------ | ------------------------------------------------------------ | -------------- |
| Arduino IDE              | Configure and test compatible XIAO hardware.                 | In use         |
| Python                   | Data processing, recording validation, and future analysis.  | Planned        |
| Linux wireless utilities | Configure compatible receivers and inspect wireless traffic. | Planned        |
| CSI acquisition software | Collect actual channel state measurements.                   | To be selected |
| Git and GitHub           | Version control, issue tracking, and code review.            | In use         |

Software selections will be updated as the team verifies hardware compatibility and finalizes the acquisition method.

## 7. Data Collection and Storage

### 7.1 Recording Procedure

The intended recording process consists of the following stages:

1. Configure the Wi-Fi transmitter and receiver.
2. Record the hardware and wireless settings used in the experiment.
3. Initialize the selected CSI capture method.
4. Acquire wireless channel measurements.
5. Associate captured measurements with timestamps.
6. Save measurements in a structured file.
7. Validate the file for consistency and missing information.
8. Preserve the results for later classification and evaluation.

### 7.2 Proposed Data Fields

The precise file format will depend on the supported CSI acquisition tool. The following fields are proposed for recording and experiment metadata.

| Field            | Description                                             |
| ---------------- | ------------------------------------------------------- |
| `session_id`     | Unique identifier for the recording session             |
| `timestamp_utc`  | Measurement timestamp                                   |
| `receiver_id`    | Identifier of the receiving device                      |
| `source_type`    | CSI, packet metadata, or synthetic test data            |
| `capture_method` | Software or firmware used to obtain measurements        |
| `wifi_channel`   | Wireless channel used during collection                 |
| `frequency_mhz`  | Operating frequency, when available                     |
| `measurement`    | Wireless measurement values in the selected data format |

If the selected acquisition system provides complex CSI values, amplitude, phase, or additional channel metadata, those values will be preserved according to the documented capture format.

### 7.3 Data Quality Validation

The validation component will inspect recorded measurements for:

- Missing required fields.
- Invalid or malformed measurement values.
- Missing or inconsistent timestamps.
- Empty recording files.
- Unexpected changes in measurement dimensions.
- Incorrectly labeled measurement types.
- Incomplete recording sessions.

The validator will report the number of records inspected, accepted, and rejected or flagged.

The original collected data will be preserved for future analysis.

### 7.4 Data Source Identification

The system shall distinguish between three recording types:

**Live CSI:** Measurements collected using a verified CSI-capable device.

**Packet Metadata:** Wireless frame information collected without full channel state measurements.

**Synthetic Data:** Artificially generated records used to test file handling and validation procedures.

This distinction is necessary to prevent packet observations or simulated measurements from being incorrectly presented as successful live CSI acquisition.

## 8. Acceptance Criteria

Acceptance criteria define the evidence required to demonstrate that each objective has been implemented successfully.

### 8.1 Objective 1.1 — Wi-Fi CSI Capture (#8)

- [ ] A Wi-Fi transmitter and receiver are configured and documented.
- [ ] The transmitter and receiver can participate in a repeatable wireless experiment.
- [ ] A compatible CSI acquisition method is identified and configured.
- [ ] At least one genuine CSI frame is successfully captured.
- [ ] Captured CSI measurements can be inspected.
- [ ] Packet-level captures are distinguished from actual CSI measurements.
- [ ] Another team member can reproduce the documented capture procedure.

### 8.2 Objective 1.2 — Data Recording and Quality (#13)

- [ ] Collected measurements can be saved to timestamped files.
- [ ] Recordings include required session metadata.
- [ ] Saved measurements can be loaded by the validation process.
- [ ] Missing or malformed measurement values are detected.
- [ ] Timestamp inconsistencies are identified.
- [ ] Validation produces a summary of accepted and rejected records.
- [ ] The recording and validation procedure can be reproduced by another team member.

### 8.3 Sprint 2 Specification Task (#45)

This specification task is complete when:

- [ ] The purpose and scope of Epic #2 are documented.
- [ ] Functional requirements are defined and linked to related user stories.
- [ ] Non-functional requirements are documented.
- [ ] Measurable acceptance criteria are provided.
- [ ] Planned equipment is distinguished from tested equipment.
- [ ] Hardware limitations and unresolved questions are identified.
- [ ] The specification is summarized and linked in proposal Section 4.
- [ ] Repository validation checks pass.
- [ ] The document is reviewed and merged into the team's development branch.

Completion of this documentation task does not imply that all sensing functionality has already been implemented.

## 9. Technical Risks and Limitations

### 9.1 Hardware Compatibility

Not every Wi-Fi device supports CSI acquisition.

The ALFA AWUS036AXM can be investigated for packet capture, but full CSI acquisition may require a different supported device or specialized firmware.

**Mitigation:** Verify acquisition capabilities before committing to the final receiver configuration.

### 9.2 Environmental Interference

Nearby wireless networks, human movement, physical obstacles, and changes in transmitter or receiver placement may affect the observed channel.

**Mitigation:** Record experimental conditions and use consistent equipment placement during controlled tests.

### 9.3 Data Consistency

Different capture methods may produce varying data structures, timestamps, and measurement formats.

**Mitigation:** Establish a standard recording schema and implement validation before collecting the main experimental datasets.

### 9.4 Detection Feasibility

Successful CSI collection does not guarantee that the measurements will reliably distinguish drones from other environmental disturbances.

**Mitigation:** Evaluate detection performance separately using labeled recordings and controlled experiments.

## 10. Open Questions

The following technical decisions remain unresolved:

| Question                                                                                     | Responsible Area       |
| -------------------------------------------------------------------------------------------- | ---------------------- |
| Which hardware and firmware combination will provide actual CSI measurements?                | Hardware / Sensing     |
| Can the team's specific XIAO device support the required CSI acquisition method?             | Hardware / Sensing     |
| What information can be reliably captured using the planned ALFA adapter?                    | Hardware / Sensing     |
| What recording format will be used for CSI measurements?                                     | Data Collection        |
| What data-quality thresholds will determine whether a recording is usable?                   | Data Processing        |
| What transmitter and receiver placement will provide repeatable experimental conditions?     | Sensing / Evaluation   |
| What environmental conditions must be recorded for later analysis?                           | Sensing / Evaluation   |
| Are there additional sponsor requirements affecting the collection environment or equipment? | Project Team / Sponsor |

These questions will be resolved through hardware verification, team design decisions, and consultation with the project sponsor where necessary.

## 11. Related Documents

- [CSI Equipment Setup and Compatibility Notes](../../prototype/csi-setup.md)
- [CSI Frame Capture Procedure](../../prototype/csi-capture.md)
- [Project Proposal](../../proposal/proposal.md)
- [Epic #2 — Wi-Fi CSI Sensing](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/2)
- [User Story #8 — CSI Frame Capture](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/8)
- [User Story #13 — CSI Recording and Quality](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/13)
- [Task #45 — Wi-Fi CSI Sensing Specification](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/45)

## 12. Current Development Status

The Wi-Fi CSI sensing component is currently in the specification and preliminary hardware verification stage.

Initial configuration of the GL.iNet router has been performed, and the Seeed Studio XIAO has been used for basic wireless scanning experiments.

The ALFA AWUS036AXM is included in the planned equipment configuration but has not yet been tested by the author of this specification.

The final CSI acquisition method, timestamped CSI recording implementation, and automated data-quality validation remain to be verified or developed.

This specification provides the requirements and acceptance criteria for those activities and will be updated as hardware compatibility and implementation decisions are confirmed.
