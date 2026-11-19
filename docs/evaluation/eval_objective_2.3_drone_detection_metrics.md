# Evaluation Report — Objective 2.3: Implement and evaluate estimates of drone position and movement in a controlled test area.

**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Epic:** #3 — Evaluation  
**User Story:** #7 — Objective 2.3  
**Related Spec:** `docs/specs/drone-detection.md` 
**Status:** Template / Procedure (pending actual reference measurements and an implemented estimator)

## 1. Purpose

This document defines how the team will test and evaluate its estimates of drone position and movement in a controlled test area (Objective 2.3, issue #7). It is the first acceptance criterion of that story: the test procedure must define the reference positions and movements, and how they are measured.

The procedure is written before any position or movement results exist. It does not claim that estimation has been implemented or that any result has been obtained. Items marked **proposed** are the author's suggestions for the team to confirm. Items marked **to confirm** are open decisions.

## 2. Scope

**In scope.**

- Defining reference positions and movements in the test area and how each is measured.
- Recording CSI sessions that are paired with those references.
- Comparing position and movement estimates with the references and reporting the errors.
- Reporting the conditions in which estimation fails, and the limitations of the setup.

**Out of scope.**

- Building the CSI capture platform (Epic #2).
- Training the drone-presence classifier (story #15).
- Detection range and the comparison with conventional radar (Epic #4).
- Any claim of suitability for field deployment.

## 3. Acceptance Criteria (from issue #7)

- [ ] The test procedure defines the reference positions, movements, and how they are measured.
- [ ] The implementation produces position and movement estimates from CSI recordings.
- [ ] Position estimates are compared with reference measurements, and position errors are reported.
- [ ] Movement estimates are compared with recorded reference movements, and the evaluation method and results are documented.
- [ ] Instructions describe how to reproduce the evaluation, including failed cases and limitations.

This document addresses the first and last criteria. The others are met by the implementation and the evaluation report.

## 4. Test Setup

The setup builds on the November indoor trial, in which five Seeed Studio XIAO ESP32-S3 receivers with external antennas on tripods recorded CSI from pings sent by a GL.iNet GL-MT3000 router over 2.4 GHz Wi-Fi. Two MacBooks each recorded two receivers through a USB hub and saved the raw readings locally.

| Item | Setting | Status |
|---|---|---|
| Transmitter | GL.iNet GL-MT3000 router, 2.4 GHz | Used in the November trial |
| Receivers | Five XIAO ESP32-S3 boards with external antennas on tripods | Used in the November trial |
| Recording computers | Two MacBooks, one Macbook with two receivers, the other Macbook with 3 recievers, and raw readings saved locally | Used in the November trial |
| Test area dimensions | Width, length, and height of the area | To confirm |
| Receiver positions | Fixed tripod positions and antenna heights, measured and recorded | To confirm |
| Router position | Fixed and recorded for every session | To confirm |

The receiver and router positions must stay fixed within a session and be recorded for every session, because a change in the transmitter or receiver placement changes the measured channel.

## 5. Reference Positions and Movements

### 5.1 Reference positions

**Proposed.** The team marks a grid of reference points on the floor of the test area and measures each point's coordinates from a fixed origin with a tape measure. Each reference position is one grid point. For a flying drone, the reference position also records the target's height above the floor.

| Item | Proposed definition |
|---|---|
| Coordinate system | A fixed origin and axes, recorded in the session sheet |
| Reference points | Grid points at a fixed spacing, each with measured coordinates |
| Height | Recorded for each reference point where the target is above the floor |
| Measurement method | Tape measure from the origin, recorded to a stated precision |
| Grid spacing and precision | To confirm |

### 5.2 Reference movements

**Proposed.** Each reference movement is a named path between reference points, performed at a stated speed and repeated several times. Movements are labeled by type so the system's movement estimate can be compared with a known answer.

| Movement label | Description | Status |
|---|---|---|
| Stationary | Target held at one reference point | Proposed |
| Straight line | Target moves along a line between two reference points | Proposed |
| Path through points | Target moves through a sequence of reference points | Proposed |
| Number of repeats and speeds | How many repetitions of each path and at what speed | To confirm |

### 5.3 Reference measurement of movement

**To confirm.** How the true path and timing of a movement are recorded. One option is to record the start and end time of each path by hand while the operator follows the marked points. Another is to use a recording of the area. The method must give timestamps that can be matched to the CSI timestamps (see Section 6).

## 6. Procedure

For each session:

1. Place the transmitter and receivers at their recorded positions and confirm that all receivers are recording.
2. Fill in the session sheet: session identifier, date, test area, equipment arrangement, receiver and router positions, and the target used.
3. Start the capture on each recording computer and note the start time.
4. For a stationary reference, place the target at a reference point and record its measured coordinates and the time the target is in place.
5. For a movement reference, perform the named path, and record the start and end time of the path.
6. Stop the capture and save the raw readings. Keep the originals unchanged.
7. Run the quality checks on the recording before it is used for estimation.
8. Add the session to the evaluation set only if it passes the checks.

The reference data and the CSI data must share a clock, or their offset must be recorded. If the clocks differ, the offset is recorded for every session so the reference times can be matched to the CSI timestamps.

## 7. Target

The target is a drone where it is possible to fly one in the test area. Any stand-in target (for example, a person carrying a marker, or a reflector) is recorded as a surrogate in the session sheet. Surrogate results are reported separately and are never presented as evidence of actual drone position or movement estimation.

## 8. Data Recorded

Each session is stored with the fields defined in the Wi-Fi CSI Sensing specification (session identifier, UTC timestamp, receiver identifier, source type, capture method, Wi-Fi channel, frequency, and measurement values) and with the following reference data.

| Field | Description |
|---|---|
| `session_id` | Identifier shared with the CSI recording |
| `target_type` | Drone or a named surrogate |
| `reference_type` | Stationary or a movement label |
| `reference_position` | Measured coordinates (and height) of the reference point |
| `reference_start` and `reference_end` | Times the reference position or movement began and ended |
| `clock_offset` | Offset between the reference clock and the CSI timestamps |
| `notes` | Anything unusual: interference, people in the area, equipment changes |

## 9. Evaluation Method

**Proposed.**

| Quantity | Definition |
|---|---|
| Position error | The distance between the estimated position and the reference position for the same time |
| Position error summary | Reported per reference point and as an overall summary across points |
| Movement consistency | The fraction of repeated movements for which the estimated movement matches the reference movement label |
| Failure case | A session in which estimation produced no result, or an error larger than a stated limit |

The error limit, the summary statistics (for example, the mean and the largest error), and the match rule for movements are **to confirm**, and are fixed before the final evaluation so they are not chosen after the results are seen.

Results are reported separately for each condition tested, and each result states the equipment, the environment, and the target actually used.

## 10. Failure Cases and Limitations

The report lists every session where estimation failed, with the cause if known, for example interference, a receiver outage, a reference measurement problem, or a poor fit between the estimate and the reference. It also states the limits of the setup: the size of the test area, the number of receivers, the reference precision, and the conditions that were not tested.

## 11. Reproducing the Evaluation

Another team member can repeat the evaluation from the repository by following these steps:

1. Obtain the recordings and the session sheets for the evaluation set.
2. Run the quality checks on each recording.
3. Run the estimation code on each recording.
4. Run the comparison script, which matches estimates with the reference data by timestamp and reports position error and movement consistency.
5. Compare the output with the reported results.

The exact commands are added here when the implementation exists. **To confirm.**

## 12. Open Questions

| Question | Responsible Area |
|---|---|
| What are the test area's dimensions, and where is the origin? | Sensing / Evaluation |
| What grid spacing and measurement precision are used for reference positions? | Sensing / Evaluation |
| How are the true path and timing of a movement recorded? | Sensing / Evaluation |
| How many repeats of each movement, and at what speeds? | Evaluation |
| What error limit counts as a failed estimate? | Evaluation |
| Will a real drone be flown, or will a surrogate be used for the first evaluation? | Project Team |
| Do the reference and CSI recordings share a clock? | Data Collection |

## 13. Related Documents

- [Wi-Fi CSI Sensing Specification](../specs/wifi-csi-sensing.md)
- [Drone Detection Specification](../specs/drone-detection.md)
- [Objective 2.3 — Issue #7](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/7)
- [Epic #3 — Drone Detection](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/3)

## 14. Current Status

This is a draft procedure. No position or movement estimates have been produced, and no reference measurements have been taken. The November trial recorded stillness, walking, and reflector conditions, and did not include reference positions. This document defines what must be added to that setup before position and movement can be evaluated.