import json
from openai import OpenAI
from ai.prompt_templates import EXPERIMENT_PROMPT

def generate_experiments(features, api_key):
    """
    Generates AI-designed experiments from features.
    """
    if not api_key or not features:
        return []
        
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = EXPERIMENT_PROMPT.format(features_data=json.dumps(features, indent=2))
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an experimentation AI. Output only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return data.get("experiments", [])
        
    except Exception as e:
        print(f"Error generating experiments: {e}")
        return []
