import streamlit as st
import plotly.express as px
import pandas as pd

def render_priorities():
    st.title("Strategic Roadmap")
    st.markdown("AI-prioritized initiatives ranked by Impact, Effort, and Confidence.")
    
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return
        
    if st.session_state.get("ai_ready"):
        priorities = st.session_state.get("ai_priorities", [])
    
        if priorities:
            # Scatter Plot: Matrix View
            df = pd.DataFrame(priorities)
            if not df.empty:
                st.subheader("Priority Matrix")
                fig = px.scatter(
                    df, 
                    x="effort_score", 
                    y="final_score", 
                    size="confidence_score", 
                    color="final_score",
                    hover_name="initiative",
                    labels={"effort_score": "Effort (High=Hard)", "final_score": "Priority Score"},
                    title="Impact vs Effort",
                    color_continuous_scale="RdYlGn"
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
            # List View
            st.divider()
            st.subheader("Ranked Initiatives")
            
            sorted_priorities = sorted(priorities, key=lambda x: x.get('rank', 99))
            
            for p in sorted_priorities:
                score = p.get('final_score', 0)
                color = "#2e7d32" if score >= 80 else "#f9a825" if score >= 60 else "#c62828"
                
                st.markdown(f"""
                <div style="background-color: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 5px solid {color};">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h4 style="margin:0;">#{p.get('rank', '-')} {p.get('initiative', 'Initiative')}</h4>
                            <p style="margin:5px 0 0 0; color:#666; font-size:0.9em;">{p.get('rationale', '')}</p>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-size:1.5em; font-weight:bold; color:{color};">{score}</span><br>
                            <span style="font-size:0.8em; color:#888;">Score</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ AI generated no roadmap priorities. Please regenerate.")

    else:
         st.info("🤖 Enter your API key and click 'Generate AI Report' in the sidebar to generate the roadmap.")
