# Digits research through Codex Luna

An independently recorded validation run of [Auto Eureka Scientist](https://github.com/BurnyCoder/auto-eureka-scientist-agent-harness), using the selected Codex CLI to research, inspect, execute and report a fixed supervised classification study. The supplied PyTorch fixture compares AdamW regularization with an unregularized MLP, logistic regression, a class-prior baseline and shuffled training labels on [UCI digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits).

The primary comparison was inconclusive. The controller accepted the research phases within the bounded run, but the subsequent publication audit found evidence hashes invalidated by Git conversion and regenerated documents. Exact historical bytes were recovered and pinned before final verification. Read the [post-run audit disclosure](reports/post-run-publication.md); these repairs are not additional autonomous model work.

![Research architecture](cycles/001/figures/architecture.png)

[Interactive results](https://burnycoder.github.io/eureka-digits-luna/) · [Paper](cycles/001/reports/paper.pdf) · [Model bundle](https://huggingface.co/BurnyCoder/eureka-digits-luna-models) · [Model collection](https://huggingface.co/collections/BurnyCoder/eureka-digits-luna-6ae39b1a9fbf13c0618b07a5)

## Reproduction and provenance

Follow the [installation, checkpoint download and regeneration guide](https://github.com/BurnyCoder/auto-eureka-scientist-agent-harness/blob/main/docs/reproduction.md). The locked harness environment provides the `eureka render` and `eureka verify` commands; no further model calls are required to regenerate saved measurements. The original [protocol](cycles/001/research/protocol.json), [training implementation](cycles/001/study.py), saved predictions, losses and publication history are retained.

The workflow applies [Neel Nanda's research process](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL): record objectives and alternatives, run informative probes, compare observations with predictions, and distill narrow claims. [Methods and interpretation](cycles/001/reports/interpretation.md) distinguish the registered primary contrast from descriptive sensitivity and control comparisons. Training used CUDA for neural models; the simple baselines ran on CPU. The reported model identifier was requested by the harness; the CLI did not expose a resolved snapshot.

This supplied-fixture development trial does not establish provider superiority or general scientific reliability. The results below are generated from saved predictions. Uncertainty conditions on the fitted models and example split; the degenerate interval is not an equivalence test.


<!-- EUREKA:RESULTS:START -->
## Recorded results

Recorded harness status: **complete**; 8 operational phases accepted. Measurements below do not imply completion of unaccepted phases.

| Experiment | Method | Seed | Split | Accuracy | Seconds | Device |
|---|---|---:|---|---:|---:|---|
| class_prior_s0 | class_prior | 0 | test | 0.102778 | 0.038 | cpu |
| logistic_s0 | logistic | 0 | test | 0.955556 | 0.107 | cpu |
| pilot_regularized_s0 | regularized | 0 | validation | 0.966574 | 7.616 | cuda |
| regularized_s0 | regularized | 0 | test | 0.963889 | 0.288 | cuda |
| regularized_s1 | regularized | 1 | test | 0.969444 | 6.002 | cuda |
| regularized_s2 | regularized | 2 | test | 0.969444 | 2.192 | cuda |
| sensitivity_s0 | sensitivity | 0 | test | 0.963889 | 2.394 | cuda |
| sensitivity_s1 | sensitivity | 1 | test | 0.969444 | 2.348 | cuda |
| sensitivity_s2 | sensitivity | 2 | test | 0.969444 | 2.258 | cuda |
| shuffled_labels_s0 | shuffled_labels | 0 | test | 0.061111 | 2.333 | cuda |
| shuffled_labels_s1 | shuffled_labels | 1 | test | 0.116667 | 2.353 | cuda |
| shuffled_labels_s2 | shuffled_labels | 2 | test | 0.108333 | 2.369 | cuda |
| unregularized_s0 | unregularized | 0 | test | 0.963889 | 2.235 | cuda |
| unregularized_s1 | unregularized | 1 | test | 0.969444 | 2.374 | cuda |
| unregularized_s2 | unregularized | 2 | test | 0.969444 | 2.323 | cuda |

The mean paired accuracy difference is 0.000000, with conditional 95% bootstrap interval [0.000000, 0.000000]. The registered decision is **inconclusive**. The sample standard deviation across seed effects is 0.000000. The interval uses 10000 paired resamples of test examples and conditions on the trained models.

See [full report](cycles/001/reports/summary.md).
<!-- EUREKA:RESULTS:END -->
