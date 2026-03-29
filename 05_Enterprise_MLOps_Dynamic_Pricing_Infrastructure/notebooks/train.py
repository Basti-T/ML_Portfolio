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

    # Standard SageMaker arguments
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))

    # These capture the hyperparameters you set in the Notebook
    parser.add_argument('--eta', type=float)
    parser.add_argument('--max_depth', type=int)
    parser.add_argument('--num_round', type=int)

    args, _ = parser.parse_known_args()

    # Load data
    data_path = os.path.join(args.train, "features.csv")
    data = pd.read_csv(data_path)

    X = data[['ctd_ratio', 'btd_ratio', 'inventory_level']]
    y = data['target_adjustment']

    # Train with the dynamic parameters from the Notebook
    dtrain = xgb.DMatrix(X, label=y)
    params = {
        "objective": "reg:squarederror",
        "eta": args.eta,
        "max_depth": args.max_depth
    }

    print(f"🚀 Training High-Def Model: Rounds={args.num_round}, Depth={args.max_depth}")
    model = xgb.train(params, dtrain, num_boost_round=args.num_round)

    # Save
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
    print("✅ High-Def Model Saved!")
