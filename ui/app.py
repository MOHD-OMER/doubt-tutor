import sys
from pathlib import Path

# Determine correct project root (folder containing src/)
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

print("PROJECT ROOT:", ROOT_DIR)
print("EXPECTS src AT:", ROOT_DIR / "src")

# Load .env from project root
import src.load_env

import streamlit as st
import base64
import json
from datetime import datetime
import re

# Add project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.models.ai_manager import AIManager
from ui.components.header import render_header
from ui.components.chat_interface import render_chat

# --------------------------------------------------
# Page Config (First thing in Streamlit)
# --------------------------------------------------
st.set_page_config(
    page_title="💡 Doubt Tutor",
    page_icon="🤔",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={}
)

# Immediately hide sidebar + header to prevent flash
hide_sidebar_css = """
<style>
header[data-testid="stHeader"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important; min-height: 0 !important; max-height: 0 !important;
    padding: 0 !important; margin: 0 !important;
    overflow: hidden !important;
    position: fixed !important; top: -9999px !important;
    pointer-events: none !important;
}
[data-testid="collapsedControl"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    position: fixed !important; top: -9999px !important;
    pointer-events: none !important;
}
[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"],#MainMenu,footer {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    position: fixed !important; top: -9999px !important;
    pointer-events: none !important;
}
section[data-testid="stSidebar"],section[data-testid="stSidebar"] > * {
    display: none !important;
    width: 0 !important; min-width: 0 !important; max-width: 0 !important;
    height: 0 !important; overflow: hidden !important;
    opacity: 0 !important; pointer-events: none !important;
}
.stApp { margin-top: 0 !important; padding-top: 0 !important; }
[data-testid="stAppViewContainer"] { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="stAppViewContainer"] > section.main,
[data-testid="stAppViewContainer"] > .main { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="stAppViewContainer"] > section.main > div,
[data-testid="stAppViewBlockContainer"],
.main > div.block-container,
.main .block-container { padding-top: 0 !important; margin-top: 0 !important; }
.css-z5fcl4,.css-1y4p8pa,.css-uf99v8,.css-k1vhr4,.css-18e3th9,
.css-ffhzg2,.css-1avcm0n,.css-14xtw13,.css-fg4pbf {
    padding-top: 0 !important; margin-top: 0 !important;
}
iframe[height="0"],iframe[height="0px"] {
    display: none !important;
    height: 0 !important;
    position: absolute !important; top: -9999px !important;
}
</style>
<script>
(function nukeST() {
    function hide() {
        var sels = [
            'header[data-testid="stHeader"]',
            '[data-testid="collapsedControl"]',
            '[data-testid="stToolbar"]',
            '[data-testid="stDecoration"]',
            '[data-testid="stStatusWidget"]',
            '#MainMenu','footer'
        ];
        sels.forEach(function(s) {
            document.querySelectorAll(s).forEach(function(el) {
                el.style.cssText = 'display:none!important;height:0!important;min-height:0!important;overflow:hidden!important;visibility:hidden!important;position:fixed!important;top:-9999px!important;';
            });
        });
        var targets = [
            '[data-testid="stAppViewContainer"]',
            '[data-testid="stAppViewContainer"] > section.main',
            '[data-testid="stAppViewBlockContainer"]',
            '.main .block-container','.stApp'
        ];
        targets.forEach(function(s) {
            document.querySelectorAll(s).forEach(function(el) {
                el.style.paddingTop = '0';
                el.style.marginTop = '0';
            });
        });
        document.querySelectorAll('iframe').forEach(function(f) {
            if (parseInt(f.height) === 0 || f.style.height === '0px') {
                f.style.cssText = 'display:none!important;height:0!important;position:absolute!important;top:-9999px!important;';
            }
        });
    }
    hide();
    new MutationObserver(hide).observe(document.body, {childList:true, subtree:true});
})();
</script>
"""
st.markdown(hide_sidebar_css, unsafe_allow_html=True)

# --------------------------------------------------
# Global Styles
# --------------------------------------------------
global_css = """
<style>
:root {
    --primary-color: #6366f1;
    --primary-hover: #5856eb;
    --secondary-color: #8b5cf6;
    --accent-color: #06b6d4;
    --bg-primary: #0f0f23;
    --bg-secondary: #1a1a2e;
    --bg-tertiary: #16213e;
    --text-primary: #f8fafc;
    --text-secondary: #e2e8f0;
    --text-muted: #94a3b8;
    --border-color: rgba(99, 102, 241, 0.2);
    --shadow-light: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-medium: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    --shadow-heavy: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    --border-radius: 12px;
    --radius-sm: 6px;
    --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --font-size-base: 0.9375rem;
    --font-size-sm: 0.875rem;
    --font-size-xs: 0.75rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;
    --font-size-2xl: 1.5rem;
    --font-size-3xl: 2rem;
    --header-height: 72px;
    --input-height: 56px;
}

.stApp {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-tertiary) 100%);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-secondary); }
::-webkit-scrollbar-thumb { background: var(--primary-color); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--primary-hover); }

.block-container {
    padding: 1rem 1rem 3rem !important;
    max-width: 1400px !important;
    margin: 0 auto !important;
}

.stMarkdown { font-size: 1rem; line-height: 1.6; }
.element-container:first-child { padding-top: 0 !important; }
.element-container { padding-top: 0 !important; }
.content { padding: 0 !important; margin: 0 !important; }

.stButton > button {
    border-radius: var(--border-radius);
    border: none;
    font-weight: 600;
    transition: var(--transition);
    box-shadow: var(--shadow-light);
    min-height: var(--input-height);
    padding: 0.75rem 1rem;
}
.stButton > button:hover { box-shadow: var(--shadow-medium); transform: translateY(-1px); }
.stButton > button:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }

.stTextInput > div > div > input {
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
    background: var(--bg-secondary);
    color: var(--text-primary);
    padding: 0.75rem 1rem;
    transition: var(--transition);
    min-height: var(--input-height);
    font-size: 16px;
}
.stTextInput > div > div > input:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.stAlert, .stToast { border-radius: var(--border-radius); border: none; box-shadow: var(--shadow-heavy); }

@media (min-width: 1441px) { .stApp { max-width: 1600px; margin: 0 auto; } }

@media (max-width: 1024px) {
    .stApp { padding: 0 var(--spacing-md); }
    .features { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: var(--spacing-md); }
}

@media (max-width: 768px) {
    :root { --header-height: 120px; --input-height: 52px; --spacing-md: 0.75rem; --spacing-lg: 1rem; }
    .stApp { padding: 0 var(--spacing-sm); }
    div[data-testid="stHorizontalBlock"] { flex-direction: column !important; gap: var(--spacing-sm) !important; }
    div[data-testid="column"]:nth-child(1),
    div[data-testid="column"]:nth-child(2),
    div[data-testid="column"]:nth-child(3) { width: 100% !important; flex: 1 !important; }
    div[data-testid="stFileUploader"],
    .stButton > button[kind="primary"],
    .stButton > button {
        width: 100% !important;
        height: var(--input-height) !important;
        min-height: var(--input-height) !important;
        padding: 0.75rem 1rem !important;
        font-size: 16px !important;
    }
    .input-container { padding: var(--spacing-md) !important; margin: 0 !important; }
    .file-item { padding: var(--spacing-sm); flex-direction: column; text-align: center; gap: var(--spacing-xs); }
    .file-info { text-align: left; width: 100%; }
    .file-name { white-space: normal; word-break: break-word; }
}

@media (max-width: 480px) {
    input[type="text"] { font-size: 16px !important; }
    .stButton > button { min-height: 44px !important; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
</style>
"""
st.markdown(global_css, unsafe_allow_html=True)

# Load custom CSS file if exists
css_path = Path("ui/styles/style.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# File uploader CSS
file_uploader_css = """
<style>
div[data-testid="stFileUploader"] {
    width: 42px !important;
    height: 42px !important;
    min-width: 42px !important;
    background: rgba(99,102,241,.15) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: var(--border-radius) !important;
    position: relative !important;
    overflow: hidden !important;
    cursor: pointer !important;
    transition: var(--transition);
    box-shadow: var(--shadow-light);
}
div[data-testid="stFileUploader"]:hover {
    background: rgba(99,102,241,.25) !important;
    box-shadow: var(--shadow-medium);
    transform: translateY(-1px);
}
div[data-testid="stFileUploader"]::after {
    content: "📎" !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    font-size: 22px !important;
    pointer-events: none !important;
    z-index: 1 !important;
    filter: drop-shadow(0 1px 2px rgba(0,0,0,0.1));
}
div[data-testid="stFileUploader"] label div,
div[data-testid="stFileUploader"] button,
div[data-testid="stFileUploader"] small,
div[data-testid="stFileUploader"] span,
div[data-testid="stFileUploader"] p,
div[data-testid="stFileUploader"] section > div { display: none !important; }
div[data-testid="stFileUploader"] * { font-size: 0 !important; color: transparent !important; }
div[data-testid="stFileUploader"] label {
    position: absolute !important; top: 0 !important; left: 0 !important;
    width: 100% !important; height: 100% !important;
    cursor: pointer !important; z-index: 2 !important; margin: 0 !important; padding: 0 !important;
}
div[data-testid="stFileUploader"] section {
    position: absolute !important; top: 0 !important; left: 0 !important;
    width: 100% !important; height: 100% !important;
    background: transparent !important; border: none !important;
}
div[data-testid="stFileUploader"] input[type="file"] {
    position: absolute !important; top: 0 !important; left: 0 !important;
    width: 100% !important; height: 100% !important;
    opacity: 0 !important; cursor: pointer !important; z-index: 10 !important;
}
@media (max-width: 768px) {
    div[data-testid="stFileUploader"] {
        width: 100% !important; height: var(--input-height) !important; min-width: auto !important;
    }
    div[data-testid="stFileUploader"]::after { font-size: 24px !important; }
}
</style>
"""
st.markdown(file_uploader_css, unsafe_allow_html=True)

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------
def encode_file(file):
    file.seek(0)
    return base64.b64encode(file.read()).decode("utf-8")

def sanitize_content(text):
    if not text:
        return ""
    text = str(text)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    dangerous_tags = ['script', 'iframe', 'object', 'embed', 'style']
    for tag in dangerous_tags:
        text = re.sub(f'<{tag}[^>]*>.*?</{tag}>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(f'<{tag}[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+(class|style)\s*=\s*["\'][^"\']*["\']', '', text)
    ui_classes = ['bubble', 'message', 'timestamp', 'meta', 'wrapper']
    for cls in ui_classes:
        text = re.sub(f'class=["\'][^"\']*{cls}[^"\']*["\']', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

# --------------------------------------------------
# Constants & Instances
# --------------------------------------------------
MAX_FILE_MB = 10
ai = AIManager()

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------
def init_session_state():
    defaults = {
        "messages": [],
        "current_model": "llama-3.1-8b-instant",
        "theme": "dark",
        "pdf_fullscreen": None,
        "files_buffer": [],
        "input_key": 0,
        "uploader_key": 0,
        "processing_response": False,
        "files_processed": set()
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# Clean existing messages on first run
if "messages_cleaned" not in st.session_state:
    if st.session_state.messages:
        cleaned = []
        for msg in st.session_state.messages:
            if isinstance(msg, dict) and "content" in msg:
                msg["content"] = sanitize_content(msg.get("content", ""))
                if msg["content"] and len(msg["content"]) > 2:
                    cleaned.append(msg)
        st.session_state.messages = cleaned
    st.session_state.messages_cleaned = True

# Sync Model from Header
if "model_select_professional" in st.session_state:
    st.session_state.current_model = st.session_state.model_select_professional

# Export Handler
if st.session_state.get("export_chat"):
    if st.session_state.messages:
        file = json.dumps({
            "exported_at": datetime.now().isoformat(),
            "model": st.session_state.current_model,
            "messages": st.session_state.messages
        }, indent=2)
        st.download_button("Download Chat Export", file, "chat_export.json", "application/json")
    st.session_state.export_chat = False

# Theme Application
if st.session_state.theme == "light":
    st.markdown("""
    <style>
    :root {
        --bg-primary: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 50%, #f1f5f9 100%);
        --bg-secondary: rgba(255, 255, 255, 0.8);
        --bg-tertiary: rgba(248, 250, 252, 0.9);
        --text-primary: #0f0f23;
        --text-secondary: #475569;
        --text-muted: #64748b;
        --border-color: rgba(99, 102, 241, 0.15);
    }
    .stApp { background: var(--bg-primary) !important; color: var(--text-primary) !important; }
    </style>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
render_header()

# --------------------------------------------------
# ✨ UPGRADED Welcome / Landing Screen
# --------------------------------------------------
if not st.session_state.messages:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    .welcome-canvas {
        position: relative;
        padding: 56px 40px 48px;
        margin: 0 0 40px;
        border-radius: 28px;
        overflow: hidden;
        background:
            radial-gradient(ellipse 80% 60% at 50% -10%, rgba(124,127,247,0.18) 0%, transparent 65%),
            radial-gradient(ellipse 50% 40% at 90% 80%,  rgba(244,114,182,0.10) 0%, transparent 60%),
            radial-gradient(ellipse 40% 40% at 10% 90%,  rgba(167,139,250,0.10) 0%, transparent 60%),
            linear-gradient(160deg, rgba(14,14,35,0.97) 0%, rgba(10,10,26,0.99) 100%);
        border: 1px solid rgba(255,255,255,0.065);
        box-shadow: 0 32px 80px rgba(0,0,0,0.55), 0 1px 0 rgba(255,255,255,0.08) inset;
    }

    /* animated mesh grid */
    .welcome-canvas::before {
        content: '';
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(124,127,247,0.045) 1px, transparent 1px),
            linear-gradient(90deg, rgba(124,127,247,0.045) 1px, transparent 1px);
        background-size: 48px 48px;
        mask-image: radial-gradient(ellipse 80% 70% at 50% 50%, black 30%, transparent 100%);
        animation: wc-grid-breathe 6s ease-in-out infinite;
        pointer-events: none;
    }
    @keyframes wc-grid-breathe {
        0%, 100% { opacity: 0.45; }
        50%       { opacity: 1.0; }
    }

    /* floating orb */
    .welcome-canvas::after {
        content: '';
        position: absolute;
        top: -80px; left: -80px;
        width: 300px; height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(124,127,247,0.14) 0%, transparent 70%);
        animation: wc-orb-drift 9s ease-in-out infinite alternate;
        pointer-events: none;
    }
    @keyframes wc-orb-drift {
        0%   { transform: translate(0, 0) scale(1); }
        100% { transform: translate(50px, 35px) scale(1.2); }
    }

    /* ── BADGE ── */
    .wc-badge {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 5px 14px 5px 8px;
        background: rgba(124,127,247,0.12);
        border: 1px solid rgba(124,127,247,0.3);
        border-radius: 30px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.78rem;
        font-weight: 500;
        color: #c4c4f5;
        letter-spacing: 0.03em;
        margin-bottom: 22px;
        position: relative;
        z-index: 1;
        animation: wc-badge-in 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
    }
    @keyframes wc-badge-in {
        from { opacity: 0; transform: translateY(-10px) scale(0.9); }
        to   { opacity: 1; transform: translateY(0) scale(1); }
    }
    .wc-badge-dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: #818cf8;
        box-shadow: 0 0 8px #818cf8;
        animation: wc-dot-pulse 2s ease-in-out infinite;
    }
    @keyframes wc-dot-pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.5; transform: scale(0.75); }
    }

    /* ── HEADLINE ── */
    .wc-headline {
        font-family: 'Syne', sans-serif;
        font-weight: 900;
        font-size: clamp(2.2rem, 5vw, 3.4rem);
        line-height: 1.08;
        letter-spacing: -0.03em;
        color: #f0f0ff;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
        animation: wc-headline-in 0.6s cubic-bezier(0.22,1,0.36,1) 0.1s both;
    }
    @keyframes wc-headline-in {
        from { opacity: 0; transform: translateY(18px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .wc-headline-grad {
        background: linear-gradient(135deg, #a5b4fc 0%, #f0abfc 55%, #fb7185 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* ── SUBTITLE ── */
    .wc-sub {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.05rem;
        font-weight: 300;
        color: #6868a0;
        line-height: 1.75;
        max-width: 540px;
        margin: 0 0 38px;
        position: relative;
        z-index: 1;
        animation: wc-sub-in 0.6s ease 0.2s both;
    }
    @keyframes wc-sub-in {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ── STATS ROW ── */
    .wc-stats {
        display: flex;
        gap: 28px;
        margin-bottom: 44px;
        position: relative;
        z-index: 1;
        animation: wc-stats-in 0.6s ease 0.28s both;
        flex-wrap: wrap;
        align-items: center;
    }
    @keyframes wc-stats-in {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .wc-stat {
        display: flex;
        flex-direction: column;
        gap: 3px;
    }
    .wc-stat-val {
        font-family: 'Syne', sans-serif;
        font-size: 1.55rem;
        font-weight: 800;
        background: linear-gradient(135deg, #e0e0ff, #a5b4fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }
    .wc-stat-lbl {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.7rem;
        color: #3e3e62;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .wc-stat-div {
        width: 1px;
        height: 36px;
        background: rgba(255,255,255,0.07);
        align-self: center;
    }

    /* ── FEATURE CARDS ── */
    .wc-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        position: relative;
        z-index: 1;
        animation: wc-cards-in 0.7s ease 0.36s both;
    }
    @keyframes wc-cards-in {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .wc-card {
        background: rgba(255,255,255,0.025);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 16px;
        padding: 20px 16px;
        transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
        position: relative;
        overflow: hidden;
        cursor: default;
    }
    .wc-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: var(--card-accent, linear-gradient(90deg,#7c7ff7,#a78bfa));
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .wc-card:hover {
        background: rgba(124,127,247,0.07);
        border-color: rgba(124,127,247,0.22);
        transform: translateY(-6px);
        box-shadow: 0 20px 44px rgba(0,0,0,0.35);
    }
    .wc-card:hover::before { opacity: 1; }
    .wc-card-icon {
        font-size: 1.65rem;
        margin-bottom: 11px;
        display: block;
        transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1);
        filter: drop-shadow(0 2px 6px rgba(0,0,0,0.3));
    }
    .wc-card:hover .wc-card-icon { transform: scale(1.18) rotate(-6deg); }
    .wc-card-title {
        font-family: 'Syne', sans-serif;
        font-size: 0.88rem;
        font-weight: 700;
        color: #d0d0f0;
        margin-bottom: 6px;
        letter-spacing: -0.01em;
    }
    .wc-card-desc {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.775rem;
        color: #484862;
        line-height: 1.55;
        font-weight: 300;
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 900px) {
        .wc-grid { grid-template-columns: repeat(2, 1fr); }
        .wc-headline { font-size: 2rem; }
    }
    @media (max-width: 560px) {
        .welcome-canvas { padding: 36px 20px 32px; border-radius: 18px; }
        .wc-grid { grid-template-columns: 1fr 1fr; gap: 8px; }
        .wc-stats { gap: 16px; }
        .wc-stat-div { display: none; }
        .wc-headline { font-size: 1.75rem; }
    }
    </style>

    <div class="welcome-canvas">

      <div class="wc-badge">
        <span class="wc-badge-dot"></span>
        AI-Powered Learning Assistant
      </div>

      <div class="wc-headline">
        Clear every doubt.<br>
        <span class="wc-headline-grad">Instantly.</span>
      </div>

      <p class="wc-sub">
        Upload documents, paste questions, or describe what's confusing you —
        and get step-by-step explanations powered by the world's fastest AI models.
      </p>

      <div class="wc-stats">
        <div class="wc-stat">
          <span class="wc-stat-val">3</span>
          <span class="wc-stat-lbl">AI Models</span>
        </div>
        <div class="wc-stat-div"></div>
        <div class="wc-stat">
          <span class="wc-stat-val">&lt;2s</span>
          <span class="wc-stat-lbl">Avg Response</span>
        </div>
        <div class="wc-stat-div"></div>
        <div class="wc-stat">
          <span class="wc-stat-val">46+</span>
          <span class="wc-stat-lbl">Languages</span>
        </div>
        <div class="wc-stat-div"></div>
        <div class="wc-stat">
          <span class="wc-stat-val">&#8734;</span>
          <span class="wc-stat-lbl">Questions</span>
        </div>
      </div>

      <div class="wc-grid">
        <div class="wc-card" style="--card-accent:linear-gradient(90deg,#7c7ff7,#a78bfa);">
          <span class="wc-card-icon">🤖</span>
          <div class="wc-card-title">Multi-Model AI</div>
          <div class="wc-card-desc">LLaMA, Qwen Vision &amp; more — pick the best tool for your question.</div>
        </div>
        <div class="wc-card" style="--card-accent:linear-gradient(90deg,#f472b6,#fb7185);">
          <span class="wc-card-icon">📎</span>
          <div class="wc-card-title">File Upload</div>
          <div class="wc-card-desc">PDFs, images, and text files processed in seconds.</div>
        </div>
        <div class="wc-card" style="--card-accent:linear-gradient(90deg,#34d399,#06b6d4);">
          <span class="wc-card-icon">⚡</span>
          <div class="wc-card-title">Groq-Powered</div>
          <div class="wc-card-desc">Lightning-fast inference — answers before you finish reading.</div>
        </div>
        <div class="wc-card" style="--card-accent:linear-gradient(90deg,#fbbf24,#f97316);">
          <span class="wc-card-icon">💾</span>
          <div class="wc-card-title">Export History</div>
          <div class="wc-card-desc">Download and revisit every learning session as JSON.</div>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Chat Area
# --------------------------------------------------
render_chat(st.session_state.messages)

# --------------------------------------------------
# Input Bar Container
# --------------------------------------------------
st.markdown("""
<style>
.input-container {
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
    padding: var(--spacing-lg);
    border-radius: var(--border-radius) var(--border-radius) 0 0;
    margin: 0 -1rem -1rem;
    box-shadow: 0 -4px 12px rgba(0,0,0,0.1);
}
@media (max-width: 768px) {
    .input-container { padding: var(--spacing-md) !important; margin: 0 !important; border-radius: 0 !important; }
}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# --------------------------------------------------
# Model Compatibility Check
# --------------------------------------------------
if st.session_state.files_buffer:
    contains_image = any(f.type.startswith("image") for f in st.session_state.files_buffer)
    contains_pdf = any(f.type == "application/pdf" for f in st.session_state.files_buffer)
    if (contains_image or contains_pdf) and st.session_state.current_model != "hf-vision":
        st.warning("⚠️ This model cannot process files. Please switch to **Qwen2-VL (Vision)**.")

# --------------------------------------------------
# File Preview
# --------------------------------------------------
if st.session_state.files_buffer:
    st.markdown("""
    <style>
    .file-preview-container {
        background: linear-gradient(135deg, var(--bg-secondary), var(--bg-tertiary));
        border-radius: var(--border-radius);
        padding: var(--spacing-md);
        margin-bottom: var(--spacing-md);
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-medium);
        backdrop-filter: blur(10px);
        animation: slideInRight 0.4s ease-out;
        max-width: 1400px;
        margin-left: auto;
        margin-right: auto;
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(-20px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    .file-preview-header {
        display: flex; align-items: center; justify-content: space-between;
        margin-bottom: var(--spacing-sm); padding-bottom: var(--spacing-xs);
        border-bottom: 1px solid var(--border-color);
    }
    .file-preview-title {
        font-size: var(--font-size-sm); font-weight: 600; color: var(--primary-color);
        text-transform: uppercase; letter-spacing: 0.05em;
        display: flex; align-items: center; gap: var(--spacing-sm);
    }
    .file-count-badge {
        background: rgba(99,102,241,0.2); color: var(--text-secondary);
        padding: var(--spacing-xs) var(--spacing-sm); border-radius: var(--radius-sm);
        font-size: var(--font-size-xs); font-weight: 700; border: 1px solid var(--primary-color);
    }
    .file-item {
        background: rgba(255,255,255,0.05); border-radius: var(--border-radius);
        padding: var(--spacing-sm); margin-bottom: var(--spacing-xs);
        border: 1px solid var(--border-color); transition: var(--transition);
        display: flex; align-items: center; gap: var(--spacing-sm);
        position: relative; overflow: hidden; animation: slideIn 0.3s ease-out;
    }
    .file-item::before {
        content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 100%;
        background: linear-gradient(180deg, var(--primary-color), var(--secondary-color));
        opacity: 0; transition: var(--transition);
    }
    .file-item:hover {
        background: rgba(255,255,255,0.08); border-color: var(--primary-color);
        transform: translateX(4px); box-shadow: var(--shadow-medium);
    }
    .file-item:hover::before { opacity: 1; }
    .file-icon { font-size: 1.75rem; min-width: 2.5rem; display: flex; align-items: center; justify-content: center; }
    .file-info { flex: 1; min-width: 0; }
    .file-name { color: var(--text-primary); font-size: var(--font-size-base); font-weight: 600;
        margin-bottom: var(--spacing-xs); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .file-meta { display: flex; align-items: center; gap: var(--spacing-sm);
        font-size: var(--font-size-sm); color: var(--text-muted); }
    .file-type-badge {
        background: rgba(99,102,241,0.15); color: var(--primary-color);
        padding: var(--spacing-xs) var(--spacing-sm); border-radius: var(--radius-sm);
        text-transform: uppercase; font-weight: 600; font-size: var(--font-size-xs);
        letter-spacing: 0.05em; border: 1px solid var(--primary-color);
    }
    .clear-all-section { margin-top: var(--spacing-sm); padding-top: var(--spacing-sm); border-top: 1px solid var(--border-color); }
    @keyframes slideIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 768px) {
        .file-preview-container { padding: var(--spacing-sm); margin: 0; }
        .file-item { flex-direction: column; text-align: center; gap: var(--spacing-sm); padding: var(--spacing-md); }
        .file-info { width: 100%; text-align: center; }
        .file-name { white-space: normal; word-break: break-word; text-align: center; }
        .file-meta { justify-content: center; flex-wrap: wrap; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='file-preview-container'>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='file-preview-header'>
        <div class='file-preview-title'>
            📎 Attached Files
            <span class='file-count-badge'>{len(st.session_state.files_buffer)}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    for i, f in enumerate(st.session_state.files_buffer):
        file_type = f.type.lower()
        icon, type_label = "📎", "FILE"
        if "pdf" in file_type:
            icon, type_label = "📄", "PDF"
        elif "image" in file_type or "png" in file_type or "jpg" in file_type or "jpeg" in file_type:
            icon, type_label = "🖼️", "IMAGE"
        elif "text" in file_type or "txt" in file_type:
            icon, type_label = "📝", "TEXT"

        size_mb = f.size / (1024 * 1024)
        size_display = f"{round(f.size / 1024, 1)} KB" if size_mb < 0.1 else f"{round(size_mb, 2)} MB"

        cols_file = st.columns([0.08, 0.75, 0.17])
        with cols_file[0]:
            st.markdown(f"<div class='file-icon'>{icon}</div>", unsafe_allow_html=True)
        with cols_file[1]:
            st.markdown(f"""
            <div class='file-info'>
                <div class='file-name' title='{f.name}'>{f.name}</div>
                <div class='file-meta'>
                    <span>💾 {size_display}</span>
                    <span class='file-type-badge'>{type_label}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with cols_file[2]:
            if st.button("🗑️", key=f"rm-file-{i}", help=f"Remove {f.name}", use_container_width=True):
                st.session_state.files_buffer.pop(i)
                st.session_state.files_processed.discard((f.name, f.size))
                st.rerun()

    st.markdown("<div class='clear-all-section'>", unsafe_allow_html=True)
    if st.button("🗑️ Clear All Files", type="secondary", use_container_width=True, key="clear_all_files"):
        st.session_state.files_buffer = []
        st.session_state.files_processed = set()
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# --------------------------------------------------
# Input Row
# --------------------------------------------------
cols = st.columns([0.6, 8.5, 0.9])

with cols[0]:
    uploaded_files = st.file_uploader(
        "Upload",
        type=["pdf", "jpg", "jpeg", "png", "txt"],
        accept_multiple_files=True,
        key=f"files_{st.session_state.uploader_key}",
        label_visibility="collapsed"
    )

with cols[1]:
    question = st.text_input(
        "Ask",
        placeholder="Ask your doubt...",
        label_visibility="collapsed",
        key=f"user_input_{st.session_state.input_key}"
    )

with cols[2]:
    send_disabled = st.session_state.processing_response
    send = st.button("➤", use_container_width=True, type="primary", disabled=send_disabled)

# --------------------------------------------------
# Process Uploaded Files
# --------------------------------------------------
if uploaded_files:
    new_files_added = False
    for file in uploaded_files:
        size_mb = file.size / (1024 * 1024)
        file_id = (file.name, file.size)
        if file_id in st.session_state.files_processed:
            continue
        if size_mb > MAX_FILE_MB:
            st.toast(f"❌ {file.name} is larger than {MAX_FILE_MB}MB", icon="⚠️")
            continue
        st.session_state.files_buffer.append(file)
        st.session_state.files_processed.add(file_id)
        new_files_added = True
    if new_files_added:
        st.rerun()

# --------------------------------------------------
# Send Message Logic
# --------------------------------------------------
if send and not st.session_state.processing_response:
    user_text = question.strip()
    if user_text or st.session_state.files_buffer:
        st.session_state.processing_response = True
        prepared_files = []
        for file in st.session_state.files_buffer:
            prepared_files.append({"name": file.name, "type": file.type, "data": encode_file(file)})
        safe_question = sanitize_content(user_text) if user_text else "[Files uploaded]"
        st.session_state.messages.append({
            "role": "user",
            "content": safe_question,
            "files": prepared_files,
            "timestamp": datetime.now().isoformat()
        })
        st.session_state.files_buffer = []
        st.session_state.files_processed = set()
        st.session_state.input_key += 1
        st.session_state.uploader_key += 1
        st.rerun()

# --------------------------------------------------
# Process AI Response
# --------------------------------------------------
if st.session_state.messages and st.session_state.processing_response:
    last = st.session_state.messages[-1]
    if last["role"] == "user":
        with st.spinner("🤔 Thinking..."):
            try:
                ai_reply = ai.generate_response(
                    question=last["content"],
                    model=st.session_state.current_model,
                    temperature=0.7,
                    files=last.get("files", [])
                )
                ai_reply = sanitize_content(ai_reply)
            except Exception as e:
                ai_reply = f"❌ AI Error: {str(e)}"
            if ai_reply:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_reply,
                    "model": st.session_state.current_model,
                    "timestamp": datetime.now().isoformat()
                })
        st.session_state.processing_response = False
        st.rerun()

# --------------------------------------------------
# Clear Chat Button
# --------------------------------------------------
if st.button("🧹 Clear Chat", type="secondary", use_container_width=True):
    st.session_state.messages = []
    st.session_state.files_buffer = []
    st.session_state.files_processed = set()
    st.session_state.input_key += 1
    st.session_state.uploader_key += 1
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
