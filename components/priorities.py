import streamlit as st

def priorities_page():
    st.title("Priorities")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to see prioritization.")
        return

    st.markdown("### 📋 AI-Ranked Roadmap")
    st.markdown("Initiatives ranked by the AI Priority Engine based on impact, confidence, and effort.")
    
    if "ai_results" in st.session_state:
        ai_priorities = st.session_state["ai_results"].get("ai_priorities", [])
        
        if ai_priorities:
            # Sort just in case the LLM returned them out of order
            sorted_priorities = sorted(ai_priorities, key=lambda x: x.get('rank', 99))
            
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
                    <div style="margin-top:10px; display:flex; gap:10px; font-size:0.8em; color:#555;">
                        <span style="background:#eee; padding:2px 6px; border-radius:4px;">Effort: {p.get('effort_score')}/10</span>
                        <span style="background:#eee; padding:2px 6px; border-radius:4px;">Confidence: {p.get('confidence_score')}/10</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("AI pipeline ran but produced no priorities.")
            
    else:
        st.info("🤖 Enter your API key and run the AI pipeline to prioritize your roadmap.")
