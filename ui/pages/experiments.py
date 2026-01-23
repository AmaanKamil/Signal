import streamlit as st
from ui.components.cards import badge

def render_experiments():
    st.title("Experiment Designs")
    st.markdown("Validation plans for AI-generated features.")
    
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return
        
    if st.session_state.get("ai_generated", False):
        experiments = st.session_state.get("ai_experiments", [])
        
        if experiments:
            st.markdown("### 🧪 Active Designs")
            for exp in experiments:
                st.markdown(f"""
                <div style="background-color: #fff; padding: 20px; border-radius: 8px; border-left: 5px solid #673ab7; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px;">
                    <h4 style="margin:0 0 10px 0; color:#4527a0;">{exp.get('hypothesis', 'Hypothesis')}</h4>
                    
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px; font-size:0.9em; margin-bottom:15px;">
                        <div>
                            <strong>Design:</strong> {exp.get('test_design', 'A/B')} <br>
                            <strong>Duration:</strong> {exp.get('duration', '2w')}
                        </div>
                        <div>
                            <strong>Primary Metric:</strong> {exp.get('primary_metric', '-')} <br>
                            <strong>Target:</strong> {exp.get('segment', 'All')}
                        </div>
                    </div>
                    
                    <div style="background:#f3e5f5; padding:10px; border-radius:4px; font-size:0.85em; color:#4a148c;">
                        <strong>Success Criteria:</strong> {exp.get('success_criteria', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
        else:
            st.info("No experiments designed yet.")

    else:
         st.info("Enter your API key and click 'Generate AI Report' in the sidebar to design experiments.")
