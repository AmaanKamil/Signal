import streamlit as st
from ui.components.badges import badge

def insight_card(title, detail, domain, severity, source="Rule-based"):
    """
    Renders a card for an insight.
    """
    border_color = {
        "critical": "#d32f2f",
        "high": "#ffa000",
        "medium": "#fbc02d",
        "low": "#388e3c",
        "unknown": "#ccc"
    }.get(str(severity).lower(), "#ccc")
    
    st.markdown(f"""
    <div style="
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid {border_color};
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    " onmouseover="this.style.transform='translateX(5px)'; this.style.box_shadow='0 4px 6px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateX(0)'; this.style.box_shadow='0 1px 3px rgba(0,0,0,0.1)';" >
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <h4 style="margin:0; color:#333;">{title}</h4>
            <span style="font-size:0.8em; color:#888;">{source}</span>
        </div>
        <p style="color:#555; font-size:0.95em; margin-bottom:15px;">{detail}</p>
        <div style="display:flex; align-items:center;">
    """, unsafe_allow_html=True)
    
    # We use columns to render streamlit widgets inside the card 'footer' if needed, 
    # but since we are mixing HTML and Streamlit widgets, we'll just close the HTML div here 
    # and call the badge function.
    
    # Render badges via columns to keep them "inline" with HTML flow is tricky, 
    # so we'll just inject the badge HTML if we want full custom.
    # For now, let's keep it simple and use the python badge function if possible,
    # or just replicate badge logic in HTML for pure card rendering.
    
    # Let's use pure HTML for the footer to ensure layout stability
    dom_color, dom_bg = "#0288d1", "#e1f5fe" # Default blue
    sev_color, sev_bg = border_color, f"{border_color}11" # Light version
    
    st.markdown(f"""
            <span style="background:{dom_bg}; color:{dom_color}; padding:2px 8px; border-radius:4px; font-size:0.8em; margin-right:10px;">{domain}</span>
            <span style="background:{sev_bg}; color:{sev_color}; padding:2px 8px; border-radius:4px; font-size:0.8em;">{severity}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def feature_card(name, description, impact, risk, source="AI"):
    """
    Renders a card for a feature concept.
    """
    st.markdown(f"""
    <div style="
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-top: 3px solid #2196f3;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    " onmouseover="this.style.transform='translateY(-3px)'; this.style.box_shadow='0 6px 12px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.box_shadow='0 2px 5px rgba(0,0,0,0.05)';" >
        <div style="display:flex; justify-content:space-between;">
            <h4 style="margin:0; color:#1565c0;">{name}</h4>
            <span style="font-size:0.75em; background:#e3f2fd; color:#1565c0; padding:2px 6px; border-radius:4px;">{source}</span>
        </div>
        <p style="margin:10px 0; color:#444;">{description}</p>
        <div style="display:flex; gap:15px; font-size:0.85em; color:#666; border-top:1px solid #eee; padding-top:10px;">
            <span><strong>Impact:</strong> {impact}</span>
            <span><strong>Risk:</strong> {risk}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def metric_card(label, value, subtext=None, trend=None):
    """
    Renders a clean metric card.
    """
    trend_color = trend if trend else "#888"
    st.markdown(f"""
    <div style="
        background-color: #fff;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    " onmouseover="this.style.transform='translateY(-2px)'; this.style.box_shadow='0 4px 6px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.box_shadow='0 1px 2px rgba(0,0,0,0.1)';" >
        <p style="color:#777; font-size:0.9em; margin:0; text-transform:uppercase; letter-spacing:0.5px;">{label}</p>
        <h2 style="color:#333; margin:5px 0; font-size:2em;">{value}</h2>
        {f'<p style="color:{trend_color}; font-size:0.8em; margin:0;">{subtext}</p>' if subtext else ''}
    </div>
    """, unsafe_allow_html=True)
