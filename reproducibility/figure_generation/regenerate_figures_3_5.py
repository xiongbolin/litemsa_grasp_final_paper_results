#!/usr/bin/env python3
"""Regenerate deterministic plots from the public Figure 3-5 source table.

This script does not recreate the manuscript layout pixel-for-pixel. It produces
one inspectable PNG per figure panel from the exact public CSV values.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "figure_3_5_compact_data.csv"
OUTPUT_DIR = ROOT / "generated"

METHOD_LABELS = {
    "litemsa": "LiteMSA",
    "litemsa_domain_aug": "LiteMSA + DA",
    "ablation_no_attention": "No attention",
    "ablation_no_attention_domain_aug": "No attention + DA",
}

Y_LABELS = {
    "depth_dropout": "Rectangle accuracy (%)",
    "depth_noise": "Rectangle accuracy (%)",
    "rgb_noise": "Rectangle accuracy (%)",
    "rectangle_acc_mean": "Rectangle accuracy (%)",
    "mean_trust_shift_mean": "Mean trust shift",
    "mean_spatial_tsi_mean": "Mean spatial TSI",
}


def load_rows() -> list[dict[str, str]]:
    with DATA_FILE.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 84:
        raise ValueError(f"Expected 84 rows, found {len(rows)}")
    return rows


def safe_name(value: str) -> str:
    return value.lower().replace(" ", "_").replace("-", "_")


def main() -> None:
    rows = load_rows()
    grouped: dict[tuple[str, str], dict[str, list[tuple[int, float]]]] = defaultdict(lambda: defaultdict(list))

    for row in rows:
        key = (row["figure"], row["panel"])
        grouped[key][row["method"]].append((int(row["severity"]), float(row["value"])))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for (figure, panel), methods in sorted(grouped.items()):
        fig, ax = plt.subplots(figsize=(6.4, 4.2))
        for method, points in sorted(methods.items()):
            points.sort(key=lambda item: item[0])
            x = [item[0] for item in points]
            y = [item[1] for item in points]
            ax.plot(x, y, marker="o", label=METHOD_LABELS.get(method, method))

        ax.set_title(f"{figure.replace('_', ' ')}: {panel.replace('_', ' ')}")
        ax.set_xlabel("Stored corruption severity")
        ax.set_ylabel(Y_LABELS.get(panel, "Value"))
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False)
        fig.tight_layout()

        output = OUTPUT_DIR / f"{safe_name(figure)}_{safe_name(panel)}.png"
        fig.savefig(output, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(f"WROTE: {output.relative_to(ROOT)}")

    print(f"PASS: generated {len(grouped)} panel plots from 84 public values")


if __name__ == "__main__":
    main()
