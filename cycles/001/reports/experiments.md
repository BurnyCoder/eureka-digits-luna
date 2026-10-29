# Registered experiments: AdamW decay on fixed digits MLP

**Stage:** Experiments / understanding. **Analysis:** The registered primary contrast is confirmatory; protocol-defined diagnostic arms are exploratory. This is a small validation study on one fixed example split, not a broad claim about regularization.

## Question and predictions

The preregistered question is whether AdamW weight decay 0.01 improves test accuracy over zero decay for the fixed `[64, 128, 10]` ReLU MLP. The primary metric is the mean of the three seed-matched test-accuracy differences. Before inspecting outcomes, H1 predicted a positive difference. Alternatives were no material effect, harm, training randomness, measurement/provenance error, and finite test-sample variation. The frozen criteria and plan are in [preregistration](preregistration.md) and [protocol](../research/protocol.json).

AdamW is a decoupled weight-decay optimizer; that algorithmic distinction and its published results in other settings motivate the question, but do not imply a result on this fixture ([Loshchilov & Hutter, 2017](https://arxiv.org/abs/1711.05101); [PyTorch AdamW documentation](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html)). The bundled digits dataset and split procedure follow [scikit-learn `load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

## Fixed method and execution

The frozen fixture split 1,078/359/360 examples stratified by class using split seed 42. Inputs were the 64 raw pixel features divided by 16. The MLP used ReLU, cross-entropy, AdamW at learning rate 0.001, batch size 64, and 50 epochs. All four neural arms used matched seeds 0, 1, and 2, deterministic algorithms, and the same minibatch-order seed rule; decay was 0.01 (`regularized`), 0 (`unregularized`), or 0.001 (`sensitivity`). The shuffled-label arm permuted training labels per seed. Logistic regression (`C=1`, max iterations 1000) and a train-class-prior predictor were fixed descriptive baselines. No outcomes selected an epoch or hyperparameter. The regularized seed-0 comparative result reused the previously published validation-pilot checkpoint, as specified in the fixture.

The full registered command completed without failed arms. Neural models trained on CUDA (RTX 5070 Laptop GPU); logistic and class-prior baselines ran on CPU. Every stored checkpoint reload was verified, all records share the same 360 test IDs and labels, and prediction-derived accuracies match stored accuracy. See [analysis code](../research/analyze_experiments.py), [derived analysis](../research/experiment-analysis.json), and experiment records in `../results/` (evidence IDs are registered in `../research/evidence.json`).

## Results

| Method | Test accuracy by seed 0 / 1 / 2 | Mean accuracy | Role |
|---|---:|---:|---|
| AdamW, decay 0.01 | 0.9639 / 0.9694 / 0.9694 | 0.9676 | Primary arm |
| AdamW, decay 0 | 0.9639 / 0.9694 / 0.9694 | 0.9676 | Primary comparator |
| AdamW, decay 0.001 | 0.9639 / 0.9694 / 0.9694 | 0.9676 | Registered decay sensitivity, exploratory |
| Shuffled labels, decay 0.01 | 0.0611 / 0.1167 / 0.1083 | 0.0954 | Negative control, exploratory |
| Logistic regression | 0.9556 | 0.9556 | Descriptive baseline |
| Train class prior | 0.1028 | 0.1028 | Trivial baseline |

The primary paired differences (regularized minus unregularized) were `0.0000`, `0.0000`, and `0.0000` for seeds 0, 1, and 2. Their mean was `0.0000` percentage points (fraction scale), sample SD across seeds `0.0000`. The preregistered 10,000-resample paired bootstrap over test example indices, RNG seed 2026, gave a conditional 95% interval `[0.0000, 0.0000]`. The models made identical correctness decisions on all test examples across primary decay settings, so every paired resample is exactly zero. The interval therefore does not demonstrate equivalence; the protocol specifies no equivalence margin.

The 0.001 arm also exactly matched the primary test accuracies for each seed. The shuffled-label controls were near the ten-class chance level and far below real-label models, as predicted; this supports the control's diagnostic behavior, not the causal attribution of any primary difference. Logistic regression was 1.22 percentage points below the MLP mean on this split; the class-prior model was 10.28% accurate. These are contextual comparisons, not inferential tests.

## Interpretation, checks, and limitations

For this fixed architecture, split, training budget, and three seeds, the experiment finds no observed accuracy benefit or penalty from changing decay from 0 to 0.01. H1's strict positive prediction was not observed. The data do not establish equivalence or show that weight decay never helps. Matching predictions across the arms are a strong local observation, but the 360 test examples, one random example split, and only three seeds sharply limit broader inference. There are no writer identities, so this is not an estimate of generalization to new writers. The paired bootstrap conditions on the fitted models and fixed split; it excludes retraining, split, and distribution-shift uncertainty.

The control outcome reduces concern that the pipeline predicts digits well without label information. Independent recomputation confirms stored metrics, test membership, labels, and checkpoint-reload assertions. These checks reduce ordinary measurement/provenance alternatives but cannot validate every aspect of the fixture implementation. Results are not evidence that decay was mechanistically inactive: matching classification accuracy does not imply identical logits, loss, or parameter norms. We did not register those as outcome measures.

No protocol amendment was made. Preserve the zero observed contrast as a negative/inconclusive result and do not select an alternate decay from test outcomes. The result remains confirmatory only for the registered contrast; controls and auxiliary comparisons are exploratory. Staging the work as exploration, testing, and distillation follows [Nanda's research-process guide](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL).

## Evidence map

The `experiment-analysis` evidence ID points to the derived calculations. The fourteen experiment IDs (`regularized_s0` through `_s2`, `unregularized_s0` through `_s2`, `sensitivity_s0` through `_s2`, `shuffled_labels_s0` through `_s2`, `logistic_s0`, and `class_prior_s0`) resolve to immutable JSON records with predictions, labels, example IDs, loss histories where applicable, hashes, environment, and checkpoint verification. See `../research/evidence.json` for each path and SHA256. Recompute with:

```powershell
& 'C:/Users/Happy/Documents/projects/auto-eureka-scientist-agent-harness/.venv/Scripts/python.exe' research/analyze_experiments.py
```
