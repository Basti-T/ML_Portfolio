# 🚀 Inventory Optimization: New Item Predictive Classifier (PCO)
### *Solving the "Cold Start" Problem: Transforming Guesswork into Prescriptive Procurement*

---

## 📊 Executive Strategic Summary

<p align="center">
  <object data="./presentations/Predicitve_Classifier.pdf" type="application/pdf" width="100%" height="800px">
    <p>Your browser does not support PDFs. 
      <a href="./presentations/Predicitve_Classifier.pdf">Click here to view the Full Strategy PDF.</a>
    </p>
  </object>
</p>

---

## 📌 Strategic Overview
In high-growth e-commerce, the initial "First-Buy" of a new SKU is traditionally a high-risk gamble. Standard ERP systems are **reactive**—classifying products only after 90 days of sales history. This results in **"C-Item" Bloat**, where 55% of new onboarded items typically become dead stock, trapping vital working capital.

The **PCO (Predictive Catalog Onboarding)** engine transitions procurement from reactive reporting to **Prescriptive Machine Learning**. By analyzing 22 "Pre-Purchase" features, this system identifies an item’s potential *before* the first Euro is invested.

**Key Achievement:** Proven at a **$3M ARR startup scale**, this implementation shifted the new-item hit rate from **10% to 25%** and slashed dead-stock onboarding by **45%**, directly accelerating cash-flow velocity.

---

## 🧠 Polarized ML Architecture
The system utilizes a "High-Integrity" **Supervised Learning Pipeline** specifically tuned for the financial extremes of retail (A-Items vs. C-Items):

1.  **Feature Engineering (The 9-Feature Core):** Distills the 22-feature SVI ecosystem into high-availability metrics including **Price-Density**, **Vendor-Success-Rate**, and **Margin-Potential**.
2.  **Ensemble Classification:** A **VotingClassifier (XGBoost + Random Forest)** cancels individual model biases to provide stable, "conservative" predictions for new catalog entries.
3.  **Risk-Averse Tuning:** Utilizes **SMOTETomek** to clean class boundaries, prioritizing **High-Recall for C-Items** (to protect capital) and **High-Precision for A-Items** (to ensure buyer trust).

### Technical Highlights:
* **Cold-Start Logic:** Achieves **72% Accuracy** on items with zero sales history—validated via **5-Fold Cross-Validation** (Mean: 0.7155).
* **Probabilistic Risk Scoring:** Provides buyers with an **AI Confidence %**, triggering "Stability Alerts" for items that sit on the border between categories.
* **Volume Regression:** Integrated **XGBoost Poisson Regressor** to calculate the optimal 30-day "Initial Buy" quantity, preventing over-indexing on unconfirmed trends.

---

## 📂 Project Structure & Navigation
To maintain data integrity and professional standards, this project is organized into functional layers:

* **[Main Notebooks](notebooks/)**: Contains the `Predict_ABC_and_Sales.ipynb` engine and the interactive **Buyer Dashboard**.
* **[Visuals & Presentations](presentations/)**: Includes the **PCO Strategic 1-Pager**, ABC distribution charts, and UI screenshots.
* **[Data Schemas](data/)**: Format specifications for `readymlproducts.csv` and `readymlvendor.csv` (compatible with standard ERP exports).

---

## 📈 Methodology & Usage
1.  **Data Input:** Load a new catalog export (Vendor, Price, Weight, Tax) into the `/data/` directory.
2.  **ML Pipeline:** Run the engine to execute the feature expansion, cluster mapping, and ensemble prediction.
3.  **Procurement Audit:** Utilize the **Interactive Dashboard** to simulate "What-If" scenarios or export the **Final Procurement Report** to automate initial Purchase Orders (POs).

---

## 🏁 The Bottom Line
The **SVI-PCO Framework** transforms procurement from a reactive historical function into a **Prescriptive Profit Engine**. By merging 22-feature vendor archetyping with predictive catalog onboarding, this system replaces "gut-feeling" with Fortune 500-level strategic clarity. 

Proven at a **$3M ARR startup scale**, this dual-module approach creates a virtuous cycle: **Better Vendor Selection → Smarter Onboarding → Maximized Working Capital.** The results are definitive: we shifted the new-item hit rate from **10% to 25%** and slashed dead-stock onboarding from **55% to 30%**. It is a plug-and-play, cloud-ready solution that turns raw business data into a continuous roadmap for cash-flow optimization and aggressive revenue growth.

---

**Author:** Sebastian Thurm  
**Role:** Head of Data, Machine Learning and AI
