# Pilot: regularized seed 0

**Stage:** Exploration (validation-only pilot)  
**Question:** Does the fixed AdamW MLP produce a useful learning signal under the registered training recipe, before comparative test evaluation?  
**Scope:** This single-run pilot does not estimate the effect of weight decay. The registered confirmatory comparison remains the paired test-accuracy difference across seeds in the preregistration.

## Prospective expectations and alternatives

Before this run, the protocol expected a real-label model to learn a useful mapping, while allowing AdamW decay 0.01 to help, hurt, or have an inconclusive effect relative to zero decay. The pilot can check whether training and validation losses move in a plausible direction and whether the prediction/checkpoint path works; it cannot distinguish the decay effect from seed or data-sample variation. Competing explanations for an unexpectedly weak or strong pilot include ordinary optimization variation, an implementation or measurement bug, and the difficulty of this particular fixed example split. The result will not be used to alter the registered architecture, epoch budget, or hyperparameters.

Prior work introduces decoupled weight decay and reports results in its own image-classification settings; PyTorch documents that AdamW decay does not accumulate in the momentum or variance. Those sources motivate the method but do not predict benefit on this fixed MLP and split ([Loshchilov & Hutter](https://arxiv.org/abs/1711.05101); [PyTorch AdamW documentation](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html)). The dataset and split follow the documented [scikit-learn digits fixture](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). The staged distinction between exploration and later evaluation follows [Nanda's research-process guide](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL).

## Exact run configuration

| Item | Pilot setting |
|---|---|
| Registered experiment | `pilot_regularized_s0` (`regularized`, seed 0) |
| Dataset and partition | `load_digits`; stratified train/validation/test split 60/20/20, split seed 42; pilot scored on validation only (359 examples) |
| Input | 64 flattened pixels divided by the fixed constant 16 |
| Network | Linear 64→128, ReLU, Linear 128→10 |
| Optimizer | `torch.optim.AdamW`; learning rate 0.001, weight decay 0.01; library defaults for betas `(0.9, 0.999)`, epsilon `1e-8`, and AMSGrad disabled |
| Training | Cross-entropy; batch size 64; 50 epochs; shuffled minibatches seeded with 0; deterministic PyTorch algorithms enabled; 2 CPU threads |
| Runtime | CUDA, NVIDIA GeForce RTX 5070 Laptop GPU; PyTorch 2.14.1+cu130; NumPy 2.5.4 |
| Duration | 7.616 seconds, as recorded by the fixture |
| Protocol/code identity | Protocol SHA256 `5edcfb3fcda62035f6ea4013f88ebca59b7d75977f49d155af208a2bb50ec257`; code SHA256 `dbf12650ab0a81f0ed6598dd7a4801920c388d7fe59f32d166cbbf95b6baf2fa` |

## Observations

- The saved validation accuracy is **347/359 = 0.9666**. Independently recomputing accuracy from the saved validation labels and predictions gives the same value. The complete `y_true`, `y_pred`, `example_ids`, and split membership arrays are preserved in the experiment record [`pilot_regularized_s0`](../results/pilot_regularized_s0.json).
- The complete per-epoch training and validation loss history is preserved in that same JSON record. Training loss fell from 2.2119 at epoch 1 to 0.0568 at epoch 50. Validation cross-entropy fell from 2.0877 to 0.1202; it fluctuated slightly late in training but continued to improve overall. These trajectories are descriptive and were not used to select an epoch or checkpoint.
- The checkpoint is [`regularized-s0.safetensors`](../models/regularized-s0.safetensors), SHA256 `a57cb6e24f5e7d2a3e83da8efd97233a4b7e0e5b8492f89b3cbe6064cb86cc3d`. The fixture reloaded it and verified exact logit equality against the in-memory model.
- The non-training fixture check passed before fitting: input shape `[1797, 64]`, split sizes 1,078/359/360, and a finite `[2, 10]` forward-pass output. This checks data partitioning and a model probe; it is not evidence about generalization.

## Interpretation and learning

This pilot establishes that the prescribed training path ran successfully on CUDA, produced a low validation loss and high validation accuracy for seed 0, and saved auditable predictions, history, and a reload-verified checkpoint. It does **not** establish that weight decay improved accuracy: no zero-decay comparator was run in this phase, and one seed on one fixed validation partition cannot separate the decay intervention from run-specific variation. The high validation score also does not establish performance on new writers or another dataset. No protocol amendment or method choice follows from this observation.

The registered next comparison should proceed only after the controller's pilot-publication handoff. This report performs no comparison, sensitivity run, or test-set evaluation.

## Evidence and provenance

- Experiment record and full predictions/loss history: [`pilot_regularized_s0`](../results/pilot_regularized_s0.json), SHA256 `9cbcc143e6b79de99c7f8404e35cf7f6c8f51e768bc74022f3c832381629225a`.
- Reload-verified model checkpoint: [`regularized-s0.safetensors`](../models/regularized-s0.safetensors); hash recorded above.
- Frozen definitions: [`protocol.json`](../research/protocol.json) and [`study.py`](../study.py); their hashes are registered in [`evidence.json`](../research/evidence.json).
- Research process: [How I Think About My Research Process](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL).
