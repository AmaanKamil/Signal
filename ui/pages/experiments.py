import streamlit as st

def render_experiments(experiments):
    st.title("Experiment Designs")
    st.markdown("Validation plans for AI-generated features.")
    
    # 1. Check for data dependency first
    if "dataset" not in st.session_state:
        st.warning("Data required.")
        return

    # 2. Check if experiments exist
    if not experiments:
        # Differentiate between "not run yet" and "ran but returned nothing"
        if not st.session_state.get("ai_ready"):
            st.info("🤖 Enter your API key and click 'Generate AI Report' in the sidebar to design experiments.")
        else:
            st.warning("⚠️ AI generated no experiments. Please regenerate.")
        return

    # 3. Valid experiments exist - Render them
    st.markdown("### 🧪 Active Designs")
    for exp in experiments:
        # Construct the HTML strictly without indentation to avoid code block issues
        hypothesis = exp.get('hypothesis', 'Hypothesis')
        test_design = exp.get('test_design', 'A/B')
        duration = exp.get('duration', '2w')
        primary_metric = exp.get('primary_metric', '-')
        segment = exp.get('segment', 'All')
        success_criteria = exp.get('success_criteria', '')
        
        html_block = f"""<div style="background-color: #fff; padding: 20px; border-radius: 8px; border-left: 5px solid #673ab7; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.box_shadow='0 4px 6px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.box_shadow='0 1px 3px rgba(0,0,0,0.1)';" >
<h4 style="margin:0 0 10px 0; color:#4527a0;">{hypothesis}</h4>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px; font-size:0.9em; margin-bottom:15px;">
<div>
<strong>Design:</strong> {test_design} <br>
<strong>Duration:</strong> {duration}
</div>
<div>
<strong>Primary Metric:</strong> {primary_metric} <br>
<strong>Target:</strong> {segment}
</div>
</div>
<div style="background:#f3e5f5; padding:10px; border-radius:4px; font-size:0.85em; color:#4a148c;">
<strong>Success Criteria:</strong> {success_criteria}
</div>
</div>"""

        st.markdown(html_block, unsafe_allow_html=True)
