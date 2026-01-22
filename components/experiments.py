import streamlit as st

def experiments_page():
    st.title("Experiments")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to design experiments.")
        return

    st.markdown("### 🧪 Experiment Validation")
    st.markdown("A/B tests designed to validate proposed features.")
    
    # Placeholder structured output
    st.markdown("""
    <div style="border-left: 5px solid #673ab7; background-color: #f3e5f5; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
        <h4>Experiment: Reorder Button Placement</h4>
        <p><strong>Hypothesis:</strong> Placing the reorder button on the home screen will increase reorders by 10%.</p>
        <p><strong>Metrics:</strong> Reorder Rate, Click-Through Rate</p>
        <p><strong>Audience:</strong> 10% of Active User Base</p>
        <p><strong>Duration:</strong> 2 Weeks</p>
    </div>

    <div style="border-left: 5px solid #673ab7; background-color: #f3e5f5; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
        <h4>Experiment: Commute Bundle Pricing</h4>
        <p><strong>Hypothesis:</strong> A price point of $50/month for the commuter bundle maximizes revenue compared to $45 or $55.</p>
        <p><strong>Metrics:</strong> Conversion Rate, Revenue per User</p>
        <p><strong>Audience:</strong> Users with >10 rides/week</p>
        <p><strong>Duration:</strong> 1 Month</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("*(AI integration for experiment design pending)*")
