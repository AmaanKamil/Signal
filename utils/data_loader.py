import pandas as pd
import streamlit as st
import os

REQUIRED_COLUMNS = [
    "user_id",
    "vertical",
    "sessions_per_week",
    "probability_of_conversion",
    "likelihood_of_repeat_usage",
    "dropoff_step",
    "avg_order_value",
    "payment_failures",
    "cross_vertical_usage",
    "time_of_day",
    "location_cluster"
]

def load_dataset(file):
    """Loads a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def validate_dataset(df):
    """Checks if the DataFrame contains all required columns."""
    if df is None:
        return False, "No dataset loaded"
    
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    
    if missing_columns:
        return False, f"Missing columns: {', '.join(missing_columns)}"
    
    return True, "Dataset is valid"

def load_sample_dataset():
    """Loads the sample dataset from the data folder."""
    data_path = os.path.join(os.getcwd(), "data", "careem_dummy_user_behavior_dataset.csv")
    if os.path.exists(data_path):
        return load_dataset(data_path)
    else:
        st.error("Sample dataset not found.")
        return None
