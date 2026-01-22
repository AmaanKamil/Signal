import streamlit as st

def problems_page():
    st.title("Problems")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to identify problems.")
        return

    st.markdown("### ⚠️ Identified Problems")
    st.markdown("Critical friction points detected in the user journey.")
    
    # Placeholder structured output
    st.markdown("""
    <div style="background-color: #fff5f5; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #d32f2f;">
        <h4>Problem: High Cart Abandonment</h4>
        <p><strong>Severity:</strong> High</p>
        <p><strong>Description:</strong> 45% of users in the 'New User' segment abandon cart at the payment details screen.</p>
        <p><strong>Impact:</strong> Estimated $15k weekly revenue loss.</p>
    </div>
    
    <div style="background-color: #fff5f5; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #ffa000;">
        <h4>Problem: Low Retention in Quick Commerce</h4>
        <p><strong>Severity:</strong> Medium</p>
        <p><strong>Description:</strong> Users who experience a delivery delay >10 mins on their first order have a 60% lower likelihood of repeat usage.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("*(AI integration for dynamic problem detection pending)*")
