#!/usr/bin/env python3
"""Verify headline values from the preserved aggregate CSV tables.

This script does not retrain models. It checks manuscript-facing values that can be
recomputed from the included aggregate tables.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def rows(name):
    with (ROOT / "tables" / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def near(a, b, tol=0.015):
    return abs(float(a) - float(b)) <= tol

main = rows("final_main_protocol_table.csv")
soft = rows("soft_reliability_paper_table.csv")
comp = rows("soft_reliability_vs_confidence_table.csv")

def one(data, **conds):
    hits = [r for r in data if all(r.get(k) == str(v) for k, v in conds.items())]
    if len(hits) != 1:
        raise AssertionError(f"Expected one row for {conds}, found {len(hits)}")
    return hits[0]

checks = []
checks.append(("Cornell LiteMSA image-wise", one(main, dataset="cornell", protocol="image-wise", method="litemsa")["mean_acc_percent"], 84.33145))
checks.append(("Cornell LiteMSA+DA image-wise", one(main, dataset="cornell", protocol="image-wise", method="litemsa_domain_aug")["mean_acc_percent"], 86.74200))
r = one(soft, group="all_corruptions", method="litemsa_domain_aug", selector="soft_reliability", coverage="0.5")
checks.extend([
    ("LiteMSA+DA full corruption accuracy", r["mean_full_accuracy_percent"], 81.49),
    ("LiteMSA+DA 50% coverage accuracy", r["mean_selective_accuracy_percent"], 89.22),
    ("LiteMSA+DA 50% coverage lift", r["mean_accuracy_lift_percent"], 7.73),
])
negative = one(comp, group="all_corruptions", method="litemsa_domain_aug", coverage="0.5")
if float(negative["soft_minus_confidence_accuracy"]) >= 0:
    raise AssertionError("Expected preserved negative result versus confidence-only ranking")

for label, observed, expected in checks:
    if not near(observed, expected):
        raise AssertionError(f"{label}: observed {observed}, expected about {expected}")
    print(f"PASS: {label}: {float(observed):.4f}")
print("PASS: composite soft-reliability selector remains below confidence-only at 50% coverage")
