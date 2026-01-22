from utils.patterns import (
    detect_engagement_patterns,
    detect_conversion_patterns,
    detect_retention_patterns,
    detect_funnel_patterns,
    detect_ecosystem_patterns
)
from utils.interpreter import interpret_patterns

def aggregate_intelligence(df):
    """
    Orchestrates pattern detection and interpretation.
    """
    all_patterns = []
    
    # Collect all patterns
    all_patterns.extend(detect_engagement_patterns(df))
    all_patterns.extend(detect_conversion_patterns(df))
    all_patterns.extend(detect_retention_patterns(df))
    all_patterns.extend(detect_funnel_patterns(df))
    all_patterns.extend(detect_ecosystem_patterns(df))
    
    # Interpret patterns into actionable intelligence
    intelligence = interpret_patterns(all_patterns)
    
    return intelligence
