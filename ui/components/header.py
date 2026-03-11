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
    /* ================================================================
       STEP 1 — Kill every Streamlit chrome element
       Using attribute selectors only (no generated class names)
    ================================================================ */
    header[data-testid="stHeader"] {{
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
        max-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
        position: fixed !important;
        top: -9999px !important;
        pointer-events: none !important;
    }}
    [data-testid="collapsedControl"] {{
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        position: fixed !important;
        top: -9999px !important;
        pointer-events: none !important;
    }}
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    #MainMenu, footer {{
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        position: fixed !important;
        top: -9999px !important;
        pointer-events: none !important;
    }}
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > * {{
        display: none !important;
        width: 0 !important;
        min-width: 0 !important;
        max-width: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }}

    /* ================================================================
       STEP 2 — Remove ALL top spacing Streamlit reserves for header
       Target the actual DOM hierarchy in Streamlit 1.35
    ================================================================ */
    .stApp {{
        margin-top: 0 !important;
        padding-top: 0 !important;
    }}
    /* The outermost app view container */
    [data-testid="stAppViewContainer"] {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}
    /* The main section */
    [data-testid="stAppViewContainer"] > section.main,
    [data-testid="stAppViewContainer"] > .main {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}
    /* The block container inside main */
    [data-testid="stAppViewContainer"] > section.main > div,
    [data-testid="stAppViewContainer"] > .main > div,
    [data-testid="stAppViewBlockContainer"],
    .main > div.block-container,
    .main .block-container {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}
    /* Legacy generated class names Streamlit 1.28–1.35 uses */
    .css-z5fcl4, .css-1y4p8pa, .css-uf99v8,
    .css-k1vhr4, .css-18e3th9, .css-ffhzg2,
    .css-1avcm0n, .css-14xtw13, .css-fg4pbf {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}

    /* ================================================================
       STEP 3 — Hide the iframe Streamlit injects for components.html
       (we are NOT using components.html — but kill it just in case)
    ================================================================ */
    iframe[title="streamlit_components"] {{
        display: none !important;
        height: 0 !important;
    }}
    /* Any zero-height iframe used for JS injection */
    iframe[height="0"], iframe[height="0px"] {{
        display: none !important;
        height: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
        top: -9999px !important;
    }}

    /* ================================================================
       STEP 4 — The glassmorphism nav styles
    ================================================================ */
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

    :root {{
        --glass-bg: rgba(10, 10, 30, 0.55);
        --glass-border: rgba(255, 255, 255, 0.07);
        --glass-shine: rgba(255, 255, 255, 0.12);
        --primary: #7c7ff7;
        --primary-soft: rgba(124, 127, 247, 0.18);
        --secondary: #a78bfa;
        --accent: #f472b6;
        --text-bright: #f0f0ff;
        --text-dim: #8888aa;
        --nav-height: 68px;
        --blur-amount: 24px;
    }}

    .glass-nav-wrapper {{
        position: relative;
        z-index: 9999;
        padding: 0 24px 0;
        margin-top: 0 !important;
    }}

    .glass-nav {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: var(--nav-height);
        padding: 0 20px 0 16px;
        background: var(--glass-bg);
        backdrop-filter: blur(var(--blur-amount)) saturate(160%);
        -webkit-backdrop-filter: blur(var(--blur-amount)) saturate(160%);
        border-radius: 20px;
        border: 1px solid var(--glass-border);
        box-shadow:
            0 8px 32px rgba(0, 0, 0, 0.4),
            0 1px 0 var(--glass-shine) inset,
            0 -1px 0 rgba(0,0,0,0.3) inset;
        position: relative;
        overflow: hidden;
    }}

    .glass-nav::before {{
        content: '';
        position: absolute;
        top: 0; left: 10%; right: 10%;
        height: 1px;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(124, 127, 247, 0.6) 30%,
            rgba(167, 139, 250, 0.8) 50%,
            rgba(124, 127, 247, 0.6) 70%,
            transparent
        );
        animation: shimmer-slide 4s ease-in-out infinite;
    }}

    @keyframes shimmer-slide {{
        0%   {{ opacity: 0.3; transform: scaleX(0.7); }}
        50%  {{ opacity: 1;   transform: scaleX(1);   }}
        100% {{ opacity: 0.3; transform: scaleX(0.7); }}
    }}

    .glass-nav::after {{
        content: '';
        position: absolute;
        top: -60px; left: 50%;
        transform: translateX(-50%);
        width: 420px; height: 120px;
        background: radial-gradient(ellipse, rgba(124,127,247,0.12) 0%, transparent 70%);
        pointer-events: none;
    }}

    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        flex-shrink: 0;
    }}

    .nav-brand-icon {{
        width: 36px; height: 36px;
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 18px;
        box-shadow: 0 4px 14px rgba(124, 127, 247, 0.45);
        flex-shrink: 0;
        transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease;
    }}

    .nav-brand-icon:hover {{
        transform: rotate(-8deg) scale(1.1);
        box-shadow: 0 6px 20px rgba(124, 127, 247, 0.6);
    }}

    .nav-brand-text {{
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.2rem;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #e0e0ff 0%, var(--primary) 60%, var(--secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }}

    .nav-model-badge {{
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 6px 14px;
        background: rgba(124, 127, 247, 0.1);
        border: 1px solid rgba(124, 127, 247, 0.22);
        border-radius: 30px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.8rem;
        font-weight: 500;
        color: #c4c4f0;
        white-space: nowrap;
        cursor: default;
        flex-shrink: 0;
    }}

    .nav-model-dot {{
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 6px #4ade80;
        animation: pulse-dot 2.5s ease-in-out infinite;
        flex-shrink: 0;
    }}

    @keyframes pulse-dot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50%       {{ opacity: 0.6; transform: scale(0.75); }}
    }}

    /* ── Streamlit button overrides inside nav columns ── */
    div[data-testid="column"] .stButton > button {{
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        color: var(--text-dim) !important;
        background: transparent !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 7px 14px !important;
        height: 36px !important;
        min-height: 36px !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
        white-space: nowrap !important;
    }}

    div[data-testid="column"] .stButton > button:hover {{
        color: var(--text-bright) !important;
        background: rgba(124, 127, 247, 0.12) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(124,127,247,0.15) !important;
    }}

    /* Export button green tint */
    div[data-testid="column"]:last-child .stButton > button {{
        color: #86efac !important;
        background: rgba(74, 222, 128, 0.07) !important;
        border: 1px solid rgba(74, 222, 128, 0.18) !important;
    }}

    div[data-testid="column"]:last-child .stButton > button:hover {{
        background: rgba(74, 222, 128, 0.14) !important;
        border-color: rgba(74, 222, 128, 0.35) !important;
        color: #bbf7d0 !important;
    }}

    div[data-testid="column"]:last-child .stButton > button:disabled {{
        opacity: 0.35 !important;
        cursor: not-allowed !important;
        transform: none !important;
    }}

    @media (max-width: 768px) {{
        .glass-nav-wrapper {{ padding: 0 12px; }}
        .nav-brand-text {{ display: none; }}
        .glass-nav {{ padding: 0 10px; }}
    }}

    /* ================================================================
       STEP 5 — JavaScript: nuke header via inline script tag in markdown
       (No iframe — uses a <script> directly in st.markdown HTML)
    ================================================================ */
    </style>

    <script>
    (function nukeST() {{
        function hide() {{
            var sels = [
                'header[data-testid="stHeader"]',
                '[data-testid="collapsedControl"]',
                '[data-testid="stToolbar"]',
                '[data-testid="stDecoration"]',
                '[data-testid="stStatusWidget"]',
                '#MainMenu', 'footer'
            ];
            sels.forEach(function(s) {{
                document.querySelectorAll(s).forEach(function(el) {{
                    el.style.cssText = 'display:none!important;height:0!important;min-height:0!important;overflow:hidden!important;visibility:hidden!important;position:fixed!important;top:-9999px!important;';
                }});
            }});
            // Remove top padding from every likely container
            var targets = [
                '[data-testid="stAppViewContainer"]',
                '[data-testid="stAppViewContainer"] > section.main',
                '[data-testid="stAppViewBlockContainer"]',
                '.main .block-container',
                '.stApp'
            ];
            targets.forEach(function(s) {{
                document.querySelectorAll(s).forEach(function(el) {{
                    el.style.paddingTop = '0';
                    el.style.marginTop = '0';
                }});
            }});
            // Hide zero-height iframes (from components.html)
            document.querySelectorAll('iframe').forEach(function(f) {{
                if (parseInt(f.height) === 0 || f.style.height === '0px') {{
                    f.style.cssText = 'display:none!important;height:0!important;position:absolute!important;top:-9999px!important;';
                }}
            }});
        }}
        hide();
        var obs = new MutationObserver(hide);
        obs.observe(document.body, {{childList: true, subtree: true}});
    }})();
    </script>

    <div class="glass-nav-wrapper">
      <div class="glass-nav">
        <div style="display:flex;align-items:center;gap:14px;flex-shrink:0;">
          <a class="nav-brand" href="#">
            <div class="nav-brand-icon">🤔</div>
            <span class="nav-brand-text">Doubt Tutor</span>
          </a>
          <div class="nav-model-badge" title="Active model">
            <span class="nav-model-dot"></span>
            {model_label}
          </div>
        </div>
        <div style="flex:1;"></div>
      </div>
    </div>
    <div style="height:8px;background:linear-gradient(180deg,rgba(6,6,18,0.3) 0%,transparent 100%);margin-bottom:6px;"></div>
    """, unsafe_allow_html=True)

    # ── NAV BUTTONS (Streamlit columns, rendered after HTML nav) ──
    cols = st.columns([1, 1, 1, 1, 1])

    with cols[0]:
        if st.button("🏠 Home", key="nav_Home", use_container_width=False):
            st.switch_page("app.py")
    with cols[1]:
        if st.button("ℹ️ About", key="nav_About", use_container_width=False):
            st.switch_page("pages/1_About.py")
    with cols[2]:
        if st.button("📖 How It Works", key="nav_How", use_container_width=False):
            st.switch_page("pages/2_How_It_Works.py")
    with cols[3]:
        if st.button("🤖 Models", key="nav_Models", use_container_width=False):
            st.switch_page("pages/3_Models.py")
    with cols[4]:
        has_messages = bool(st.session_state.get("messages"))
        if has_messages:
            if st.button("💾 Export", key="export_btn", use_container_width=False):
                st.session_state["export_chat"] = True
                st.rerun()
        else:
            st.button("💾 Export", key="export_btn_disabled", disabled=True, use_container_width=False)

    # Divider
    st.markdown("""
    <div style="height:1px;
                background:linear-gradient(90deg,transparent,rgba(124,127,247,0.25),transparent);
                margin: 8px 0 18px;">
    </div>
    """, unsafe_allow_html=True)
