# ui/components/header.py
import streamlit as st

def render_header():
    model_key = "model_select_professional"
    if model_key not in st.session_state:
        st.session_state[model_key] = "llama-3.1-8b-instant"

    selected_model = st.session_state.get(model_key, "llama-3.1-8b-instant")

    model_display_names = {
        "llama-3.1-8b-instant": "🦙 LLaMA 3.1 · Groq",
        "phi-3-mini":           "🔷 LLaMA 3.1 · HF",
        "hf-vision":            "🖼️ Qwen2-VL · Vision",
        "mistral":              "🌬️ Mistral 7B",
        "deepseek-r1":          "🔬 DeepSeek R1",
    }
    model_label = model_display_names.get(selected_model, selected_model)

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500;600&display=swap');

    /* ── Kill Streamlit chrome ── */
    header[data-testid="stHeader"],
    [data-testid="collapsedControl"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    #MainMenu, footer {{
        display: none !important;
        height: 0 !important;
        min-height: 0 !important;
        overflow: hidden !important;
        visibility: hidden !important;
        position: fixed !important;
        top: -9999px !important;
        pointer-events: none !important;
    }}
    section[data-testid="stSidebar"] {{
        display: none !important;
        width: 0 !important;
        min-width: 0 !important;
        overflow: hidden !important;
        pointer-events: none !important;
    }}

    /* ── Remove ALL top padding/margin from Streamlit containers ── */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section.main,
    [data-testid="stAppViewContainer"] > .main,
    [data-testid="stAppViewBlockContainer"],
    .main .block-container,
    .main > div.block-container {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}

    /* ── Make block-container full width so nav can escape ── */
    .main .block-container {{
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
    }}

    /* ── Full-width sticky nav bar ── */
    .dt-nav {{
        position: sticky;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        width: 100%;
        background: linear-gradient(180deg, rgba(8,8,22,0.98) 0%, rgba(8,8,22,0.94) 100%);
        backdrop-filter: blur(20px) saturate(160%);
        -webkit-backdrop-filter: blur(20px) saturate(160%);
        border-bottom: 1px solid rgba(124,127,247,0.15);
        box-shadow: 0 4px 24px rgba(0,0,0,0.4);
        padding: 0 32px;
        display: flex;
        align-items: center;
        height: 64px;
        gap: 20px;
    }}

    /* shimmer top line */
    .dt-nav::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg,
            transparent 0%,
            rgba(124,127,247,0.7) 30%,
            rgba(167,139,250,0.9) 50%,
            rgba(124,127,247,0.7) 70%,
            transparent 100%);
        animation: nav-shimmer 4s ease-in-out infinite;
    }}
    @keyframes nav-shimmer {{
        0%,100% {{ opacity:0.3; }} 50% {{ opacity:1; }}
    }}

    /* ── Brand ── */
    .dt-brand {{
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        flex-shrink: 0;
    }}
    .dt-brand-icon {{
        width: 36px; height: 36px;
        background: linear-gradient(135deg, #7c7ff7 0%, #f472b6 100%);
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 18px;
        box-shadow: 0 4px 14px rgba(124,127,247,0.45);
        transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1);
    }}
    .dt-brand-icon:hover {{ transform: rotate(-8deg) scale(1.1); }}
    .dt-brand-text {{
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.2rem;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #e0e0ff 0%, #7c7ff7 60%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }}

    /* ── Model badge ── */
    .dt-badge {{
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 5px 13px;
        background: rgba(124,127,247,0.1);
        border: 1px solid rgba(124,127,247,0.25);
        border-radius: 30px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.78rem;
        font-weight: 500;
        color: #c4c4f0;
        white-space: nowrap;
        flex-shrink: 0;
    }}
    .dt-badge-dot {{
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 6px #4ade80;
        animation: dot-pulse 2.5s ease-in-out infinite;
        flex-shrink: 0;
    }}
    @keyframes dot-pulse {{
        0%,100% {{ opacity:1; transform:scale(1); }}
        50% {{ opacity:0.5; transform:scale(0.7); }}
    }}

    /* ── Spacer ── */
    .dt-spacer {{ flex: 1; }}

    /* ── Streamlit column buttons inside nav ── */
    /* Negative margin to pull the button row INTO the nav bar */
    .dt-btn-row {{
        display: flex;
        align-items: center;
        gap: 2px;
        flex-shrink: 0;
    }}

    /* Override Streamlit button styles for nav buttons */
    .stButton > button {{
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.84rem !important;
        font-weight: 500 !important;
        color: #7878a8 !important;
        background: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 6px 13px !important;
        height: 34px !important;
        min-height: 34px !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
        white-space: nowrap !important;
    }}
    .stButton > button:hover {{
        color: #f0f0ff !important;
        background: rgba(124,127,247,0.12) !important;
        transform: translateY(-1px) !important;
    }}

    /* ── Content padding restored below nav ── */
    .dt-content-wrap {{
        padding: 0 32px;
    }}

    /* ── Divider below nav ── */
    .dt-divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(124,127,247,0.2), transparent);
        margin: 6px 32px 20px;
    }}

    @media (max-width: 768px) {{
        .dt-nav {{ padding: 0 16px; gap: 10px; }}
        .dt-brand-text {{ display: none; }}
        .dt-content-wrap {{ padding: 0 16px; }}
        .dt-divider {{ margin: 6px 16px 16px; }}
    }}
    </style>

    <script>
    (function() {{
        function nukeChrome() {{
            ['header[data-testid="stHeader"]',
             '[data-testid="collapsedControl"]',
             '[data-testid="stToolbar"]',
             '[data-testid="stDecoration"]',
             '[data-testid="stStatusWidget"]',
             '#MainMenu','footer'
            ].forEach(function(s) {{
                document.querySelectorAll(s).forEach(function(el) {{
                    el.style.cssText='display:none!important;height:0!important;overflow:hidden!important;visibility:hidden!important;position:fixed!important;top:-9999px!important;';
                }});
            }});
            // Zero out top padding
            ['[data-testid="stAppViewContainer"]',
             '[data-testid="stAppViewContainer"] > section.main',
             '[data-testid="stAppViewBlockContainer"]',
             '.main .block-container','.stApp'
            ].forEach(function(s) {{
                document.querySelectorAll(s).forEach(function(el) {{
                    el.style.paddingTop='0';
                    el.style.marginTop='0';
                }});
            }});
            // Full width block container
            document.querySelectorAll('.main .block-container').forEach(function(el) {{
                el.style.maxWidth='100%';
                el.style.paddingLeft='0';
                el.style.paddingRight='0';
            }});
        }}
        nukeChrome();
        new MutationObserver(nukeChrome).observe(document.body,{{childList:true,subtree:true}});
    }})();
    </script>

    <nav class="dt-nav">
      <a class="dt-brand" href="#">
        <div class="dt-brand-icon">🤔</div>
        <span class="dt-brand-text">Doubt Tutor</span>
      </a>
      <div class="dt-badge">
        <span class="dt-badge-dot"></span>
        {model_label}
      </div>
      <div class="dt-spacer"></div>
    </nav>
    """, unsafe_allow_html=True)

    # ── Nav buttons rendered as Streamlit columns (appear right after nav) ──
    # Wrap in a styled container that sits flush under the nav
    st.markdown("""
    <style>
    /* Pull the button row up and style it like part of the nav */
    [data-testid="stHorizontalBlock"] {
        background: rgba(8,8,22,0.92) !important;
        backdrop-filter: blur(20px) !important;
        border-bottom: 1px solid rgba(124,127,247,0.12) !important;
        padding: 4px 32px !important;
        margin: 0 !important;
        gap: 0 !important;
    }
    [data-testid="stHorizontalBlock"] [data-testid="column"] {
        padding: 0 2px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns([1, 1, 1, 1, 1])
    with cols[0]:
        if st.button("🏠 Home", key="nav_Home", use_container_width=True):
            st.switch_page("app.py")
    with cols[1]:
        if st.button("ℹ️ About", key="nav_About", use_container_width=True):
            st.switch_page("pages/1_About.py")
    with cols[2]:
        if st.button("📖 How It Works", key="nav_How", use_container_width=True):
            st.switch_page("pages/2_How_It_Works.py")
    with cols[3]:
        if st.button("🤖 Models", key="nav_Models", use_container_width=True):
            st.switch_page("pages/3_Models.py")
    with cols[4]:
        has_messages = bool(st.session_state.get("messages"))
        if has_messages:
            if st.button("💾 Export", key="export_btn", use_container_width=True):
                st.session_state["export_chat"] = True
                st.rerun()
        else:
            st.button("💾 Export", key="export_btn_disabled",
                      disabled=True, use_container_width=True)

    st.markdown('<div class="dt-divider"></div>', unsafe_allow_html=True)
