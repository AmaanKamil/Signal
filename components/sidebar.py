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
                    # Process and Store Data
                    from utils.data_engine import process_data, get_global_metrics
                    from utils.segmentation import get_segments, get_segment_counts
                    import utils.analytics as analytics
                    
                    processed_df = process_data(df)
                    st.session_state["dataset"] = processed_df
                    st.session_state["global_metrics"] = get_global_metrics(processed_df)
                    
                    segments = get_segments(processed_df)
                    st.session_state["segments"] = segments
                    st.session_state["segment_counts"] = get_segment_counts(segments)
                    
                    st.session_state["funnel_stats"] = analytics.get_funnel_stats(processed_df)
                    st.session_state["vertical_stats"] = analytics.get_vertical_stats(processed_df)
                    st.session_state["time_stats"], st.session_state["location_stats"] = analytics.get_contextual_stats(processed_df)
                    
                    # Intelligence Engine
                    from utils.intelligence_engine import aggregate_intelligence
                    st.session_state["intelligence"] = aggregate_intelligence(processed_df)
                    
                    st.success("Dataset loaded, processed, and analyzed successfully!")
                else:
                    st.error(message)
        
        if st.button("Load Sample Dataset"):
            df = load_sample_dataset()
            if df is not None:
                # Process and Store Data (Sample)
                from utils.data_engine import process_data, get_global_metrics
                from utils.segmentation import get_segments, get_segment_counts
                import utils.analytics as analytics
                
                processed_df = process_data(df)
                st.session_state["dataset"] = processed_df
                st.session_state["global_metrics"] = get_global_metrics(processed_df)
                
                segments = get_segments(processed_df)
                st.session_state["segments"] = segments
                st.session_state["segment_counts"] = get_segment_counts(segments)
                
                st.session_state["funnel_stats"] = analytics.get_funnel_stats(processed_df)
                st.session_state["vertical_stats"] = analytics.get_vertical_stats(processed_df)
                st.session_state["time_stats"], st.session_state["location_stats"] = analytics.get_contextual_stats(processed_df)

                # Intelligence Engine
                from utils.intelligence_engine import aggregate_intelligence
                st.session_state["intelligence"] = aggregate_intelligence(processed_df)

                st.success("Sample dataset loaded, processed, and analyzed!")
            else:
                st.error("Sample dataset not found")

        if "dataset" in st.session_state:
            st.info(f"Loaded: {len(st.session_state['dataset'])} rows")

        st.divider()
        st.subheader("🤖 Signal AI")
        
        api_key = st.text_input("OpenAI API Key", type="password", help="Enter your key to enable AI features")
        
        if api_key:
            if st.button("Generate AI Report"):
                if "intelligence" in st.session_state:
                    from ai.orchestrator import run_signal_ai_pipeline
                    
                    results = run_signal_ai_pipeline(st.session_state["intelligence"], api_key)
                    
                    # basic check if results dictionary has content
                    if results and isinstance(results, dict) and results.get("insights"):
                        # Write to persistent state keys
                        st.session_state["ai_insights"] = results.get("insights", [])
                        st.session_state["ai_features"] = results.get("features", [])
                        st.session_state["ai_experiments"] = results.get("experiments", [])
                        st.session_state["ai_priorities"] = results.get("priorities", [])
                        
                        st.session_state["ai_ready"] = True
                        st.session_state["ai_generated"] = True
                        st.session_state["ai_results"] = results # Keep for backward compatibility
                        
                        st.success("AI pipeline completed!")
                        st.rerun()
                    else:
                        st.error("AI pipeline failed to generate results. Please check API key and try again.")
                else:
                    st.warning("Please load a dataset first.")
                    
            # Debug Panel (Temporary)
            st.divider()
            st.subheader("🛠 Debug Panel")
            st.write("AI_READY:", st.session_state.get("ai_ready"))
            st.write("AI_INSIGHTS:", len(st.session_state.get("ai_insights", [])))
            st.write("AI_FEATURES:", len(st.session_state.get("ai_features", [])))
            st.write("AI_EXPERIMENTS:", len(st.session_state.get("ai_experiments", [])))
            st.write("AI_PRIORITIES:", len(st.session_state.get("ai_priorities", [])))
        else:
            st.warning("AI disabled. Add API key to enable.")

        return page
