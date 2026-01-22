def interpret_patterns(patterns):
    """
    Maps raw patterns to structured Intelligence Objects.
    Returns lists of insights, problems, and opportunities.
    """
    insights = []
    problems = []
    opportunities = []
    
    for p in patterns:
        p_type = p["pattern_type"]
        signals = "; ".join(p["signals"])
        
        # High Engagement -> Insight & Opportunity
        if p_type == "high_engagement":
            insights.append({
                "title": "Strong Power User Base",
                "detail": signals,
                "domain": "Retention",
                "severity": "low"
            })
            opportunities.append({
                "title": "Launch Loyalty Program",
                "detail": "Target power users with exclusive rewards to lock in loyalty.",
                "domain": "Monetization",
                "impact": "High"
            })
            
        # Low Engagement -> Problem & Opportunity
        elif p_type == "low_engagement":
            problems.append({
                "title": "High Dormancy Rate",
                "detail": signals,
                "domain": "Retention",
                "severity": "High"
            })
            opportunities.append({
                "title": "Re-engagement Campaign",
                "detail": "Target inactive users with push notifications or discounts.",
                "domain": "Growth",
                "impact": "Medium"
            })
            
        # Friction -> Problem
        elif p_type == "friction":
            problems.append({
                "title": "Browsing without Buying",
                "detail": f"Users are exploring but not verifying. {signals}",
                "domain": "Conversion",
                "severity": "High"
            })
            opportunities.append({
                "title": "Simplify Checkout Flow",
                "detail": "Reduce steps or offer guest checkout to improve conversion.",
                "domain": "Conversion",
                "impact": "High"
            })

        # Trust Breakdown -> Critical Problem
        elif p_type == "trust_breakdown":
             problems.append({
                "title": "Payment Reliability Issues",
                "detail": signals,
                "domain": "Reliability",
                "severity": "Critical"
            })
            
        # Funnel Leak -> Problem
        elif p_type == "funnel_leak":
            problems.append({
                "title": "Funnel Leakage",
                "detail": signals,
                "domain": "Conversion",
                "severity": "High"
            })
            
        # Siloed Usage -> Opportunity
        elif p_type == "siloed_usage":
            opportunities.append({
                "title": "Cross-Sell Campaign",
                "detail": "Encourage single-vertical users to try a second service (e.g., Ride -> Food).",
                "domain": "Ecosystem",
                "impact": "High"
            })
            insights.append({
                "title": "Ecosystem Untapped Potential",
                "detail": signals,
                "domain": "Growth",
                "severity": "medium"
            })

    return {
        "insights": insights,
        "problems": problems,
        "opportunities": opportunities
    }
