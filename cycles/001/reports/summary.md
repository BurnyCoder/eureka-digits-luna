# All experiments

Research is in progress; no final run-status snapshot is available.

| Experiment | Method | Seed | Split | Accuracy | Seconds | Device |
|---|---|---:|---|---:|---:|---|
| pilot_regularized_s0 | regularized | 0 | validation | 0.966574 | 7.616 | cuda |

The registered primary comparison is pending; no confirmatory conclusion is available.

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

This is a preliminary artifact generated before final interpretation. All available outcomes are retained; a completed experiment is not evidence that the favored hypothesis is true.

## Sources

- [loshchilov-hutter-2019-adamw: Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101)
- [pytorch-adamw-docs: torch.optim.AdamW](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html)
- [sklearn-load-digits-docs: load_digits — scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html)
- [sklearn-train-test-split-docs: train_test_split — scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [nanda-research-process-2025: How I Think About My Research Process: Explore, Understand, Distill](https://www.alignmentforum.org/posts/hjMy4ZxS5ogA9cTYK/how-i-think-about-my-research-process-explore-understand)
- [lones-2024-ml-pitfalls: How to avoid machine learning pitfalls: a guide for academic researchers](https://arxiv.org/abs/2108.02497)
- [lipton-steinhardt-2018: Troubling Trends in Machine Learning Scholarship](https://arxiv.org/abs/1807.03341)
- [neurips-paper-checklist-guidelines: NeurIPS Paper Checklist Guidelines](https://neurips.cc/public/guides/PaperChecklist)
