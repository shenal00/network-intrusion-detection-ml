Machine Learning–Based Network Intrusion Detection System (IDS)

This repository contains a complete, production-grade Intrusion Detection System (IDS) built using machine learning.
It includes data preprocessing, model training, evaluation, saved model artefacts, exploratory notebooks, architecture diagrams, and an interactive dashboard for real-time intrusion predictions.

This project is submitted as Evidence 3 – Technical Contribution for the UK Global Talent Visa (Digital Technology).


	1.	Project Overview

Modern networks generate large volumes of traffic, making manual monitoring insufficient for detecting malicious activity.
This system uses supervised machine learning to classify network traffic into:
	•	Normal (0)
	•	Attack (1)

The IDS is built using:
	•	NSL-KDD dataset (cleaned and binary-labeled)
	•	Random Forest classification model
	•	Custom data preprocessing pipeline
	•	Automated training pipeline
	•	Interactive prediction dashboard
	•	Saved model (intrusion_model.pkl)

This repository demonstrates practical experience in machine learning, data engineering, and deployment workflows.

	2.	Repository Structure

network-intrusion-detection-ml/
│
├── data/
│   ├── nsl_kdd_train_binary.csv
│   ├── nsl_kdd_test_binary.csv
│   ├── intrusion_model.pkl
│   └── placeholder.txt
│
├── docs/
│   └── figures/
│       ├── ids_architecture.png
│       ├── ids_pipeline.png
│       └── ids_dashboard.png
│
├── notebooks/
│   └── exploration_intrusion_ids.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── train_ids_pipeline.py
│   └── dashboard_app.py
│
├── README.md
├── TECH_NATION_EVIDENCE.md
├── requirements.txt
└── LICENSE

	3.	System Architecture

Architecture Diagram:
docs/figures/ids_architecture.png

Training Pipeline:
docs/figures/ids_pipeline.png

Dashboard Workflow:
docs/figures/ids_dashboard.png

	4.	Installation Guide

Clone the repository:

git clone https://github.com/akinyeraakintunde/network-intrusion-detection-ml.git
cd network-intrusion-detection-ml

Install dependencies:

pip install -r requirements.txt

	5.	Training the Model

Run the complete end-to-end training pipeline:

python src/train_ids_pipeline.py

This will:
	1.	Load & clean NSL-KDD datasets
	2.	Encode categorical features
	3.	Train Random Forest classifier
	4.	Print evaluation metrics
	5.	Save the trained model to data/intrusion_model.pkl


	6.	Running the Prediction Dashboard


Start the dashboard:

python src/dashboard_app.py

Features:
	•	CSV upload for network traffic
	•	Batch intrusion predictions
	•	Downloadable results file
	•	Summary of normal vs attack records


	7.	Model Performance


Typical results on NSL-KDD (binary classification):
	•	Accuracy: 97%–99%
	•	Strong detection across attack categories
	•	Robust generalisation between training and test sets

A full classification report is generated automatically during training.


	8.	Evidence for UK Global Talent Visa

This repository includes:

TECH_NATION_EVIDENCE.md

It contains:
	•	Problem summary
	•	System architecture
	•	Technical contribution explanation
	•	Pipeline overview
	•	Diagrams and artefacts
	•	Source code references

	9.	Key Technical Features

	•	End-to-end ML IDS system
	•	Clean and modular Python code
	•	Reproducible training pipeline
	•	Professional architecture diagrams
	•	Interactive prediction dashboard
	•	Real-world dataset (NSL-KDD)


	10.	License

This project is released under the MIT License.
