import json
import os
from openai import OpenAI
from ai.prompt_templates import INSIGHT_PROMPT

def generate_insights(intelligence_summary, api_key):
    """
    Generates AI-powered insights from rule-based intelligence summary.
    """
    if not api_key:
        return []
        
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = INSIGHT_PROMPT.format(intelligence_data=json.dumps(intelligence_summary, indent=2))
        
        response = client.chat.completions.create(
            model="gpt-4o", # Or configurable model
            messages=[
                {"role": "system", "content": "You are a product intelligence AI. Output only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return data.get("insights", [])
        
    except Exception as e:
        print(f"Error generating insights: {e}")
        return []
