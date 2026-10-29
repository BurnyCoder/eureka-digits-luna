---
title: "eureka-digits-luna: reproducible research report"
author: 'Libor “Burny” Burian'
geometry: margin=1in
fontsize: 10pt
---

# Abstract

This report records a bounded research cycle executed through Codex. The mean paired accuracy difference is 0.000000, with conditional 95% bootstrap interval [0.000000, 0.000000]. The registered decision is **inconclusive**. The sample standard deviation across seed effects is 0.000000. The interval uses 10000 paired resamples of test examples and conditions on the trained models.

Recorded harness status: **complete**; 8 operational phases accepted. Measurements below do not imply completion of unaccepted phases.

# Context, motivation, and introduction

Does AdamW weight decay improve held-out accuracy of a small MLP on the bundled digits data?

The objective is reproducible evidence and an inspectable research process. This study does not establish broad scientific reliability or superiority of an agent model.

# Background and method

- **question**: "Does AdamW weight decay improve held-out accuracy of a small MLP on the bundled digits data?"
- **architecture**: [64, 128, 10]
- **optimizer**: "AdamW"
- **learning_rate**: 0.001
- **batch_size**: 64
- **epochs**: 50
- **methods**: ["regularized", "unregularized", "sensitivity", "shuffled_labels", "logistic", "class_prior"]
- **seeds**: [0, 1, 2]
- **data_boundaries**: "Frozen stratified 60/20/20 train/validation/test partition. Split seed 42. Divide pixels by the documented constant 16. Pilot reports validation only. No learned preprocessing or selection uses test data. Generalization is limited to this random example split, not new writers or datasets."
- **analysis_plan**: "Use 10000 paired bootstrap resamples of test example indices with RNG seed 2026, preserving pairing across methods and all trained seeds. This interval conditions on the trained models and does not estimate training-population uncertainty. Separately show each seed effect and its sample standard deviation. Treat other comparisons as descriptive, with no post-hoc primary selection."
- **hyperparameter_rationale**: "Small prespecified network and fixed training budget provide fast feedback on an established task. The three decay values are a descriptive local sensitivity check, not a test-selected sweep. Three seeds expose limited initialization sensitivity; they do not support broad population claims."

![Research architecture](../figures/architecture.png)

# Results

| Method | Seed | Split | Accuracy | Seconds | Device |
|-------------------------|-----:|------------|-----------:|----------:|----------|
| class prior | 0 | test | 0.102778 | 0.038 | cpu |
| logistic | 0 | test | 0.955556 | 0.107 | cpu |
| regularized | 0 | validation | 0.966574 | 7.616 | cuda |
| regularized | 0 | test | 0.963889 | 0.288 | cuda |
| regularized | 1 | test | 0.969444 | 6.002 | cuda |
| regularized | 2 | test | 0.969444 | 2.192 | cuda |
| sensitivity | 0 | test | 0.963889 | 2.394 | cuda |
| sensitivity | 1 | test | 0.969444 | 2.348 | cuda |
| sensitivity | 2 | test | 0.969444 | 2.258 | cuda |
| shuffled labels | 0 | test | 0.061111 | 2.333 | cuda |
| shuffled labels | 1 | test | 0.116667 | 2.353 | cuda |
| shuffled labels | 2 | test | 0.108333 | 2.369 | cuda |
| unregularized | 0 | test | 0.963889 | 2.235 | cuda |
| unregularized | 1 | test | 0.969444 | 2.374 | cuda |
| unregularized | 2 | test | 0.969444 | 2.323 | cuda |

The mean paired accuracy difference is 0.000000, with conditional 95% bootstrap interval [0.000000, 0.000000]. The registered decision is **inconclusive**. The sample standard deviation across seed effects is 0.000000. The interval uses 10000 paired resamples of test examples and conditions on the trained models.

![All recorded accuracies](../figures/accuracy.png)

![Recorded learning curves](../figures/loss.png)

# Claims and evidence

- **claim-primary-no-observed-benefit**: In the registered fixed-MLP comparison, the positive directional prediction for AdamW decay 0.01 over zero decay was not observed: each matched seed has identical test correctness outcomes in the preserved predictions. Evidence: [regularized_s0](../results/regularized_s0.json), [regularized_s1](../results/regularized_s1.json), [regularized_s2](../results/regularized_s2.json), [unregularized_s0](../results/unregularized_s0.json), [unregularized_s1](../results/unregularized_s1.json), [unregularized_s2](../results/unregularized_s2.json). Limitations: This is a narrow result for the registered architecture, optimization recipe, example-level split, and seeds. Identical correctness does not establish identical logits, losses, parameters, or optimization trajectories. No equivalence margin was specified, so the observed null is not evidence of equivalence.
- **claim-bootstrap-conditional**: The post-run paired bootstrap summary is degenerate at zero because paired correctness outcomes agree; this resampling calculation is exploratory and conditional on the fitted models and fixed test examples. Evidence: [ev-experiment-analysis](../research/experiment-analysis.json), [regularized_s0](../results/regularized_s0.json), [regularized_s1](../results/regularized_s1.json), [regularized_s2](../results/regularized_s2.json), [unregularized_s0](../results/unregularized_s0.json), [unregularized_s1](../results/unregularized_s1.json), [unregularized_s2](../results/unregularized_s2.json). Limitations: It does not quantify retraining, split-to-split, writer-level, or distribution-shift uncertainty. No equivalence margin was registered.
- **claim-shuffled-label-diagnostic**: The shuffled-label controls are far below the real-label MLP arms and near the ten-class chance reference, consistent with their intended diagnostic role; this does not identify the causal effect of weight decay. Evidence: [shuffled_labels_s0](../results/shuffled_labels_s0.json), [shuffled_labels_s1](../results/shuffled_labels_s1.json), [shuffled_labels_s2](../results/shuffled_labels_s2.json), [regularized_s0](../results/regularized_s0.json), [regularized_s1](../results/regularized_s1.json), [regularized_s2](../results/regularized_s2.json), [class_prior_s0](../results/class_prior_s0.json). Limitations: This is a descriptive control check, not a registered inferential comparison. It cannot rule out every data, model, or implementation issue.
- **claim-literature-motivation-not-prediction**: Decoupled weight decay differs from adding an L2 penalty under adaptive methods, and prior work reports results in its tested settings. These sources motivate the comparison but do not predict a benefit for this digits MLP. Evidence: [loshchilov-hutter-2019-adamw](https://arxiv.org/abs/1711.05101), [pytorch-adamw-docs](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html). Limitations: The cited work and API documentation do not establish an effect for this architecture, data split, decay value, or training budget.
- **claim-provenance-checks**: A post-run audit recomputed accuracy from saved predictions and labels, checked common test IDs and labels, and verified checkpoint reload flags across experiment arms. These checks reduce ordinary metric and provenance concerns but do not establish that the implementation is free of all conceptual or software defects. Evidence: [ev-experiment-analysis](../research/experiment-analysis.json), [regularized_s0](../results/regularized_s0.json), [regularized_s1](../results/regularized_s1.json), [regularized_s2](../results/regularized_s2.json), [unregularized_s0](../results/unregularized_s0.json), [unregularized_s1](../results/unregularized_s1.json), [unregularized_s2](../results/unregularized_s2.json), [sensitivity_s0](../results/sensitivity_s0.json), [sensitivity_s1](../results/sensitivity_s1.json), [sensitivity_s2](../results/sensitivity_s2.json), [shuffled_labels_s0](../results/shuffled_labels_s0.json), [shuffled_labels_s1](../results/shuffled_labels_s1.json), [shuffled_labels_s2](../results/shuffled_labels_s2.json), [logistic_s0](../results/logistic_s0.json), [class_prior_s0](../results/class_prior_s0.json). Limitations: This is a post-hoc audit of supplied records and code; it is not independent replication or exhaustive implementation verification.

# Discussion, implications, and learnings

# Analysis interpretation: AdamW weight decay on the fixed digits MLP

## Motivation and context

AdamW separates decoupled weight shrinkage from the adaptive gradient update. Loshchilov and Hutter motivate this optimizer design and report results in their tested settings; those results do not establish an effect for this fixture ([paper](https://arxiv.org/abs/1711.05101); source ID `loshchilov-hutter-2019-adamw`). The [PyTorch AdamW API](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html) documents the optimizer behavior used by the fixture (`pytorch-adamw-docs`). The dataset is scikit-learn's handwritten digits set, split by stratified random examples; the dataset has no writer identities ([dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html); [split API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)). These primary sources were checked during this cycle's web research.

The question was whether the preregistered decay setting improves held-out accuracy over zero decay for the fixed ReLU MLP and training recipe. This is an illustrative validation study, not evidence about other datasets, writer-independent generalization, or research-agent reliability. The analysis follows Neel Nanda's staged research-process guidance (`nanda-research-process-2025`) and reporting advice in Lones's pitfalls review and Lipton and Steinhardt's critique ([Lones](https://arxiv.org/abs/2108.02497); [Lipton & Steinhardt](https://arxiv.org/abs/1807.03341)).

## Methods and analysis boundary

The immutable protocol specifies a fully connected 64–128–10 network with ReLU, AdamW, fixed input scaling, stratified train/validation/test partitions, deterministic training, and matched seeds (`fixed-protocol`). The primary outcome is the mean paired difference in test accuracy between decay and zero decay. The registered analysis resamples test examples while preserving pairing across methods and seeds. Saved predictions, labels, example IDs, checkpoints, protocol and code hashes, and reload flags are preserved in the six primary result records (`regularized_s0`–`regularized_s2`; `unregularized_s0`–`unregularized_s2`). The record-level comparison is confirmatory for this protocol only.

The post-run analysis (`ev-experiment-analysis`) recomputes metrics, checks shared test IDs and labels, verifies reload flags, and produces a paired conditional bootstrap summary. Following the evidence policy, this derived audit and its claims are classified as exploratory even though the primary contrast was preregistered. The bootstrap is conditional on fitted models and the fixed test set. The implementation is in `cycles/001/study.py`; protocol and evidence hashes are in `cycles/001/research/protocol.json` and `cycles/001/research/evidence.json`.

## Findings and implications

The registered positive directional prediction was not observed: the regularized and zero-decay models have identical correct/incorrect decisions on the fixed test examples for each matched seed (`regularized_s0`–`regularized_s2`; `unregularized_s0`–`unregularized_s2`). The record-level result therefore supplies no observed accuracy advantage for decay in this comparison. The derived paired bootstrap summary also collapses to zero (`ev-experiment-analysis`), but that post-run calculation does not establish equivalence. The protocol specified no equivalence margin.

The shuffled-label controls performed far below the real-label arms and near the ten-class chance reference, consistent with their intended diagnostic role (`shuffled_labels_s0`–`shuffled_labels_s2`; `regularized_s0`–`regularized_s2`; `class_prior_s0`). Logistic regression provides descriptive context (`logistic_s0`). These auxiliary comparisons are exploratory; they do not estimate the primary causal contrast and do not broaden its scope. Sensitivity results remain descriptive (`sensitivity_s0`–`sensitivity_s2`).

For this fixed recipe, the practical conclusion is that observed test correctness did not favor decay over zero decay. The broader question of equivalence or effects in other settings remains unresolved. Preserving the null result and avoiding test-set tuning are consistent with reporting guidance from Lipton and Steinhardt and the [NeurIPS checklist](https://neurips.cc/public/guides/PaperChecklist), used here as guidance rather than a claim of venue-level compliance.

## Alternative explanations and validity checks

Seed-matched training and the common recorded test examples reduce differences due to data or order mismatch in the primary contrast. Prediction-derived metric checks and checkpoint reload assertions reduce ordinary evaluation and serialization errors (`ev-experiment-analysis`). They cannot eliminate every bug or conceptual confound. Identical correctness can conceal changes in confidence or margins. The finite example split may not represent a new sample, and the small seed set provides limited information about training variability.

The bootstrap conditions on these fitted models and this fixed split. It does not cover retraining variation, new splits, new writers, or distribution shift. Writer IDs are absent, so no writer-held-out conclusion is available. These constraints narrow the claim; they do not erase the recorded observation.

## Related work

- Loshchilov and Hutter, [*Decoupled Weight Decay Regularization*](https://arxiv.org/abs/1711.05101): optimizer-method motivation and results in other tested settings.
- [PyTorch AdamW API](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html): reference for the optimizer implementation.
- scikit-learn [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html): references for bundled data and split procedure.
- Neel Nanda, [*How I Think About My Research Process: Explore, Understand, Distill*](https://www.alignmentforum.org/posts/hjMy4ZxS5ogA9cTYK/how-i-think-about-my-research-process-explore-understand): process guidance for recording expectations, anomalies, and learning.
- Michael A. Lones, [*How to avoid machine learning pitfalls*](https://arxiv.org/abs/2108.02497), and Zachary Lipton and Jacob Steinhardt, [*Troubling Trends in Machine Learning Scholarship*](https://arxiv.org/abs/1807.03341): guidance on evaluation and disciplined empirical claims.

This report is the analysis-phase interpretation. Numeric tables, figures, paper composition, and site publication are generated or handled by the harness controller in later phases.


# Limitations

- Conditional test-example intervals do not estimate variation over new training seeds, writers, or datasets.
- A small single-task study does not establish general model or harness superiority.
- No discordant predictions were observed in the primary pairs. The empirical bootstrap interval collapses to zero; this is not an equivalence test or a guarantee about unseen examples.

Exploratory outcomes do not become confirmatory by inclusion in this document. Missing metrics are not zero. Measurements without an applicable recorded objective are omitted; see the requirement checklist for explanations.

# Related work and sources

- [loshchilov-hutter-2019-adamw: Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101)
- [pytorch-adamw-docs: torch.optim.AdamW](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html)
- [sklearn-load-digits-docs: load_digits — scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html)
- [sklearn-train-test-split-docs: train_test_split — scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [nanda-research-process-2025: How I Think About My Research Process: Explore, Understand, Distill](https://www.alignmentforum.org/posts/hjMy4ZxS5ogA9cTYK/how-i-think-about-my-research-process-explore-understand)
- [lones-2024-ml-pitfalls: How to avoid machine learning pitfalls: a guide for academic researchers](https://arxiv.org/abs/2108.02497)
- [lipton-steinhardt-2018: Troubling Trends in Machine Learning Scholarship](https://arxiv.org/abs/1807.03341)
- [neurips-paper-checklist-guidelines: NeurIPS Paper Checklist Guidelines](https://neurips.cc/public/guides/PaperChecklist)

# Conclusion

The mean paired accuracy difference is 0.000000, with conditional 95% bootstrap interval [0.000000, 0.000000]. The registered decision is **inconclusive**. The sample standard deviation across seed effects is 0.000000. The interval uses 10000 paired resamples of test examples and conditions on the trained models.

# Appendix: reproducibility and provenance

The committed protocol, per-experiment JSON files, saved predictions, loss histories, and checkpoints are the source of all numerical tables and figures. Rebuild using `eureka render`. See `docs/reproduction.md` for execution commands and environment details.

# AI statement

Codex wrote the harness and study fixture; Codex performed this cycle and authored its interpretation. The harness generated this paper from recorded artifacts. A human supplied the exact specification. Human cleanup and rewriting are in progress.
