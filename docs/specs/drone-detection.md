**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Sponsor:** Raytheon Applied Signal Technology (RTX-AST)  
**Epic:** #3 — Drone Detection  
**Related User Stories:** #14, #15, #7
**Task:** #49 - Write Drone Detection Specification  
**Sprint:** Sprint 2  
**Status:** Draft

---

## 1. Overview

The purpose of the Drone Detection is to determine whether Wi-Fi channel measurements can distinguish drone activity from non-drone conditions, and whether they can support estimates of a drone's position and movement.

The component builds on the recordings produced by the Wi-Fi CSI Sensing epic (#2). It will collect labeled recordings for four conditions (drone activity, empty background, human movement, and interference), train and evaluate a classifier on them, and implement position and movement estimates in a controlled test area.

Changes in wireless measurements are not unique to drones. A central challenge is separating drone-related changes from changes caused by people, interference, or ordinary background variation.

## 2. Scope

### 2.1 In Scope

- Collect labeled CSI datasets for drone activity, empty background, human movement, and interference conditions.
- Record the condition and equipment arrangement for each recording.
- Document the amount of data collected for each condition.
- Train a classifier that distinguishes drone presence from non-drone conditions.
- Evaluate the classifier on recordings
- Implement and evaluate estimates of drone position and movement in a controlled test area.
- Report position error and movement consistency, including conditions where estimation fails.

### 2.2 Out of Scope

- Building the CSI capture and recording platform (Epic #2).
- Final accuracy, missed-detection, false-detection, and effective-range measurements, and the comparison with conventional radar (Epic #4).
- Developing a production-ready drone surveillance system.
- Field deployment and operational security use.

## 3. Related Epics and User Stories

### Epic #3 — Drone Detection

Detect drones and estimate their position and movement using Wi-Fi CSI.

### User Story #14 — Objective 2.1

**Train and evaluate a classifier that distinguishes drone presence from non-drone conditions.**

The dataset must record the condition and equipment arrangement of each recording, document how much data was collected for each condition, and keep training and evaluation recordings separate.

### User Story #15 — Objective 2.2

**Implement and evaluate estimates of drone position and movement in a controlled test area.**

The classifier must be evaluated on recordings excluded from training, and its predictions must be reported for all four conditions.

### User Story #7 — Objective 2.3

**Collect labeled CSI datasets for drone activity, empty background, human movement, and interference conditions.**

The estimates must be compared with recorded reference positions and movements, and the report must include position error, movement consistency, and conditions where estimation fails.

## 4. Functional Requirements

| ID    | Functional Requirement                                                                                                                                       | Related Story |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| FR-01 | When a recording is added to the dataset, the system shall record its condition (drone activity, empty background, human movement, or interference) and the equipment arrangement. | #14 |
| FR-02 | The dataset shall document the amount of data collected for each condition.                                                                                  | #14           |
| FR-03 | The dataset shall keep training recordings and evaluation recordings separate.                                                                               | #14           |
| FR-04 | Each recording shall identify its data source type (live CSI, packet metadata, or synthetic data) as defined in the Wi-Fi CSI Sensing specification.         | #14           |
| FR-05 | When given a recording, the classifier shall predict drone presence or non-drone.                                                      | #15           |
| FR-06 | The evaluation shall report the classifier's predictions for drone activity, empty background, human movement, and interference conditions.                  | #15           |
| FR-07 | When a drone is flown in the controlled test area, the system shall estimate its position and movement.                                                      | #7            |
| FR-08 | The evaluation shall compare the estimates with recorded reference positions and movements, and report position error and how consistently movement is identified. | #7        |
| FR-09 | The evaluation shall report conditions where position or movement estimation fails.                                                                          | #7            |

### 4.1 Requirements Traceability

**Objective 2.1 — Issue #14**

Requirements FR-01, FR-02, FR-03, and FR-04 define how labeled recordings are described, counted, and separated.

**Objective 2.2 — Issue #15**

Requirements FR-05 and FR-06 define classifier behavior and how its predictions are reported.

**Objective 2.3 — Issue #7**

Requirements FR-07, FR-08, FR-09 define position and movement estimation and its evaluation against reference data.

## 5. Non-Functional Requirements

| ID     | Requirement                                                                                                                                       | Purpose         |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| NFR-01 | Substitute targets, if used during development, must be identified separately and must not be presented as evidence of actual drone detection.   | Integrity       |
| NFR-02 | Each recording shall be reproducible from its documented condition and equipment arrangement.                                                     | Reproducibility |       |
| NFR-03 | Original recordings shall be preserved when labeled or processed versions are generated.                                                          | Data integrity  |
| NFR-04 | Another team member shall be able to reproduce the reported predictions from the same recordings and documented procedure.                        | Reproducibility |

## 6. Dependencies

This epic depends on the recordings produced by Epic #2 (see `wifi-csi-sensing.md`):

- Recordings are saved to timestamped files with session identifiers and a source type.
- Recordings are validated for missing or malformed records before use.

The Wi-Fi CSI Sensing specification states that the complete CSI acquisition method has not yet been verified and that the planned ALFA AWUS036AXM adapter may support packet-level capture without full CSI. Until live CSI capture is verified, packet metadata or synthetic data must not be presented as evidence of drone detection (FR-04, NFR-01).

## 7. Data and Labeling

| Condition        | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| Drone activity   | A drone (or a documented substitute) operating in the area |
| Empty background | The test area with no target present                       |
| Human movement   | A person moving through the test area                      |
| Interference     | Other wireless activity present during recording           |

## 8. Acceptance Criteria

### 8.1 Objective 2.1 — Labeled Datasets (#14)

- [ ] Recordings include drone activity, empty background, human movement, and documented interference conditions.
- [ ] Each recording has a condition label, session identifier, and equipment/setup information.
- [ ] The inventory reports the number and duration of recordings for each condition.
- [ ] Entire recording sessions are assigned to separate training and evaluation sets, with no session shared between them.
- [ ] A teammate can follow the documentation to load recordings and identify

### 8.2 Objective 2.2 — Classifier (#15)

- [ ] The classifier is trained using the labeled CSI training recordings from #14.
- [ ] Evaluation uses recording sessions excluded from training and model selection.
- [ ] Results report correct detections, missed drones, and false detections, separately for the tested conditions.
- [ ] Training and evaluation instructions document the data split, configuration, and commands needed to reproduce the results.

### 8.3 Objective 2.3 — Position and Movement (#7)

- [ ] The test procedure defines the reference positions, movements, and how they are measured.
- [ ] The implementation produces position and movement estimates from CSI recordings.
- [ ] Position estimates are compared with reference measurements, and position errors are reported.
- [ ] Movement estimates are compared with recorded reference movements, and the evaluation method and results are documented.
- [ ] Instructions describe how to reproduce the evaluation, including failed cases and limitations.

### 8.4 Specification Task

This specification task is complete when:

- [ ] The purpose and scope of Epic #3 are documented.
- [ ] Functional requirements are defined and linked to related user stories.
- [ ] Non-functional requirements are documented.
- [ ] Measurable acceptance criteria are provided.
- [ ] Dependencies, risks, and unresolved questions are identified.
- [ ] The specification is summarized and linked in proposal Section 4.
- [ ] Repository validation checks pass.
- [ ] The document is reviewed and merged into the team's development branch.

Completion of this documentation task does not imply that any detection functionality has been implemented.


## 9. Open Questions

| Question                                                                                    | Responsible Area       |
| ------------------------------------------------------------------------------------------- | ---------------------- |
| Which classifier approach will be used?                                                     | Data Processing        |
| How will training and evaluation recordings be split?                                       | Data Processing        |
| Which drone or substitutes target will be used, and how will substitutes be labeled?           | Data Collection        |
| What is the size of the controlled test area?                                               | Sensing / Evaluation   |
| How will reference positions and movements be recorded?                                     | Sensing / Evaluation   |
| How much data per condition is needed?                                                      | Data Collection        |

These questions will be resolved through hardware verification and team design decisions.

## 10. Related Documents

- [Wi-Fi CSI Sensing Specification](wifi-csi-sensing.md)
- Evaluation Specification (epic #4, pending its own PR)
- [Project Proposal](../../proposal/proposal.md)
- [Epic #3 — Drone Detection](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/3)
- [User Story #14 — Labeled CSI Datasets](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/14)
- [User Story #15 — Classifier](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/15)
- [User Story #7 — Position and Movement](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/7)

## 11. Current Development Status

This document is a requirements specification. It does not claim that any dataset collection, classifier training, or position estimation has been completed or verified.

The work depends on verified CSI capture from Epic #2, which the Wi-Fi CSI Sensing specification describes as still in preliminary hardware verification.