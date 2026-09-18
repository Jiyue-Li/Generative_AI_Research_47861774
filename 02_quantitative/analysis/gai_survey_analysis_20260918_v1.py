"""Placeholder analysis script for dummy survey data."""

from pathlib import Path
import csv

DATA = Path(__file__).resolve().parents[1] / "processed" / "gai_survey_cleaned-responses_20260918_v1.csv"


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    n = len(rows)
    mean_freq = sum(int(row["q1_frequency"]) for row in rows) / n
    print(f"n={n}")
    print(f"mean frequency rating={mean_freq:.2f}")


if __name__ == "__main__":
    main()
