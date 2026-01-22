import streamlit as st
from ui.components.cards import insight_card

def render_problems():
    st.title("Problem Clusters")
    st.markdown("Critical friction points categorized by severity and domain.")
    
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return
        
    intelligence = st.session_state.get("intelligence", {})
    problems = intelligence.get("problems", [])
    
    if not problems:
        st.success("No critical problems detected.")
        return
        
    # Cluster by Severity
    critical = [p for p in problems if str(p.get('severity')).lower() == 'critical']
    high = [p for p in problems if str(p.get('severity')).lower() == 'high']
    medium = [p for p in problems if str(p.get('severity')).lower() in ['medium', 'low']]
    
    if critical:
        st.subheader(f"🚨 Critical Issues ({len(critical)})")
        for p in critical:
            insight_card(p['title'], p['detail'], p['domain'], 'Critical', "Signal Intelligence")
            
    if high:
        st.divider()
        st.subheader(f"⚠️ High Priority ({len(high)})")
        for p in high:
            insight_card(p['title'], p['detail'], p['domain'], 'High', "Signal Intelligence")
            
    if medium:
        st.divider()
        st.subheader(f"Constructive Issues ({len(medium)})")
        for p in medium:
            insight_card(p['title'], p['detail'], p['domain'], 'Medium', "Signal Intelligence")
