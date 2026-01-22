import pandas as pd

def get_segments(df):
    """
    Creates dynamic user segments based on behavioral data.
    Returns a dictionary where keys are segment names and values are user counts (or sub-dataframes if needed later).
    """
    if df is None or df.empty:
        return {}
    
    segments = {}
    
    # Engagement Segments
    segments["High Engagement"] = df[df["sessions_per_week"] > 10]
    segments["Low Engagement"] = df[df["sessions_per_week"] < 3]
    
    # Conversion Segments
    segments["High Conversion Propensity"] = df[df["probability_of_conversion"] > 0.6]
    segments["Low Conversion Propensity"] = df[df["probability_of_conversion"] < 0.3]
    
    # Retention
    segments["Loyal Users"] = df[df["likelihood_of_repeat_usage"] > 0.7]
    segments["Churn Risk"] = df[df["likelihood_of_repeat_usage"] < 0.3]
    
    # Value
    median_aov = df["avg_order_value"].median()
    segments["High Value Users"] = df[df["avg_order_value"] > median_aov]
    
    # Ecosystem Depth
    segments["Single Vertical Users"] = df[df["cross_vertical_usage"] == 1]
    segments["Ecosystem Users"] = df[df["cross_vertical_usage"] >= 3]
    
    return segments

def get_segment_counts(segments):
    """Returns a dictionary of segment names and their counts."""
    return {k: len(v) for k, v in segments.items()}
