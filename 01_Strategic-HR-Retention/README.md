# 📊 Strategic HR: AI-Powered Employee Retention
**Business Case:** Reducing high-value employee turnover through predictive modeling and interactive risk assessment.

---

## 🏛️ Executive Strategy & Tooling
Standard HR models often prioritize overall accuracy, failing to detect the minority of employees who actually quit. This project implements a **"Recall-First" strategy**, successfully flagging **51% of all leavers**—a 3x improvement in actionable intelligence. 

### 📄 Strategic Analysis Report 
[![(PDF) Strategic Attrition Forecasting](./Presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.png)](./Presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.pdf)
*Click image to view the [Full Strategy PDF](./Presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.pdf)*

### 🛠️ Interactive Risk Dashboard
[![(PDF) Enterprise Attrition Tool](./Presentations/Enterprise%20Attrition%20Tool%20Interactive%20Risk%20Dashboard.png)](./Presentations/Enterprise%20Attrition%20Tool%20Interactive%20Risk%20Dashboard.pdf)
*Click image to view the [Dashboard Guide PDF](./Presentations/Enterprise%20Attrition%20Tool%20Interactive%20Risk%20Dashboard.pdf)*

---

## 🛠️ Project Components & Navigation

This repository is organized into functional modules for ease of review. You can explore the logic and implementation in the folders below:

### 1. [Risk Analysis Model](./notebooks/)
Located in the `notebooks/` directory, the technical engine handles data cleaning, **SMOTE balancing**, and model optimization, achieving a **Mean Recall of 0.80+**.
* **The Strategic 8 Drivers:** Focuses on actionable levers like **Overtime**, **Monthly Income**, and **Job Level** while filtering out non-predictive noise.

### 2. [Enterprise Attrition Tool](./notebooks/)
The interactive dashboard logic is housed within the `notebooks/` folder, providing a functional HR interface for real-time decision-making.

![HR Tool Demo](./Presentations/Strategic%20Attrition%20Forecasting%20Predictive%20Risk%20Model.gif)

* **What-If Simulations:** Adjust variables (e.g., Overtime or Salary) to see the immediate impact on risk scores.
* **Bulk Reporting:** Upload department-wide data to identify "Flight-Risk Clusters" instantly.

---

## 📂 Repository Directory
| Folder | Contents |
| :--- | :--- |
| **[notebooks/](./notebooks/)** | Core AI logic, Model Training, and Interactive Dashboard code. |
| **[Presentations/](./Presentations/)** | Executive PDFs, Strategy documentation, and visual demos. |
| **[data/](./data/)** | Masked HR datasets used for model validation. |

---

## 🚀 Strategic Recommendations (Short-Term Actions)
Directly derived from the model's highest-weighted predictors:
* **15% Overtime Cap:** Mandatory leadership review for departments exceeding 15% overtime.
* **"Stay Interview" Triggers:** Automated alerts for Single, Job Level 1/2 staff at their 18-month mark.
* **Income Benchmarking:** Surgical salary audits for junior roles to "lock in" loyalty.
* **Success Roadmaps:** Documented growth paths for employees hitting the 2-year mark without promotion.

---

## 🏛️ Bottom Line Summary
This project moves HR from a **cost center (replacing talent)** to a **strategic asset (preserving talent)**. By focusing on the tipping points where employees decide to exit, we provide the evidence-based justification needed to reallocate budgets toward high-impact retention.

---

**Author:** Sebastian Thurm  
**Role:** Head of Data, Machine Learning and AI




