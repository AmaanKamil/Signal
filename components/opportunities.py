import streamlit as st

def opportunities_page():
    st.title("Opportunities")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to reveal opportunities.")
        return
        
    st.markdown("### 🚀 Growth Opportunities")
    st.markdown("Potential areas for growth and optimization based on user behavior.")
    
    # Placeholder structured output
    st.markdown("""
    <div style="background-color: #f0f4c3; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #afb42b;">
        <h4>Opportunity: Subscription Upsell</h4>
        <p><strong>Potential Impact:</strong> High</p>
        <p><strong>Insight:</strong> Users with high frequency (>5 rides/week) and high average spend are prime candidates for the 'Careem Plus' subscription.</p>
        <p><strong>Action:</strong> Target this segment with a free 1-month trial offer.</p>
    </div>
    
    <div style="background-color: #e1f5fe; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #0288d1;">
        <h4>Opportunity: Food & Ride Synergy</h4>
        <p><strong>Potential Impact:</strong> Medium</p>
        <p><strong>Insight:</strong> 30% of users who book a ride home between 6-8 PM order food within 30 minutes.</p>
        <p><strong>Action:</strong> Implement 'Order Food' prompt on ride completion screen during evening hours.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("*(AI integration for opportunity generation pending)*")
