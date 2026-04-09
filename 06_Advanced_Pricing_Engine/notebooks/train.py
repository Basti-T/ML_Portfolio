import argparse
import os
import pandas as pd
import xgboost as xgb
import joblib

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--eta', type=float, default=0.05)
    parser.add_argument('--max_depth', type=int, default=5)
    parser.add_argument('--num_round', type=int, default=200)
    parser.add_argument('--reg_lambda', type=float, default=5.0) 

    args, _ = parser.parse_known_args()

    # 1. Load data
    data_path = os.path.join(args.train, "features.csv")
    data = pd.read_csv(data_path)

    # 2. THE FULL-SIGNAL FEATURE LIST
    # We are now using the "Rich" features discovered in your preview
    features = [
        'base_cost', 
        'current_msrp', 
        'inventory_level', 
        'inv_pressure',
        'elasticity_factor', 
        'ideal_velocity',
        'ctd_ratio', 
        'btd_ratio', 
        'friction_score'
    ]
    
    X = data[features]
    y = data['target_adjustment']

    # 3. Train
    dtrain = xgb.DMatrix(X, label=y)
    
    params = {
        "objective": "reg:squarederror",
        "eta": args.eta,
        "max_depth": args.max_depth,
        "lambda": args.reg_lambda,
        "verbosity": 1
    }

    print(f"🚀 Training Ultra-HD Model with {len(features)} features...")
    model = xgb.train(params, dtrain, num_boost_round=args.num_round)

    # 4. Save
    os.makedirs(args.model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
    print("✅ Full-Signal Model Trained Successfully!")