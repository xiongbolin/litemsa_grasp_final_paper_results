# Run the public checks

From the repository root:

```bash
python -m pip install -r reproducibility/requirements.txt
python reproducibility/verify_public_package.py
python reproducibility/figure_generation/regenerate_figures_3_5.py
```

Expected outcomes:

- the verifier ends with `PUBLIC PACKAGE VERIFICATION: PASS`;
- the figure script reports nine generated panel plots under `reproducibility/figure_generation/generated/`.
