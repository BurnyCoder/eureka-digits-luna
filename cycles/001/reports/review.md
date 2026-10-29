# Review: cycle 001

## Scope and outcome

This is one substantive review of the fixed training/evaluation code, registered comparison, evidence and claims, generated paper, and the website's source/data and local links. The supplied protocol and measurements were preserved; no training or test-based model selection occurred. The required non-training check passed. One malformed evidence-ledger terminator was repaired and is rechecked below.

## Code and scientific validity

- `study.py check` passed: 1,797 × 64 inputs, disjoint stratified partitions of 1,078/359/360, and finite two-example logits of shape 2 × 10; the output explicitly says `training_performed: false` (`ev-review-check`). The code's model is the registered 64–128–10 ReLU MLP. The primary arms differ in the registered `weight_decay` value while using matched seeds and split/order setup (`ev-study-fixture-code`, `ev-fixed-protocol`).
- The optimizer call agrees with the current [PyTorch AdamW API](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html): decay is a parameter to AdamW and does not accumulate in its momentum or variance. This confirms method identity, not that decay should help. The motivation is consistent with [Loshchilov and Hutter](https://arxiv.org/abs/1711.05101), whose results do not establish an effect for this fixture.
- The registered result remains narrow: the saved primary pairs show identical test correctness for the three matched seeds, and the registered decision is inconclusive. A conditional bootstrap over those same fitted models and examples is not an equivalence test and does not quantify seed- or split-level uncertainty (`ev-regularized_s0`–`ev-regularized_s2`, `ev-unregularized_s0`–`ev-unregularized_s2`, `ev-experiment-analysis`). The shuffled-label, logistic, and class-prior arms are reported descriptively and are not substituted for the primary contrast (`ev-shuffled_labels_s0`–`ev-shuffled_labels_s2`, `ev-logistic_s0`, `ev-class_prior_s0`).
- Recomputed each of the 15 website experiment accuracies from its displayed `y_true`/`y_pred` and verified array lengths against example IDs; all values matched the records (`ev-review-site-data`). This also checks that the first-example cards have aligned labels and predictions.

## Paper and website inspection

- The PDF is six pages, unencrypted, and its metadata names Libor “Burny” Burian. I rendered and visually inspected pages 1 and 2; the text extraction and images are legible, and the result table/accuracy plot are visible. Page 1 ends with a “Results” heading immediately before the page break, which is mildly awkward. Page 2 begins with the architecture figure and contains the results table and accuracy plot. I did not visually inspect every page (`ev-review-pdf-metadata`, `ev-review-paper-page-1`, `ev-review-paper-page-2`).
- The paper currently says “Research is in progress; no final run-status snapshot is available.” This is a temporary controller-state placeholder, not a scientific result. Publication should regenerate the paper and site after the controller provides its final status snapshot. Do not infer a completed publication state from this review (`ev-review-cycle-paper`, `ev-review-site-paper-source`).
- The website has working local download targets for `paper.pdf`, `paper.md`, and `data.json`; HTML IDs are unique; its inline JavaScript passes `node --check`; the JSON parses and contains all 15 result records and the registered inconclusive primary summary (`ev-review-site-index`, `ev-review-site-data`). Dynamic record/source text is inserted with `textContent`, and source links are limited to HTTP(S). The prediction table supplies a text alternative to canvas plots.
- Browser runtime interaction was not verified: browser access is disabled in Work settings (`ev-review-browser-availability`). I therefore make no claim that the page was opened interactively or that its filters/canvas render correctly in a browser. The PDF was visually checked using rendered page images; the website was checked statically.

## Concrete repair and remaining handoff

The prior validation failure was real: `cycles/001/research/evidence.json` ended in a literal `\\n` after its closing JSON array, causing `JSONDecodeError: Extra data` at line 236. Removed the trailing characters; JSON parsing now succeeds and all evidence paths/hashes are checked below. This repairs evidence serialization only and does not alter any result or protocol (`ev-evidence-ledger`).

Residual issues for the controller's later publication step: refresh the temporary run-status text; inspect the remaining PDF pages and live website when a browser is available; the site is not shown here to have been deployed. No scientific revisit is required based on this review. The fixed example split has no writer IDs, the neural comparison has only three seeds, and equal correctness can mask differences in logits, confidence, loss, or weights. The review does not independently reproduce training or establish generality beyond this task.

## Sources checked

- [Loshchilov & Hutter, *Decoupled Weight Decay Regularization*](https://arxiv.org/abs/1711.05101) (`loshchilov-hutter-2019-adamw`).
- [PyTorch `torch.optim.AdamW`](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html) (`pytorch-adamw-docs`).
- [NeurIPS Paper Checklist guidance](https://neurips.cc/public/guides/PaperChecklist), used as reporting guidance rather than evidence of venue compliance.
