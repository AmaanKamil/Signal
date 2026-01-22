import streamlit as st
from ui.components.cards import insight_card

def render_opportunities():
    st.title("Growth Opportunities")
    st.markdown("Strategic areas for acquisition, monetization, and ecosystem growth.")
    
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return
        
    intelligence = st.session_state.get("intelligence", {})
    opps = intelligence.get("opportunities", [])
    
    if not opps:
        st.info("No specific opportunities available.")
        return
        
    # Group by impact
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("High Impact")
        high_opps = [o for o in opps if str(o.get('impact', '')).lower() == 'high']
        if high_opps:
            for o in high_opps:
                 insight_card(o['title'], o['detail'], o['domain'], 'Growth', "Signal Intelligence")
        else:
            st.info("None detected.")

    with c2:
        st.subheader("Medium Impact")
        med_opps = [o for o in opps if str(o.get('impact', '')).lower() != 'high']
        if med_opps:
            for o in med_opps:
                 insight_card(o['title'], o['detail'], o['domain'], 'Growth', "Signal Intelligence")
        else:
            st.info("None detected.")
