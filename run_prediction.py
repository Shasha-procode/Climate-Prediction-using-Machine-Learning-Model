# run_prediction.py
"""
Load a saved model (climate_model.pk) and run predictions on an input CSV.
Usage:
    python run_prediction.py                # reads seattle-weather.csv by default
    python run_prediction.py input.csv      # read a custom CSV
Output:
    predictions.csv  (contains original data + prediction column)
"""

import sys
import os
import pandas as pd
import joblib
from pathlib import Path

MODEL_FILE = "climate_model.pk"
DEFAULT_INPUT = "seattle-weather.csv"
OUTPUT_FILE = "predictions.csv"

def load_model(path=MODEL_FILE):
    if not Path(path).exists():
        raise FileNotFoundError(f"Model file not found: {path}")
    model = joblib.load(path)
    print(f"Loaded model from {path} -> {type(model)}")
    return model

def preprocess(df):
    df = df.copy()
    # parse date (if present)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day
    # fill numeric missing values with median (simple strategy)
    for c in df.select_dtypes(include=["number"]).columns:
        df[c] = df[c].fillna(df[c].median())
    return df

def main():
    # Accept optional input CSV path from command line
    input_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    if not Path(input_path).exists():
        print(f"ERROR: input file not found: {input_path}")
        return

    # Load data
    df = pd.read_csv(input_path)
    print("Input rows:", len(df))
    print("Columns:", df.columns.tolist())

    # Preprocess
    df_proc = preprocess(df)

    # Ensure model exists & load it
    try:
        model = load_model(MODEL_FILE)
    except Exception as e:
        print("ERROR loading model:", e)
        return

    # Decide features used for prediction
    # NOTE: These must match what you used during training.
    # Default used in training: ["precipitation", "temp_min", "wind"]
    features = ["precipitation", "temp_min", "wind"]
    missing = [f for f in features if f not in df_proc.columns]
    if missing:
        print("ERROR: These required feature columns are missing from the input file:", missing)
        print("Available columns:", df_proc.columns.tolist())
        return

    X = df_proc[features]

    # Predict
    try:
        preds = model.predict(X)
    except Exception as e:
        print("ERROR during model.predict:", e)
        return

    # Save results
    df_result = df.copy()  # keep original order/columns
    df_result["prediction"] = preds
    df_result.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved predictions to {OUTPUT_FILE} ({len(df_result)} rows).")
    print("Preview:")
    print(df_result.head())

if __name__ == "__main__":
    main()
