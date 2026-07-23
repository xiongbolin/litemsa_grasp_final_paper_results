#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def rows(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def one(data: list[dict[str, str]], **conditions: str) -> dict[str, str]:
    matches = [
        row for row in data
        if all(row.get(key) == str(value) for key, value in conditions.items())
    ]
    if len(matches) != 1:
        raise AssertionError(f"Expected one row for {conditions}, found {len(matches)}")
    return matches[0]


def near(observed: str, expected: float, tolerance: float = 0.015) -> bool:
    return abs(float(observed) - expected) <= tolerance


main = rows("evidence_tables/final_main_protocol_table.csv")
headline_checks = [
    ("Cornell LiteMSA image-wise", one(main, dataset="cornell", protocol="image-wise", method="litemsa")["mean_acc_percent"], 84.33145),
    ("Cornell LiteMSA+DA image-wise", one(main, dataset="cornell", protocol="image-wise", method="litemsa_domain_aug")["mean_acc_percent"], 86.74200),
    ("Cornell LiteMSA+DA object-group-wise", one(main, dataset="cornell", protocol="object-group-wise", method="litemsa_domain_aug")["mean_acc_percent"], 85.29012),
    ("Jacquard LiteMSA+DA object-wise", one(main, dataset="jacquard", protocol="object-wise", method="litemsa_domain_aug")["mean_acc_percent"], 96.36050),
]
for label, observed, expected in headline_checks:
    if not near(observed, expected):
        raise AssertionError(f"{label}: observed {observed}, expected {expected}")
    print(f"PASS: {label}: {float(observed):.5f}")

# This public audit is a frozen manuscript-facing regression register. Recompute
# every pass/fail decision from its observed, expected and tolerance columns.
audit = rows("audit/g9_numeric_audit.csv")
if len(audit) != 48:
    raise AssertionError(f"Expected 48 audit rows, found {len(audit)}")
for row in audit:
    if row["observed"] in {"True", "False"}:
        calculated_pass = row["observed"] == row["expected"]
    else:
        difference = abs(float(row["observed"]) - float(row["expected"]))
        calculated_pass = difference <= float(row["tolerance"])
        if row["absolute_difference"]:
            if abs(difference - float(row["absolute_difference"])) > 1e-12:
                raise AssertionError(f"Stored difference mismatch: {row['check_id']}")
    if not calculated_pass or row["status"] != "pass":
        raise AssertionError(f"Audit failure: {row['check_id']}")
print("PASS: numeric audit decisions recomputed: 48/48")

compact = rows("figure_generation/figure_3_5_compact_data.csv")
if len(compact) != 84:
    raise AssertionError(f"Expected 84 plotted values, found {len(compact)}")
if {row["figure"] for row in compact} != {"Figure_3", "Figure_4", "Figure_5"}:
    raise AssertionError("Unexpected Figure 3-5 coverage")
print("PASS: Figure 3-5 compact source data contains 84 values")

comparison = rows("evidence_tables/soft_reliability_vs_confidence_table.csv")
negative = one(comparison, group="all_corruptions", method="litemsa_domain_aug", coverage="0.5")
if float(negative["soft_minus_confidence_accuracy"]) >= 0:
    raise AssertionError("Expected preserved negative selector result")
print("PASS: negative soft-reliability versus confidence-only result preserved")
print("PUBLIC PACKAGE VERIFICATION: PASS")
