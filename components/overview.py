import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
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
    
    if "global_metrics" in st.session_state:
        metrics = st.session_state["global_metrics"]
        
        st.subheader("Global Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Users", f"{metrics.get('total_users', 0)}")
            st.metric("Avg Order Value", f"${metrics.get('avg_order_value', 0):.2f}")
        with col2:
            st.metric("Avg Sessions/Week", f"{metrics.get('avg_sessions_per_week', 0):.2f}")
            st.metric("Avg Payment Failures", f"{metrics.get('avg_payment_failures', 0):.2f}")
        with col3:
            st.metric("Avg Conversion Prob", f"{metrics.get('avg_probability_of_conversion', 0):.2%}")
            st.metric("Avg Cross-Vertical Usage", f"{metrics.get('avg_cross_vertical_usage', 0):.2f}")
        with col4:
            st.metric("Avg Repeat Usage", f"{metrics.get('avg_likelihood_of_repeat_usage', 0):.2%}")
            
        st.divider()
        
        # User Segments
        if "segment_counts" in st.session_state:
            st.subheader("User Segmentation")
            seg_counts = st.session_state["segment_counts"]
            
            # Create a dataframe for the chart
            seg_df = pd.DataFrame(list(seg_counts.items()), columns=["Segment", "Count"])
            
            fig_seg = px.bar(
                seg_df, 
                x="Segment", 
                y="Count", 
                color="Segment", 
                title="User Counts by Behavioral Segment",
                text="Count"
            )
            fig_seg.update_layout(showlegend=False)
            st.plotly_chart(fig_seg, use_container_width=True)

        st.divider()
        
        c1, c2 = st.columns(2)
        
        # Funnel Analysis
        with c1:
            st.subheader("Funnel Dropoff")
            if "funnel_stats" in st.session_state:
                funnel_df = st.session_state["funnel_stats"]
                if not funnel_df.empty:
                    fig_funnel = px.funnel(
                        funnel_df, 
                        y='Step', 
                        x='Dropoff Count', 
                        title="User Dropoff by Step"
                    )
                    st.plotly_chart(fig_funnel, use_container_width=True)
                else:
                    st.info("No funnel data available.")
        
        # Vertical Performance
        with c2:
            st.subheader("Vertical Performance")
            if "vertical_stats" in st.session_state:
                vert_df = st.session_state["vertical_stats"]
                if not vert_df.empty:
                    fig_vert = px.bar(
                        vert_df, 
                        x="Vertical", 
                        y=["Avg Sessions", "Avg Conv Prob"], 
                        barmode="group",
                        title="Key Metrics by Vertical",
                        labels={"value": "Score", "variable": "Metric"}
                    )
                    st.plotly_chart(fig_vert, use_container_width=True)
                else:
                    st.info("No vertical data available.")

    else:
        st.info("Please upload a dataset or load the sample dataset from the sidebar to view metrics.")
