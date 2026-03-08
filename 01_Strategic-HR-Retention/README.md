# 📊 Strategic HR: AI-Powered Employee Retention
**Business Case:** Reducing high-value employee turnover through predictive modeling and interactive risk assessment.

---

## 🏛️ Executive Strategy & Tooling
Standard HR models often prioritize overall accuracy, failing to detect the minority of employees who actually quit. This project implements a **"Recall-First" strategy**, successfully flagging **51% of all leavers**—a 3x improvement in actionable intelligence.

| 📄 Strategic Analysis Report | 🛠️ Interactive Risk Dashboard |
| :--- | :--- |
| [![Report Preview](./presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.png)](./presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.pdf) | [![Tool Preview](./presentations/Enterprise%20Attrition%20Tool%20Interactive%20Risk%20Dashboard.png)](./presentations/Enterprise%20Attrition%20Tool%20Interactive%20Risk%20Dashboard.pdf) |
| *Click to view Full Strategy PDF* | *Click to view Dashboard Guide PDF* |

---

## 🛠️ Project Components

### 1. [Attrition Risk Analysis Model](./01_Attrition_Risk_Analysis_Model.ipynb)
The technical engine of the project. This pipeline handles data cleaning, **SMOTE balancing**, and model optimization, achieving a **Mean Recall of 0.80+**.
* **The Strategic 8 Drivers:** Focuses on actionable levers like **Overtime**, **Monthly Income**, and **Job Level** while filtering out non-predictive noise.

### 2. [Enterprise Attrition Tool (Dashboard)](./02_Interactive_Retention_Dashboard.ipynb)
A functional HR interface for real-time decision-making. 

![HR Tool Demo](./presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.gif)

* **What-If Simulations:** Adjust variables (e.g., Overtime or Salary) to see the immediate impact on risk scores.
* **Bulk Reporting:** Upload department-wide data to identify "Flight-Risk Clusters" instantly.

---

## 🚀 Strategic Recommendations (Short-Term Actions)
Directly derived from the model's highest-weighted predictors:
* **15% Overtime Cap:** Mandatory leadership review for departments exceeding 15% overtime.
* **"Stay Interview" Triggers:** Automated alerts for Single, Job Level 1/2 staff at their 18-month mark.
* **Income Benchmarking:** Surgical salary audits for junior roles to "lock in" loyalty.
* **Success Roadmaps:** Documented growth paths for employees hitting the 2-year mark without promotion.

---

## 💻 How to Use the Dashboard
Because GitHub renders notebooks statically, the interactive widgets require a live environment:
1. Open the **[Dashboard Notebook](./02_Interactive_Retention_Dashboard.ipynb)**.
2. Click the **"Open in Colab"** badge at the top.
3. Run all cells to initialize the HR Tool.

---

## 🏛️ Bottom Line Summary
This project moves HR from a **cost center (replacing talent)** to a **strategic asset (preserving talent)**. By focusing on the tipping points where employees decide to exit, we provide the evidence-based justification needed to reallocate budgets toward high-impact retention.
