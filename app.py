import streamlit as st
from components.sidebar import sidebar
from ui.layouts.header import render_header

# Import UI pages
from ui.pages.overview import render_overview
from ui.pages.insights import render_insights
from ui.pages.problems import render_problems
from ui.pages.opportunities import render_opportunities
from ui.pages.features import render_features
from ui.pages.experiments import render_experiments
from ui.pages.priorities import render_priorities

st.set_page_config(
    page_title="Signal",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Global Styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333333;
    }
    .sub-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #666666;
        font-size: 18px;
    }
    div.stButton > button {
        width: 100%;
    }
# AI State Initialization
if "ai_ready" not in st.session_state:
    st.session_state["ai_ready"] = False
if "ai_insights" not in st.session_state:
    st.session_state["ai_insights"] = []
if "ai_features" not in st.session_state:
    st.session_state["ai_features"] = []
if "ai_experiments" not in st.session_state:
    st.session_state["ai_experiments"] = []
if "ai_priorities" not in st.session_state:
    st.session_state["ai_priorities"] = []

def main():
    selected_page = sidebar()
    
    # Global Header
    render_header()
    
    if selected_page == "Overview":
        render_overview()
    elif selected_page == "Insights":
        render_insights()
    elif selected_page == "Problems":
        render_problems()
    elif selected_page == "Opportunities":
        render_opportunities()
    elif selected_page == "Features":
        render_features()
    elif selected_page == "Experiments":
        render_experiments()
    elif selected_page == "Priorities":
        render_priorities()

if __name__ == "__main__":
    main()
