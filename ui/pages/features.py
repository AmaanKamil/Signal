import streamlit as st
from ui.components.cards import feature_card

def render_features():
    st.title("Feature Concepts")
    st.markdown("AI-generated feature proposals to capture opportunities and solve problems.")
    
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return
    
    ai_results = st.session_state.get("ai_results", {})
    ai_features = ai_results.get("ai_features", [])
    
    if ai_features:
        st.markdown("### 🧠 AI Proposals")
        for f in ai_features:
            feature_card(
                f.get('name', 'Feature'),
                f.get('description', ''),
                f.get('expected_impact', 'Medium'),
                f.get('risk_level', 'Medium')
            )
    else:
         st.info("Enter your API key and click 'Generate AI Report' in the sidebar to populate features.")
