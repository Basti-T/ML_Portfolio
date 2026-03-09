# 🚀 Strategic E-Commerce Commander: Hybrid ML Sales Forecast
### *Transforming Reactive Data into Executive Action & Operational Efficiency*

[![Open In NBViewer](https://img.shields.io/badge/Render-NBViewer-orange)](https://nbviewer.org/github/Basti-T/ML_Portfolio/blob/main/02_Hybrid_ML_Sales_Forecast/Forecast_Ecommerce_Business.ipynb)

---

## 📊 Executive Strategic Summary
![Strategic Commander Summary](presentations/Hybrid%20ML%20Forecasting.png)

---

## 📌 Strategic Overview
This project bridges the gap between raw Shopify data and executive decision-making. By merging long-term seasonal intelligence with 30-day tactical momentum, it transforms static e-commerce data into a functional interface for leadership. It provides the critical lead time required to optimize warehouse staffing and marketing spend, protecting the bottom line from operational waste.

**Key Achievement:** Implementation of this logic has historically contributed to a **~12% improvement in labor efficiency** by aligning warehouse staffing with forecasted package volumes.

---

## 🧠 Hybrid Intelligence Architecture (Level 4 DS)
The system utilizes a professional-grade **Dual-Model Ensemble** to ensure the forecast is both visionary and realistic:

1.  **Prophet (Strategic Base):** Decodes multi-year seasonality, holiday peaks, and weekday performance patterns. It provides the "Strategic Vision" based on long-term historical cycles.

2.  **XGBoost (Tactical Anchor):** Uses a **30-day rolling mean** and lag features to tether the forecast to recent performance, preventing "forecast drift" during sudden market shifts.


### Technical Highlights:
* **Logarithmic Scaling:** Employs $log(1+y)$ transformation to stabilize variance across high-growth periods.
* **Feature Engineering:** Automated lag features (1, 7, 30 days) and rolling monthly averages act as "Stability Anchors."
* **Dynamic Regressors:** Marketing campaigns are injected as binary indicators, allowing the AI to learn the specific "Lift" of past events.

---

## 🛠️ Interactive Strategic Capabilities
The notebook features a custom-built **Management Interface** using `ipywidgets` for real-time simulations:

* **Executive "Challenge" Engine:** Move beyond passive forecasting. Leadership can set growth targets (e.g., +15%) to visualize the exact daily sales required to hit long-term benchmarks.
* **Marketing Campaign Simulator:** Teams input planned dates and expected lifts to simulate the outcome on the monthly total *before* budget is deployed.
* **The 3-Day Signal Logic:** If actual sales fall under the forecast for 3 consecutive days, the system flags the need for immediate strategy pivots.
* **Operational Staffing Alignment:** Translates sales forecasts into package volume projections, allowing warehouse managers to standardize labor hours.

---

## 📂 Repository Structure
| File | Description |
| :--- | :--- |
| [`Forecast_Ecommerce_Business.ipynb`](Forecast_Ecommerce_Business.ipynb) | **The Command Center.** Main interactive notebook with UI and Hybrid Models. |
| [`data/Example_data_for_Forecast.ipynb`](data/Example_data_for_Forecast.ipynb) | **Data Creator.** Notebook used to generate or prepare the environment data. |
| [`data/Shopify_NetSales.csv`](data/Shopify_NetSales.csv) | **Sample Data.** Masked dataset following standard Shopify export schema. |
| `presentations/` | Contains high-impact business documentation including `Hybrid_ML_Forecasting.png`. |

---

## 📈 How to Use
1.  **Prepare Data:** Navigate to the `/data/` folder and run [`Example_data_for_Forecast.ipynb`](data/Example_data_for_Forecast.ipynb) to initialize your dataset.
2.  **Environment:** Open the main notebook [`Forecast_Ecommerce_Business.ipynb`](Forecast_Ecommerce_Business.ipynb) in Google Colab.
3.  **Simulation:** Use the **Strategic Commander** sliders to adjust growth targets, history lookback, and forecast horizons.
4.  **Action:** Use the generated **Variance Table** to adjust warehouse staffing or marketing spend in real-time.

---

## 🎯 The Bottom Line
This tool moves E-commerce from a **"Guessing Culture"** to a **"Strategic Asset."** It eliminates information asymmetry between departments, ensuring that the CEO, Marketing, and the Warehouse are all steering toward the same number.

---
**Author:** Sebastian Thurm  
**Role:** Strategic Data Scientist & AI Architect

---
**Author:** Sebastian Thurm  
**Role:** Strategic Data Scientist & AI Architect
