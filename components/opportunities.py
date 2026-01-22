import streamlit as st

def opportunities_page():
    st.title("Opportunities")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to reveal opportunities.")
        return
        
    st.markdown("### 🚀 Growth Opportunities")
    st.markdown("Potential areas for growth and optimization.")
    
    if "intelligence" in st.session_state:
        odds = st.session_state["intelligence"].get("opportunities", [])
        
        if not odds:
            st.info("No specific opportunities identified.")
            
        for item in odds:
            st.markdown(f"""
            <div style="background-color: #e1f5fe; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #0288d1;">
                <h4>{item['title']}</h4>
                <p><strong>Impact:</strong> {item.get('impact', 'Medium')}</p>
                <p>{item['detail']}</p>
                <small>Domain: {item['domain']}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Run the intelligence engine to see opportunities.")
