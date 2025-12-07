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
    initial_sidebar_state="collapsed"
)

# Immediately hide sidebar to prevent flash - inject CSS as early as possible
hide_sidebar_css = """
<style>
/* Aggressively hide sidebar from the start */
section[data-testid="stSidebar"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    min-width: 0 !important;
    max-width: 0 !important;
    opacity: 0 !important;
    transform: translateX(-100%) !important;
    transition: all 0s !important; /* No transition to avoid flash */
}
/* Hide any sidebar-related elements */
[role="complementary"], .css-1d391kg, .css-1v3f6k1 {
    display: none !important;
}
</style>
"""
st.markdown(hide_sidebar_css, unsafe_allow_html=True)

# --------------------------------------------------
# Global Styles - Enhanced Modern UI
# --------------------------------------------------
global_css = """
<style>
/* Root variables for consistent theming */
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
    --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* App-wide background gradient */
.stApp {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-tertiary) 100%);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Enhanced scrollbars */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-track {
    background: var(--bg-secondary);
}
::-webkit-scrollbar-thumb {
    background: var(--primary-color);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--primary-hover);
}

/* Container enhancements */
.stMarkdown {
    font-size: 1rem;
    line-height: 1.6;
}
.element-container {
    padding-top: 1rem;
}

/* Button enhancements */
.stButton > button {
    border-radius: var(--border-radius);
    border: none;
    font-weight: 600;
    transition: var(--transition);
    box-shadow: var(--shadow-light);
}
.stButton > button:hover {
    box-shadow: var(--shadow-medium);
    transform: translateY(-1px);
}
.stButton > button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
}

/* Input enhancements */
.stTextInput > div > div > input {
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
    background: var(--bg-secondary);
    color: var(--text-primary);
    padding: 0.75rem 1rem;
    transition: var(--transition);
}
.stTextInput > div > div > input:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

/* Toast enhancements */
.stAlert, .stToast {
    border-radius: var(--border-radius);
    border: none;
    box-shadow: var(--shadow-heavy);
}
</style>
"""
st.markdown(global_css, unsafe_allow_html=True)

# Load custom CSS file if exists
css_path = Path("ui/styles/style.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# Additional inline CSS for file upload (enhanced with theme vars)
file_uploader_css = """
<style>
/* File uploader paperclip - Enhanced */
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
div[data-testid="stFileUploader"] section > div {
    display: none !important;
}

div[data-testid="stFileUploader"] * {
    font-size: 0 !important;
    color: transparent !important;
}

div[data-testid="stFileUploader"] label {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    cursor: pointer !important;
    z-index: 2 !important;
    margin: 0 !important;
    padding: 0 !important;
}

div[data-testid="stFileUploader"] section {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background: transparent !important;
    border: none !important;
}

div[data-testid="stFileUploader"] input[type="file"] {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    opacity: 0 !important;
    cursor: pointer !important;
    z-index: 10 !important;
}
</style>
"""
st.markdown(file_uploader_css, unsafe_allow_html=True)

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------
def encode_file(file):
    """Encode file to base64"""
    file.seek(0)
    return base64.b64encode(file.read()).decode("utf-8")

def sanitize_content(text):
    """Sanitize content while preserving valid formatting"""
    if not text:
        return ""
    
    text = str(text)
    
    # Remove script tags and their content
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove dangerous HTML tags (but allow safe markdown/formatting)
    dangerous_tags = ['script', 'iframe', 'object', 'embed', 'style']
    for tag in dangerous_tags:
        text = re.sub(f'<{tag}[^>]*>.*?</{tag}>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(f'<{tag}[^>]*>', '', text, flags=re.IGNORECASE)
    
    # Remove class and style attributes that could inject UI elements
    text = re.sub(r'\s+(class|style)\s*=\s*["\'][^"\']*["\']', '', text)
    
    # Remove known UI injection class names
    ui_classes = ['bubble', 'message', 'timestamp', 'meta', 'wrapper']
    for cls in ui_classes:
        text = re.sub(f'class=["\'][^"\']*{cls}[^"\']*["\']', '', text, flags=re.IGNORECASE)
    
    # Clean excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    return text.strip()

# --------------------------------------------------
# Constants
# --------------------------------------------------
MAX_FILE_MB = 10

# --------------------------------------------------
# Instances
# --------------------------------------------------
ai = AIManager()

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------
def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        "messages": [],
        "current_model": "llama-3.1-8b-instant",
        "theme": "dark",
        "pdf_fullscreen": None,
        "files_buffer": [],
        "input_key": 0,
        "uploader_key": 0,
        "processing_response": False,
        "files_processed": set()  # Track processed files to avoid duplicates
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# --------------------------------------------------
# Clean existing messages on first run
# --------------------------------------------------
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

# --------------------------------------------------
# Sync Model from Header
# --------------------------------------------------
if "model_select_professional" in st.session_state:
    st.session_state.current_model = st.session_state.model_select_professional

# --------------------------------------------------
# Export Handler
# --------------------------------------------------
if st.session_state.get("export_chat"):
    if st.session_state.messages:
        file = json.dumps({
            "exported_at": datetime.now().isoformat(),
            "model": st.session_state.current_model,
            "messages": st.session_state.messages
        }, indent=2)

        st.download_button(
            "Download Chat Export",
            file,
            "chat_export.json",
            "application/json"
        )

    st.session_state.export_chat = False

# --------------------------------------------------
# Theme Application (Enhanced for light mode)
# --------------------------------------------------
if st.session_state.theme == "light":
    light_theme_css = """
    <style>
    :root {
        --bg-primary: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 50%, #f1f5f9 100%);
        --bg-secondary: rgba(255, 255, 255, 0.8);
        --bg-tertiary: rgba(248, 250, 252, 0.9);
        --text-primary: #0f0f23;
        --text-secondary: #475569;
        --text-muted: #64748b;
        --border-color: rgba(99, 102, 241, 0.15);
        --primary-color: #6366f1;
        --primary-hover: #5856eb;
    }
    .stApp {
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }
    /* Invert shadows for light mode if needed */
    .bubble, .card, .chat {
        filter: none;
    }
    </style>
    """
    st.markdown(light_theme_css, unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
render_header()

st.markdown('<div class="content">', unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section (Enhanced with better layout and animations)
# --------------------------------------------------
welcome_css = """
<style>
.welcome {
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.1));
    border-radius: var(--border-radius);
    margin-bottom: 2rem;
    box-shadow: var(--shadow-medium);
    backdrop-filter: blur(10px);
    border: 1px solid var(--border-color);
    animation: fadeInUp 0.6s ease-out;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.welcome h1 {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.025em;
}
.welcome p {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}
.card {
    background: var(--bg-secondary);
    border-radius: var(--border-radius);
    padding: 1.5rem;
    text-align: center;
    border: 1px solid var(--border-color);
    transition: var(--transition);
    box-shadow: var(--shadow-light);
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
    opacity: 0;
    transition: var(--transition);
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-heavy);
    background: var(--bg-tertiary);
}
.card:hover::before {
    opacity: 1;
}
.card-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}
.card-desc {
    color: var(--text-muted);
    font-size: 0.95rem;
    line-height: 1.5;
}
</style>
"""
st.markdown(welcome_css, unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown("""
    <div class="welcome">
        <h1>🤔 Welcome to Doubt Tutor</h1>
        <p>Upload your documents, ask any question, and receive instant AI-powered explanations tailored to your needs.</p>
    </div>
    <div class="features">
        <div class="card"><div class="card-title">🤖 Smart AI</div><div class="card-desc">Advanced multi-model support for precise answers</div></div>
        <div class="card"><div class="card-title">📎 Multi-Upload</div><div class="card-desc">Seamlessly handle PDFs, images, and text files</div></div>
        <div class="card"><div class="card-title">⚡ Instant Help</div><div class="card-desc">Context-aware explanations that clarify doubts</div></div>
        <div class="card"><div class="card-title">💾 Export History</div><div class="card-desc">Export and revisit your learning conversations</div></div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Chat Area
# --------------------------------------------------
render_chat(st.session_state.messages)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Input Bar Container
# --------------------------------------------------
input_container_css = """
<style>
.input-container {
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
    padding: 1.5rem;
    border-radius: var(--border-radius) var(--border-radius) 0 0;
    margin: 0 -1rem -1rem;
    box-shadow: 0 -4px 12px rgba(0,0,0,0.1);
}
</style>
"""
st.markdown(input_container_css, unsafe_allow_html=True)
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# --------------------------------------------------
# Model Compatibility Check (Updated for HF Vision Model)
# --------------------------------------------------
if st.session_state.files_buffer:
    contains_image = any(f.type.startswith("image") for f in st.session_state.files_buffer)
    contains_pdf = any(f.type == "application/pdf" for f in st.session_state.files_buffer)

    # Only Qwen2-VL Vision supports file reading
    if (contains_image or contains_pdf) and st.session_state.current_model != "hf-vision":
        st.warning("⚠️ This model cannot process files. Please switch to **Qwen2-VL (Vision)**.")

# --------------------------------------------------
# Enhanced File Preview (Further polished)
# --------------------------------------------------
if st.session_state.files_buffer:
    # Enhanced CSS for file preview with vars
    file_preview_css = """
    <style>
    .file-preview-container {
        background: linear-gradient(135deg, var(--bg-secondary), var(--bg-tertiary));
        border-radius: var(--border-radius);
        padding: 1.25rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-medium);
        backdrop-filter: blur(10px);
        animation: slideInRight 0.4s ease-out;
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .file-preview-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid var(--border-color);
    }
    
    .file-preview-title {
        font-size: 0.875rem;
        font-weight: 600;
        color: var(--primary-color);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .file-count-badge {
        background: rgba(99, 102, 241, 0.2);
        color: var(--text-secondary);
        padding: 0.125rem 0.5rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid var(--primary-color);
    }
    
    .file-item {
        background: rgba(255,255,255,0.05);
        border-radius: var(--border-radius);
        padding: 0.875rem;
        margin-bottom: 0.625rem;
        border: 1px solid var(--border-color);
        transition: var(--transition);
        display: flex;
        align-items: center;
        gap: 0.75rem;
        position: relative;
        overflow: hidden;
    }
    
    .file-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 3px;
        height: 100%;
        background: linear-gradient(180deg, var(--primary-color), var(--secondary-color));
        opacity: 0;
        transition: var(--transition);
    }
    
    .file-item:hover {
        background: rgba(255,255,255,0.08);
        border-color: var(--primary-color);
        transform: translateX(4px);
        box-shadow: var(--shadow-medium);
    }
    
    .file-item:hover::before {
        opacity: 1;
    }
    
    .file-icon {
        font-size: 28px;
        min-width: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
    }
    
    .file-info {
        flex: 1;
        min-width: 0;
    }
    
    .file-name {
        color: var(--text-primary);
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.25rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    .file-meta {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 0.75rem;
        color: var(--text-muted);
    }
    
    .file-size {
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }
    
    .file-type-badge {
        background: rgba(99, 102, 241, 0.15);
        color: var(--primary-color);
        padding: 0.125rem 0.5rem;
        border-radius: 6px;
        text-transform: uppercase;
        font-weight: 600;
        font-size: 0.65rem;
        letter-spacing: 0.05em;
        border: 1px solid var(--primary-color);
    }
    
    .clear-all-section {
        margin-top: 0.75rem;
        padding-top: 0.75rem;
        border-top: 1px solid var(--border-color);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .file-item {
        animation: slideIn 0.3s ease-out;
    }
    </style>
    """
    st.markdown(file_preview_css, unsafe_allow_html=True)
    
    # Container start
    st.markdown("<div class='file-preview-container'>", unsafe_allow_html=True)
    
    # Header with file count
    st.markdown(f"""
    <div class='file-preview-header'>
        <div class='file-preview-title'>
            📎 Attached Files
            <span class='file-count-badge'>{len(st.session_state.files_buffer)}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # File items
    for i, f in enumerate(st.session_state.files_buffer):
        file_type = f.type.lower()
        
        # Enhanced icon selection
        icon = "📎"
        type_label = "FILE"
        if "pdf" in file_type:
            icon = "📄"
            type_label = "PDF"
        elif "image" in file_type or "png" in file_type or "jpg" in file_type or "jpeg" in file_type:
            icon = "🖼️"
            type_label = "IMAGE"
        elif "text" in file_type or "txt" in file_type:
            icon = "📝"
            type_label = "TEXT"
        
        # Calculate file size with better formatting
        size_mb = f.size / (1024 * 1024)
        if size_mb < 0.1:
            size_display = f"{round(f.size / 1024, 1)} KB"
        else:
            size_display = f"{round(size_mb, 2)} MB"

        # Create columns for layout
        cols_file = st.columns([0.08, 0.75, 0.17])

        with cols_file[0]:
            st.markdown(f"<div class='file-icon'>{icon}</div>", unsafe_allow_html=True)

        with cols_file[1]:
            st.markdown(f"""
            <div class='file-info'>
                <div class='file-name' title='{f.name}'>{f.name}</div>
                <div class='file-meta'>
                    <span class='file-size'>💾 {size_display}</span>
                    <span class='file-type-badge'>{type_label}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with cols_file[2]:
            if st.button("🗑️", key=f"rm-file-{i}", help=f"Remove {f.name}", use_container_width=True):
                st.session_state.files_buffer.pop(i)
                st.session_state.files_processed.discard((f.name, f.size))
                st.rerun()

    # Clear all button section
    st.markdown("<div class='clear-all-section'>", unsafe_allow_html=True)
    if st.button("🗑️ Clear All Files", type="secondary", use_container_width=True, key="clear_all_files"):
        st.session_state.files_buffer = []
        st.session_state.files_processed = set()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Container end
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Input Row (Enhanced spacing)
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
# Process uploaded files (only new ones)
# --------------------------------------------------
if uploaded_files:
    new_files_added = False
    
    for file in uploaded_files:
        size_mb = file.size / (1024 * 1024)
        file_id = (file.name, file.size)

        # Skip if already processed
        if file_id in st.session_state.files_processed:
            continue

        if size_mb > MAX_FILE_MB:
            st.toast(f"❌ {file.name} is larger than {MAX_FILE_MB}MB", icon="⚠️")
            continue

        # Add to buffer and mark as processed
        st.session_state.files_buffer.append(file)
        st.session_state.files_processed.add(file_id)
        new_files_added = True
    
    # Only rerun if new files were actually added
    if new_files_added:
        st.rerun()

# --------------------------------------------------
# Send Message Logic
# --------------------------------------------------
if send and not st.session_state.processing_response:
    user_text = question.strip()
    
    if user_text or st.session_state.files_buffer:
        # Mark as processing to prevent double-send
        st.session_state.processing_response = True
        
        # Prepare files
        prepared_files = []
        for file in st.session_state.files_buffer:
            prepared_files.append({
                "name": file.name,
                "type": file.type, 
                "data": encode_file(file)
            })

        # Sanitize user input
        safe_question = sanitize_content(user_text) if user_text else "[Files uploaded]"

        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": safe_question,
            "files": prepared_files,
            "timestamp": datetime.now().isoformat()
        })

        # Clear inputs
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
                # Get AI response
                ai_reply = ai.generate_response(
                    question=last["content"],
                    model=st.session_state.current_model,
                    temperature=0.7,
                    files=last.get("files", [])
                )
                
                # Sanitize response
                ai_reply = sanitize_content(ai_reply)
                
            except Exception as e:
                ai_reply = f"❌ AI Error: {str(e)}"

            if ai_reply:
                # Save AI message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_reply,
                    "model": st.session_state.current_model,
                    "timestamp": datetime.now().isoformat()
                })

        # Done processing
        st.session_state.processing_response = False
        st.rerun()

# Clear Chat button (moved from sidebar to input area for accessibility)
if st.button("🧹 Clear Chat", type="secondary", use_container_width=True):
    st.session_state.messages = []
    st.session_state.files_buffer = []
    st.session_state.files_processed = set()
    st.session_state.input_key += 1
    st.session_state.uploader_key += 1
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)