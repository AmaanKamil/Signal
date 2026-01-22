import streamlit as st

def features_page():
    st.title("Features")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to view feature suggestions.")
        return

    st.markdown("### ✨ Proposed Features")
    st.markdown("New feature concepts to address problems and capture opportunities.")
    
    # Check for AI results
    if "ai_results" in st.session_state:
        ai_features = st.session_state["ai_results"].get("ai_features", [])
        
        if ai_features:
            for f in ai_features:
                st.markdown(f"""
                <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; border-top: 5px solid #2196f3;">
                    <h3>{f.get('name', 'Feature')}</h3>
                    <p>{f.get('description', '')}</p>
                    <p><strong>Target Segment:</strong> {f.get('target_segment', 'All Users')}</p>
                    <div style="display:flex; justify-content:space-between; margin-top:10px;">
                        <span>Impact: <strong>{f.get('expected_impact', 'Medium')}</strong></span>
                        <span>Risk: <strong>{f.get('risk_level', 'Medium')}</strong></span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("AI pipeline ran but produced no features.")
            
    else:
        # Fallback to placeholders or empty state instructions
        st.info("🤖 Enter your API key and run the AI pipeline to generate feature ideas based on your data.")
        
        # Keep placeholders visible for demo purposes if verified user wants them, 
        # but the prompt implies we want AI content. I'll leave one static placeholder as an example.
        st.markdown("""
        <div style="opacity: 0.6; filter: grayscale(1);">
            <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px;">
                <h3>Example Feature: 'One-Tap Reorder'</h3>
                <p>Reduces friction for high-frequency users who repeat the same orders.</p>
                <small>(Generate AI Report to replace this with real data-driven ideas)</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
