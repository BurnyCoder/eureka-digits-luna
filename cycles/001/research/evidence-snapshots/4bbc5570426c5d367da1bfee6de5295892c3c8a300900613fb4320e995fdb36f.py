"""Recompute registered accuracy summaries and paired conditional bootstrap."""
from pathlib import Path
import hashlib
import json

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUT = ROOT / "research" / "experiment-analysis.json"


def read(identifier):
    """Load a preserved fixture record by its registered experiment ID."""
    return json.loads((RESULTS / f"{identifier}.json").read_text(encoding="utf-8"))


def main():
    """Validate predictions and derive all summaries from stored observations."""
    methods = ("regularized", "unregularized", "sensitivity", "shuffled_labels")
    records = {f"{method}_s{seed}": read(f"{method}_s{seed}")
               for method in methods for seed in range(3)}
    records.update({name: read(name) for name in ("logistic_s0", "class_prior_s0")})
    reference_ids = records["regularized_s0"]["example_ids"]
    reference_y = records["regularized_s0"]["y_true"]
    for key, record in records.items():
        assert record["split"] == "test" and record["example_ids"] == reference_ids, key
        assert record["y_true"] == reference_y, key
        recomputed = float(np.mean(np.asarray(record["y_pred"]) == np.asarray(record["y_true"])))
        assert np.isclose(recomputed, record["accuracy"], atol=1e-15), key
        assert record["checkpoint_reload_verified"]
    seed_differences = []
    for seed in range(3):
        reg = np.asarray(records[f"regularized_s{seed}"]["y_pred"])
        unreg = np.asarray(records[f"unregularized_s{seed}"]["y_pred"])
        truth = np.asarray(reference_y)
        seed_differences.append(float(np.mean((reg == truth).astype(float) - (unreg == truth).astype(float))))
    # Resample test-example indices, keeping each seed's methods paired.
    per_example = np.stack([
        (np.asarray(records[f"regularized_s{seed}"]["y_pred"]) == np.asarray(reference_y)).astype(float)
        - (np.asarray(records[f"unregularized_s{seed}"]["y_pred"]) == np.asarray(reference_y)).astype(float)
        for seed in range(3)
    ]).mean(axis=0)
    rng = np.random.default_rng(2026)
    samples = np.empty(10000)
    for i in range(len(samples)):
        samples[i] = per_example[rng.integers(0, len(per_example), len(per_example))].mean()
    summary = {
        "id": "experiment-analysis", "analysis_kind": "exploratory",
        "n_test": len(reference_y), "seed_differences": seed_differences,
        "mean_paired_difference": float(np.mean(seed_differences)),
        "sample_sd_seed_differences": float(np.std(seed_differences, ddof=1)),
        "paired_conditional_bootstrap_95": [float(v) for v in np.quantile(samples, [0.025, 0.975])],
        "bootstrap_resamples": len(samples), "bootstrap_seed": 2026,
        "accuracies": {key: records[key]["accuracy"] for key in records},
        "checkpoint_reload_verified_all": True,
        "result_hashes": {key: hashlib.sha256((RESULTS / f"{key}.json").read_bytes()).hexdigest()
                          for key in records},
        "interpretation_limit": "Bootstrap is conditional on fitted models and fixed example split."
    }
    OUT.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
