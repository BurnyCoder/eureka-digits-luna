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
