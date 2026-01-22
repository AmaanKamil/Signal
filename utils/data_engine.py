import pandas as pd
import streamlit as st

def process_data(df):
    """
    Cleans, normalizes, and type-casts the raw dataframe.
    """
    try:
        # Create a copy to avoid SettingWithCopyWarning
        processed_df = df.copy()
        
        # Standardize column names (lowercase, strip whitespace)
        processed_df.columns = [col.lower().strip() for col in processed_df.columns]
        
        # Fill missing numeric values with 0
        numeric_cols = [
            "sessions_per_week", 
            "probability_of_conversion", 
            "likelihood_of_repeat_usage", 
            "avg_order_value", 
            "payment_failures",
            "cross_vertical_usage"
        ]
        
        for col in numeric_cols:
            if col in processed_df.columns:
                processed_df[col] = pd.to_numeric(processed_df[col], errors='coerce').fillna(0)
                
        # Fill missing text values with 'Unknown'
        text_cols = ["vertical", "dropoff_step", "time_of_day", "location_cluster"]
        for col in text_cols:
             if col in processed_df.columns:
                 processed_df[col] = processed_df[col].fillna("Unknown")

        return processed_df
    except Exception as e:
        st.error(f"Error processing data: {e}")
        return df

def get_global_metrics(df):
    """
    Computes high-level aggregated metrics from the dataframe.
    """
    if df is None or df.empty:
        return {}
        
    metrics = {
        "total_users": len(df),
        "avg_sessions_per_week": df["sessions_per_week"].mean(),
        "avg_probability_of_conversion": df["probability_of_conversion"].mean(),
        "avg_likelihood_of_repeat_usage": df["likelihood_of_repeat_usage"].mean(),
        "avg_order_value": df["avg_order_value"].mean(),
        "avg_payment_failures": df["payment_failures"].mean(),
        "avg_cross_vertical_usage": df["cross_vertical_usage"].mean()
    }
    return metrics
