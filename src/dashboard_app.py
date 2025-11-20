import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = DATA_DIR / "intrusion_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


st.title("Network Intrusion Detection – Binary Classifier")
st.write(
    "Upload a CSV file with the same feature columns used for training. "
    "The model will classify each row as normal traffic (0) or attack (1)."
)

if not MODEL_PATH.exists():
    st.error(f"Model file not found at {MODEL_PATH}. Please run src/train_ids_pipeline.py first.")
else:
    model = load_model()
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("Preview of uploaded data")
        st.dataframe(df.head())

        if st.button("Run Intrusion Detection"):
            preds = model.predict(df)
            df_results = df.copy()
            df_results["prediction"] = preds

            st.subheader("Predictions (first 50 rows)")
            st.dataframe(df_results.head(50))

            attack_count = int((preds == 1).sum())
            normal_count = int((preds == 0).sum())

            st.markdown(f"Total rows: {len(preds)}")
            st.markdown(f"Normal traffic (0): {normal_count}")
            st.markdown(f"Attacks detected (1): {attack_count}")

            st.download_button(
                "Download predictions as CSV",
                data=df_results.to_csv(index=False).encode("utf-8"),
                file_name="ids_predictions.csv",
                mime="text/csv",
            )