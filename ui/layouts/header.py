import streamlit as st

def render_header():
    """
    Renders the top global status bar.
    """
    # Create a container for the header
    header = st.container()
    
    with header:
        # Top strip
        c1, c2, c3 = st.columns([2, 4, 2])
        
        with c1:
            st.markdown("<h3 style='margin:0; padding:0; color:#333;'>Signal <span style='font-weight:normal; font-size:0.6em; color:#888;'>v1.0</span></h3>", unsafe_allow_html=True)
            
        with c2:
            st.empty() # Spacer
            
        with c3:
            # Status indicators
            status_html = ""
            
            # Dataset Status
            if "dataset" in st.session_state:
                status_html += "<span style='color:#388e3c; font-size:0.8em; margin-right:15px;'>● Dataset Active</span>"
            else:
                status_html += "<span style='color:#757575; font-size:0.8em; margin-right:15px;'>○ No Data</span>"
                
            # AI Status
            if "ai_results" in st.session_state:
                status_html += "<span style='color:#7b1fa2; font-size:0.8em;'>● AI Enabled</span>"
            else:
                status_html += "<span style='color:#757575; font-size:0.8em;'>○ AI Idle</span>"
                
            st.markdown(f"<div style='text-align:right;'>{status_html}</div>", unsafe_allow_html=True)
            
        st.divider()
