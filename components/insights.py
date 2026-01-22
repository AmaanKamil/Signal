import streamlit as st

def insights_page():
    st.title("Insights")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to generate insights.")
        return

    st.markdown("### 💡 Key Insights")
    st.markdown("Automated insights derived from behavioral patterns.")
    
    if "intelligence" in st.session_state:
        insights = st.session_state["intelligence"].get("insights", [])
        
        if not insights:
            st.info("No specific insights detected in the current dataset.")
        
        for item in insights:
            # Color coding based on severity (conceptually inverted for insights, green is good)
            color = "#00c853" # Green
            
            st.markdown(f"""
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid {color};">
                <strong>{item['title']}</strong><br>
                <span style="font-size: 0.9em; color: #555;">{item['detail']}</span><br>
                <small style="color: #888;">Domain: {item['domain']}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Run the intelligence engine to see insights.")
