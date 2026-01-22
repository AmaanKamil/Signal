import streamlit as st

def badge(text, type="default"):
    """
    Renders a styled badge.
    Types: critical, high, medium, low, success, info, neutral
    """
    colors = {
        "critical": ("#d32f2f", "#ffebee"), # Red
        "high": ("#f57c00", "#fff3e0"),     # Orange
        "medium": ("#fbc02d", "#fffde7"),   # Yellow
        "low": ("#388e3c", "#e8f5e9"),      # Green
        "success": ("#388e3c", "#e8f5e9"),  # Green
        "growth": ("#0288d1", "#e1f5fe"),   # Blue
        "retention": ("#7b1fa2", "#f3e5f5"),# Purple
        "monetization": ("#388e3c", "#e8f5e9"), # Green
        "reliability": ("#d32f2f", "#ffebee"), # Red
        "ecosystem": ("#0097a7", "#e0f7fa"), # Cyan
        "neutral": ("#616161", "#eeeeee"),  # Grey
        "default": ("#616161", "#eeeeee")
    }
    
    text_color, bg_color = colors.get(type.lower(), colors["default"])
    
    st.markdown(f"""
    <span style="
        background-color: {bg_color};
        color: {text_color};
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        font-weight: 600;
        margin-right: 5px;
        display: inline-block;
    ">{text}</span>
    """, unsafe_allow_html=True)
