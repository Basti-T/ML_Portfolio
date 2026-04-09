import pandas as pd
import numpy as np
import time
import os

def run_processing():
    # 1. SETUP PATHS (SageMaker Standard)
    input_data = "/opt/ml/processing/input"
    output_data = "/opt/ml/processing/output"
    
    # Load raw data from S3 (mounted by SageMaker)
    df_p = pd.read_csv(f"{input_data}/product_master.csv")
    df_s = pd.read_csv(f"{input_data}/clickstream_normal.csv")

    # 2. FEATURE ENGINEERING: AGGREGATE CLICKSTREAM
    # Finding the "Interest Gap" (views vs. carts vs. buys)
    agg = df_s.groupby('sku_id').agg(
        views=('session_id', 'count'),
        carts=('action', lambda x: (x==1).sum()),
        buys=('action', lambda x: (x==2).sum())
    ).reset_index()

    # Calculate ratios
    agg['ctd_ratio'] = agg['carts'] / agg['views'].replace(0, 1)
    agg['btd_ratio'] = agg['buys'] / agg['views'].replace(0, 1)
    agg['event_time'] = time.time()

    # 3. MERGE DATASETS
    final = pd.merge(df_p, agg, on='sku_id', how='left').fillna(0)

    # 4. HIGH-DEFINITION GRADIENT TARGET LOGIC
    # Friction Score: High means customers are adding to cart but NOT buying
    final['friction_score'] = (final['ctd_ratio'] - (final['btd_ratio'] * 2)).clip(0, 1)
    
    # Inventory Pressure: Normalized scale based on 15k warehouse limit
    inventory_max = 15000 
    final['inv_pressure'] = final['inventory_level'] / inventory_max
    
    # --- THE AMPLIFIER FIX ---
    # We multiply by -100.0 so the model learns whole numbers (e.g. -15.0 for 15%)
    # instead of tiny decimals (e.g. -0.0015) which get lost in the noise.
    final['target_adjustment'] = -100.0 * (final['friction_score'] * final['inv_pressure'])
    
    # Round to 2 decimals for a clean "Percentage" target
    final['target_adjustment'] = final['target_adjustment'].round(2)

    # 5. EXPORT FOR TRAINING
    os.makedirs(f"{output_data}/train", exist_ok=True)
    final.to_csv(f"{output_data}/train/features.csv", index=False)
    print(f"✅ Processing Complete: Engineered features with Scaled HD targets.")

if __name__ == "__main__":
    run_processing()