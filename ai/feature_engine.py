import json
from openai import OpenAI
from ai.prompt_templates import FEATURE_PROMPT

def generate_features(insights, api_key):
    """
    Generates AI-powered feature concepts from insights.
    """
    if not api_key or not insights:
        return []
        
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = FEATURE_PROMPT.format(insights_data=json.dumps(insights, indent=2))
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a product design AI. Output only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return data.get("features", [])
        
    except Exception as e:
        print(f"Error generating features: {e}")
        return []
