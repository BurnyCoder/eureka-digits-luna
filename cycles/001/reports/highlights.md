# Research highlights and anomalies

## 2026-10-29 — fixture check, before model training

- **Observation:** `study.py check` passed and produced 1,797 rows × 64 features, split as 1,078 train / 359 validation / 360 test. Evidence: `fixture-check` in `../research/evidence.json`.
- **Interpretation:** The bundled partition has expected dimensions and the fixture's assertions passed for disjoint/complete splits, normalized pixel bounds, seed registration, and registered decay-arm names. This is a code/data sanity check only; it says nothing about accuracy or regularization.
- **Anomaly / caution:** The protocol labels its primary comparison confirmatory, but the only result so far is research/setup validation. The directional hypothesis remains prospective until comparative training is complete. No confirmatory result exists yet.
- **Alternatives to a future apparent gain:** random initialization/training variation; an implementation or metric error; differences in checkpoint provenance; finite test-example variation. Matched seeds, deterministic execution, checkpoint reload checks, stored predictions, baselines, and paired resampling address some of these explanations but cannot eliminate all of them.
- **Learning:** Literature supports AdamW as a distinct decoupled regularization method and reports benefits in other settings; it supplies no valid basis to assume that this fixed digits result must be positive. Preserve positive, negative, and inconclusive outcomes symmetrically.

No model has been trained and no result has been excluded.
