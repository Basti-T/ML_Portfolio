# 🚀 Strategic E-Commerce Commander: Hybrid ML Sales Forecast
### *Transforming Reactive Data into Executive Action & Operational Efficiency*

[![View Project in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Basti-T/ML_Portfolio/blob/main/02_Hybrid_ML_Sales_Forecast/Forecast_Ecommerce_Business.ipynb)

---

## 📊 Executive Strategic Summary
![Strategic Commander Summary](presentations/Hybrid%20ML%20Forecasting.png)

---

## 📌 Strategic Overview
This project bridges the gap between raw Shopify data and executive decision-making. By merging long-term seasonal intelligence with 30-day tactical momentum, it transforms static e-commerce data into a functional interface for leadership. 

**Key Achievement:** Implementation of this logic has historically contributed to a **~12% improvement in labor efficiency** by aligning warehouse staffing with forecasted package volumes.

---

## 🧠 Hybrid Intelligence Architecture

The system utilizes a professional-grade **Dual-Model Ensemble** (Level 4 DS) as seen in your implementation:

* **Prophet (Strategic Base):** Decodes multi-year seasonality and holiday peaks. It provides the "Strategic Vision" based on long-term historical cycles.
* **XGBoost (Tactical Anchor):** Uses a **30-day rolling mean** (`rolling_30`) and monthly lags (`lag_30`) to tether the forecast to recent performance, preventing "forecast drift".

### Technical Highlights:
* **Logarithmic Scaling:** Employs `np.log1p` transformation to stabilize variance across high-growth periods.
* **Dynamic Regressors:** Marketing campaigns are injected as binary indicators, allowing the AI to learn the specific "Lift" of past events.

---

## 🛠️ Interactive Strategic Capabilities
The notebook features a custom-built **Management Interface** using `ipywidgets` for real-time simulations:

* **Executive "Challenge" Engine:** Leadership can set growth targets via the `growth_slider` to visualize the exact daily sales required to hit benchmarks.
* **Marketing Campaign Simulator:** Teams can input planned dates and expected lifts via the `quick_input` field to simulate revenue impact.
* **Operational Staffing Alignment:** Translates sales forecasts into daily volume projections, allowing for standardized labor hour planning.

---

## 📂 Repository Structure
| File | Description |
| :--- | :--- |
| [`Forecast_Ecommerce_Business.ipynb`](Forecast_Ecommerce_Business.ipynb) | **The Command Center.** Main interactive notebook with UI and Hybrid Models. |
| [`data/Example_data_for_Forecast.ipynb`](data/Example_data_for_Forecast.ipynb) | **Data Creator.** Setup for the environment. |
| [`data/Shopify_NetSales.csv`](data/Shopify_NetSales.csv) | **Sample Data.** Masked Shopify sales dataset. |
| `presentations/` | Visual documentation and summary PNGs. |

---

## 📈 How to Use
1.  **Prepare Data:** Navigate to `/data/` and run [`Example_data_for_Forecast.ipynb`](data/Example_data_for_Forecast.ipynb) to generate the CSV.
2.  **Environment:** Open [`Forecast_Ecommerce_Business.ipynb`](Forecast_Ecommerce_Business.ipynb) in Colab and upload the generated CSV.
3.  **Simulate:** Use the **Strategic Commander** sliders to adjust growth targets and marketing campaigns.

---
**Author:** Sebastian Thurm  
**Role:** Strategic Data Scientist & AI Architect
