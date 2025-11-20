# Model Card – Network Intrusion Detection System (IDS)

## 1. Overview

This model is a supervised machine learning classifier for detecting malicious network traffic using the NSL-KDD dataset. It predicts whether a given network connection is **normal** or **attack**, enabling early detection of intrusions in enterprise environments.

The model is used inside a full pipeline that includes:

- Data preprocessing and feature engineering
- Model training and evaluation
- Persisted model artefacts (`intrusion_model.pkl`)
- FastAPI prediction API
- Real-time intrusion analysis dashboard
- ROC curve and performance reporting

## 2. Intended Use

- **Primary use:** Educational and experimental IDS for research, teaching, and portfolio demonstration.
- **Intended users:** Data scientists, security engineers, students, and reviewers evaluating Ibrahim Akintunde Akinyera’s technical work.
- **Scope:** Binary classification – attack vs normal traffic on NSL-KDD-style tabular features.

The model is **not** a plug-and-play substitute for a production SIEM or NDR platform, but it can be extended in that direction.


## 3. Dataset

- **Name:** NSL-KDD (derived from the original KDD’99 intrusion dataset)
- **Source:** Public research dataset
- **Preprocessing:**
  - Conversion to a binary problem (attack vs normal)
  - Handling of categorical features (e.g., protocol type, service)
  - Normalisation / scaling of numeric attributes
  - Train/test split using disjoint NSL-KDD train/test files

---

## 4. Model Details

- **Algorithm:** Random Forest Classifier (scikit-learn)
- **Inputs:** Tabular features representing a single network connection record
- **Output:** Binary label (`attack` or `normal`) plus probability scores where supported

Hyperparameters are tuned for a balance between **recall** (catching attacks) and **precision** (limiting false positives).

---

## 5. Evaluation

The model is evaluated on the NSL-KDD test set.

| Metric            | Score  |
|-------------------|--------|
| Accuracy          | ~96%   |
| Precision (attack)| ~95%   |
| Recall (attack)   | ~97%   |
| F1-score          | ~96%   |
| ROC-AUC           | ~0.961 |

A ROC curve (`docs/figures/roc_curve.png`) visualises the trade-off between true positive rate and false positive rate.

## 6. Ethical and Security Considerations

- The model is trained on a synthetic / simulated dataset; real-world network traffic may differ significantly.
- False negatives (missed attacks) are **high-risk** in security contexts. This model should be one component of a wider defence-in-depth strategy, not a single line of defence.
- Data used is public and anonymised; no personally identifiable information (PII) is processed.

## 7. Limitations

- Dataset is limited to patterns captured in NSL-KDD; modern attack techniques (e.g., zero-days, encrypted traffic patterns) may not be represented.
- The model assumes features are preprocessed in the **same way** as during training. Incorrect preprocessing will degrade performance.
- No automatic concept drift handling is implemented.

## 8. Maintenance and Future Work

Planned improvements include:

- Experimenting with gradient boosting and deep learning models
- Incorporating additional datasets (e.g., UNSW-NB15)
- Adding drift detection and scheduled retraining
- Deploying the API to a managed cloud service with observability

**Owner:** Ibrahim Akintunde Akinyera  
**Contact:** ibrahim.akinyera@outlook.com