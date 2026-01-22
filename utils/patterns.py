import pandas as pd

def detect_engagement_patterns(df):
    """Detects high and low engagement patterns."""
    patterns = []
    
    # High Engagement
    high_engagement = df[df["sessions_per_week"] > 10]
    if not high_engagement.empty:
        patterns.append({
            "pattern_type": "high_engagement",
            "segment": "Power Users",
            "signals": [f"{len(high_engagement)} users have > 10 sessions/week"],
            "severity": "low", # Positive signal
            "impact_domain": "retention"
        })

    # Low Engagement (Churn Risk)
    low_engagement = df[df["sessions_per_week"] < 2]
    if not low_engagement.empty:
        patterns.append({
            "pattern_type": "low_engagement",
            "segment": "Inactive Users",
            "signals": [f"{len(low_engagement)} users have < 2 sessions/week"],
            "severity": "high",
            "impact_domain": "retention"
        })
        
    return patterns

def detect_conversion_patterns(df):
    """Detects friction and conversion issues."""
    patterns = []
    
    # High Friction (High Sessions, Low Conversion)
    friction = df[(df["sessions_per_week"] > 5) & (df["probability_of_conversion"] < 0.2)]
    if not friction.empty:
        patterns.append({
            "pattern_type": "friction",
            "segment": "Frustrated Users",
            "signals": [f"{len(friction)} users browse often but rarely convert"],
            "severity": "high",
            "impact_domain": "monetization"
        })
        
    return patterns

def detect_retention_patterns(df):
    """Detects retention risks or loyalty."""
    patterns = []
    
    # Loyal Users
    loyal = df[df["likelihood_of_repeat_usage"] > 0.8]
    if not loyal.empty:
        patterns.append({
            "pattern_type": "loyalty",
            "segment": "Champions",
            "signals": [f"{len(loyal)} users are highly likely to repeat"],
            "severity": "low",
            "impact_domain": "growth"
        })
        
    return patterns

def detect_funnel_patterns(df):
    """Detects specific step dropoffs."""
    patterns = []
    
    # Payment Failures
    payment_fails = df[df["payment_failures"] > 0]
    if not payment_fails.empty:
        total_failures = payment_fails["payment_failures"].sum()
        patterns.append({
            "pattern_type": "trust_breakdown",
            "segment": "Affected by Errors",
            "signals": [f"Processed {total_failures} payment failures across user base"],
            "severity": "critical",
            "impact_domain": "reliability"
        })
        
    # Dropoff Analysis (Simplified)
    # Finding the most common dropoff step
    if "dropoff_step" in df.columns:
        most_common_dropoff = df["dropoff_step"].mode()[0]
        count = len(df[df["dropoff_step"] == most_common_dropoff])
        patterns.append({
            "pattern_type": "funnel_leak",
            "segment": "All Users",
            "signals": [f"Major dropoff at '{most_common_dropoff}' step ({count} users)"],
            "severity": "high",
            "impact_domain": "conversion"
        })
        
    return patterns

def detect_ecosystem_patterns(df):
    """Detects cross-vertical usage patterns."""
    patterns = []
    
    # Single Vertical Users (Growth Opp)
    single_vertical = df[df["cross_vertical_usage"] == 1]
    if not single_vertical.empty:
        patterns.append({
            "pattern_type": "siloed_usage",
            "segment": "Single Service Users",
            "signals": [f"{len(single_vertical)} users only use one vertical"],
            "severity": "medium",
            "impact_domain": "ecosystem"
        })
        
    return patterns
