# Cycle 001 reproduction guide

This guide records the fixed, staged run for the AdamW weight-decay study. The registered protocol is [`research/protocol.json`](../research/protocol.json); its scientific definitions must remain unchanged. The implementation uses scikit-learn's bundled handwritten digits data and a PyTorch `[64, 128, 10]` ReLU MLP. The dataset contains 1,797 examples with 64 integer-valued pixel features and ten classes ([dataset documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html)). The split uses `train_test_split` with stratification and fixed random state 42 ([API documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)). Pixels are divided by the known constant 16.

## Environment and checks

Use Python with the dependencies in the repository's `pyproject.toml`: NumPy, SciPy, scikit-learn, PyTorch, safetensors, and Matplotlib. In the supplied harness, the research interpreter is:

```powershell
C:/Users/Happy/Documents/projects/auto-eureka-scientist-agent-harness/.venv/Scripts/python.exe study.py check
```

Run that command from `cycles/001`. It checks the fixed split sizes and class presence, input bounds, registered seeds and arms, and a finite two-example model forward pass. It does not fit a model. The rerunnable command is also recorded in [`research/checks.json`](../research/checks.json).

## Fixed run order

1. Run the non-training check above.
2. The harness publishes core artifacts and creates the pilot-publication handoff. Do not run either training command before that controller handoff.
3. After core publication, run `study.py pilot` from this directory. This fits only the registered regularized seed-0 arm and evaluates it on validation data. Preserve its result and checkpoint.
4. After the harness records pilot publication, run `study.py experiments`. The fixture refuses to begin comparisons without `research/pilot-publication.json`. It evaluates the registered arms on the fixed test split. Do not use test results to choose parameters, epochs, models, or arms.

The script logs timestamped epoch losses to stdout, writes JSON records in `results/`, and saves model checkpoints in `models/`. Existing records are reused only after protocol and code hash checks. Do not delete or overwrite failed, negative, pilot, or comparison records. The fixture enables deterministic PyTorch algorithms and saves/reloads neural checkpoints with exact-logit verification; CUDA is selected when available, otherwise CPU is used. PyTorch describes AdamW's decay as decoupled from its moment estimates ([AdamW API](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html)); this property motivates the intervention but does not imply that decay improves this particular evaluation.

## Methods and comparisons

| Role | Registered method | Definition and interpretation |
|---|---|---|
| Primary intervention | `regularized` | AdamW weight decay 0.01; paired against `unregularized` for each seed. |
| Primary comparator | `unregularized` | Same MLP and training protocol with weight decay 0. |
| Local sensitivity | `sensitivity` | Same MLP with weight decay 0.001; descriptive check of a nearby setting, not a searched winner. |
| Negative control | `shuffled_labels` | Training labels are permuted; evaluation still uses the true labels. This checks whether the pipeline depends on the input-label relation. |
| Simple baseline | `logistic` | Train-only logistic regression (`C=1`, max iterations 1,000); contextual baseline with a different model family. |
| Trivial baseline | `class_prior` | Predicts the most frequent training class for every example; sanity reference, not a competitive classifier. |

The neural arms use seeds 0, 1, and 2, a fixed 50-epoch budget, learning rate 0.001, batch size 64, and identical architecture. Logistic regression and class-prior records are produced once. The protocol identifies the mean seed-paired test-accuracy difference between 0.01 and 0 as primary. Its 10,000-resample bootstrap is conditional on the fitted models and does not capture training-run or split uncertainty. See the preregistration for the exact analysis and falsification rule.

## Evidence and limitations

The partition is an example-level split without writer identifiers, so it does not estimate performance on unseen writers or external data. Three neural seeds provide only a limited view of run-to-run variation. A null-crossing interval is inconclusive, not evidence that the methods are equivalent. Keep code, protocol, records, and checkpoints together so their recorded hashes can be audited. Supporting sources and prior-work context are indexed in [`research/sources.json`](../research/sources.json) and discussed in [`reports/research.md`](../reports/research.md).
