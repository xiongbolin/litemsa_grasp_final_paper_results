#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def rows(rel):
    with (ROOT/rel).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def one(data, **conds):
    hits=[r for r in data if all(r.get(k)==str(v) for k,v in conds.items())]
    if len(hits)!=1: raise AssertionError(f"Expected one row for {conds}, found {len(hits)}")
    return hits[0]

def near(a,b,tol=0.015): return abs(float(a)-float(b))<=tol

main=rows("evidence_tables/final_main_protocol_table.csv")
checks=[
("Cornell LiteMSA image-wise", one(main,dataset="cornell",protocol="image-wise",method="litemsa")["mean_acc_percent"],84.33145),
("Cornell LiteMSA+DA image-wise", one(main,dataset="cornell",protocol="image-wise",method="litemsa_domain_aug")["mean_acc_percent"],86.74200),
("Cornell LiteMSA+DA object-group-wise", one(main,dataset="cornell",protocol="object-group-wise",method="litemsa_domain_aug")["mean_acc_percent"],85.29012),
("Jacquard LiteMSA+DA object-wise", one(main,dataset="jacquard",protocol="object-wise",method="litemsa_domain_aug")["mean_acc_percent"],96.36050),
]
for label,obs,exp in checks:
    if not near(obs,exp): raise AssertionError(f"{label}: observed {obs}, expected {exp}")
    print(f"PASS: {label}: {float(obs):.5f}")

audit=rows("audit/g9_numeric_audit.csv")
if len(audit)!=48 or any(r["status"]!="pass" for r in audit):
    raise AssertionError("Expected 48/48 passing numeric checks")
for r in audit:
    if not (ROOT/r["source"]).exists(): raise AssertionError(f"Missing audit source: {r['source']}")
print("PASS: numeric audit 48/48 and all source tables present")

compact=rows("figure_generation/figure_3_5_compact_data.csv")
if len(compact)!=84: raise AssertionError(f"Expected 84 compact plotted values, found {len(compact)}")
print("PASS: Figure 3-5 compact source data contains 84 values")

comp=rows("evidence_tables/soft_reliability_vs_confidence_table.csv")
negative=one(comp,group="all_corruptions",method="litemsa_domain_aug",coverage="0.5")
if float(negative["soft_minus_confidence_accuracy"])>=0: raise AssertionError("Expected preserved negative selector result")
print("PASS: negative soft-reliability vs confidence-only result preserved")
print("PUBLIC PACKAGE VERIFICATION: PASS")
