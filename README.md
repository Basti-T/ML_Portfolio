# 🏆 The ML Gold Standard: Business-First Engineering Manifesto

**Version 2.1 — Effective Date: March 8, 2026**

This repository defines my professional standards for Machine Learning. I prioritize **Data Integrity**, **Scientific Rigor**, and **Business Impact** over model complexity.

> **Core Philosophy:** I solve real-world business problems by applying rigorous engineering standards to messy data. I deliver actionable results through a "simple-first" architecture that ensures reliability and clear ROI.

---

## 📂 I. Simplified Project Structure
*Designed for clarity and high-speed iteration in Google Colab:*

* **`data/`**: Raw datasets (read-only).
* **`visuals/`**: Exported plots, GIFs of widgets, and model performance charts.
* **`notebooks/`**: The engine. Contains the end-to-end pipeline from EDA to Interactive UI.
* **`Presentation/`**: The 5-slide Executive PDF (if not embedded in the README).
* **`README.md`**: This Manifesto + The Executive Summary for the specific project.

---

## 🛠 II. The 10 Commandments of High-Integrity Pipelines

### 1. The "Wall of Silence" (Data Splitting)
* **The Law**: Data must be split before any human or machine "looks" at it.

* **Small Data (<10k)**: Mandatory `StratifiedKFold` to maintain class ratios.
* **Time-Series**: Use `TimeSeriesSplit`; never shuffle chronologically dependent data.

### 2. Signal-First Missing Value Handling
* **The Law**: Never delete data unless it is a duplicate. Missingness is a business signal.
* **Strategy**: Instead of dropping rows, use an `is_missing` boolean flag to capture the pattern of absence. Use **Iterative Imputation** or **Median/Mode** within the pipeline to keep the data whole.

### 3. The Transformation Engine (Leakage Prevention)
* **The Law**: Use `sklearn.pipeline.Pipeline` to automate scaling and modeling.

* **Techniques**:
    * **Standardization**: For algorithms sensitive to magnitude (Linear Regression, SVM, KNN).
    * **Normalization**: For data with specific bounds or non-Gaussian distributions.
* **Constraint**: Calculate parameters (mean, std) **only** on the Training set.

### 4. The Complexity Threshold (Baseline vs. SOTA)
* **The Law**: Complex models (XGBoost, CatBoost) are only used if they provide a **>5-10% improvement** over a simple Baseline.
* **Reasoning**: If a simple Decision Tree gets you 90% of the way there, the extra 10% from an "ensemble" model must justify its lack of interpretability and higher compute cost.

### 5. Metric Realism (KPI Alignment)
* **The Law**: Use the KPI that matches the business cost of a mistake.
* **Accuracy**: Only used if classes are perfectly balanced and every error has an equal cost.
* **Cost of Error**:
    * If a **False Positive** (wrongly flagging a good customer) is expensive, optimize for **Precision**.
    * If a **False Negative** (missing a critical leaver) is expensive, optimize for **Recall**.

### 6. The Bias-Variance Tradeoff (Stability Check)
* **The Law**: A high score is worthless if it is unstable.
* **Validation**: Report the **Standard Deviation** of your Cross-Validation scores (e.g., $0.85 \pm 0.05$).
    * **High Deviation**: Your model has high **Variance** (overfitting to specific slices).
    * **Consistently Low Score**: Your model has high **Bias** (underfitting).
* **Goal**: Find the "Sweet Spot" where the error is low and the score is stable across all folds.


### 7. The Post-Mortem (Error Analysis)
* **The Law**: Analyze *why* the model failed on specific rows.
* **Visuals**: Use Confusion Matrices for classification and Residual Plots for regression to see where the model is systematically biased.

### 8. Algorithm-Specific Rigor
* **The Law**: Respect the mathematical assumptions of your chosen tool.
* **Linear/Distance**: Scaling is mandatory to prevent features with large numbers from dominating.
* **Trees**: Check for extrapolation; trees cannot predict values higher than what they saw in training.

### 9. Efficiency via LLM
* **The Rule**: LLMs are for **Code Execution**, not **Architecture**.
* **Standard**: I use LLMs to generate boilerplate code and UI widgets, freeing my focus for data strategy, feature engineering, and result interpretation.

### 10. The Validation Layer (Non-Technical UI)
* **The Law**: If a stakeholder can't "touch" the model, they won't trust it.
* **Interface**: Every project ends with an `ipywidgets` dashboard.
* **The Hook**: A GIF in the README showing the model reacting to user input is the final proof of utility.
