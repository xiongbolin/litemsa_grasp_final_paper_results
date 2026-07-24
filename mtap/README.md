# Current MTAP manuscript verification

## Manuscript

**LiteMSA-Grasp: Lightweight multimodal RGB-D grasp-map prediction with corruption repair and attention diagnostics**

This directory maps the numerical claims in the current manuscript to the frozen public audit located at:

```text
reproducibility/audit/g9_numeric_audit.csv
```

## Files

- `claim_map.csv` records the current manuscript claim, audit identifier and expected value.
- `verify_mtap_manuscript.py` checks the current manuscript claims against the frozen audit.

## Run

```bash
python mtap/verify_mtap_manuscript.py
```

Expected final line:

```text
CURRENT MTAP MANUSCRIPT VERIFICATION: PASS
```

## Scope

The check covers the headline clean-accuracy summaries, selected exact sign-flip results, corruption AUCs and stored-severity attention diagnostics reported in the current manuscript. It does not retrain a model, redistribute third-party image datasets or claim physical-robot validation.
