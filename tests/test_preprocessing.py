import os
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def test_train_and_test_datasets_exist():
    train_path = DATA_DIR / "nsl_kdd_train_binary.csv"
    test_path = DATA_DIR / "nsl_kdd_test_binary.csv"

    assert train_path.exists(), f"Missing file: {train_path}"
    assert test_path.exists(), f"Missing file: {test_path}"


def test_train_dataset_has_rows_and_columns():
    train_path = DATA_DIR / "nsl_kdd_train_binary.csv"
    df = pd.read_csv(train_path)

    # basic sanity checks
    assert df.shape[0] > 0, "Training dataset has no rows"
    assert df.shape[1] > 1, "Training dataset must have features + label"