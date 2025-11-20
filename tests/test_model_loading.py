from pathlib import Path
import pickle

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "data" / "intrusion_model.pkl"


def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Model file does not exist: {MODEL_PATH}"


def test_model_can_be_loaded():
    with MODEL_PATH.open("rb") as f:
        model = pickle.load(f)

    # scikit-learn estimators have a predict method
    assert hasattr(model, "predict"), "Loaded object does not have predict()"