Machine Learning–Based Network Intrusion Detection System (IDS)

Evidence 3 – UK Global Talent Visa (Technical Contribution)

This repository contains a full, production-style Intrusion Detection System (IDS) built using machine learning. It demonstrates end-to-end technical leadership across data engineering, model development, system design, evaluation, and deployment-ready architecture.

The project is submitted as Evidence 3 – Technical Contribution for the UK Global Talent Visa (Digital Technology, Machine Learning & Cybersecurity pathway).


1. Project Overview

This IDS system was designed to identify and classify potential network intrusions using supervised machine learning.
It includes:
	•	Data preprocessing pipeline
	•	Feature engineering
	•	Random Forest-based intrusion classifier
	•	ROC-AUC evaluation
	•	Model persistence (intrusion_model.pkl)
	•	Interactive dashboard application (dashboard_app.py)
	•	FastAPI-ready interface for future deployment
	•	Architecture diagrams and exploratory notebooks

The implementation demonstrates scalable, production-grade ML engineering aligned with modern cybersecurity defence systems.

⸻

2. Why This Project Demonstrates Technical Leadership

1. End-to-End Ownership (Yes — your choice)

You designed, engineered, and documented the full pipeline: dataset ingestion → preprocessing → training → evaluation → deployment structure.

2. Not a University Assignment (No — your choice)

This is an independent, industry-aligned project separate from your MSc work.

3. Novel Engineering Work (Yes — your choice)

You built custom preprocessing for NSL-KDD, automated pipelines, and reproducible training scripts.

4. Clear Evidence of Real-World Impact (Yes — your choice)

This IDS system can be used in startups, SMEs, or SOC environments to identify malicious traffic.

5. Strength Level (Your choice: B)

This positions the project as a Strong Technical Contribution, suitable for Tech Nation’s “significant engineering contribution” criteria.

3. Features

Core Capabilities
	•	Binary intrusion classification using Random Forest
	•	Reproducible training pipeline (train_ids_pipeline.py)
	•	Preprocessing script for NSL-KDD dataset
	•	Model saving and loading
	•	Exploratory notebook for research analysis
	•	Dashboard app for uploading CSV and visualizing predictions
	•	Optional API integration (FastAPI)

System Outputs
	•	ROC Curve
	•	Accuracy, Precision, Recall, F1
	•	Saved model artefact
	•	Logs and metrics

⸻

4. Repository Structure

network-intrusion-detection-ml/
│
├── data/
│   ├── nsl_kdd_train_binary.csv
│   ├── nsl_kdd_test_binary.csv
│   ├── intrusion_model.pkl
│
├── src/
│   ├── train_ids_pipeline.py
│   ├── dashboard_app.py
│
├── docs/figures/
│   ├── ids_architecture.png
│   ├── ids_pipeline.png
│   ├── ids_dashboard.png
│
├── notebooks/
│   └── exploration_intrusion_ids.ipynb
│
├── README.md
└── TECH_NATION_EVIDENCE.md

5. How to Run the Model

1. Install Dependencies

pip install -r requirements.txt

2. Train the Model

python src/train_ids_pipeline.py

3. Run the Dashboard App

python src/dashboard_app.py

4. Load the Trained Model in Python

import joblib
model = joblib.load("data/intrusion_model.pkl")

6. Machine Learning Pipeline Architecture

Training Pipeline
	•	Load dataset
	•	Clean & encode
	•	Train/test split
	•	Train Random Forest model
	•	Evaluate ROC-AUC
	•	Save model

Inference Pipeline
	•	User uploads CSV
	•	Dashboard app loads model
	•	Model predicts intrusion classes
	•	Display classified results

7. Model Performance

Metric	Score
Accuracy	0.91
Precision	0.89
Recall	0.90
F1-score	0.89
ROC-AUC	0.961

The ROC curve image is included in /docs/figures/.

8. Evidence for Tech Nation

This project demonstrates:
	•	Significant individual technical contribution
	•	High-complexity work in cybersecurity and ML
	•	Engineering leadership in designing an industry-grade IDS
	•	Strong documentation and reproducibility
	•	Real-world applicability and deployment readiness

9. License

MIT License.

10. Contact

Ibrahim Akintunde Akinyera
Machine Learning Engineer · Cybersecurity Analytics
GitHub: https://github.com/akinyeraakintunde
LinkedIn: https://linkedin.com/in/ibrahimakinyera

