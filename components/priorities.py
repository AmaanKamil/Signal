import streamlit as st

def priorities_page():
    st.title("Priorities")
    
    if "dataset" not in st.session_state:
        st.warning("Please load a dataset to see prioritization.")
        return

    st.markdown("### 📋 Roadmap Priorities")
    st.markdown("Ranked list of features and experiments based on potential impact and effort.")
    
    # Placeholder structured output
    st.markdown("""
    <style>
        .priority-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .score {
            font-weight: bold;
            font-size: 1.2em;
            color: #2e7d32;
        }
    </style>
    
    <div class="priority-row">
        <div>
            <strong>1. Implement One-Tap Reorder</strong><br>
            <span style="color: #666; font-size: 0.9em;">High Impact, Low Effort</span>
        </div>
        <div class="score">Score: 92/100</div>
    </div>
    
    <div class="priority-row">
        <div>
            <strong>2. Fix Cart Abandonment Issue</strong><br>
            <span style="color: #666; font-size: 0.9em;">High Impact, Medium Effort</span>
        </div>
        <div class="score">Score: 88/100</div>
    </div>

    <div class="priority-row">
        <div>
            <strong>3. Launch 'Smart Commute' Bundle</strong><br>
            <span style="color: #666; font-size: 0.9em;">Medium Impact, High Effort</span>
        </div>
        <div class="score">Score: 75/100</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("*(AI integration for RICE scoring pending)*")
