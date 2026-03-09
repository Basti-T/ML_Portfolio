# 🚀 Strategic E-Commerce Commander: Hybrid ML Sales Forecast
### *Bridging Data Science and Executive Strategy for Shopify Growth*

[![View Project in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Basti-T/ML_Portfolio/blob/main/02_Hybrid_ML_Sales_Forecast/Forecast_Ecommerce_Business.ipynb)

---

## 📊 Executive Strategic Summary
![Strategic Commander Summary](presentations/Hybrid%20ML%20Forecasting.png)

---

## 📌 Strategic Overview
This project transforms raw Shopify export data into a **proactive steering tool**. While standard analytics look backward, the Strategic Commander looks ahead, allowing leadership to simulate the revenue impact of marketing campaigns and set "Growth Challenges" for the business.

**Key Achievement:** By aligning warehouse staffing with predictive package volumes, this logic enables a **~12% improvement in labor efficiency**.

---

## 🧠 Hybrid Intelligence Architecture (Level 4 DS)
The engine utilizes a sophisticated **Dual-Model Ensemble** designed to balance long-term trends with short-term stability:

1.  **Prophet (The Strategic Base):** Decodes 2-year historical seasonality, holiday peaks, and weekday performance patterns. It provides the "Vision" for where sales should be based on long-term trends.
2.  **XGBoost (The Tactical Anchor):** Focuses on the most recent 365 days, utilizing a **30-Day Stability Anchor** (Rolling Mean & Monthly Lag). This prevents the forecast from over-reacting to outliers while staying tethered to current market reality.

### Technical Implementation:
* **Logarithmic Scaling:** Employs $log1p$ transformation to stabilize variance across high-growth periods.
* **Stability Features:** Uses `lag_1`, `lag_7`, `lag_30`, and `rolling_30` to provide the model with tactical context.
* **Dynamic Regressors:** Marketing campaigns are injected as binary regressors, allowing the models to learn the specific "Lift" of past promotions.

---

## 🛠️ Interactive Strategic Capabilities
The notebook features an integrated **Management Interface** for real-time revenue simulation:

* **Executive "Challenge" Slider:** Leadership can set growth targets (e.g., +15%) to visualize the daily sales trajectory required to hit long-term goals.
* **Marketing Campaign Simulator:** Quickly test "what-if" scenarios by entering custom dates and expected lift percentages to see instant revenue projections.
* **Operational Variance Tracking:** A dynamic table compares actual sales vs. targets, flagging "Hit" or "Miss" days to trigger immediate strategic pivots.

---

## 📂 Repository Structure
| File | Description |
| :--- | :--- |
| [`Forecast_Ecommerce_Business.ipynb`](Forecast_Ecommerce_Business.ipynb) | **The Command Center.** Main interactive notebook with Hybrid Models and UI. |
| [`data/Example_data_for_Forecast.ipynb`](data/Example_data_for_Forecast.ipynb) | **Data Creator.** Notebook used to generate or prepare the environment data. |
| [`data/Shopify_NetSales.csv`](data/Shopify_NetSales.csv) | **Sample Data.** Masked dataset following standard Shopify export schema. |
| `presentations/` | High-impact documentation including `Hybrid ML Forecasting.png`. |

---

## 📈 How to Use
1.  **Prepare Data:** Navigate to the [`/data/`](data/) folder and run the generator to initialize your dataset.
2.  **Run Command Center:** Open [`Forecast_Ecommerce_Business.ipynb`](Forecast_Ecommerce_Business.ipynb) in Google Colab and upload your CSV.
3.  **Simulate:** Use the **Strategic Commander** sliders to adjust growth targets and forecast horizons.

---
**Author:** Sebastian Thurm  
**Role:** Strategic Data Scientist & AI Architect
