import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

TRAIN_PATH = DATA_DIR / "nsl_kdd_train_binary.csv"
TEST_PATH = DATA_DIR / "nsl_kdd_test_binary.csv"
MODEL_PATH = DATA_DIR / "intrusion_model.pkl"


def main() -> None:
    print(f"Loading training data from: {TRAIN_PATH}")
    print(f"Loading test data from: {TEST_PATH}")

    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    X_train = train_df.drop(columns=["binary_label"])
    y_train = train_df["binary_label"]
    X_test = test_df.drop(columns=["binary_label"])
    y_test = test_df["binary_label"]

    print("Training RandomForestClassifier...")
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy on test set: {acc:.4f}")
    print("Classification report:")
    print(classification_report(y_test, y_pred))

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Saved trained model to: {MODEL_PATH}")


if __name__ == "__main__":
    main()