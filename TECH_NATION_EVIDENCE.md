# Technical Contribution Evidence – Machine Learning–Based Network Intrusion Detection System (IDS)

## Overview

This repository demonstrates a complete end-to-end machine learning Intrusion Detection System (IDS) developed by Ibrahim Akintunde Akinyera.  
It is submitted as part of the **UK Global Talent Visa – Evidence 3 (Technical Contribution)** to showcase practical ability in cybersecurity analytics, data engineering, applied machine learning, and production-focused software development.

The project implements a binary classification model capable of detecting malicious network activities using the NSL-KDD dataset, which is a recognised benchmark in academic and industry cybersecurity research.

---

## Summary of Technical Contributions

1. **End-to-End Machine Learning Engineering**
   - Designed and implemented a full IDS pipeline covering dataset ingestion, preprocessing, encoding, feature engineering, model training, evaluation, and deployment.
   - Structured the project in a production-style format, separating data, models, source code, and documentation for clarity and reproducibility.

2. **Cybersecurity Domain Expertise**
   - Applied machine learning techniques to a real-world network security problem.
   - Used the NSL-KDD dataset, converting it into a binary classification problem suitable for operational intrusion detection (normal vs attack).

3. **Model Development and Evaluation**
   - Built a RandomForest model with competitive accuracy (~78%) on the official NSL-KDD test set.
   - Performed data cleaning, one-hot encoding, and model optimisation.
   - Exported the final model (`intrusion_model.pkl`) for integration into dashboards or monitoring systems.

4. **Production-Ready Implementation**
   - Delivered a clean and maintainable codebase with well-organised modules, including `src/train_ids_pipeline.py`, preprocessing scripts, and optional dashboard interface.
   - Ensured the project can be reproduced by assessors through `requirements.txt` and detailed instructions.

5. **Documentation and Clarity**
   - Provided full architectural diagrams, dataset breakdown, model pipeline documentation, and results.
   - Ensured transparency for assessors by including clear commentary, data provenance, and model evaluation metrics.

---

## Repository Structure (Relevant to Evidence Submission)

```
data/
  nsl_kdd_train_binary.csv        # Cleaned and encoded training data
  nsl_kdd_test_binary.csv         # Cleaned and encoded test data
  intrusion_model.pkl             # Trained RandomForest IDS model

src/
  train_ids_pipeline.py           # End-to-end model training pipeline
  data_preprocessing.py           # Dataset ingestion and encoding
  dashboard_app.py                # Optional Streamlit interface
  network_intrusion_detection.py  # Supporting ML logic

docs/
  figures/
    ids_architecture.png          # System architecture visual
    ids_pipeline.png              # ML pipeline visual
    ids_dashboard.png             # Dashboard flow visual

README.md                         # Full project documentation
TECH_NATION_EVIDENCE.md           # Current evidence summary
```

---

## Evidence Relevance to Tech Nation Criteria

This work aligns with the **“Technical Contribution”** pathway as defined by Tech Nation by demonstrating:

- Significant high-level technical output in an applied domain (cybersecurity).
- Independent design, development, and documentation of an ML system.
- Strong understanding of algorithmic decision-making, data quality, and model evaluation.
- Practical engineering approach with deployment-ready deliverables.
- Clear contribution to advancing security-focused software capabilities.

---

## Contact and Verification

**Ibrahim Akintunde Akinyera**  
Machine Learning Engineer • Cybersecurity & Risk Analytics  
GitHub: https://github.com/akinyeraakintunde  
LinkedIn: https://www.linkedin.com/in/ibrahimakinyera/

---