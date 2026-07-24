# LiteMSA-Grasp paper-support and reproducibility repository

This public repository supports the manuscript **“LiteMSA-Grasp: Lightweight multimodal RGB-D grasp-map prediction with corruption repair and attention diagnostics.”**

## Current manuscript materials

The files under [`mtap/`](mtap/) provide a manuscript-specific map from reported values to the frozen public audit:

- `mtap/README.md` — scope and file guide for the current manuscript;
- `mtap/claim_map.csv` — current manuscript claims and their registered audit identifiers;
- `mtap/verify_mtap_manuscript.py` — deterministic verification of the current headline values against `reproducibility/audit/g9_numeric_audit.csv`.

Run the current-manuscript check from the repository root:

```bash
python mtap/verify_mtap_manuscript.py
```

## Broader public reproducibility materials

The repository also provides two broader verification levels:

1. **Fast table-level verification** using the CSV files in `tables/` and `analysis/verify_core_tables.py`.
2. **Public reproducibility package** under `reproducibility/`, containing source code, configurations, environment files, split audits, run/checkpoint inventories, frozen evidence tables, a 48-check numeric audit, compact figure source data and deterministic figure-generation code.

Run the broader public checks with:

```bash
python analysis/verify_core_tables.py
python reproducibility/verify_public_package.py
python reproducibility/figure_generation/regenerate_figures_3_5.py
```

## Data and scope boundaries

Cornell and Jacquard images are third-party datasets and are not redistributed. Obtain them from their original providers and follow their licences. Raw-data retraining requires those datasets and suitable compute.

The repository supports source inspection, configuration inspection, split auditing, table-level verification, figure-data inspection and rerunning when the external datasets are supplied. It does not establish physical-robot grasp success, real-sensor generalization or strict Cornell object-wise evaluation based on an authoritative image-to-object map.

Some archived files preserve additional analyses developed during the study. The current MTAP manuscript verifier uses only the claims listed in `mtap/claim_map.csv`.

See `REPRODUCIBILITY_SCOPE.md` and `mtap/README.md` for the exact claim boundary.
