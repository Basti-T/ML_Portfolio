import pandas as pd
import numpy as np
import time
import os

def run_processing():
    # SageMaker paths
    input_data = "/opt/ml/processing/input"
    output_data = "/opt/ml/processing/output"
    
    # Load raw data from S3 (mounted by SageMaker)
    df_p = pd.read_csv(f"{input_data}/product_master.csv")
    df_s = pd.read_csv(f"{input_data}/clickstream_normal.csv")

    # 1. Feature Engineering: Calculate "Friction"
    agg = df_s.groupby('sku_id').agg(
        views=('session_id', 'count'),
        carts=('action', lambda x: (x==1).sum()),
        buys=('action', lambda x: (x==2).sum())
    ).reset_index()

    # Math: Cart-to-Detail and Buy-to-Detail
    agg['ctd_ratio'] = agg['carts'] / agg['views']
    agg['btd_ratio'] = agg['buys'] / agg['views']
    
    # 2. Add 'Event Time' (Required for Feature Store)
    current_time = time.time()
    agg['event_time'] = current_time

    # 3. Join with Master Data
    final = pd.merge(df_p, agg, on='sku_id', how='left').fillna(0)

    # 4. Create the Training Target (The "Optimal Label")
    # Goal: Identify products with High Interest (CtD > 0.07) but Low Sales (BtD < 0.03)
    # and suggest a -15% adjustment to hit that 4% target.
    final['target_adjustment'] = np.where(
        (final['ctd_ratio'] > 0.07) & (final['btd_ratio'] < 0.03), 
        -0.15, 0.0
    )

    # Save to output for Step 6 (Training)
    os.makedirs(f"{output_data}/train", exist_ok=True)
    final.to_csv(f"{output_data}/train/features.csv", index=False)
    print(f"Processed {len(final)} SKUs. Target Lift identified.")

if __name__ == "__main__":
    run_processing()