import json
from openai import OpenAI
from ai.prompt_templates import PRIORITY_PROMPT

def generate_priorities(features, experiments, api_key):
    """
    Generates a prioritized roadmap from features and experiments.
    """
    if not api_key or (not features and not experiments):
        return []
        
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = PRIORITY_PROMPT.format(
            features_data=json.dumps(features, indent=2),
            experiments_data=json.dumps(experiments, indent=2)
        )
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a product strategy AI. Output only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return data.get("priorities", [])
        
    except Exception as e:
        print(f"Error generating priorities: {str(e)}")
        # Return empty list on failure to prevent pipeline crash
        return []
