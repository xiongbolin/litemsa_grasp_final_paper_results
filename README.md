# LiteMSA-Grasp paper-support repository

This repository supports the manuscript **“LiteMSA-Grasp: Robust RGB-D Grasp Perception with Attention-Derived Trust Diagnostics under Sensor Corruption.”**

## Included

- Selected Cornell and Jacquard configuration files preserved from the supplied project archive.
- Core protocol and post-hoc soft-reliability result tables.
- A small verification script that checks the headline values used in the manuscript.
- A reproducibility-scope statement documenting what the historical archive does and does not contain.

## Important scope limitation

This is a paper-support evidence repository, not a claim of complete end-to-end retraining reproducibility. The supplied historical archive did not contain the complete original training/evaluation code, model checkpoints, frozen dataset split files, or an environment lock. These items have not been reconstructed or fabricated. See `REPRODUCIBILITY_SCOPE.md`.

## Data

Cornell and Jacquard are third-party datasets and are not redistributed here. Obtain them from their original providers and follow their licenses.

## Verify headline result tables

```bash
python analysis/verify_core_tables.py
```

The verification script uses only the included CSV files and Python's standard library.
