from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
RESULT_DIR = BASE_DIR / "logs_500"
OUTPUT_FILE = RESULT_DIR / "WT_kea3_vccn1_6panel.png"

SERIES = {
    "WT": {
        "path": RESULT_DIR / "WT_500uE_simulated.csv",
        "color": "black",
    },
    "kea3": {
        "path": RESULT_DIR / "kea3_500uE_simulated.csv",
        "color": "blue",
    },
    "vccn1": {
        "path": RESULT_DIR / "vccn1_500uE_simulated.csv",
        "color": "red",
    },
}

VARIABLES = [
    "pHlumen",
    "Dy",
    "pmf",
    "Klumen",
    "Cl_lumen",
    "Cl_stroma",
]


def main():
    data = {
        name: pd.read_csv(settings["path"])
        for name, settings in SERIES.items()
    }

    plt.rcParams.update(
        {
            "font.size": 14,
            "axes.labelsize": 16,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 10,
        }
    )

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))

    for axis, variable in zip(axes.flat, VARIABLES):
        for name, settings in SERIES.items():
            frame = data[name]
            axis.plot(
                frame["time_axis"],
                frame[variable],
                label=name,
                color=settings["color"],
                alpha=0.75,
            )

        axis.set_xlabel("Time/s")
        axis.set_ylabel(variable)
        axis.legend(
            loc="upper center",
            bbox_to_anchor=(0.5, 1.1),
            ncol=3,
            frameon=False,
        )
        axis.grid(False)

    fig.tight_layout()
    fig.savefig(OUTPUT_FILE, dpi=200, bbox_inches="tight")
    print(f"Saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
