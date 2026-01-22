import streamlit as st

def features_page():
    st.title("Features")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to view feature suggestions.")
        return

    st.markdown("### ✨ Proposed Features")
    st.markdown("New feature concepts to address problems and capture opportunities.")
    
    # Placeholder structured output
    st.markdown("""
    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;">
        <h3>Feature: 'One-Tap Reorder'</h3>
        <p><strong>Type:</strong> UI Interaction</p>
        <p><strong>Rationale:</strong> Reduces friction for high-frequency users who repeat the same orders.</p>
        <p><strong>Expected Outcome:</strong> 15% increase in repeat order frequency.</p>
        <hr>
        <small>Status: Draft | Priority: High</small>
    </div>

    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;">
        <h3>Feature: 'Smart Commute' Bundle</h3>
        <p><strong>Type:</strong> New Product Offering</p>
        <p><strong>Rationale:</strong> Targets daily commuters with a discounted ride pack.</p>
        <p><strong>Expected Outcome:</strong> Increase LTV (Life Time Value) of commuter segment.</p>
        <hr>
        <small>Status: Concept | Priority: Medium</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("*(AI integration for feature brainstorming pending)*")
