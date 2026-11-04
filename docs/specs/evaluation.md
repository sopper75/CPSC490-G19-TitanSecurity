**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Sponsor:** Raytheon Applied Signal Technology (RTX-AST)  
**Epic:** #4 — Evaluation  
**Related User Stories:** #6, #16, #17  
**Task:** #50 - Evaluation Specification  
**Sprint:** Sprint 2  
**Status:** Draft

---

## 1. Overview

The purpose of the Evaluation specification is to measure how well the Radar over WiFi prototype detects drones and to describe its practical trade-offs compared with conventional radar.

The component evaluates the classifier developed under the Drone Detection epic (#3) on held-out test recordings, measures detection at multiple distances to find the effective range, and compares the prototype's cost, portability, and setup effort with selected conventional radar systems.

The benefits of the approach (affordability, portability, and setup effort) will be measured rather than assumed. Results will describe only the equipment, environments, and conditions actually tested.

The radar comparison is literature-based. The team is not committing to obtain radar equipment.

## 2. Scope

### 2.1 In Scope

- Measure drone-detection accuracy, missed detections, and false detections on held-out test recordings.
- Define how each metric is calculated.
- Present results separately for each tested condition.
- Measure detection performance at multiple distances to determine the effective detection range.
- Define the distance reference, test arrangement, and success criterion before testing.
- Record the prototype's equipment cost, physical size, weight, and setup time.
- Compare these measurements with published information for selected conventional radar systems.

### 2.2 Out of Scope

- Building the CSI capture platform (Epic #2).
- Training the classifier and building position estimation (Epic #3).
- Obtaining, operating, or testing radar equipment.
- Any claim of suitability for operational security or field deployment.

## 3. Related Epics and User Stories

### Epic #4 — Evaluation

Evaluate detection performance and practical trade-offs against conventional radar.

### User Story #6 — Objective 3.1

**Measure drone-detection accuracy, missed detections, and false detections on held-out test recordings.**

The report must define how each metric is calculated and present results separately for the tested conditions, so that the effects of human movement and interference are visible.

### User Story #16 — Objective 3.2

**Measure drone-detection performance at multiple distances to determine the effective detection range.**

The distance reference, test arrangement, and success criterion must be defined before the evaluation. Trials are repeated at each tested distance, and the farthest tested distance that meets the criterion is reported.

### User Story #17 — Objective 3.3

**Compare prototype cost, portability, and setup effort with selected conventional radar systems using documented evidence.**

The comparison must identify unavailable data and differences in capabilities or testing conditions.

## 4. Functional Requirements

| ID    | Functional Requirement                                                                                                                       | Related Story |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| FR-01 | When the classifier is run on held-out test recordings, the evaluation shall report drone-detection accuracy, missed detections, and false detections. | #6    |
| FR-02 | The evaluation report shall define how each metric is calculated.                                                                            | #6            |
| FR-03 | The evaluation shall present results separately for each tested condition so that the effects of human movement and interference are visible. | #6           |
| FR-04 | Before testing at multiple distances, the team shall define the distance reference, test arrangement, and criterion for successful detection. | #16          |
| FR-05 | When testing at each distance, the team shall repeat trials.                                                                                 | #16           |
| FR-06 | The evaluation shall report the farthest tested distance that meets the detection criterion under the tested conditions.                     | #16           |
| FR-07 | The team shall record the prototype's equipment cost, physical size, weight, and setup time.                                                 | #17           |
| FR-08 | The comparison shall use published information for the selected radar systems.                                                               | #17           |
| FR-09 | The comparison shall identify unavailable data and differences in capabilities or testing conditions.                                        | #17           |

### 4.1 Requirements Traceability

**Objective 3.1 — Issue #6**

Requirements FR-01, FR-02, and FR-03 define the detection metrics and how they are reported.

**Objective 3.2 — Issue #16**

Requirements FR-04, FR-05, and FR-06 define the effective-range measurement.

**Objective 3.3 — Issue #17**

Requirements FR-07, FR-08, and FR-09 define the cost, portability, and setup comparison.

## 5. Non-Functional Requirements

| ID     | Requirement                                                                                                                                       | Purpose         |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| NFR-01 | Surrogate targets, if used during development, shall be identified separately and shall not be presented as evidence of actual drone detection.   | Integrity       |
| NFR-02 | Performance thresholds, trial counts, and test distances shall be specified before the final evaluation.                                          | Validity        |
| NFR-03 | Every reported result shall state the equipment, environment, and conditions actually tested.                                                     | Traceability    |
| NFR-04 | Every figure taken from published radar information shall cite its source.                                                                        | Verifiability   |
| NFR-05 | Another team member shall be able to reproduce the reported metrics from the same recordings and documented procedure.                            | Reproducibility |

## 6. Dependencies

- Held-out test recordings and the classifier come from Epic #3 (see `drone-detection.md`).
- Recordings and their metadata come from Epic #2 (see `wifi-csi-sensing.md`).

The Wi-Fi CSI Sensing specification states that live CSI capture has not yet been verified. Until it is, evaluation results must not be presented as evidence of actual drone detection if the underlying data is packet metadata or synthetic (NFR-01).

## 7. Evaluation Design

The following items are defined before final testing (NFR-02):

| Item                          | To be defined                                         |
| ----------------------------- | ----------------------------------------------------- |
| Metrics                       | How accuracy, missed detections, and false detections are calculated |
| Conditions                    | Drone activity, empty background, human movement, interference |
| Distance reference            | Where distance is measured from and to                |
| Test arrangement              | Equipment placement and environment                   |
| Detection criterion           | What counts as a successful detection                 |
| Distances and trials          | Which distances are tested and how many trials each   |
| Prototype measurements        | Cost, size, weight, and setup time                    |
| Radar comparison              | Which radar systems and which published sources       |

## 8. Acceptance Criteria

### 8.1 Objective 3.1 — Detection Metrics (#6)

- [ ] Evaluation uses labeled recording sessions excluded from training and model selection.
- [ ] The report defines the evaluation unit and how accuracy, missed-detection rate, and false-detection rate are calculated.
- [ ] Results include correct detections, missed drones, false detections, and correct non-drone predictions.
- [ ] Results are reported separately for drone activity, empty background, human movement, and interference conditions, using applicable metrics.
- [ ] The report identifies the dataset and model used and provides instructions to reproduce the evaluation.

### 8.2 Objective 3.2 — Effective Range (#16)

- [ ] Before testing, document the equipment arrangement, distance reference, tested distances, trials per distance, and successful-detection criterion.
- [ ] Conduct repeated drone-present and drone-absent trials at each tested distance.
- [ ] Report detection rates, missed detections, and false detections at each distance.
- [ ] Identify the farthest tested distance meeting the predefined criterion, or report that none met it.
- [ ] Document test conditions and limitations without claiming performance beyond the tested distances.

### 8.3 Objective 3.3 — Radar Comparison (#17)

- [ ] Record the prototype’s equipment list, costs, physical size, and weight.
- [ ] Measure setup time using a documented start and end condition.
- [ ] Identify the radar systems selected for comparison and cite the sources used.
- [ ] Compare available cost, portability, and setup information; mark unavailable information explicitly.
- [ ] Explain differences in capabilities and testing conditions without claiming equivalent performance.

### 8.4 Specification Task

This specification task is complete when:

- [ ] The purpose and scope of Epic #4 are documented.
- [ ] Functional requirements are defined and linked to related user stories.
- [ ] Non-functional requirements are documented.
- [ ] Measurable acceptance criteria are provided.
- [ ] Dependencies, risks, and unresolved questions are identified.
- [ ] The specification is summarized and linked in proposal Section 4.
- [ ] Repository validation checks pass.
- [ ] The document is reviewed and merged into the team's development branch.

Completion of this documentation task does not imply that any evaluation has been performed.

## 9. Technical Risks and Limitations

### 9.1 Criteria Chosen After Seeing Results

Setting thresholds or distances after seeing results can bias the evaluation.

**Mitigation:** Specify performance thresholds, trial counts, and test distances before the final evaluation (NFR-02).

### 9.2 Limited Published Radar Data

Published information for conventional radar systems may be incomplete or measured under different conditions.

**Mitigation:** Identify unavailable data and differences in testing conditions explicitly (FR-09).

### 9.3 Limited Test Environment

Results from a controlled area may not carry over to other environments.

**Mitigation:** State the equipment, environment, and conditions with every result (NFR-03).

### 9.4 Non-CSI Data

If only packet metadata or synthetic data is available, the evaluation cannot show actual drone detection.

**Mitigation:** Label the source type of all evaluation data and report results accordingly (NFR-01).

## 10. Open Questions

| Question                                                                         | Responsible Area       |
| -------------------------------------------------------------------------------- | ---------------------- |
| Which conventional radar systems will be compared?                               | Evaluation             |
| What is the success criterion for detection at a given distance?                 | Evaluation             |
| Which distances will be tested, and how many trials at each?                     | Evaluation             |
| What counts as setup time, and how is it timed?                                  | Evaluation             |
| Which items count toward the prototype's equipment cost?                         | Evaluation             |
| How is each detection metric calculated?                                         | Data Processing        |

These questions will be resolved through team design decisions before the final evaluation.

## 11. Related Documents

- [Wi-Fi CSI Sensing Specification](wifi-csi-sensing.md)
- [Drone Detection Specification](drone-detection.md)
- [Project Proposal](../../proposal/proposal.md)
- [Epic #4 — Evaluation](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/4)
- [User Story #6 — Detection Metrics](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/6)
- [User Story #16 — Effective Range](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/16)
- [User Story #17 — Radar Comparison](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/17)

## 12. Current Development Status

This document is a requirements specification. It does not claim that any evaluation has been performed or that any result has been obtained.

The evaluation depends on the classifier from Epic #3, which in turn depends on verified CSI capture from Epic #2. This specification will be updated as those results are confirmed.