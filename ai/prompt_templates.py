# Prompt templates for Signal AI

INSIGHT_PROMPT = """
Analyze the following user behavior intelligence data and identifying strategic product insights.

INTELLIGENCE DATA:
{intelligence_data}

INSTRUCTIONS:
1. Identify 3-5 distinct strategic insights (risks, opportunities, or patterns).
2. For each insight, provide a title, detailed explanation (signals), potential business risk, impact domain (Retention, Monetization, etc.), and severity.
3. OUTPUT MUST BE STRICT VALID JSON ONLY.
4. DO NOT use markdown code blocks (```json).
5. DO NOT include any text outside the JSON.

JSON STRUCTURE:
{{
    "insights": [
        {{
            "title": "Insight Title",
            "signals": "Explanation of the pattern observed...",
            "business_risk": "What happens if we ignore this?",
            "impact_domain": "Retention",
            "severity": "High"
        }}
    ]
}}
"""

FEATURE_PROMPT = """
Based on the following strategic insights, brainstorm 3-5 concrete product features to address them.

INSIGHTS:
{insights_data}

INSTRUCTIONS:
1. Propose features that directly solve the identified risks or capture opportunities.
2. For each feature, provide a name, description, expected impact (High/Medium/Low), risk level, and target segment.
3. OUTPUT MUST BE STRICT VALID JSON ONLY.
4. DO NOT use markdown code blocks.
5. DO NOT include any text outside the JSON.

JSON STRUCTURE:
{{
    "features": [
        {{
            "name": "Feature Name",
            "description": "What is the feature and how does it work?",
            "expected_impact": "High",
            "risk_level": "Low",
            "target_segment": "All Users"
        }}
    ]
}}
"""

EXPERIMENT_PROMPT = """
Design A/B validation experiments for the following new feature concepts.

FEATURES:
{features_data}

INSTRUCTIONS:
1. Design one validation experiment for each feature features.
2. Define the hypothesis, test design (A/B, Fake Door, etc.), primary metric, and success criteria.
3. OUTPUT MUST BE STRICT VALID JSON ONLY.
4. DO NOT use markdown code blocks.
5. DO NOT include any text outside the JSON.

JSON STRUCTURE:
{{
    "experiments": [
        {{
            "feature_name": "Feature Name",
            "hypothesis": "If we do X, then Y will happen...",
            "test_design": "A/B Test",
            "primary_metric": "Conversion Rate",
            "segment": "New Users",
            "duration": "2 weeks",
            "success_criteria": "5% uplift in conversion"
        }}
    ]
}}
"""

PRIORITY_PROMPT = """
Act as a Head of Product. Prioritize the following initiatives based on Impact, Confidence, and Ease (ICE framework).

FEATURES:
{features_data}

EXPERIMENTS:
{experiments_data}

INSTRUCTIONS:
1. Score each initiative on Impact (1-10), Confidence (1-10), and Effort (1-10, where 10 is hardest, so inverse for score).
2. Calculate a final priority score (0-100).
3. Provide a brief rationale.
4. OUTPUT MUST BE STRICT VALID JSON ONLY.
5. DO NOT use markdown code blocks.
6. DO NOT include any text outside the JSON.

JSON STRUCTURE:
{{
    "priorities": [
        {{
            "initiative": "Feature Name",
            "rank": 1,
            "final_score": 85,
            "impact_score": 9,
            "confidence_score": 8,
            "effort_score": 5,
            "rationale": "High impact but medium effort..."
        }}
    ]
}}
"""
