import streamlit as st
import pandas as pd
from components.sidebar import sidebar

# Import page components
# Note: These will be implemented in the next steps
try:
    from components.overview import overview_page
    from components.insights import insights_page
    from components.problems import problems_page
    from components.opportunities import opportunities_page
    from components.features import features_page
    from components.experiments import experiments_page
    from components.priorities import priorities_page
except ImportError:
    # Fallback for when components are not yet created
    def overview_page(): st.write("Overview Page Placeholder")
    def insights_page(): st.write("Insights Page Placeholder")
    def problems_page(): st.write("Problems Page Placeholder")
    def opportunities_page(): st.write("Opportunities Page Placeholder")
    def features_page(): st.write("Features Page Placeholder")
    def experiments_page(): st.write("Experiments Page Placeholder")
    def priorities_page(): st.write("Priorities Page Placeholder")

st.set_page_config(
    page_title="Signal",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
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
</style>
""", unsafe_allow_html=True)

def main():
    selected_page = sidebar()
    
    st.markdown("<h1 class='main-header'>Signal</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Turning behavior into product decisions at Careem</p>", unsafe_allow_html=True)
    st.divider()
    
    if selected_page == "Overview":
        overview_page()
    elif selected_page == "Insights":
        insights_page()
    elif selected_page == "Problems":
        problems_page()
    elif selected_page == "Opportunities":
        opportunities_page()
    elif selected_page == "Features":
        features_page()
    elif selected_page == "Experiments":
        experiments_page()
    elif selected_page == "Priorities":
        priorities_page()

if __name__ == "__main__":
    main()
