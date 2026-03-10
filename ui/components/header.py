# ui/components/header.py
import streamlit as st

def render_header():
    model_key = "model_select_professional"
    if model_key not in st.session_state:
        st.session_state[model_key] = "llama-3.1-8b-instant"

    selected_model = st.session_state.get(model_key, "llama-3.1-8b-instant")

    # Hide default sidebar
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        min-width: 0 !important;
        max-width: 0 !important;
        opacity: 0 !important;
        transform: translateX(-100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

    :root {
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
    }

    /* ── OUTER WRAPPER ── */
    .glass-nav-wrapper {
        position: sticky;
        top: 0;
        z-index: 9999;
        padding: 10px 24px 0;
        background: linear-gradient(
            180deg,
            rgba(6, 6, 18, 0.98) 0%,
            rgba(6, 6, 18, 0.0) 100%
        );
    }

    /* ── MAIN NAV PILL ── */
    .glass-nav {
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
    }

    /* top shimmer line */
    .glass-nav::before {
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
    }

    @keyframes shimmer-slide {
        0%   { opacity: 0.3; transform: scaleX(0.7); }
        50%  { opacity: 1;   transform: scaleX(1);   }
        100% { opacity: 0.3; transform: scaleX(0.7); }
    }

    /* ambient glow blob */
    .glass-nav::after {
        content: '';
        position: absolute;
        top: -60px; left: 50%;
        transform: translateX(-50%);
        width: 420px; height: 120px;
        background: radial-gradient(ellipse, rgba(124,127,247,0.12) 0%, transparent 70%);
        pointer-events: none;
    }

    /* ── BRAND ── */
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        flex-shrink: 0;
    }

    .nav-brand-icon {
        width: 36px; height: 36px;
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 18px;
        box-shadow: 0 4px 14px rgba(124, 127, 247, 0.45);
        flex-shrink: 0;
        transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1),
                    box-shadow 0.3s ease;
    }

    .nav-brand-icon:hover {
        transform: rotate(-8deg) scale(1.1);
        box-shadow: 0 6px 20px rgba(124, 127, 247, 0.6);
    }

    .nav-brand-text {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.2rem;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #e0e0ff 0%, var(--primary) 60%, var(--secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }

    /* ── MODEL BADGE ── */
    .nav-model-badge {
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
        transition: all 0.25s ease;
        cursor: default;
        flex-shrink: 0;
    }

    .nav-model-badge:hover {
        background: rgba(124, 127, 247, 0.18);
        border-color: rgba(124, 127, 247, 0.4);
        color: var(--text-bright);
        box-shadow: 0 0 16px rgba(124,127,247,0.2);
    }

    .nav-model-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 6px #4ade80;
        animation: pulse-dot 2.5s ease-in-out infinite;
        flex-shrink: 0;
    }

    @keyframes pulse-dot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.6; transform: scale(0.75); }
    }

    /* ── NAV LINKS GROUP ── */
    .nav-links-group {
        display: flex;
        align-items: center;
        gap: 2px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 14px;
        padding: 4px;
    }

    /* ── EXPORT BUTTON ── */
    .nav-export-btn {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 7px 16px;
        background: rgba(74, 222, 128, 0.08);
        border: 1px solid rgba(74, 222, 128, 0.2);
        border-radius: 10px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
        color: #86efac;
        cursor: pointer;
        transition: all 0.25s ease;
        flex-shrink: 0;
    }

    .nav-export-btn:hover {
        background: rgba(74, 222, 128, 0.15);
        border-color: rgba(74, 222, 128, 0.4);
        box-shadow: 0 0 18px rgba(74,222,128,0.2);
        transform: translateY(-1px);
    }

    /* ── BOTTOM FADE SEPARATOR ── */
    .glass-nav-fade {
        height: 18px;
        background: linear-gradient(180deg, rgba(6,6,18,0.3) 0%, transparent 100%);
        margin-bottom: 6px;
    }

    /* ── STREAMLIT BUTTON OVERRIDES inside nav columns ── */
    div[data-testid="column"] .stButton > button {
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
        letter-spacing: 0.01em !important;
        position: relative !important;
        overflow: hidden !important;
        box-shadow: none !important;
        white-space: nowrap !important;
    }

    div[data-testid="column"] .stButton > button:hover {
        color: var(--text-bright) !important;
        background: rgba(124, 127, 247, 0.12) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(124,127,247,0.15) !important;
    }

    div[data-testid="column"] .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Export button green tint */
    div[data-testid="column"]:last-child .stButton > button {
        color: #86efac !important;
        background: rgba(74, 222, 128, 0.07) !important;
        border: 1px solid rgba(74, 222, 128, 0.18) !important;
    }

    div[data-testid="column"]:last-child .stButton > button:hover {
        background: rgba(74, 222, 128, 0.14) !important;
        border-color: rgba(74, 222, 128, 0.35) !important;
        box-shadow: 0 0 16px rgba(74,222,128,0.15) !important;
        color: #bbf7d0 !important;
    }

    div[data-testid="column"]:last-child .stButton > button:disabled {
        opacity: 0.35 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .glass-nav-wrapper { padding: 8px 12px 0; }
        .nav-brand-text { display: none; }
        .nav-model-badge span:not(.nav-model-dot) { display: none; }
        .glass-nav { padding: 0 10px; gap: 6px; }
    }
    </style>
    """, unsafe_allow_html=True)

    # ── BRAND HTML ──
    st.markdown("""
    <div class="glass-nav-wrapper">
      <div class="glass-nav">
    """, unsafe_allow_html=True)

    # ── STREAMLIT LAYOUT inside nav ──
    model_display_names = {
        "llama-3.1-8b-instant": "🦙 LLaMA 3.1 · Groq",
        "phi-3-mini":           "🔷 LLaMA 3.1 · HF",
        "hf-vision":            "🖼️ Qwen2-VL · Vision",
        "mistral":              "🌬️ Mistral 7B",
        "deepseek-r1":          "🔬 DeepSeek R1",
    }
    model_label = model_display_names.get(selected_model, selected_model)

    # Brand + model badge (left side)
    st.markdown(f"""
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
        <!-- spacer -->
        <div style="flex:1;"></div>
        <!-- nav links + export rendered via Streamlit below -->
      </div><!-- .glass-nav -->
    </div><!-- .glass-nav-wrapper -->
    <div class="glass-nav-fade"></div>
    """, unsafe_allow_html=True)

    # ── STREAMLIT BUTTONS ROW (rendered below the HTML nav for functionality) ──
    nav_css = """
    <style>
    .nav-btn-row {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 4px;
        background: rgba(10,10,30,0.5);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 4px 6px;
        margin: -62px 24px 0 auto;
        width: fit-content;
        position: relative;
        z-index: 9998;
    }
    </style>
    """
    st.markdown(nav_css, unsafe_allow_html=True)

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
