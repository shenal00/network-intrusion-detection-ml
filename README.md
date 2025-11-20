<!DOCTYPE html>
<html lang="en">
<head> 
  <meta charset="UTF-8" />
  <title>Machine Learning–Based Network Intrusion Detection System (IDS)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {
      margin: 0;
      padding: 2rem 1.5rem 4rem;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
        Roboto, Helvetica, Arial, sans-serif;
      background-color: #050816;
      color: #e5e7eb;
      line-height: 1.6;
    }
    a {
      color: #38bdf8;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    h1,
    h2,
    h3 {
      color: #f9fafb;
      margin-top: 2.2rem;
      margin-bottom: 0.75rem;
      font-weight: 650;
    }
    h1 {
      font-size: 2.1rem;
      margin-top: 0;
    }
    h2 {
      font-size: 1.5rem;
      border-bottom: 1px solid rgba(148, 163, 184, 0.5);
      padding-bottom: 0.4rem;
    }
    h3 {
      font-size: 1.25rem;
    }
    p {
      margin: 0.35rem 0 0.75rem;
    }
    code {
      font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
        "Courier New", monospace;
      background: rgba(15, 23, 42, 0.9);
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
      font-size: 0.95em;
    }
    pre {
      background: rgba(15, 23, 42, 0.9);
      padding: 1rem 1.25rem;
      border-radius: 8px;
      overflow-x: auto;
      font-size: 0.9rem;
      border: 1px solid rgba(30, 64, 175, 0.6);
      box-shadow: 0 18px 45px rgba(15, 23, 42, 0.8);
    }
    pre code {
      background: transparent;
      padding: 0;
    }
    ul {
      margin: 0.25rem 0 0.75rem 1.25rem;
    }
    li {
      margin-bottom: 0.25rem;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.15rem 0.55rem;
      border-radius: 999px;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      border: 1px solid rgba(94, 234, 212, 0.6);
      color: #a5f3fc;
      background: radial-gradient(circle at top left, #022c22, #020617);
      margin-bottom: 0.75rem;
    }
    .section {
      max-width: 980px;
      margin: 0 auto;
    }
    .section-inner {
      background: radial-gradient(circle at top left, #020617, #020617 40%, #000 100%);
      border-radius: 16px;
      padding: 1.75rem 1.5rem;
      border: 1px solid rgba(148, 163, 184, 0.35);
      box-shadow: 0 26px 65px rgba(15, 23, 42, 0.9);
      margin-bottom: 1.75rem;
    }
    .repo-structure {
      font-size: 0.88rem;
    }
    .images-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
      margin-top: 0.75rem;
    }
    .image-card {
      background: rgba(15, 23, 42, 0.9);
      border-radius: 12px;
      padding: 0.75rem 0.75rem 1rem;
      border: 1px solid rgba(55, 65, 81, 0.8);
    }
    .image-card img {
      width: 100%;
      border-radius: 8px;
      border: 1px solid rgba(31, 41, 55, 0.9);
      display: block;
    }
    .image-caption {
      font-size: 0.8rem;
      color: #9ca3af;
      margin-top: 0.55rem;
    }
    @media (min-width: 900px) {
      body {
        padding-left: 3rem;
        padding-right: 3rem;
      }
    }
  </style>
</head>
<body>
  <main class="section">
    <header class="section-inner">
      <div class="badge">Evidence 3 – Technical Contribution</div>
      <h1>Machine Learning–Based Network Intrusion Detection System (IDS)</h1>
      <p>
        This repository contains a complete, production-style Intrusion Detection System (IDS)
        built using machine learning. It includes end-to-end data preprocessing, model training,
        evaluation, saved artefacts, exploratory notebooks, diagrams, and an interactive dashboard
        for real-time intrusion predictions.
      </p>
      <p>
        The project is used as <strong>Evidence 3 – Technical Contribution</strong> for the
        UK Global Talent Visa (Digital Technology).
      </p>
    </header>

    <!-- 1. Project Overview -->
    <section class="section-inner">
      <h2>1. Project Overview</h2>
      <p>
        Modern networks generate large volumes of traffic, making manual threat detection
        increasingly difficult. This project implements a machine learning–based Intrusion
        Detection System that classifies network traffic into:
      </p>
      <ul>
        <li><strong>Normal (0)</strong></li>
        <li><strong>Attack (1)</strong></li>
      </ul>
      <p>Key components include:</p>
      <ul>
        <li>NSL-KDD dataset (cleaned and converted to binary labels)</li>
        <li>Random Forest classification model</li>
        <li>Custom data preprocessing pipeline</li>
        <li>End-to-end training pipeline</li>
        <li>Saved production model (<code>intrusion_model.pkl</code>)</li>
        <li>Interactive dashboard for predictions</li>
      </ul>
      <p>
        This project demonstrates strong capabilities in data engineering, model development,
        evaluation, and lightweight deployment.
      </p>
    </section>

    <!-- 2. Repository Structure -->
    <section class="section-inner">
      <h2>2. Repository Structure</h2>
      <pre class="repo-structure"><code>network-intrusion-detection-ml/
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
└── LICENSE</code></pre>
    </section>

    <!-- 3. System Architecture -->
    <section class="section-inner">
      <h2>3. System Architecture &amp; Pipelines</h2>

      <div class="images-grid">
        <div class="image-card">
          <img src="docs/figures/ids_architecture.png" alt="IDS Architecture Diagram" />
          <div class="image-caption">
            Figure 1 – High-level system architecture showing data flow from NSL-KDD through
            preprocessing, model training, saved artefacts, and dashboard.
          </div>
        </div>

        <div class="image-card">
          <img src="docs/figures/ids_pipeline.png" alt="IDS Training Pipeline Diagram" />
          <div class="image-caption">
            Figure 2 – Training pipeline: data loading, cleaning, feature encoding, model training,
            evaluation and model export.
          </div>
        </div>

        <div class="image-card">
          <img src="docs/figures/ids_dashboard.png" alt="IDS Dashboard Workflow" />
          <div class="image-caption">
            Figure 3 – Dashboard workflow for CSV upload, scoring with
            <code>intrusion_model.pkl</code> and results display.
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Installation -->
    <section class="section-inner">
      <h2>4. Installation</h2>
      <p>Clone the repository:</p>
      <pre><code>git clone https://github.com/akinyeraakintunde/network-intrusion-detection-ml.git
cd network-intrusion-detection-ml</code></pre>

      <p>Install dependencies:</p>
      <pre><code>pip install -r requirements.txt</code></pre>
    </section>

    <!-- 5. Training the Model -->
    <section class="section-inner">
      <h2>5. Training the Model</h2>
      <p>
        The full IDS training process is automated within a single pipeline script:
      </p>
      <pre><code>python src/train_ids_pipeline.py</code></pre>
      <p>This script will:</p>
      <ul>
        <li>Load and clean NSL-KDD train and test datasets</li>
        <li>Encode categorical features</li>
        <li>Train a Random Forest classifier</li>
        <li>Evaluate performance metrics (accuracy and classification report)</li>
        <li>Save <code>intrusion_model.pkl</code> into the <code>data/</code> directory</li>
      </ul>
    </section>

    <!-- 6. Running the Dashboard -->
    <section class="section-inner">
      <h2>6. Running the Dashboard</h2>
      <p>Launch the interactive prediction dashboard:</p>
      <pre><code>python src/dashboard_app.py</code></pre>
      <p>
        The dashboard allows you to upload a CSV file containing network traffic records and
        returns:
      </p>
      <ul>
        <li>Intrusion prediction (normal vs attack)</li>
        <li>Prediction counts for normal and attack records</li>
        <li>Downloadable CSV containing predictions</li>
      </ul>
    </section>

    <!-- 7. Model Performance -->
    <section class="section-inner">
      <h2>7. Model Performance</h2>
      <p>
        After training, the model typically achieves:
      </p>
      <ul>
        <li><strong>Accuracy:</strong> high performance on the NSL-KDD test split</li>
        <li>Strong detection capability for malicious traffic</li>
        <li>Consistent performance across training and testing sets</li>
      </ul>
      <p>
        Metrics are displayed automatically when <code>train_ids_pipeline.py</code> completes,
        including accuracy and a detailed classification report.
      </p>
    </section>

    <!-- 8. Evidence for UK Global Talent Visa -->
    <section class="section-inner">
      <h2>8. Evidence for UK Global Talent Visa</h2>
      <p>
        The repository includes a dedicated evidence document:
      </p>
      <ul>
        <li><code>TECH_NATION_EVIDENCE.md</code></li>
      </ul>
      <p>This document summarises:</p>
      <ul>
        <li>The technical problem addressed</li>
        <li>System architecture and design decisions</li>
        <li>Engineering contributions and implementation detail</li>
        <li>Data processing and modelling approach</li>
        <li>Key diagrams, screenshots and supporting artefacts</li>
      </ul>
      <p>
        The structure aligns with expectations for a Technical Contribution evidence document
        under the UK Global Talent Visa guidelines.
      </p>
    </section>

    <!-- 9. Key Highlights -->
    <section class="section-inner">
      <h2>9. Key Highlights</h2>
      <ul>
        <li>End-to-end machine learning system for network intrusion detection</li>
        <li>Clean and modular codebase organised into logical components</li>
        <li>Professional architecture and pipeline diagrams</li>
        <li>Reproducible training pipeline and saved model artefacts</li>
        <li>Interactive dashboard for real-time predictions</li>
        <li>
          Strong demonstration of technical excellence for Global Talent Visa
          technical contribution evidence
        </li>
      </ul>
    </section>

    <!-- 10. License -->
    <section class="section-inner">
      <h2>10. License</h2>
      <p>
        This project is licensed under the <strong>MIT License</strong>. See the
        <code>LICENSE</code> file for details.
      </p>
    </section>
  </main>
</body>
</html>