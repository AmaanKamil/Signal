import streamlit as st
import plotly.express as px
import pandas as pd
from ui.components.cards import metric_card, insight_card

def render_overview():
    """
    Renders the Executive Product Health Dashboard.
    """
    st.title("Product Health Dashboard")
    st.markdown("High-level signals on ecosystem performance and behavioral health.")
    
    if "dataset" not in st.session_state:
        st.info("Please load a dataset to view the dashboard.")
        return

    metrics = st.session_state.get("global_metrics", {})
    intelligence = st.session_state.get("intelligence", {})
    
    # 1. Product Health Strip
    st.subheader("Signal Vitals")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        metric_card("Active Users", metrics.get('total_users', 0), "Total analyzed")
    with c2:
        metric_card("Engagement", f"{metrics.get('avg_sessions_per_week', 0):.1f}", "Sessions / Week")
    with c3:
        metric_card("Conversion", f"{metrics.get('avg_probability_of_conversion', 0):.1%}", "Avg Probability")
    with c4:
        metric_card("Retention", f"{metrics.get('avg_likelihood_of_repeat_usage', 0):.1%}", "Repeat Likelihood")

    st.divider()
    
    # 2. Intelligence Snapshot
    col_intel, col_charts = st.columns([1, 2])
    
    with col_intel:
        st.subheader("Risk & Opportunity Radar")
        
        # Display top 2 critical problems
        problems = intelligence.get("problems", [])
        if problems:
            st.markdown("#### 🚨 Top Risks")
            for p in problems[:2]:
                insight_card(p['title'], p['detail'], p['domain'], p['severity'], "Detected by Signal")
        
        # Display top 2 opportunities
        opps = intelligence.get("opportunities", [])
        if opps:
            st.markdown("#### 🚀 Top Opportunities")
            for o in opps[:2]:
                insight_card(o['title'], o['detail'], o['domain'], "growth", "Detected by Signal")
                
    with col_charts:
        st.subheader("Ecosystem Composition")
        
        if "segment_counts" in st.session_state:
            seg_counts = st.session_state["segment_counts"]
            seg_df = pd.DataFrame(list(seg_counts.items()), columns=["Segment", "Count"])
            
            fig = px.bar(
                seg_df, 
                x="Count", 
                y="Segment", 
                orientation='h', 
                color="Count",
                color_continuous_scale="Blues",
                title="User Behavior Segments"
            )
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
