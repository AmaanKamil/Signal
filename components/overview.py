import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def overview_page():
    st.title("Overview")
    
    # Product Description Card
    st.markdown("""
    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px;">
        <h3>Product: Signal</h3>
        <p>Signal is an internal analytics tool designed to transform raw user behavior data into actionable product decisions. 
        It aggregates metrics, identifies friction points, and helps prioritize roadmap items based on data.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if "dataset" in st.session_state:
        df = st.session_state["dataset"]
        
        st.subheader("Dataset Summary")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Total Users", len(df))
        with col2:
            st.metric("Avg Sessions/Week", f"{df['sessions_per_week'].mean():.2f}")
        with col3:
            st.metric("Avg Conversion Prob", f"{df['probability_of_conversion'].mean():.2%}")
        with col4:
            st.metric("Avg Repeat Usage", f"{df['likelihood_of_repeat_usage'].mean():.2%}")
        with col5:
            st.metric("Avg Order Value", f"${df['avg_order_value'].mean():.2f}")
            
        st.divider()
        
        # Simple Charts
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("User Distribution by Vertical")
            vertical_counts = df['vertical'].value_counts()
            fig_vertical = go.Figure(data=[go.Pie(labels=vertical_counts.index, values=vertical_counts.values, hole=.3)])
            fig_vertical.update_layout(margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig_vertical, use_container_width=True)
            
        with c2:
            st.subheader("Conversion Probability Distribution")
            fig_hist = go.Figure(data=[go.Histogram(x=df['probability_of_conversion'], nbinsx=20)])
            fig_hist.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="Probability", yaxis_title="Count")
            st.plotly_chart(fig_hist, use_container_width=True)

    else:
        st.info("Please upload a dataset or load the sample dataset from the sidebar to view metrics.")
