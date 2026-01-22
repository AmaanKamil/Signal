import streamlit as st
from ai.insight_engine import generate_insights
from ai.feature_engine import generate_features
from ai.experiment_engine import generate_experiments
from ai.priority_engine import generate_priorities

def run_signal_ai_pipeline(intelligence_summary, api_key):
    """
    Orchestrates the full AI pipeline:
    Intelligence -> Insights -> Features -> Experiments -> Priorities
    """
    results = {
        "ai_insights": [],
        "ai_features": [],
        "ai_experiments": [],
        "ai_priorities": []
    }
    
    if not api_key:
        return results, "API Key missing. AI pipeline skipped."

    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Step 1: Generate Insights
        status_text.text("AI: Analyzing intelligence patterns...")
        ai_insights = generate_insights(intelligence_summary, api_key)
        results["ai_insights"] = ai_insights
        progress_bar.progress(25)
        
        # Step 2: Generate Features
        status_text.text("AI: Ideating features...")
        ai_features = generate_features(ai_insights, api_key)
        results["ai_features"] = ai_features
        progress_bar.progress(50)
        
        # Step 3: Generate Experiments
        status_text.text("AI: Designing experiments...")
        ai_experiments = generate_experiments(ai_features, api_key)
        results["ai_experiments"] = ai_experiments
        progress_bar.progress(75)
        
        # Step 4: Prioritize
        status_text.text("AI: Prioritizing roadmap...")
        ai_priorities = generate_priorities(ai_features, ai_experiments, api_key)
        results["ai_priorities"] = ai_priorities
        progress_bar.progress(100)
        
        status_text.text("AI processing complete!")
        return results, "Success"
        
    except Exception as e:
        return results, f"AI Pipeline Error: {str(e)}"
    finally:
        progress_bar.empty()
