# Research highlights and anomalies

## 2026-10-29 — fixture check, before model training

- **Observation:** `study.py check` passed and produced 1,797 rows × 64 features, split as 1,078 train / 359 validation / 360 test. Evidence: `fixture-check` in `../research/evidence.json`.
- **Interpretation:** The bundled partition has expected dimensions and the fixture's assertions passed for disjoint/complete splits, normalized pixel bounds, seed registration, and registered decay-arm names. This is a code/data sanity check only; it says nothing about accuracy or regularization.
- **Anomaly / caution:** The protocol labels its primary comparison confirmatory, but the only result so far is research/setup validation. The directional hypothesis remains prospective until comparative training is complete. No confirmatory result exists yet.
- **Alternatives to a future apparent gain:** random initialization/training variation; an implementation or metric error; differences in checkpoint provenance; finite test-example variation. Matched seeds, deterministic execution, checkpoint reload checks, stored predictions, baselines, and paired resampling address some of these explanations but cannot eliminate all of them.
- **Learning:** Literature supports AdamW as a distinct decoupled regularization method and reports benefits in other settings; it supplies no valid basis to assume that this fixed digits result must be positive. Preserve positive, negative, and inconclusive outcomes symmetrically.

No model has been trained and no result has been excluded.

## 2026-10-29 — registered comparisons, after pilot publication

- **Observation:** The complete registered comparison finished successfully. Regularized, unregularized, and 0.001-decay MLPs had identical test accuracies for each seed: 96.39%, 96.94%, and 96.94%. The matched primary differences were all zero; paired conditional bootstrap interval was exactly [0, 0]. Evidence: `experiment-analysis` and the fourteen run IDs in `../research/evidence.json`.
- **Control/baseline observations:** Shuffled-label accuracies were 6.11%, 11.67%, and 10.83%; logistic regression was 95.56%; class prior was 10.28%. The control is consistent with the expected loss of useful signal after shuffling labels. Auxiliary comparisons remain exploratory/descriptive.
- **Learning:** The directional prediction of a positive benefit was not observed. An interval of exactly zero here results from identical paired correctness outcomes and does not establish equivalence, identify an effect on logits/loss/weights, or generalize beyond this split and training recipe.
- **Checks:** The separate analysis recomputed accuracy from predictions, verified identical test IDs and labels, and confirmed checkpoint reload flags for every arm. All neural arms ran on CUDA. No arm failed or was excluded, and no protocol change was made.
