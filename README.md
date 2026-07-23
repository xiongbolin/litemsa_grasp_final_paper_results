# LiteMSA-Grasp paper-support and reproducibility repository

This public repository supports the manuscript **“LiteMSA-Grasp: Soft trust allocation and corruption repair for lightweight RGB-D grasp perception.”**

## Public reproducibility materials

The repository provides two levels of verification:

1. **Fast table-level verification** using the CSV files in `tables/` and `analysis/verify_core_tables.py`.
2. **Public S1 reproducibility package** at `reproducibility/LiteMSA_Grasp_S1_Reproducibility_Public.zip`, containing source code, configurations, environment files, split audits, run/checkpoint inventories, frozen evidence tables, a 48-check numeric audit, Figure 3–5 source data, and deterministic figure-generation code.

Package SHA-256:

```text
1b6c93df67ed3b95d5764b72934024115d171a4e3f595efe7426dc60183a5ef0
```

## Quick verification

Verify the tables already visible in the repository:

```bash
python analysis/verify_core_tables.py
```

For the complete public package, download and extract the S1 ZIP, then run:

```bash
python verify_public_package.py
python figure_generation/regenerate_figures_3_5.py
```

The public-package verifier checks four headline protocol values, confirms the 48/48 numeric audit and its source tables, verifies the 84 plotted values for Figures 3–5, and preserves the reported negative soft-reliability-versus-confidence result.

## Included in S1

- model, loss, geometry, data-manifest, training and evaluation source code;
- Cornell and Jacquard experiment configurations;
- environment specifications;
- split-audit records;
- experiment, processed-manifest and checkpoint inventories;
- frozen manuscript-facing result tables;
- full numeric audit and figure-generation lineage.

## Data and scope boundaries

Cornell and Jacquard images are third-party datasets and are not redistributed. Obtain them from their original providers and follow their licences. Raw-data retraining requires those datasets and suitable compute.

The separately registered checkpoint archive is not included in ordinary Git history because it exceeds GitHub's normal file-size limit. The public materials support source inspection, configuration inspection, split auditing, table-level verification, Figure 3–5 regeneration, and rerunning when the external datasets are supplied. Physical-robot grasp-success validation is outside the study.

See `REPRODUCIBILITY_SCOPE.md` and `reproducibility/README.md` for the exact claim boundary.