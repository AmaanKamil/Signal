import streamlit as st

def experiments_page():
    st.title("Experiments")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to design experiments.")
        return

    st.markdown("### 🧪 Experiment Validation")
    st.markdown("A/B tests designed to validate proposed features.")
    
    if "ai_results" in st.session_state:
        ai_experiments = st.session_state["ai_results"].get("ai_experiments", [])
        
        if ai_experiments:
            for exp in ai_experiments:
                st.markdown(f"""
                <div style="border-left: 5px solid #673ab7; background-color: #f3e5f5; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
                    <h4>🧪 {exp.get('hypothesis', 'Hypothesis')}</h4>
                    <p><strong>Design:</strong> {exp.get('test_design', 'A/B Test')}</p>
                    <p><strong>Metrics:</strong> {exp.get('primary_metric', '')} (Primary), {exp.get('secondary_metrics', '')} (Secondary)</p>
                    <p><strong>Audience:</strong> {exp.get('segment', 'All Users')} | <strong>Duration:</strong> {exp.get('duration', '2 weeks')}</p>
                    <p><strong>Success Criteria:</strong> {exp.get('success_criteria', '')}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("AI pipeline ran but produced no experiments.")
            
    else:
        st.info("🤖 Enter your API key and run the AI pipeline to design experiments for your features.")
