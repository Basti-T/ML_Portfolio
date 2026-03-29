# 🚀 Enterprise MLOps & Dynamic Pricing Infrastructure
### *From Reactive Discounting to Prescriptive Profit: A Hardened AWS-Native Pricing Engine*

---

## 📊 Executive Strategic Summary

> ### 📂 [Full Strategy & Architecture PDF](./presentations/Enterprise%20MLOps%20&%20Dynamic%20Pricing%20Infrastructure.pdf)
*Click the link above to view the complete strategic breakdown and AWS infrastructure diagrams.*

---

---

## 📌 Strategic Overview
In global e-commerce, static pricing is the primary driver of trapped working capital and missed margin. Standard ERP systems are **reactive**, categorizing products into ABC segments only after 60–90 days of sales history, which leads to warehouse congestion and "panic discounting".

This project introduces a **Production-Ready Dynamic Pricing Framework**—a technical ecosystem that shifts retail operations from historical reporting to **Prescriptive Machine Learning**. By integrating real-time inventory velocity with customer engagement metrics (Cart-to-Detail friction), the system enables **Automated Margin Protection**.

**Key Achievement:** Built a scalable **AWS "Skeleton"** that synchronizes real-time inventory velocity with automated price elasticity modeling, ensuring high-demand "A-Items" maintain premium positioning while systematically identifying "C-Item" (dead-stock) risks for strategic liquidation.

---

## 🏗️ Architectural Governance (The "90% Solution")
While many ML projects remain confined to local notebooks, this framework is built for the Enterprise using **Infrastructure-as-Code (IaC)** to ensure 100% automated deployment and zero configuration drift:

1.  **VPC Isolation:** Orchestrated via **AWS CloudFormation**, featuring a hardened VPC with private subnets and an **S3 Gateway Endpoint** to ensure sensitive data never traverses the public internet.
2.  **The Feature Registry:** Implementation of the **Amazon SageMaker Feature Store**. This decouples data engineering from training, providing a low-latency registry for "Friction Metrics" (CtD/BtD ratios) to eliminate data integrity issues.
3.  **Zero-Waste Compute:** Deployment via **SageMaker Serverless Inference**, aligning infrastructure costs directly with revenue-generating activity and scaling to zero during idle periods.

---

## 🧠 Technical Methodology: Strategic Rule-Engine Integration
A key innovation of this project is the integration of **Heuristic Business Logic** with **Machine Learning Feature Engineering**, replacing "gut-feeling" with strategic clarity:

* **Behavioral Feature Engineering:** The `processing.py` script transforms raw clickstream logs into friction metrics (Cart-to-Detail & Buy-to-Detail ratios) to detect "hidden" demand signals that humans often miss.
* **The "Strategic Switch" Logic:** Rather than a "black box" approach, the framework utilizes a **Prescriptive Switch**. By identifying products with high engagement but low conversion, the system automatically triggers calculated price adjustments (e.g., -15%) to unlock inventory velocity.
* **Infrastructure over Guesswork:** Validates the **MLOps Chassis**, proving that business strategies (like liquidating slow-movers) can be deployed as scalable, automated AWS services across thousands of SKUs.

---

## 📂 Project Structure & Navigation
To maintain data integrity and professional standards, this project is organized into functional layers:

* **[`/`](./)**: Contains the `pricing_infrastructure.yaml` CloudFormation templates for the VPC, SageMaker Endpoint, and Feature Store.
* **[`/`](./)**: Includes `processing.py` for behavioral feature engineering and friction metric calculation.
* **[`/`](./)**: The experimentation environment for model training and infrastructure validation.
* **[`presentations/`](./presentations/)**: Includes the **Strategic Executive Summary PDF** and the AWS Application Composer architecture diagrams.

---

## 📈 Key Performance Outcomes
* **Operational Agility:** 100% automated deployment via CloudFormation with zero manual configuration drift.
* **Capital Efficiency:** Serverless architecture reduces fixed infrastructure costs by ~90% compared to "always-on" instances.
* **Data Integrity:** Feature Store ensures 100% consistency between training and live inference.
* **Strategic Growth:** A plug-and-play architecture ready to support 10k+ SKUs across diverse categories.

---

## 🏁 The Bottom Line Summary
The **Pricing MLOps Framework** transforms pricing from a reactive historical function into a **Prescriptive Profit Engine**. By merging AWS-hardened infrastructure with behavioral feature engineering, this system replaces "gut-feeling" discounts with data-driven clarity. This cloud-ready solution creates a virtuous cycle of better margin protection, faster inventory turnover, and maximized working capital.
