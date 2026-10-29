# Preregistration: AdamW weight decay on the fixed digits MLP

**Cycle:** 001  
**Stage:** Understanding / prospective confirmatory protocol  
**Status:** Frozen protocol supplied by the harness; this report records it without changing its scientific definitions.  
**Question:** Does AdamW weight decay 0.01 improve held-out accuracy of the fixed ReLU MLP on the bundled digits split?

## Objective and scope

The objective is to estimate the effect of the registered AdamW weight-decay intervention for one small MLP, one fixed example-level split, and the registered training procedure. An improvement, decrease, or inconclusive estimate are all valid outcomes. This is an illustrative validation study, not evidence about unseen writers, other datasets, or general agent/scientific reliability.

The method motivation comes from Loshchilov and Hutter, who distinguish decoupled weight decay from an L2 loss penalty under adaptive optimizers and report empirical improvements in their own settings ([paper](https://arxiv.org/abs/1711.05101)). PyTorch documents that `AdamW` applies weight decay without accumulating it in the momentum or variance ([API](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html)). Neither source predicts a positive result for this specific task. The dataset and split APIs are grounded in the [scikit-learn digits documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). The staged separation of exploration, testing, and distillation follows Neel Nanda's [research-process guide](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL).

## Registered hypotheses and alternatives

**H1 (directional):** The mean across registered seeds of test accuracy with weight decay 0.01 minus test accuracy with weight decay 0 is positive.

Competing explanations are:

1. **No material effect:** the decay intervention has little or no effect under this fixed setup.
2. **Harm:** the 0.01 decay setting lowers held-out accuracy.
3. **Training variation:** an apparent difference is due to initialization or optimization randomness rather than the decay setting.
4. **Implementation or measurement error:** a mismatch in data, model, checkpoint, or accuracy computation creates an apparent difference.
5. **Finite test-sample variation:** the observed example split gives an uncertain estimate even for the trained models.

The protocol does not define a smallest practically meaningful effect or an equivalence margin. Consequently, an interval crossing zero is inconclusive and cannot establish equivalence.

## Distinguishing predictions and falsification

- Under H1, the registered mean paired accuracy difference is greater than zero.
- If the paired, conditional 95% bootstrap interval lies wholly below zero, that contradicts the directional H1. If it includes zero, the result is inconclusive; if wholly above zero, it is directionally consistent with H1, subject to the scope limits below.
- Identical model architecture, optimizer settings other than the registered decay, seed-matched initialization, data, and shuffled minibatch order make the primary contrast an intervention on `weight_decay` within the fixture.
- The shuffled-label control is expected to lose useful predictive accuracy relative to real-label training. It is a control diagnostic, not a replacement primary endpoint.
- Recomputing accuracy and paired differences from the stored held-out labels, predictions, and example IDs should agree with reported metrics; disagreement would indicate a measurement or provenance problem.
- The seed-specific effects and their sample standard deviation will be shown. Three seeds are a small sensitivity check and do not precisely characterize the distribution over training runs.

These predictions are prospective. No pilot or comparative training outcomes are included in this preregistration.

## Methods fixed by the protocol

| Component | Registered value |
|---|---|
| Dataset | scikit-learn `load_digits`; 1,797 examples, 64 flattened features, ten classes |
| Data partition | Stratified 60/20/20 train/validation/test; split seed 42; evaluation ID `digits-stratified-42-test-v1` |
| Input transform | Divide raw pixel values by the documented constant 16; no fitted preprocessing |
| Model | Fully connected `[64, 128, 10]` network with ReLU between linear layers |
| Optimizer and training | AdamW; learning rate 0.001; batch size 64; 50 epochs; deterministic algorithms enabled in fixture |
| Registered seeds | 0, 1, 2 |
| Primary arms | `regularized`: decay 0.01; `unregularized`: decay 0.0 |
| Additional registered arms | `sensitivity`: decay 0.001; `shuffled_labels`: decay 0.01; logistic regression (`C=1`, max iterations 1000); train-set class-prior baseline |
| Primary metric | Mean across seeds of test accuracy(`regularized`) minus test accuracy(`unregularized`) |
| Interval | 10,000 paired bootstrap resamples of test example indices, RNG seed 2026; resample pairing is retained across methods and trained seeds |
| Pilot ordering | Publish the regularized seed-0 validation-only pilot and checkpoint before comparative fits |
| Budget | 60 active minutes and 20 CLI invocations for the entire validation run; no automatic extension |

The pilot uses validation only. Hyperparameters, epochs, and checkpoint selection may not be chosen using test outcomes. The test partition is used only for the registered final evaluation and its stated analysis. The fixture uses one common architecture and changes the registered decay setting across neural arms; baselines are descriptive contextual comparisons.

## Analysis plan

1. Preserve the supplied `research/protocol.json` and `study.py` scientific definitions. Run the fixture's non-training check before model fitting.
2. Run and publish the regularized seed-0 validation-only pilot and checkpoint before any comparative arm, as fixed by the harness ordering.
3. Run every registered method and seed; retain failures and negative results. Do not choose or omit arms based on observed accuracy.
4. Compute the primary metric exactly as the arithmetic mean of the three seed-level test-accuracy differences. Report every seed-level difference and their sample standard deviation.
5. Use the registered 10,000 paired bootstrap resamples (seed 2026) over test example indices to form a conditional 95% interval for the mean effect. Preserve method pairing and seed structure. State explicitly that this interval conditions on these fitted models and does not quantify training-run or split-to-split uncertainty.
6. Recompute reported accuracies from saved predictions and labels and verify example IDs, split membership, checkpoint reload, and protocol/code provenance before interpretation.
7. Report sensitivity, shuffled-label, logistic, and class-prior comparisons descriptively; do not promote any to a new primary comparison or make test-selected claims.
8. Interpret the finding narrowly. Report evidence against the directional hypothesis, null-crossing uncertainty, and any confounds or deviations. Do not infer equivalence from a null-crossing interval.

## Data boundaries and limitations

The data boundary is the fixed stratified random example split, with no writer identities. The evaluation therefore does not estimate generalization to new writers or external datasets. The bootstrap resamples test examples conditional on the trained models; it does not capture uncertainty due to retraining, changing the split, or dataset shift. Three seeds provide limited visibility into training variation. Additional arms are diagnostic/descriptive and have no registered multiplicity-adjusted inferential claims.

## Evidence state at preregistration

The supplied fixture check passed with shape `[1797, 64]` and split counts 1,078 / 359 / 360; it did not train a model. See `research/evidence.json` IDs `fixture-check`, `study-fixture-code`, `fixed-protocol`, `research-review`, and `research-highlights` for the prior phase's evidence and hashes. The check was rerun during this phase with the required research Python and passed with the same dimensions. It is a data/code sanity check, not evidence about H1. No training outcome exists at preregistration. The protocol itself remains at `research/protocol.json`.
