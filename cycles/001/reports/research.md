# Research phase: AdamW weight decay on the fixed digits MLP

**Cycle:** 001  
**Stage:** Exploration, with a preregistered confirmatory question reserved for the experiment phase  
**Question:** Does AdamW weight decay 0.01 improve held-out accuracy relative to weight decay 0 for this fixed small ReLU MLP and bundled digits split?

## Domain and prior work

The study uses scikit-learn's `load_digits` dataset: 1,797 handwritten 8×8 grayscale digit images, represented as 64 features with values from 0 through 16 and ten classes ([`sklearn-load-digits-docs`](../research/sources.json)). The code divides the pixels by the known constant 16, then partitions examples into stratified train, validation, and test subsets with fixed split seed 42. This is an example-level random split; there are no writer identities, so the study cannot estimate transfer to unseen writers.

The intervention is AdamW's `weight_decay` argument. Loshchilov and Hutter show why weight decay under adaptive optimizers should be distinguished from adding an L2 penalty to the loss, and report gains in their image-classification experiments ([`loshchilov-hutter-2019-adamw`](../research/sources.json)). PyTorch documents AdamW as decoupled weight decay ([`pytorch-adamw-docs`](../research/sources.json)). This establishes the method's meaning, not a universal direction of effect. Their tested workloads differ from this small MLP and dataset; here, improvement, no measurable difference, or a decrease are all plausible.

For process, Neel Nanda's guide recommends separating information-seeking exploration from hypothesis testing and distillation, maintaining highlights, and challenging interpretations with alternatives ([`nanda-research-process-2025`](../research/sources.json)). Lones' guide emphasizes sound comparisons and valid conclusions; Lipton and Steinhardt warn against confusing speculation with evidence or failing to identify sources of gains ([`lones-2024-ml-pitfalls`](../research/sources.json), [`lipton-steinhardt-2018`](../research/sources.json)). NeurIPS checklist guidance is useful for limitations and reproducibility reporting, but this small validation study is not represented as meeting any particular venue standard ([`neurips-paper-checklist-guidelines`](../research/sources.json)).

## Protocol and prospective predictions

The immutable protocol fixes a `[64, 128, 10]` MLP with ReLU, AdamW, learning rate 0.001, batch size 64, 50 epochs, and three seeds (0, 1, 2). The registered primary estimand is the mean across seeds of test accuracy at decay 0.01 minus test accuracy at decay 0. The analysis plan specifies 10,000 paired bootstrap resamples of test examples (bootstrap RNG seed 2026), paired by example across the two methods and all trained seeds. It also reports seed-level effects and their standard deviation. This bootstrap interval is conditional on the fitted models; it does not represent variation over new training runs. Only three seeds are available, so their spread is descriptive and weakly characterizes training randomness.

The directional prediction is a positive mean paired effect. A paired conditional 95% bootstrap interval wholly below zero would contradict that direction; an interval containing zero is inconclusive and is not evidence of equivalence. Registered alternative explanations include no effect, lower accuracy under regularization, training randomness, or implementation/arithmetic error. The study includes a decay-0.001 sensitivity arm, shuffled-label control, logistic-regression baseline, and class-prior baseline; these are descriptive and cannot replace the registered primary comparison. Pilot validation results must be published before comparative fits. Test data are not to select checkpoints, epochs, or hyperparameters.

These predictions are prospective requirements from the supplied protocol, not findings. No training outcomes exist in this research phase.

## Fixture review and checks

`study.py` implements a single shared network and changes the registered weight decay by method. The split is generated before model fitting; all split indices are asserted disjoint and collectively cover the dataset. Pixel normalization uses the documented fixed scale, not a fitted statistic. The logistic baseline is fit on train only. The shuffled-label arm permutes training labels while evaluation uses original labels. Neural checkpoints are saved and reloaded, then logits are required to match exactly before predictions are recorded. Test evaluation records include example IDs, true labels, predictions, checkpoint hash, code hash, protocol hash, dataset hash, device, and training history.

The required non-training check passed: shape `[1797, 64]`; split sizes were train 1,078, validation 359, test 360 (`fixture-check`; implementation `study-fixture-code`). It verifies input bounds, expected registered seeds and decay methods, disjoint partitions, and coverage. It does not validate training convergence or CUDA availability. The fixture's split check uses stratified `train_test_split`, whose API supports reproducible random partitions and class stratification ([`sklearn-train-test-split-docs`](../research/sources.json)). Protocol details are registered as `fixed-protocol`.

## Highlights and anomalies

See [`highlights.md`](highlights.md) for the concise anomaly register. The key current observation is a process boundary, not a model result: the protocol calls this a confirmatory study while the pilot is validation-only, and the primary test comparison is still prospective. If implementation or data problems appear in later phases, preserve the prescribed comparison but qualify or revisit its interpretation rather than silently revising the protocol.

## Scope and limitations already known

- One fixed random example split from a small dataset; no writer-level or external-dataset generalization.
- Three neural seeds do not provide a precise estimate of the training-run population effect.
- Conditional bootstrap resampling reflects finite test-example uncertainty for these trained models, not model-training uncertainty or split-to-split variation.
- The same fixture and documented known pixel scale improve reproducibility, but code-level checks cannot rule out every conceptual confound.
- The registered study answers a narrow question about one architecture, optimizer, training budget, split, and decay value. Existing AdamW results on other datasets do not predict this exact outcome.

## Evidence and phase boundary

Source IDs are defined in [`sources.json`](../research/sources.json). Local code and check output are hash-registered in [`evidence.json`](../research/evidence.json). The check was run with the supplied research Python environment. No training, pilot, comparative experiment, test-set inspection, publication, upload, or controller-state change occurred in this phase.
