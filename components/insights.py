import streamlit as st

def insights_page():
    st.title("Insights")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to generate insights.")
        return

    st.markdown("### 💡 Key Insights")
    st.markdown("Automated insights derived from user behavior patterns.")
    
    # Placeholder structured output
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #00c853;">
        <strong>High Value Cohort:</strong> Users in the 'Food' vertical with >3 sessions/week have a 40% higher conversion probability.
    </div>
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #ffab00;">
        <strong>Drop-off Alert:</strong> Significant drop-off observed at the 'Payment' step for users in 'Ride Hailing'.
    </div>
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #2962ff;">
        <strong>Cross-sell Opportunity:</strong> High correlation between 'Grocery' and 'Food' usage during evening hours.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("*(AI integration for dynamic insight generation pending)*")
