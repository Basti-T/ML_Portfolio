# 🚀 Strategic E-Commerce Commander: Hybrid ML Sales Forecast
### *Transforming Reactive Data into Executive Action & Operational Efficiency*

---

## 📊 Executive Strategic Summary
![Strategic Commander Summary](presentations/Hybrid%20ML%20Forecasting.png)

---

## 📌 Strategic Overview
This project bridges the gap between raw Shopify data and executive decision-making. By merging long-term seasonal intelligence with 30-day tactical momentum, it transforms static e-commerce data into a functional interface for leadership. 

**Key Achievement:** Implementation of this logic has historically contributed to a **~12% improvement in labor efficiency** by aligning warehouse staffing with forecasted package volumes.

---

## 🧠 Hybrid Intelligence Architecture
The system utilizes a professional-grade **Dual-Model Ensemble** (Level 4 DS) to ensure the forecast is both visionary and realistic:

1.  **Prophet (Strategic Base):** Decodes multi-year seasonality, holiday peaks, and weekday performance patterns. It provides the "Strategic Vision" based on long-term historical cycles.
2.  **XGBoost (Tactical Anchor):** Uses a **30-day rolling mean** (`rolling_30`) and monthly lags (`lag_30`) to tether the forecast to recent performance, preventing "forecast drift" during sudden market shifts.



### Technical Highlights:
* **Logarithmic Scaling:** Employs `np.log1p` transformation to stabilize variance across high-growth periods.
* **Feature Engineering:** Automated lag features (1, 7, 30 days) and rolling monthly averages act as "Stability Anchors."
* **Dynamic Regressors:** Marketing campaigns are injected as binary indicators, allowing the AI to learn the specific "Lift" of past events.

---

## 📂 Project Structure & Navigation
To maintain data integrity and a clean environment, this project is split into functional directories. Please navigate to the folders below to explore the code:

* **[Main Notebooks](notebooks/)**: Contains the primary forecasting engine and the interactive **Strategic Commander** interface.
* **[Data & Preparation](data/)**: Includes the `Shopify_NetSales.csv` sample and the notebook used to generate environment-ready data.
* **[Presentations](presentations/)**: Visual assets and executive summary documentation.

---

## 📈 Methodology & Usage
1.  **Data Generation:** Run the preparation script in the `/data/` folder to initialize the Shopify schema.
2.  **Model Training:** The `Forecast_Ecommerce_Business.ipynb` notebook performs a hybrid fit, blending the Prophet trend with XGBoost residuals.
3.  **Executive Simulation:** The interface allows for real-time "Growth Challenge" scaling and marketing campaign lift simulations.

---
**Author:** Sebastian Thurm  
**Role:** Strategic Data Scientist & AI Architect
