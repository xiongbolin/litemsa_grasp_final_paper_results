# LiteMSA-Grasp S1 public reproducibility package

## Purpose

This package supports audit and reproduction of the reported paper evidence. It does not redistribute Cornell or Jacquard images and does not claim physical robot validation.

## Verification

Run:

```bash
python verify_public_package.py
```

The verifier checks:

- headline Cornell evaluation values;
- 48/48 numeric audit rows;
- Figure 3–5 source-data coverage (84 values);
- preserved negative soft-reliability-versus-confidence comparison.

## Figure regeneration

Run:

```bash
python figure_generation/regenerate_figures_3_5.py
```

## Scope

Supported:

- source inspection;
- configuration inspection;
- result-table verification;
- figure lineage verification.

Not included:

- Cornell/Jacquard raw images;
- complete original hardware environment;
- physical robot execution logs.
