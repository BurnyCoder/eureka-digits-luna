# Post-publication provenance audit

The controller recorded a completed run within its limits; the authoritative call count, active time and accepted phases are in [the execution summary](run-6800b91601cb.json). The subsequent parent audit found that publication had changed bytes referenced by accepted evidence. Therefore, the original completion record alone did not establish that the final public artifacts passed verification.

The initial failing audit and byte diagnosis are preserved under `reports/verification/`. Git had converted Windows line endings in scientific JSON and authored Markdown. Separately, rendering had replaced generated documents cited by the review. The parent developer recovered the exact previously hashed bytes: reversing newline conversion reproduced the original hashes, and saved reviewed copies supplied the original generated documents. No scientific values were changed. The repair ledger records each recovery.

Public evidence now points to immutable, content-addressed snapshots. Scoped Git attributes preserve exact cycle and website bytes, and the harness checks artifacts again after publication. The parent regenerated the final presentation, loaded checkpoints, inspected the PDFs and browser, and published these receipts after the bounded run. This work involved no additional model invocation and is not counted as autonomous work by Luna. The earlier audit failure remains evidence of a harness defect.

The trial used a shared, supplied training fixture and inherited harness repairs discovered during the earlier Haiku trial. These development executions do not rank the providers or demonstrate frozen-version, unattended scientific reliability. The CLI recorded the requested Luna identifier but did not expose a resolved model snapshot; the harness made no model substitution.

The pilot fixture forwards test features through an evaluation-only network while checking checkpoint reload. It stores and scores validation predictions for the pilot; test labels do not enter training, model selection or the pilot metric. A statement that the pilot never accesses test features would therefore be too strong. This example-level split does not establish generalization to unseen writers.

Reproduce the numerical artifacts and checkpoint checks using the [harness reproduction guide](https://github.com/BurnyCoder/auto-eureka-scientist-agent-harness/blob/main/docs/reproduction.md). The preserved review snapshots are historical evidence; current presentation files can be regenerated without erasing them.
