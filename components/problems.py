import streamlit as st

def problems_page():
    st.title("Problems")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to identify problems.")
        return

    st.markdown("### ⚠️ Identified Problems")
    st.markdown("Critical friction points detected in the user journey.")
    
    if "intelligence" in st.session_state:
        problems = st.session_state["intelligence"].get("problems", [])
        
        if not problems:
            st.success("No critical problems detected!")
            
        for item in problems:
            severity = item.get('severity', 'Medium').lower()
            
            color = "#d32f2f" if severity == "critical" else "#ffa000" if severity == "high" else "#fbc02d"
            
            st.markdown(f"""
            <div style="background-color: #fff5f5; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid {color};">
                <h4>{item['title']}</h4>
                <p><strong>Severity:</strong> {item['severity']}</p>
                <p>{item['detail']}</p>
                <small>Domain: {item['domain']}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Run the intelligence engine to see problems.")
