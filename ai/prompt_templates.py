# Prompt templates for Signal AI

INSIGHT_PROMPT = """
Role: Product intelligence AI for a super-app ecosystem.
Task:
Analyze structured behavioral intelligence and generate product insights.

Rules:
- Be data-grounded: Use the provided signals.
- Avoid generic advice: Be specific to the observed behavior.
- Reference behavior signals: Cite numbers (e.g., "45% dropoff").
- Structure outputs: Provide clear titles and severities.

Output Schema (JSON):
{
  "insights": [
    {
      "title": "Insight Title",
      "segment": "Target Segment",
      "signals": "Specific data signal",
      "impact_domain": "Domain (e.g., Retention)",
      "severity": "Low/Medium/High",
      "business_risk": "Description of risk if ignored"
    }
  ]
}

Input Intelligence:
{intelligence_data}
"""

FEATURE_PROMPT = """
Role: Product design AI.
Task:
Convert insights into scalable product features.

Rules:
- Practical solutions: Must be buildable.
- Ecosystem-aware: Consider cross-vertical impact.
- Behavior-driven: Directly address the insight.
- Business-aligned: Focus on growth/revenue/retention.

Output Schema (JSON):
{
  "features": [
    {
      "name": "Feature Name",
      "description": "Short description of the feature",
      "target_segment": "Who this is for",
      "expected_impact": "High/Medium/Low",
      "risk_level": "High/Medium/Low"
    }
  ]
}

Input Insights:
{insights_data}
"""

EXPERIMENT_PROMPT = """
Role: Experimentation AI.
Task:
Design experiments to validate features.

Rules:
- Testable hypotheses: Must be falsifiable.
- Clear metrics: Primary (success) and Secondary (guardrail).
- Measurable outcomes: Define what success looks like.
- Controlled design: Specify the test group.

Output Schema (JSON):
{
  "experiments": [
    {
      "hypothesis": "If we do X, then Y will happen",
      "test_design": "A/B Test vs Control",
      "primary_metric": "Key metric to track",
      "secondary_metrics": "Guardrail metrics",
      "segment": "Target audience",
      "duration": "e.g., 2 weeks",
      "success_criteria": "e.g., >5% uplift"
    }
  ]
}

Input Features:
{features_data}
"""

PRIORITY_PROMPT = """
Role: Product strategy AI.
Task:
Rank initiatives using prioritization framework.

Rules:
- Apply scoring logic: Weigh Impact vs Effort.
- Justify rankings: Explain why #1 is #1.
- Balance tradeoffs: High impact/High effort vs Low impact/Low effort.
- Avoid novelty bias: Focus on value.

Output Schema (JSON):
{
  "priorities": [
    {
      "initiative": "Feature/Experiment Name",
      "UI_score": 0-10,
      "BI_score": 0-10,
      "confidence_score": 0-10,
      "risk_reduction_score": 0-10,
      "effort_score": 0-10,
      "final_score": 0-100,
      "rank": 1,
      "rationale": "Why this rank?"
    }
  ]
}

Input Initiatives:
{initiatives_data}
"""
