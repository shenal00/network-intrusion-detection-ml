from pathlib import Path
import pickle

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
MODEL_PATH = DATA_DIR / "intrusion_model.pkl"


def _load_model():
    with MODEL_PATH.open("rb") as f:
        return pickle.load(f)


def test_model_can_predict_on_sample_row():
    train_path = DATA_DIR / "nsl_kdd_train_binary.csv"
    df = pd.read_csv(train_path)

    # assume binary label column is named "label" or "target"
    label_cols = [c for c in df.columns if c.lower() in {"label", "target", "class"}]
    assert (
        len(label_cols) == 1
    ), "Could not uniquely identify label column in training data"

    label_col = label_cols[0]
    X = df.drop(columns=[label_col])

    model = _load_model()
    sample = X.iloc[[0]]  # keep as DataFrame

    preds = model.predict(sample)
    assert len(preds) == 1, "Model did not return a single prediction"