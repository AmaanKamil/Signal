import pandas as pd

def get_funnel_stats(df):
    """
    Computes funnel dropoff statistics.
    """
    if df is None or df.empty:
        return pd.DataFrame()
        
    # Count users at each dropoff step
    dropoff_counts = df["dropoff_step"].value_counts().reset_index()
    dropoff_counts.columns = ["Step", "Dropoff Count"]
    
    # Enhance with avg conversion probability for users dropping off at this step
    step_metrics = df.groupby("dropoff_step")["probability_of_conversion"].mean().reset_index()
    step_metrics.columns = ["Step", "Avg Conversion Prob"]
    
    funnel_stats = pd.merge(dropoff_counts, step_metrics, on="Step")
    
    # Sort logically if possible, otherwise by count
    # Ideally, we'd have a mapping of step order. For now, we sort by count descending (biggest leakage first)
    funnel_stats = funnel_stats.sort_values("Dropoff Count", ascending=False)
    
    return funnel_stats

def get_vertical_stats(df):
    """
    Aggregates key metrics by vertical.
    """
    if df is None or df.empty:
        return pd.DataFrame()
        
    vertical_stats = df.groupby("vertical").agg({
        "user_id": "count",
        "sessions_per_week": "mean",
        "probability_of_conversion": "mean",
        "likelihood_of_repeat_usage": "mean",
        "avg_order_value": "mean"
    }).reset_index()
    
    vertical_stats.columns = [
        "Vertical", "Users", "Avg Sessions", "Avg Conv Prob", "Avg Repeat Prob", "Avg Order Value"
    ]
    
    return vertical_stats

def get_contextual_stats(df):
    """
    Aggregates metrics by Time of Day and Location Cluster.
    """
    if df is None or df.empty:
        return {}, {}
        
    time_stats = df.groupby("time_of_day").agg({
        "probability_of_conversion": "mean",
        "sessions_per_week": "mean"
    }).reset_index()
    
    location_stats = df.groupby("location_cluster").agg({
        "avg_order_value": "mean",
        "sessions_per_week": "mean"
    }).reset_index()
    
    return time_stats, location_stats
