"""Register experiment records and derived report artifacts with SHA256."""
from pathlib import Path
import hashlib
import json

PROJECT = Path(__file__).resolve().parents[3]
CYCLE = PROJECT / "cycles" / "001"
LEDGER = CYCLE / "research" / "evidence.json"


def digest(path):
    """Hash exact bytes so ledger citations identify the artifact version."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(entries, identifier, path, kind):
    """Replace a matching evidence ID while preserving all earlier records."""
    rel = path.relative_to(PROJECT).as_posix()
    entries[:] = [entry for entry in entries if entry["id"] != identifier]
    entries.append({"id": identifier, "path": rel, "sha256": digest(path), "analysis_kind": kind})


def main():
    """Update hashes for all completed arms, analyses, and experiment reports."""
    entries = json.loads(LEDGER.read_text(encoding="utf-8"))
    for result in sorted((CYCLE / "results").glob("*.json")):
        record = json.loads(result.read_text(encoding="utf-8"))
        add(entries, record["id"], result, record["analysis_kind"])
    add(entries, "experiment-analysis", CYCLE / "research" / "experiment-analysis.json", "exploratory")
    add(entries, "experiment-analysis-code", CYCLE / "research" / "analyze_experiments.py", "not_applicable")
    add(entries, "experiment-evidence-registration", Path(__file__), "not_applicable")
    add(entries, "experiment-report", CYCLE / "reports" / "experiments.md", "exploratory")
    add(entries, "research-highlights", CYCLE / "reports" / "highlights.md", "exploratory")
    LEDGER.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    print(f"Registered {len(entries)} evidence records.")


if __name__ == "__main__":
    main()
