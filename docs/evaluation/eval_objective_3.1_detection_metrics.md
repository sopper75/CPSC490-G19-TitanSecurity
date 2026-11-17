# Evaluation Report — Objective 3.1: Drone-Detection Metrics on Held-Out Test Recordings

**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Epic:** #4 — Evaluation  
**User Story:** #6 — Objective 3.1  
**Related Spec:** `docs/specs/evaluation.md` (FR-01 to FR-03, AC 8.1)  
**Status:** Template / Procedure (pending actual held-out recordings and classifier)

---

## 1. Purpose

This document defines the evaluation unit, metric calculations, and reporting structure for measuring drone-detection accuracy, missed detections, and false detections on held-out test recordings (Issue #6). Results will be reported separately by condition so the effects of human movement and interference are visible.

## 2. Evaluation Unit

- **Unit of evaluation:** One labeled recording session (entire session kept together; no mixing of training/evaluation sessions per FR-03 / NFR-05).
- **Prediction:** Classifier output of “drone present” or “non-drone” for the session (or for fixed-length windows if the implementation uses sliding windows — document the choice).
- **Ground truth:** Session condition label from the dataset inventory (drone activity, empty background, human movement, interference).

## 3. Metric Definitions

| Metric | Definition | Formula |
|--------|------------|---------|
| Correct detection (True Positive) | Drone-activity session predicted as drone present | TP |
| Missed drone (False Negative) | Drone-activity session predicted as non-drone | FN |
| False detection (False Positive) | Non-drone session (empty / human / interference) predicted as drone present | FP |
| Correct non-drone (True Negative) | Non-drone session predicted as non-drone | TN |
| Accuracy | (TP + TN) / (TP + TN + FP + FN) | — |
| Missed-detection rate | FN / (TP + FN) | Also called miss rate or false-negative rate |
| False-detection rate | FP / (FP + TN) | Also called false-alarm rate |

**Reporting rules:**
- Report counts and rates separately for each condition.
- For empty / human / interference, the primary interest is the false-detection rate.
- State the evaluation unit and any windowing or aggregation method.

## 4. Required Results Table (Example / Simulated Data)

**Note:** The numbers below are **simulated example results** generated for documentation completeness. They illustrate the expected reporting format. Replace with actual held-out evaluation results when available. These do **not** represent measured performance of the prototype.

| Condition | Sessions | TP | FN | FP | TN | Accuracy | Missed-detection rate | False-detection rate |
|-----------|----------|----|----|----|----|----------|-----------------------|----------------------|
| Drone activity | 12 | 10 | 2 | — | — | 83% | 17% | — |
| Empty background | 10 | — | — | 1 | 9 | 90% | — | 10% |
| Human movement | 10 | — | — | 2 | 8 | 80% | — | 20% |
| Interference | 8 | — | — | 2 | 6 | 75% | — | 25% |
| **Overall** | 40 | 10 | 2 | 5 | 23 | 82.5% | 17% | 18% |

Example observations (simulated):  
- Strong performance on empty background.  
- Higher false detections under human movement and interference, as expected for CSI-based sensing.  
- Missed detections mainly at edge cases or low signal strength.

## 5. Reproduction Instructions

1. Use only recording sessions assigned to the held-out evaluation set (documented in the dataset inventory from Objective 2.1 / #14).
2. Load the trained classifier (version / commit hash).
3. Run the evaluation script (to be added under `prototype/`) on the held-out files.
4. Generate the results table above and any confusion matrix.
5. Record the environment (Python version, dependencies, hardware) and the exact command.

**Example command placeholder:**
```bash
python prototype/evaluate.py --data data/eval/ --model models/drone_clf_v1.pkl --output reports/eval_3.1.md
```

## 6. Acceptance Criteria Checklist (#6)

- [ ] Evaluation uses labeled recording sessions excluded from training and model selection.
- [ ] The report defines the evaluation unit and how accuracy, missed-detection rate, and false-detection rate are calculated.
- [ ] Results include correct detections, missed drones, false detections, and correct non-drone predictions.
- [ ] Results are reported separately for drone activity, empty background, human movement, and interference conditions.
- [ ] The report identifies the dataset and model used and provides instructions to reproduce the evaluation.

## 7. Notes / Limitations

- Until verified live CSI capture and labeled held-out sessions exist, this remains a procedure template.
- Surrogate targets (if any) must be identified separately and must not be presented as evidence of actual drone detection (NFR-01).
- All results must state the equipment, environment, and conditions actually tested (NFR-03).

---

**Next steps:** Once held-out recordings and a trained classifier are available, fill the results table and attach the raw output. Link this document from the Evaluation epic (#4) and from Issue #6.
