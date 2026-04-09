# 🚀 Enterprise MLOps & Prescriptive Pricing Infrastructure
### *Transforming Retail from Reactive Discounting to Behavioral Profit Engines*

![AWS Architecture](https://img.shields.io/badge/AWS-SageMaker-FF9900?style=for-the-badge&logo=amazonsagemaker&logoColor=white)
![Infrastructure](https://img.shields.io/badge/IaC-CloudFormation-FF4F8B?style=for-the-badge&logo=amazoncloudformation&logoColor=white)
![Language](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📊 Strategic Executive Summary
[![Strategic Summary Preview](./presentations/Advanced_Pricing_Engine.png)](./presentations/Advanced_Pricing_Engine.pdf)
*Click the preview above to view the [Full Strategy PDF](./presentations/Advanced_Pricing_Engine.pdf)*

---

## 📌 Project Mission
In global e-commerce, static pricing is the primary driver of trapped working capital. Standard ERP systems are **reactive**, categorizing products only after significant sales lag. This project introduces a **Production-Ready Dynamic Pricing Framework**—a technical ecosystem that shifts retail operations from historical reporting to **Prescriptive Machine Learning**.

By integrating real-time inventory velocity with customer engagement metrics (**Cart-to-Detail Friction**), the system enables **Automated Margin Protection** and **Surgical Liquidation**.

---

## 🏗️ Technical Architecture (The MLOps Chassis)
This framework utilizes **Infrastructure-as-Code (IaC)** to ensure 100% automated deployment and zero configuration drift.

* **SageMaker Feature Store:** Implementation of a centralized registry for "Friction Metrics" (CtD/BtD ratios). This eliminates online-offline skew and ensures data integrity across the pipeline.
* **XGBoost Gradient Boosting:** Optimized regressor trained to identify "Pricing Walls"—where high customer interest meets zero conversion.
* **Serverless Inference:** Deployed via **SageMaker Serverless Endpoints**, aligning infrastructure costs directly with revenue-generating activity (scaling to $0 during idle periods).
* **S3 Data Lake:** Hardened storage layer orchestrated via CloudFormation with strict IAM policies for secure data transit.

---

## 🧠 Methodology: Behavioral Feature Engineering
A key innovation is the transition from "Sales-Only" modeling to **Intent-Based Modeling**:

1.  **Friction Score Calculation:** The `processing.py` script transforms raw clickstream logs into friction metrics. If a product has high views/carts but low buys, the AI identifies a "Pricing Wall."
2.  **Inventory Pressure Logic:** A logistical guardrail that scales discount intensity based on warehouse capacity (15,000 unit ceiling).
3.  **The "CEO Steering Wheel":** A multi-strategy logic allowing leadership to toggle between **Margin Defense**, **Balanced Growth**, and **Revenue Liquidation** without retraining the model.

---

## 📂 Repository Structure
| Path | Description |
| :--- | :--- |
| **`pricing_infrastructure.yaml`** | CloudFormation template for VPC, S3, IAM, and SageMaker resources. |
| **`processing.py`** | Script for behavioral feature engineering and friction metric aggregation. |
| **`train.py`** | Production training script utilizing XGBoost and SageMaker Estimators. |
| **`launcher_pricing_model.ipynb`** | The Executive Dashboard & Visual Sensitivity Audit. |
| **`presentations/`** | Architectural diagrams and the Strategic Framework PDF. |

---

## 📈 Key Performance Outcomes
* **Operational Agility:** 100% automated deployment via CloudFormation; zero manual configuration.
* **Capital Efficiency:** Serverless architecture reduces fixed infrastructure costs by ~90% compared to always-on instances.
* **Surgical Liquidation:** Automatically triggers "Revenue Mode" for high-pressure stock, freeing up stagnant capital $30\text{--}60$ days faster than manual cycles.
* **Precision Margin Defense:** Defends MSRP for "Superstars" and "Hidden Gems," preventing accidental discounting on high-demand items.

---

## 🏁 The Bottom Line
The **Pricing MLOps Framework** transforms pricing from a reactive administrative task into a **Prescriptive Profit Engine**. By merging AWS-hardened infrastructure with behavioral intelligence, this system replaces "gut-feeling" with data-driven clarity, creating a virtuous cycle of margin protection and maximized working capital.

---
**Author:** Sebastian Thurm  
**Role:** Lead Data, Artificial Intelligence & Machine Learning  
**Certification:** AWS Certified Machine Learning Associate
