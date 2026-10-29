# Final research report: AdamW weight decay on a fixed digits MLP

**Cycle:** 001  
**Research stage:** Distillation  
**Overall interpretation:** The preregistered directional benefit was not observed; the evidence is inconclusive about equivalence or effects outside this fixed study.  
**Author:** Libor “Burny” Burian

## Abstract

This fixed validation study asked whether AdamW weight decay of 0.01 improves test accuracy over zero decay for a ReLU MLP on a stratified example-level split of scikit-learn's handwritten digits data. The fixed network had widths 64–128–10; the registered training used AdamW, learning rate 0.001, batch size 64, 50 epochs, and seeds 0, 1, and 2. Each matched seed pair produced the same test accuracy and identical correctness decisions: 96.39%, 96.94%, and 96.94%. The mean paired accuracy difference was zero; the registered decision was inconclusive. A paired bootstrap interval also collapsed to zero because no paired correctness outcomes differed, but it conditions on the trained models and is not an equivalence test. Shuffled-label controls were near the ten-class chance reference, while logistic regression reached 95.56% and the class-prior baseline 10.28%; these comparisons are descriptive. The result is limited to this model, recipe, split, and seeds and does not estimate generalization to new writers or datasets.

## Question, motivation, and prior work

The question was whether the registered intervention, changing AdamW's weight-decay parameter from 0 to 0.01, improves held-out accuracy for this particular fixed MLP. Loshchilov and Hutter motivate decoupling weight decay from adaptive gradient moments and report results in their own settings; those results do not imply a benefit here ([paper](https://arxiv.org/abs/1711.05101), source ID `loshchilov-hutter-2019-adamw`). PyTorch's [AdamW API](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html) documents the optimizer behavior implemented by the fixture (`pytorch-adamw-docs`). The dataset and stratified split follow scikit-learn's [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) documentation.

The workflow records expectations, alternatives, observations, and learning across the stages described in [Neel Nanda's research-process guide](https://www.alignmentforum.org/posts/hjMy4ZxS5ogA9cTYK/how-i-think-about-my-research-process-explore-understand). The preregistered positive direction was motivated by the literature, not guaranteed by it. The analysis keeps the primary comparison distinct from exploratory diagnostic arms, consistent with the reporting cautions in [Lones](https://arxiv.org/abs/2108.02497) and [Lipton and Steinhardt](https://arxiv.org/abs/1807.03341). Sources checked for this cycle are indexed in [`research/sources.json`](../research/sources.json).

## Methods and evidence boundary

The supplied protocol is preserved at [`research/protocol.json`](../research/protocol.json), with its registration in [`research/registration.json`](../research/registration.json). The bundled dataset contains 1,797 examples, 64 pixel features, and ten classes. The frozen split has 1,078 training, 359 validation, and 360 test examples, stratified with split seed 42. Pixel values are divided by the fixed constant 16. The network is a fully connected 64–128–10 MLP with ReLU, trained for 50 epochs using cross-entropy and AdamW at learning rate 0.001 and batch size 64.

The primary intervention and comparator differ in weight decay (0.01 versus 0); all three registered seeds are paired. The primary metric is the mean across seeds of the test-accuracy difference (regularized minus unregularized). The registered interval uses 10,000 paired bootstrap resamples of test example indices with RNG seed 2026. Its uncertainty is conditional on the fitted models and this fixed test set. It does not cover new training runs, new splits, new writers, or distribution shift. The validation-only regularized seed-0 pilot preceded comparisons as registered. Test results were not used to select a model or hyperparameter.

Experiment JSON records preserve predictions, labels, example IDs, provenance, and checkpoint-reload checks. The evidence ledger at [`research/evidence.json`](../research/evidence.json) resolves the cited experiment IDs to paths and SHA256 hashes. The primary registered records are `regularized_s0`, `regularized_s1`, `regularized_s2`, `unregularized_s0`, `unregularized_s1`, and `unregularized_s2`. The derived audit is `ev-experiment-analysis` and is exploratory. The review record reports a successful non-training fixture check, recomputed prediction accuracies, common test membership and labels, and verified reload flags; it is an audit of this fixture and its saved records, not an independent replication.

## Results

| Registered or diagnostic arm | Test accuracy, seeds 0 / 1 / 2 | Mean test accuracy | Evidence classification |
|---|---:|---:|---|
| AdamW, decay 0.01 | 96.39% / 96.94% / 96.94% | 96.76% | Confirmatory primary arm |
| AdamW, decay 0 | 96.39% / 96.94% / 96.94% | 96.76% | Confirmatory primary comparator |
| AdamW, decay 0.001 | 96.39% / 96.94% / 96.94% | 96.76% | Exploratory sensitivity arm |
| Shuffled training labels | 6.11% / 11.67% / 10.83% | 9.54% | Exploratory negative control |
| Logistic regression, C=1 | — | 95.56% | Exploratory descriptive baseline |
| Training-set class prior | — | 10.28% | Exploratory trivial baseline |

All six primary result records show identical correct/incorrect decisions between the paired decay settings. The seed-specific accuracy differences were 0, 0, and 0 percentage points; their mean and sample standard deviation were both zero. The protocol-defined 95% paired bootstrap interval was [0, 0], with the registered conclusion `inconclusive` (`ev-experiment-analysis`). Since every paired correctness outcome is the same, resampling these test examples cannot create a nonzero difference. This interval does not establish that the methods are equivalent: the protocol specified no equivalence margin.

The 0.001 sensitivity arm also matched the primary accuracies on these seeds. Shuffled-label performance was near the 10% uniform-class reference and far below real-label MLP performance, which is consistent with the control's diagnostic purpose; it does not identify a weight-decay effect. Logistic regression and class-prior results provide context only. All auxiliary comparisons remain exploratory and were not used to replace or tune the registered primary contrast.

Figures generated from recorded artifacts are available as [architecture](../figures/architecture.png), [accuracy comparison](../figures/accuracy.png), and [loss histories](../figures/loss.png). They illustrate this fixed study and are not additional independent evidence.

## Interpretation, predictions, and alternatives

The preregistered prediction was a positive mean paired accuracy difference for decay 0.01 over zero. That directional prediction was not observed. This is a negative result for the predicted improvement in this comparison, alongside an inconclusive statistical decision: the records show no observed accuracy advantage, but they do not show equivalence or rule out effects on unmeasured quantities.

Competing explanations and remaining limits include:

- **No accuracy effect under this recipe:** consistent with the identical correctness outcomes, but not established as equivalence because no equivalence margin was registered.
- **Effects hidden by the metric:** models can have identical class decisions while differing in logits, confidence, losses, parameter values, or optimization trajectories; these were not registered outcomes for the primary question.
- **Training or sampling variability:** three seeds on one fixed random example split provide limited coverage of run and sample variation. The conditional bootstrap does not estimate either new-run or split-to-split uncertainty.
- **Measurement or provenance error:** independently recomputed metrics, common test IDs and labels, and checkpoint reload assertions reduce ordinary measurement concerns, but do not rule out every software or conceptual defect. The analysis is not independent replication.
- **Limited population:** the split has no writer IDs and comes from one bundled dataset. No claim about unseen writers, external datasets, or distribution shift follows.

The evidence supports only this narrow statement: for the registered architecture, optimizer recipe, decay values, seeds, and fixed test examples, no test-accuracy or correctness difference was observed between decay 0.01 and zero decay. It does not support the claim that AdamW decay generally helps, generally has no effect, or is harmful.

## Reproducibility and artifact reconciliation

The protocol, preregistration, per-experiment reports, aggregate experiment report, interpretation, highlights, reproduction guide, claims, requirement checklist, and evidence ledger are preserved in this cycle. [`docs/reproduction.md`](../docs/reproduction.md) documents the supplied fixture commands and fixed run order. The recorded review checked the non-training fixture check and static site assets; it could not verify browser runtime behavior because browser access was unavailable. Review also visually inspected only pages 1 and 2 of the six-page PDF. These checks are not evidence of a deployed website or a complete visual review.

At handoff, README and generated summary/paper source still contain temporary “not yet executed” or “research in progress” status text despite embedding the completed records. Those strings are stale publication placeholders, not scientific findings. The controller owns regeneration and publication; use the recorded results and this report as the final interpretation when refreshing generated artifacts. The existing `requirements.json` records phase-scoped checklist statuses; any final publication statuses and controller-owned deployment checks should be set only from their actual completion evidence. No claim of repository push, Pages deployment, Hugging Face upload, or completed publication is made here.

## Conclusion

The positive directional prediction did not hold in the registered fixed comparison: the three paired test-accuracy differences were all zero. The prescribed conditional bootstrap is exactly zero because paired correctness was identical, yet the study is inconclusive about equivalence and does not quantify run-, split-, writer-, or dataset-level uncertainty. The diagnostic controls and baselines behaved as contextual checks, not as evidence broadening the primary claim. The study is a small validation exercise and does not establish general scientific reliability or agent superiority.

## Sources

- Loshchilov and Hutter, [*Decoupled Weight Decay Regularization*](https://arxiv.org/abs/1711.05101).
- PyTorch, [`torch.optim.AdamW`](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html).
- scikit-learn, [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).
- Nanda, [*How I Think About My Research Process: Explore, Understand, Distill*](https://www.alignmentforum.org/posts/hjMy4ZxS5ogA9cTYK/how-i-think-about-my-research-process-explore-understand).
- Lones, [*How to avoid machine learning pitfalls*](https://arxiv.org/abs/2108.02497).
- Lipton and Steinhardt, [*Troubling Trends in Machine Learning Scholarship*](https://arxiv.org/abs/1807.03341).
- NeurIPS, [Paper Checklist Guidelines](https://neurips.cc/public/guides/PaperChecklist), used as reporting guidance and not as evidence of venue compliance.
