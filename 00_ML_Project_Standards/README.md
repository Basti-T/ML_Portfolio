# 🏆 The ML Gold Standard: Business-First Engineering Manifesto

**Version 3.0 — Effective Date: March 8, 2026**

This repository defines my professional standards for Machine Learning Engineering. I prioritize **Data Integrity**, **Scientific Rigor**, and **Business Impact** over model complexity. 

> **Core Philosophy:** I solve real-world business problems by applying rigorous engineering standards to messy data. I deliver "Production-Ready" assets through a standardized architecture that ensures reliability, transparency, and a clear path from a Google Colab sandbox to an AWS production factory.

---

## 🏛️ Strategic Framework (Executive View)
*This visual summary outlines the high-level pillars of my methodology. Click the image to access the full documentation.*

[![ML Gold Standard Manifesto](./presentations/The%20ML%20Gold%20Standard%20Business-First%20Engineering.png)](./presentations/The%20ML%20Gold%20Standard%20Business-First%20Engineering.pdf)

---

## 🛠️ The Dual-Engine Mother Templates
*Use these pre-configured environments to jumpstart high-integrity ML pipelines with built-in validation layers and "The 11 Commandments" pre-coded.*

### 📈 [1. The Regression Engine (Continuous Prediction)](./notebooks/ML_Standard_Template_Regression.ipynb)
* **Focus:** Pricing, Forecasting, and Value Quantification.
* **Logic:** XGBoost excellence, Residual Analysis, and Variance Stability.

### 🎯 [2. The Classification Engine (Decision Logic)](./notebooks/ML_Standard_Template_Classification.ipynb)
* **Focus:** Churn, Fraud, and Risk Categorization.
* **Logic:** Random Forest/XGBoost, Probability Calibration, and Performance Slicing.

---

## 📂 I. Standardized Project Structure
*Designed for high-speed iteration in Google Colab and zero-friction handover to AWS Pipelines:*

* **`data/`**: Raw datasets (Read-only source of truth).
* **`visuals/`**: Exported Residual Plots, Feature Importances, and Segment Audits.
* **`notebooks/`**: The engine. Contains the Regression and Classification Mother Templates.
* **`presentations/`**: The Executive PDF Manifesto and Strategic Visuals.
* **`Presentation/`**: **The Deployment Package (The Handover Asset)**
    * 📦 `[model_name]_v3_[date].pkl`: The serialized Pipeline (Preprocessing + Model).
    * 📄 `requirements.txt`: The Selective Environment Lock for AWS.

---

## 🛠 II. The 11 Commandments of High-Integrity Pipelines

### 0.5 The Sanity Gate (Pre-Flight Check)
* **The Law**: Automatically kill "noise" before training. Remove zero-variance features, high-cardinality IDs, and sparse columns to prevent the model from learning "mirages."

### 1. The "Wall of Silence" (Data Splitting)
* **The Law**: Data must be split before any human or machine "looks" at it. Use Stratified Splitting to ensure real-world performance matches laboratory results.

### 2. Signal-First Feature Engineering
* **The Law**: Missingness is a business signal. Never delete data; use boolean flags to capture patterns of absence.

### 3. The Transformation Engine (Pipeline Architecture)
* **The Law**: Bundle all Scaling, Encoding, and Imputation into a `scikit-learn` Pipeline. The resulting `.pkl` is a portable "black box" for AWS.

### 4. The Complexity Threshold (Baseline vs. SOTA)
* **The Law**: Advanced models (XGBoost) must provide a **>10% improvement** over simple Baselines to justify their deployment.

### 5. Metric Realism (KPI Alignment)
* **The Law**: Optimize for the metric that matches the business cost of a mistake (e.g., MAE for value; F1/Precision/Recall for decisions).

### 8. Mathematical Rigor & Scaling
* **The Law**: Respect algorithm assumptions. Scaling is mandatory for distance-based logic; extrapolation checks are required for tree-based models.

### 8.1 The Bias Audit (Performance Slicing)
* **The Law**: A high total score is worthless if it fails on key business segments. Audit performance across slices like Region or Category to ensure fairness.

### 9.5 Model Persistence (The Handover)
* **The Law**: Secure the asset. Automatically export the full pipeline with a timestamped versioning system for immediate AWS integration.

### 10. The Validation Layer (Stakeholder Dashboard)
* **The Law**: If a stakeholder can't "touch" the model, they won't trust it. Every project ends with an interactive UI to test model intuition in real-time.

### 11. The Environment Lock (AWS Readiness)
* **The Law**: "It works on my machine" is a failure. Generate a selective `requirements.txt` to lock the exact core library versions used in the experiment.

---

## 🚀 III. The "Sandbox-to-Factory" Workflow
1.  **Experiment (Colab):** Rapidly iterate using the Mother Templates to find the "Perfect Model."
2.  **Export (Packaging):** Run Commandments 9.5 and 11 to generate the `.pkl` engine and `requirements.txt` blueprint.
3.  **Deployment (AWS):** Upload the `Presentation/` folder to AWS. The pipeline handles live data processing automatically, ensuring 100% parity with the experiment.

***
**Author:** Sebastian Thurm  
**Standard:** Professional-Grade ML Engineering (v3.0)
