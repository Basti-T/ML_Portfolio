# 📊 Strategic HR: AI-Powered Employee Retention
**Business Case:** Reducing high-value employee turnover through predictive modeling and interactive risk assessment.

## 🛠️ Project Components
1. **[01_Attrition_Risk_Analysis_Model.ipynb](./01_Attrition_Risk_Analysis_Model.ipynb):** - Full data pipeline: EDA, SMOTE balancing, and model comparison.
   - Cross-validation for performance stability (Mean Recall: 0.80+).
2. **[02_Interactive_Retention_Dashboard.ipynb](./02_Interactive_Retention_Dashboard.ipynb):** - A functional HR tool for "What-If" scenarios.
   - Bulk upload feature for department-wide risk reporting.

## 🚀 How to use the Interactive Dashboard
Because GitHub renders notebooks statically, the interactive widgets require a live environment:
1. Open the **[Dashboard Notebook](./02_Interactive_Retention_Dashboard.ipynb)**.
2. Click the **"Open in Colab"** badge at the top.
3. Run all cells to initialize the HR Tool.

## 📈 Key Insights
- **Top Risk Factors:** Frequent Overtime and Distance from Home.
- **Model Choice:** Logistic Regression was selected as the "Winner" due to its high **Recall**, ensuring HR identifies the maximum number of employees at risk.
