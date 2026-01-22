import streamlit as st
from ui.components.cards import insight_card

def render_insights():
    st.title("Strategic Insights")
    st.markdown("Deep dive into behavioral patterns and strategic signals.")
    
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return
        
    # Controls
    c1, c2 = st.columns([3, 1])
    with c2:
        source_filter = st.multiselect("Source", ["Rule-based", "AI"], default=["Rule-based", "AI"])
        
    st.divider()
    
    # Collect Insights
    all_insights = []
    
    # Rules
    if "Rule-based" in source_filter and "intelligence" in st.session_state:
        for i in st.session_state["intelligence"].get("insights", []):
            i['source'] = 'Rule-based'
            all_insights.append(i)
            
    # AI
    if "AI" in source_filter and "ai_results" in st.session_state:
        for i in st.session_state["ai_results"].get("ai_insights", []):
            # Normalizing AI structure to fit card
            all_insights.append({
                'title': i.get('title', 'AI Insight'),
                'detail': f"{i.get('signals', '')}\n\nRisk: {i.get('business_risk', '')}",
                'domain': i.get('impact_domain', 'Strategy'),
                'severity': i.get('severity', 'Medium'),
                'source': 'AI Engine'
            })
            
    if not all_insights:
        st.info("No insights found for selected filters.")
        return
        
    # Render grid
    for insight in all_insights:
        insight_card(
            insight['title'],
            insight['detail'],
            insight['domain'],
            insight['severity'],
            insight['source']
        )
