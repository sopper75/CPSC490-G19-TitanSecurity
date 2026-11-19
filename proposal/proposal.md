# Project Proposal — Radar over WiFi

**Department of Computer Science**

**CPSC 490 Undergraduate Seminar in Computer Science — Proposal for Capstone Project**

**Group G19 — Titan Security** · Sponsor: RTX-2  
Authors: Do, Jonathan (23jdo5), Cao, Delvin (@sopper75), Headley, Zachary (Zwach), Le, Alex (dappurs), Sisavath, Chase (Badtzi)  
Repository: https://github.com/sopper75/CPSC490-G19-TitanSecurity  
Semester: Fall 2026  
Original proposal date: October 4, 2026  
Draft revision date: October 8, 2026  


**Draft status:** Sections 0–2 combine the team's supplied project description with revised wording and proposed objectives. Section 4 now includes the planned Wi-Fi CSI data-flow diagrams and associated design-document references. Sections 3 and 5–7, along with the remaining environment and architecture details in Section 4, still require team completion. The team must review the draft, resolve **TO CONFIRM** fields, add actual issue links, and verify references before submission.

## 0. Abstract

In the present day, cheap and inexpensive drones are widely accessible to the average consumer, increasingly being used to disrupt critical infrastructure, or even pose a potential threat to the public. Early detection of these drones is a critical need as the time between detection and impact can determine how well protected people are from potential drone attacks.  

The problem lies within Radar being the obvious solution, but it has a high cost to implement, especially in the case of detecting relatively small objects such as drones which have small radar signatures.  

Our proposal for a solution involves Wi-Fi. Wi-Fi infrastructure is already widespread within homes, campuses, and venues. Using Wi-Fi signals, one can potentially passively detect drones which create a disturbance in the radio waves being emitted. This disturbance can be picked up by analyzing the Channel State Information [1], allowing detection and even estimation of position and movement without the need to implement or install expensive Radar equipment [2].  

This solution is significant, because it potentially resolves a problem using inexpensive yet effective infrastructure. Wi-Fi signals are low energy, short range, yet highly sensitive to reflectance, interference, and background noise, which allows for detection in the first place.  

The goal of this project is to build a prototype which is effective at detecting small drones or signatures representing drones through Wi-Fi signal waves, with evaluations to it’s accuracy, effective range, and rate of false detections. The expected outcome is an assessment of how useful Wi-Fi sensing at an effective cost could provide useful information far ahead of time to those who need it. The reset of the proposal details our methodology, system design, and evaluation plan. 

## 1. Introduction

Radar detects objects by transmitting radio waves and analyzing reflected signals. Wi-Fi also uses radio waves, primarily to exchange data between devices. Signals can reach a receiver along multiple paths after reflecting from surrounding objects. Movement can change these paths and the measured wireless channel. CSI provides measurements that researchers can use to investigate these changes [1].  

Radar over WiFi will examine whether accessible Wi-Fi equipment can provide useful information about nearby drone activity. A central challenge is distinguishing drone-related changes from changes caused by people, interference, or ordinary background variation. Detecting motion alone would not satisfy the project's drone-detection objective.  

The project is motivated by affordability, portability, and setup effort. These benefits will be evaluated rather than assumed. The initial scope is a controlled experimental prototype; results will describe the equipment, environments, and conditions actually tested. They will not establish suitability for operational security or field deployment.  

### 1.1 Related Work

Halperin et al. describe a tool for collecting CSI, providing a foundation for experimental wireless-channel measurements [1]. Geng's thesis and the related DensePose From WiFi paper investigate estimating human pose from Wi-Fi measurements [2], [3]. These works motivate the use of wireless measurements for sensing, but their human-sensing results do not establish drone-detection performance.  

The team's supplied literature review also identifies BFId, which investigates identity inference using Wi-Fi beamforming feedback [4]. Its relevance is that wireless measurements may reveal information beyond their original communication purpose. It addresses a different measurement source and task from the proposed drone classifier. The ESP-CSI project provides a practical example of human-presence sensing with ESP32 equipment [5]. As a project account, it offers implementation context rather than direct evidence of performance for this project's target.  

| Existing approach | Contribution relevant to this project | Strength | Limitation for our project | How Radar over WiFi differs |
|---|---|---|---|---|
| CSI collection tool [1] | Collection of wireless-channel measurements | Provides a basis for reproducible measurement work | Collection alone does not identify drones; equipment compatibility must be checked | Adds labeled drone experiments and detection evaluation |
| Human-pose estimation [2], [3] | Learning relationships between Wi-Fi measurements and physical activity | Investigates richer outputs than presence alone | Human-pose results do not demonstrate drone sensing or transfer to our equipment | Evaluates drone presence and investigates position and movement |
| BFId [4] | Identity inference from beamforming feedback | Highlights information exposed by wireless measurements | Uses a different task and measurement approach | Focuses on drone-versus-non-drone conditions |
| ESP-CSI presence project [5] | Practical sensing with accessible hardware | Offers prototype and deployment context | Human-presence results are not drone-detection results | Measures drone detection, confounding conditions, and range |

These approaches differ in their measurements, targets, and outputs. The proposed contribution is not that Wi-Fi sensing is new, but that the team will evaluate a specific accessible setup for drone sensing and document its practical limitations. Hardware selection and testing must establish which lessons transfer to this project.

**TO CONFIRM:** Team members must verify the comparison against the sources they have read. Select and cite the conventional radar systems used for the later cost and deployment comparison; none have been identified yet.

### 1.2 Problem Statements

**P1. Reproducible measurements:** The project needs a repeatable way to obtain and preserve usable wireless-channel measurements so experiments can be compared and checked.

**P2. Target discrimination and estimation:** Changes in wireless measurements are not unique to drones. It remains uncertain whether the selected equipment can distinguish drone activity from human movement and interference and support useful estimates of position and movement.

**P3. Performance and practicality:** The detection range, error rates, cost, portability, and setup effort of the proposed system have not been established. Without these measurements, its usefulness and trade-offs relative to conventional radar cannot be assessed.

| Problem | Addressed by |
|---|---|
| P1 | Goal 1; Objectives 1.1–1.2 |
| P2 | Goal 2; Objectives 2.1–2.3 |
| P3 | Goal 3; Objectives 3.1–3.3 |

## 2. Goals and Objectives

### Goal 1: Build a Wi-Fi CSI sensing platform

**[[epic:#2]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/2).**

**Objective 1.1: Set up a Wi-Fi transmitter and receiver pair and demonstrate CSI frame capture.**  
Document the equipment and configuration needed to reproduce the setup, and verify that the receiver captures CSI frames during a test recording. **[[story:#8]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/8).**

**Objective 1.2: Save CSI measurements to timestamped files and verify their data quality.**  
Implement a recording process and check the saved measurements for missing or malformed records and timestamp consistency. Document the checks and their results. **[[story:#13]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/13).**

### Goal 2: Detect drones and estimate their position and movement using Wi-Fi CSI

**[[epic:#3]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/3).**

**Objective 2.1: Collect labeled CSI datasets for drone activity, empty background, human movement, and interference conditions.**  
Record the condition and equipment arrangement for each recording. Document the amount of data collected for each condition and separate training and evaluation recordings. **[[story:#14]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/14).**

**Objective 2.2: Train and evaluate a classifier that distinguishes drone presence from non-drone conditions.**  
Use the labeled datasets to develop the classifier and evaluate it on recordings excluded from training. Report its predictions for drone activity, empty background, human movement, and interference conditions. **[[story:#15]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/15).**

**Objective 2.3: Implement and evaluate estimates of drone position and movement in a controlled test area.**  
Compare the estimates with recorded reference positions and movements. Report position error and how consistently the system identifies movement, including conditions where estimation fails. **[[story:#7]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/7).**

### Goal 3: Evaluate detection performance and practical trade-offs against conventional radar

**[[epic:#4]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/4).**

**Objective 3.1: Measure drone-detection accuracy, missed detections, and false detections on held-out test recordings.**  
Report the evaluation results and define how each metric is calculated. Present results separately for the tested conditions so that the effects of human movement and interference are visible. **[[story:#6]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/6).**

**Objective 3.2: Measure drone-detection performance at multiple distances to determine the effective detection range.**  
Define the distance reference, test arrangement, and criterion for successful detection before conducting the evaluation. Repeat trials at each tested distance and report the farthest tested distance that meets the criterion under those conditions. **[[story:#16]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/16).**

**Objective 3.3: Compare prototype cost, portability, and setup effort with selected conventional radar systems using documented evidence.**  
Record the prototype's equipment cost, physical size, weight, and setup time. Compare these measurements with available published information for the selected radar systems, identifying unavailable data and differences in capabilities or testing conditions. **[[story:#17]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/17).**

The proposed radar comparison is literature-based rather than a commitment to obtain radar equipment. The team must confirm this scope. Performance thresholds, trial counts, and test distances will be specified before final evaluation. Surrogate targets, if used during development, will be identified separately and will not be presented as evidence of actual drone detection.

### Goal 4: Maintain clear team organization and documentation [[epic: #55]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/55)

**Objective 4.1: Define and document team roles and leadership designation.**  
Record each team member's role and the designated team leader in the project README. **[[story:#56]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/56).**

**Objective 4.2: Define different approaches considered and choosen approach.**
Define the approaches considered for achieving the stated goals, listing possible strategies and reasoning that decided between them. **[[story:#67]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/67).**

**Objective 4.3: Complete Sprint 2 Review.**  
Complete the Sprint 2 review in `docs/sprint-reviews/sprint-2.md`, recording progress, velocity, carry-overs, and member contributions for Sprint 2. **[[story:#69]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/69).**

**Objective 4.4: Release the end-of-Sprint-2 build to main.**  
Merge the reviewed Sprint 2 work from develop into main through a release branch and tag it v0.2, so main holds the work submitted for the sprint. **[[story:#73]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/73).**

**Objective 4.5: Add documentation for project proposal for enviornment**
Write §4 environment of the Titan Security project proposal, describing the operating and testing environment, three per-epic specification summaries and a design narrative. **[[story:#97]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/97).**


## 3. Proposed Approaches

Our approach consists of mounting Wifi antennas to tripods, connected to a mini microcontroller detecting CSI packets, and sending the packets received to two computers. These two computers jobs are to filter the packets for any traffic that is not needed. The computers will then send the filtered packets to a main processing computer, which then processes the CSI packets to detect for drone movement & detection.

We considered two alternatives. One was to have only computer filter the CSI packets to be sent for processing. This streamlines the process, and makes the test setup easier to configure. But this creates a single bottleneck, meaning if the packet rate increases, or all the antennas start sending traffic, could slow down the filtering or worse, shut down the pipeline if the computer is overwhelmed. Another was to use standard Wifi adapters to intercept traffic instead of the microcontrollers. These are more familar and more widely available, but usually it's signifcantly harder to capture CSI packets without specailized hardware, making it harder to configure the setup.

We chose two filtering computers feeding one processing computer, using the microcontroller modules, because this keeps each stage's workload manageable and gives us direct access to CSI. Exact implementation is described in §4.

## 4. Required Environment, Resources, and Planned Activities

### 4.1 Environment and resources

For the November indoor trial, we placed four Seeed Studio XIAO ESP32-S3 receivers with external antennas on tripods around the test area. Each board sent pings to a GL.iNet GL-MT3000 router over 2.4 GHz Wi-Fi and recorded channel state information (CSI) from incoming Wi-Fi frames. CSI describes how the signal reaches a receiver at different frequencies. We used a movable metal reflector to compare the readings during stillness, walking, reflector movement, and walking with the reflector.

Two MacBooks each recorded data from two receivers through a USB hub. Each MacBook saved the raw readings locally so we could reanalyze the trial afterward. It also sent a summary over an Ethernet switch to a third MacBook, which displayed one live graph per receiver. The switch connected the three computers. The router provided the wireless link to the receivers and was separate from that wired network.

We built the receiver firmware in C with ESP-IDF 6.0.3 using Espressif’s ESP-CSI router example. We first tested a single receiver on Windows 11 before running the four-receiver setup on macOS. On the recording laptops, Python and pyserial read the USB data. For offline analysis, we used NumPy to calculate how much the signal amplitude varied and Matplotlib to plot those changes over time. The November graphs used these calculations directly; machine learning remains a later stage of the project. [task:#86](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/86)

#### Testing environment

Testing takes place in a controlled area chosen so that the conditions of each session can be documented and repeated. The November indoor trial established the baseline arrangement. Four receivers stood on tripods around the test area, and the router was at a fixed position. A movable metal reflector stood in for a drone. The trial compared four conditions: stillness, a person walking, the reflector moving, and a person walking while the reflector moved. Reflector recordings are labeled as surrogate trials and kept separate from drone trials.

Later sessions will add flights with an actual drone and extend the conditions to the four classes defined in the Drone Detection specification: drone activity, empty background, human movement, and wireless interference. For the effective-range tests under Objective 3.2, the team plans to mount the receivers at roughly 1.2 to 1.5 m and measure distance as the horizontal ground distance from the center of the receiver array to the target. The tested distances, the number of trials at each distance, and the success criterion will be fixed before any range trial is run, so that the results cannot shape the criteria used to judge them.

#### Environmental conditions and setup considerations

Because CSI reflects every path the signal takes from transmitter to receiver, anything that changes those paths changes the measurement. Indoors, walls, floors, furniture, and equipment create multipath reflections, so the same target can produce different readings in different rooms or at different positions within one room. A person is a larger and more reflective target than a small drone, which makes human movement both a likely source of false detections and an explicit test condition. The 2.4 GHz band is shared with campus Wi-Fi networks, Bluetooth devices, and other equipment, whose traffic can add noise to the channel. The team therefore records the channel used in each session and filters out frames that did not come from the test devices.

Antenna height, orientation, and spacing all affect signal strength, as do the distance between transmitter and receivers and whether the path between them is line-of-sight. For that reason, the equipment arrangement is recorded with every session and held constant within any set of trials that will be compared. Because two separate computers record the receivers, their clocks need to be aligned before recordings from different receivers can be combined. Outdoor sessions add wind, temperature changes, and nearby moving vehicles or vegetation as further sources of variation, and these will be noted with each recording. To control for these effects, the team plans to begin each session with a recording of the empty area as its baseline, and to store the condition label, session identifier, equipment arrangement, and channel alongside every timestamped recording. [task:#99](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/99)

**Design diagrams:** This section includes the Wi-Fi CSI sensing data-flow diagrams. The team must also supply a high-level architecture diagram and a system/context diagram, along with other appropriate design views, and keep authoritative copies in `docs/design/`.

### 4.2 Epic Specification Summaries

**Wi-Fi CSI Sensing (Epic #2).** The sensing specification defines how the team configures the transmitter and receivers, captures CSI, and prepares recordings for later analysis. It covers Objective 1.1 (#8), which requires a working transmitter–receiver pair and a demonstrated capture of genuine CSI frames, and Objective 1.2 (#13), which requires each recording to be saved to a timestamped file with a session identifier and checked for missing fields, malformed values, and timestamp inconsistencies. The validator reports how many records it inspected, accepted, and rejected, and original recordings are preserved whenever processed versions are created. The non-functional requirements center on reproducibility: a teammate must be able to repeat the setup and validation using only the documentation. The full requirements and acceptance criteria are in [`docs/specs/wifi-csi-sensing.md`](../docs/specs/wifi-csi-sensing.md).

**Drone Detection (Epic #3).** The detection specification builds on the validated recordings from Epic #2. Objective 2.1 (#14) requires labeled datasets for drone activity, empty background, human movement, and interference. Each recording must document its condition and equipment arrangement, and the dataset must report how much data exists for each condition. Objective 2.2 (#15) requires a classifier that distinguishes drone presence from non-drone conditions. Whole recording sessions are assigned to training, validation, or final test groups, so segments from one session never appear in more than one group. Objective 2.3 (#7) requires estimates of drone position and movement in a controlled area, compared against recorded reference positions, with position error, movement consistency, and failure cases reported. Surrogate targets such as the metal reflector must be labeled separately, and only sessions with a confirmed drone flight count as evidence of drone presence. The full specification is in [`docs/specs/drone-detection.md`](../docs/specs/drone-detection.md).

**Evaluation (Epic #4).** The evaluation specification defines how the prototype's performance and practical trade-offs are measured. Objective 3.1 (#6) requires accuracy, missed detections, and false detections on held-out recordings, with each metric's calculation defined and results reported separately for each condition so that the effects of human movement and interference are visible. Objective 3.2 (#16) requires repeated trials at several distances, against a success criterion fixed in advance, and reports the farthest tested distance that meets it, or states that none did. Objective 3.3 (#17) compares the prototype's cost, size, weight, and setup time with published information for selected conventional radar systems. This comparison is based on the literature: the team is not acquiring radar equipment, and it marks unavailable data and differences in testing conditions explicitly. The full specification is in [`docs/specs/evaluation.md`](../docs/specs/evaluation.md).

The three epics form a dependency chain. Detection relies on validated recordings from sensing, and evaluation relies on the classifier from detection. Each specification therefore states that results built on packet metadata or synthetic data cannot be presented as evidence of drone detection.

### 4.3 Wi-Fi CSI Sensing — Data Flow Design

The proposed Wi-Fi sensing system will collect wireless channel measurements and prepare them for later drone-detection analysis. The data-flow design supports Objective 1.1 (CSI acquisition, issue #8) and Objective 1.2 (timestamped recording and data quality, issue #13).

Figure 1 illustrates the external components involved in the sensing process. The GL.iNet Wi-Fi transmitter sends signals through the experimental environment, where moving objects and interference may affect the wireless channel. A compatible receiver and sensing system will collect measurements and provide recordings and quality reports to the experiment operator. The planned drone detection pipeline will later consume validated CSI data.

![Level 0 CSI data flow showing the transmitter, test environment, sensing system, experiment operator, and future drone detection pipeline](../docs/design/diagrams/csi-dfd-level0.png)

**Figure 1 — Level 0 Wi-Fi CSI Data Flow Diagram.**

Figure 2 expands the sensing system into three proposed processes: capturing CSI measurements, adding timestamps and experimental metadata, and validating recorded data. The design separates raw recordings, validated datasets, and quality reports to support reproducible experiments.

![Level 1 CSI data flow showing measurement capture, timestamping, raw storage, validation, and output datasets](../docs/design/diagrams/csi-dfd-level1.png)

**Figure 2 — Level 1 Wi-Fi CSI Data Flow Diagram.**

Both diagrams describe the planned design rather than completed functionality. Full CSI capture and automated validation have not yet been demonstrated, and the final compatible receiver and acquisition method remain to be confirmed.

The editable Mermaid diagrams, detailed descriptions, and data-flow documentation are maintained in [CSI Data Flow Design](../docs/design/csi-data-flow.md), tracked under [issue #47](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/47).

![High-Level Architecture Diagram](../docs/design/diagrams/high-level-architecture.png)

**Figure 3 - High-level Architecture Diagram.**

Figure 3 provides an overview of the overall Titan Security system and illustrates how its major components work together. The architecture shows how Wi-Fi signals are transmitted through the test environment and collected by multiple ESP32-S3 receivers. The collected CSI measurements are transferred to recording computers, where the data can be stored, processed, and analyzed. The diagram also illustrates how the sensing platform supports the planned drone-detection and evaluation components. This architecture provides a general view of how the individual hardware and software components contribute to the project's overall goal of investigating Wi-Fi-based drone detection.

![System Context](../docs/design/diagrams/system-context.png)

**Figure 4 - System Context Diagram.**

Figure 4 illustrates Titan Security within its surrounding environment and identifies the external components that interact with the system. These include the Wi-Fi transmitter, ESP32-S3 receiver boards, recording computers, and experiment operator. The diagram establishes the system boundary and provides a clearer understanding of which components belong to Titan Security and which provide external input or interaction. The operator is responsible for arranging the equipment, starting and monitoring data collection, and managing the recordings used during testing. The external Wi-Fi equipment provides the signals needed for CSI measurements, while the surrounding test environment can introduce reflections, movement, and interference that affect the collected data. This context helps define the system's operating environment and the equipment required to conduct controlled experiments.

![Sequence Diagram](../docs/design/diagrams/sequence-diagram.png)

**Figure 5 - Sequence Diagram.**

Figure 5 illustrates the sequence of interactions between the different components of the Titan Security system during the data collection process. It shows how the components communicate and how information moves through the system over time. The process begins with the Wi-Fi transmitter sending signals through the test environment. The ESP32-S3 receivers collect CSI measurements from the incoming Wi-Fi frames and transfer the recorded information to the connected computers. The recording computers then store the measurements so they can be reviewed and processed for further analysis. This sequence helps explain the order in which the system components operate and how CSI measurements move from initial collection to later processing and evaluation.

#### Design narrative

Figures 3 through 5 together describe how Titan Security's components interact, following the order in which data moves through the system. As Figure 5 shows, a session begins when the experiment operator configures the router's network, channel, and bandwidth, then starts recording on the capture computers and enters the session's condition and equipment arrangement. The router transmits through the test area, and each ESP32-S3 receiver exchanges traffic with it and extracts CSI from the incoming frames. The drone, people, or objects in the area alter those frames before they arrive.

Each receiver streams its measurements over USB to a capture computer, which reads them with Python and pyserial. Two capture computers each serve two receivers through a USB hub. They save the raw readings locally, so every trial can be reanalyzed, and forward a summary over a wired Ethernet switch to a third computer that displays one live graph per receiver. Sending these summaries over the wired network keeps recording traffic off the wireless channel being measured. A traffic filter then removes baseline traffic and frames from devices outside the test, and the remaining frames are written as timestamped recordings tagged with the session identifier. The validator checks each recording and returns counts of accepted and rejected records to the operator, and accepted recordings enter the validated dataset.

Figure 4 draws the system boundary around this sensing pipeline. The operator, the transmitter, and the test environment lie outside it and supply settings, signals, and disturbances. The drone detection pipeline sits downstream as a consumer of validated recordings. Within Figure 3, the acquisition and processing stages exist in their current form: the November trial produced live graphs and offline NumPy analysis of amplitude variation. The analysis stages are planned. The classifier developed under Epic #3 will consume labeled, validated recordings, and the evaluation work under Epic #4 will score its predictions against the recorded conditions.

Several design decisions shaped this architecture. The team uses several inexpensive receivers placed around the area rather than one specialized receiver. This gives the system multiple views of the same disturbance while keeping the cost and weight of the kit low. ESP32-S3 boards were chosen as receivers because the ALFA adapters' driver does not expose CSI. The alternatives considered were patched OpenWrt firmware that extracts CSI on the MediaTek-based router, and packet-only sensing through the ALFA adapters in monitor mode. The first adds firmware risk, and the second gives a weaker signal than true CSI. Raw recordings are preserved alongside processed versions so that later changes to filtering or validation can be applied to earlier trials without repeating them.

### 4.4 Specification and design documents

**Every specification and design document the team writes must be listed here** with the objective it serves. This section acts as the index of the project's technical detail. CI gate G9 checks for links to these documents.

| Document                                                             | Kind          | Covers                                                                                                | Issues                                                                      |
| -------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [Wi-Fi CSI Sensing Specification](../docs/specs/wifi-csi-sensing.md) | specification | Hardware configuration, CSI acquisition, timestamped recording, data quality, and acceptance criteria | [task:#45](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/45) |
| [CSI Data Flow Design](../docs/design/csi-data-flow.md)              | design        | Level 0 and Level 1 CSI data flow; Objectives 1.1–1.2, high level architecture, sequence diagram, system context diagram | [task:#47](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/47) and [task:#65](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/65)|
| [Drone Detection Specification](../docs/specs/drone-detection.md) | specification | Drone detection requirements and acceptance criteria | [task:#49](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/49) |
| [Evaluation Specification](../docs/specs/evaluation.md) | specification | Detection performance and evaluation requirements | [task:#50](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/50) |

| Document | Kind | Covers | Issues |
|---|---|---|---|
| 〈docs/specs/account-management.md〉 | specification | 〈account management requirements〉 | 〈#n, #n〉 |
| 〈docs/design/architecture.md〉 | design | 〈system architecture + data model〉 | 〈#n〉 |

The CSI Data Flow Design documents the proposed sensing subsystem through Level 0 and Level 1 diagrams. It identifies external inputs, measurement capture, timestamping, raw recording storage, validation, and the intended downstream detection pipeline. It also contains a high level architecture diagram showing how all parts of the system is connected, sequence diagram showing the structural view, and context diagram showing the workflow. Its editable Mermaid source and exported images are maintained in `docs/design/`.

The specification was merged through for Wi_Fi Sensing Specification [PR #46](https://github.com/sopper75/CPSC490-G19-TitanSecurity/pull/46), Drone Detection Specification [PR#59] https://github.com/sopper75/CPSC490-G19-TitanSecurity/pull/59. and Evaluation Specification [PR#61]. The design document was developed under [issue #47](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/47) and [issue:#65](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/65)

**Remaining documentation:** The team must add other specifications and design documents to this index as they are completed. The repository's worked examples, `docs/specs/example-spec.md` and `docs/design/example-design.md`, should be handled according to the course repository instructions.

### 4.5 Planned activities — the work items

The goals and objectives are listed in §2 as epics and user stories. The following table links supporting work items.

| Issue | Type | Activity | Parent | Owner | Sprint |
|---|---|---|---|---|---|
| [[task:#11]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/11) | task | Update proposal sections 0–2 | Standalone | 23jdo5 | Sprint 1 |
| [[task:#20]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/20) | task | Clean up proposal header and §2 issue links | Standalone | sopper75 | Sprint 1 |
| [[task:#23]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/23) | task | Update course files to CPSC 490 c155339 | Standalone | sopper75 | Sprint 1 |
| [[task:#26]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/26) | task | Revise §0–§1 from HW#4 feedback | Standalone | sopper75 | Sprint 1 |
| [[task:#27]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/27) | task | Write §1.1 Related Work (comparative table) | Standalone | Zwach | Sprint 1 |
| [[task:#28]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/28) | task | Write §1.2 Problem Statements P1..Pn | Standalone | Zwach | Sprint 1 |
| [[task:#29]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/29) | task | Write §2 Goals and Objectives | Standalone | 23jdo5 | Sprint 1 |
| [[task:#34]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/34) | task | Add #23 and #26-#29 to §4 | Standalone | dappurs | Sprint 1 |
| [[task:#51]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/51) | task | Add Drone Detection (#49) and Evaluation (#50) specifications to proposal §4 | Standalone | dappurs | Sprint 2 |
| [[story:#13]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/13) | user-story | Objective 1.2: Save CSI measurements to timestamped files and verify their data quality | Epic #2 | sopper75 | Sprint 3 |
| [[story:#14]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/14) | user-story | Objective 2.1: Collect labeled CSI datasets for drone activity, empty background, human movement, and interference conditions | Epic #3 | Badtzi | Sprint 3 |
| [[story:#15]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/15) | user-story | Objective 2.2: Train and evaluate a classifier that distinguishes drone presence from non-drone conditions | Epic #3 | 23jdo5 | Sprint 3 |
| [[story:#7]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/7) | user-story | Objective 2.3: Implement and evaluate estimates of drone position and movement in a controlled test area | Epic #3 | dappurs | Sprint 3 |
| [[task:#86]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/86) | task | Write the hardware and software setup in proposal §4 (merged in [PR #87](https://github.com/sopper75/CPSC490-G19-TitanSecurity/pull/87)) | Standalone | 23jdo5 | Sprint 3 |
| [[task:#88]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/88) | task | Write the classifier training and evaluation plan (merged in [PR #89](https://github.com/sopper75/CPSC490-G19-TitanSecurity/pull/89)) | Objective 2.2 | 23jdo5 | Sprint 3 |
| [[pr:#90]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/pull/90) | pull request | Add evaluation report for Objective 3.1 | Objective 3.1 | Badtzi | Sprint 3 |
| [[task:#91]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/91) | task | Add Sprint 3 and 4 work items under Planned Activities | Standalone | sopper75 | Sprint 3 |
| [[story:#6]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/6) | user-story | Objective 3.1: Measure drone-detection accuracy, missed detections, and false detections on held-out test recordings | Epic #4 | dappurs | Sprint 4 |
| [[story:#16]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/16) | user-story | Objective 3.2: Measure drone-detection performance at multiple distances to determine the effective detection range | Epic #4 | Zachary-Headley | Sprint 4 |
| [[story:#17]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/17) | user-story | Objective 3.3: Compare prototype cost, portability, and setup effort with selected conventional radar systems using documented evidence | Epic #4 | 23jdo5 | Sprint 4 |

### 4.6 Remaining work

Sprint 3 builds the data and modeling foundation. Titan Security plans to finish the recording process so CSI measurements are saved to timestamped files and checked for missing or malformed records (Objective 1.2), then use it to collect labeled datasets for drone activity, empty background, human movement, and interference conditions (Objective 2.1). A classifier that separates drone presence from non-drone conditions will be trained and evaluated on recordings held out from training (Objective 2.2). Position and movement estimates will be implemented and compared against recorded reference positions in a controlled test area (Objective 2.3). The hardware and software setup description, the classifier training and evaluation plan, and an evaluation report for Objective 3.1 are merged. The Drone Detection and Evaluation specification text for §4 carries over from Sprint 2.

Sprint 4 turns the Sprint 3 results into the project's evaluation. The team plans to measure detection accuracy, missed detections, and false detections on held-out recordings, reporting results separately for each tested condition (Objective 3.1). Detection will then be repeated at multiple distances against a success criterion defined beforehand, to find the farthest tested distance that meets it (Objective 3.2). Finally, the prototype's cost, portability, and setup effort will be compared with published information for the selected conventional radar systems, noting unavailable data and differences in testing conditions (Objective 3.3). Performance thresholds, trial counts, and test distances will be fixed before final evaluation, and results will describe only the equipment and conditions actually tested.

## 5. Project Outcomes

> Describe the outcomes or deliverables, e.g., final project report, user manuals, source code, data or database files, etc.
>
> Note: the deliverables always include the team GitHub repository, which must already contain prototype v0 (a thin end-to-end proof-of-concept, however small, running when this proposal is submitted). Briefly describe what your v0 demonstrates and how to run it.

〈**One or two paragraphs** explaining the project outcome overall — what will exist when the project is finished, and what it will let someone do. Keep it prose, not a checklist; name the deliverables inside the paragraphs, and say briefly what prototype v0 demonstrates today and how to run it.〉

## 6. Project Timeline

> Identifies tasks (project objectives) to be performed, milestones to be met, and the estimated number of hours for each task.

〈**This is the plan for CPSC 491 next semester** — the implementation timeline, not this semester's proposal work. Identify the tasks (your objectives from §2), the milestones, and the estimated hours for each task, in the order they will be built. State the assumptions it rests on (sponsor availability, data access, hardware).〉

| Task (objective) | Milestone | Owner | Est. hours | Spring phase |
|---|---|---|---|---|
| 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 |
| 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 |

〈Do **not** put this fall's four proposal sprints here — those live on the project board and in `docs/sprint-reviews/`. This section answers "how does the system actually get built next semester?"〉

## 7. AI Usage

> Per the course AI policy (see the syllabus, Use of AI Tools), disclose the AI tools used in preparing this proposal and the prototype: which tools, for what tasks (e.g., code generation, test writing, debugging, diagramming), and approximately what fraction of each artifact was AI-assisted.
>
> Reminder: the prose of this proposal must be your own writing. You remain fully responsible for the correctness of all AI-assisted work, including the prototype code.

〈Your disclosure. Naming the tool is not disclosure — name what it drafted, what fraction of each artifact was AI-assisted, and how you verified it.〉

## 8. References

The following references are retained from the team's supplied draft. Their bibliographic details and support for the statements above require team verification; inclusion here does not certify that they have been independently checked.

[1] Halperin, D., Hu, W., Sheth, A., and Wetherall, D. “Tool Release: Gathering 802.11n Traces with Channel State Information.” *ACM SIGCOMM Computer Communication Review*, 41(1), p. 53, 2011. https://doi.org/10.1145/1925861.1925870

[2] Geng, J. *Dense Human Pose Estimation From WiFi*. Master's thesis, Carnegie Mellon University, Technical Report CMU-RI-TR-22-59, 2022. https://publications.ri.cmu.edu/dense-human-pose-estimation-from-wifi

[3] Geng, J., Huang, D., and De la Torre, F. *DensePose From WiFi*. arXiv:2301.00250. https://arxiv.org/abs/2301.00250. **TO CONFIRM: publication year; the supplied draft lists 2022.**

[4] Todt, J., Morsbach, F., and Strufe, T. “BFId: Identity Inference Attacks Utilizing Beamforming Feedback Information.” *Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security*, pp. 2399–2413, 2025. https://doi.org/10.1145/3719027.3765062

[5] Mengdu. “ESP-CSI: DIY WiFi Human Presence Detection.” *Hackster.io*, January 15, 2026. https://www.hackster.io/limengdu0117/esp-csi-diy-wifi-human-presence-detection-f80508. Accessed October 4, 2026, as recorded in the team's draft.
