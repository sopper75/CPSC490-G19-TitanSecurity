# Evaluation Report — Objective 3.2: Effective Detection Range

**Project:** Titan Security — Radar over WiFi  
**Group:** G19  
**Epic:** #4 — Evaluation  
**User Story:** #16 — Objective 3.2  
**Related Spec:** `docs/specs/evaluation.md` (FR-04 to FR-06, AC 8.2)  
**Status:** Procedure template (to be executed when hardware and classifier are ready)

---

## 1. Purpose

Document the range-test procedure, predefined success criterion, repeated trials at multiple distances, and the farthest tested distance that meets the criterion (Issue #16).

## 2. Pre-Test Definitions (must be fixed before any trials)

| Item | Definition for this evaluation |
|------|--------------------------------|
| **Distance reference** | Horizontal ground distance from the geometric center of the receiver antenna array to the center of the drone (or surrogate). Measured with a laser rangefinder or marked tape on the ground. |
| **Test arrangement** | Receivers on ULANZI MT-79 tripods at approximately 1.2–1.5 m height. Transmitter (GL.iNet GL-MT3000) fixed. Clear line-of-sight preferred; note any obstructions. Indoor or outdoor controlled area. |
| **Successful-detection criterion** | A distance is considered “successful” if the detection rate (correct drone-present predictions) ≥ 80% across the repeated trials at that distance, and the false-detection rate on interleaved drone-absent trials remains ≤ 20%. (Team may adjust the thresholds before testing; record the final values.) |
| **Distances to test** | Suggested starting set: 2 m, 5 m, 10 m, 15 m, 20 m, 30 m (adjust based on preliminary CSI signal strength). Stop when the criterion is no longer met or practical limits are reached. |
| **Trials per distance** | Minimum 10 drone-present trials and 10 drone-absent (empty background) trials per distance. Randomize order within each distance block. |
| **Session length** | Each trial is a fixed-duration recording (e.g., 10–15 s) with the drone either present and hovering/moving at the target distance or absent. |

## 3. Test Procedure

1. Document the full equipment arrangement, exact distances, and the success criterion in this file before starting.
2. For each distance:
   - Position the drone (or surrogate) at the measured distance.
   - Conduct the required number of drone-present recordings.
   - Conduct the required number of drone-absent recordings (interleaved or blocked, but document the method).
   - Label every recording with distance, condition, trial number, and session ID.
3. Run the classifier on all range-test recordings (these may be separate from the held-out set used in Objective 3.1, or a designated subset — document the choice).
4. Compute per-distance metrics.

## 4. Results Table (Example / Simulated Data)

**Note:** The numbers below are **simulated example results** for documentation completeness. They show a plausible short-range degradation curve for a Wi-Fi CSI prototype. Replace with actual range-test data. These do **not** represent measured performance.

| Distance (m) | Drone-present trials | Correct detections | Missed | Detection rate | Drone-absent trials | False detections | False-detection rate | Meets criterion? |
|--------------|----------------------|--------------------|--------|----------------|---------------------|------------------|----------------------|------------------|
| 2 | 10 | 10 | 0 | 100% | 10 | 0 | 0% | Yes |
| 5 | 10 | 9 | 1 | 90% | 10 | 1 | 10% | Yes |
| 10 | 10 | 8 | 2 | 80% | 10 | 2 | 20% | Yes |
| 15 | 10 | 7 | 3 | 70% | 10 | 2 | 20% | No |
| 20 | 10 | 5 | 5 | 50% | 10 | 3 | 30% | No |
| 30 | 10 | 3 | 7 | 30% | 10 | 4 | 40% | No |

**Effective detection range (example):** 10 m (farthest tested distance meeting the ≥80% detection / ≤20% false-detection criterion under the simulated conditions).

Example notes: Detection rate drops with distance as expected for passive CSI sensing. False detections increase at longer ranges due to weaker signal and higher relative noise.

## 5. Acceptance Criteria Checklist (#16)

- [ ] Before testing, document the equipment arrangement, distance reference, tested distances, trials per distance, and successful-detection criterion.
- [ ] Conduct repeated drone-present and drone-absent trials at each tested distance.
- [ ] Report detection rates, missed detections, and false detections at each distance.
- [ ] Identify the farthest tested distance meeting the predefined criterion, or report that none met it.
- [ ] Document test conditions and limitations without claiming performance beyond the tested distances.

## 6. Limitations

- Results apply only to the distances, environment, drone model (or surrogate), and conditions actually tested.
- Do not extrapolate beyond the farthest tested distance.
- Note any differences between indoor/outdoor, multipath, or interference present during the trials.

---

**Next steps:** Finalize the criterion and distance list with the team, then execute the trials and fill the table. Link from Issue #16.
