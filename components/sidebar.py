import streamlit as st
from utils.data_loader import load_dataset, validate_dataset, load_sample_dataset

def sidebar():
    with st.sidebar:
        st.title("Signal")
        st.markdown("*Turning behavior into product decisions at Careem*")
        
        st.divider()
        
        page = st.radio(
            "Navigation",
            [
                "Overview",
                "Insights",
                "Problems",
                "Opportunities",
                "Features",
                "Experiments",
                "Priorities"
            ]
        )
        
        st.divider()
        
        st.subheader("Dataset")
        
        uploaded_file = st.file_uploader("Upload CSV", type="csv")
        
        if uploaded_file is not None:
            df = load_dataset(uploaded_file)
            if df is not None:
                is_valid, message = validate_dataset(df)
                if is_valid:
                    st.session_state["dataset"] = df
                    st.success("Dataset loaded successfully!")
                else:
                    st.error(message)
        
        if st.button("Load Sample Dataset"):
            df = load_sample_dataset()
            if df is not None:
                is_valid, message = validate_dataset(df)
                if is_valid:
                    st.session_state["dataset"] = df
                    st.success("Sample dataset loaded!")
                else:
                    st.error(message)

        if "dataset" in st.session_state:
            st.info(f"Loaded: {len(st.session_state['dataset'])} rows")
            
        return page
