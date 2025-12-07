# ui/pages/3_Models.py
import streamlit as st
from pathlib import Path

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AI Models - Doubt Tutor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Immediately hide sidebar
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------
css_path = Path("ui/styles/style.css")
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Enhanced styling
st.markdown("""
<style>
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    --success: #10b981;
    --bg-card: rgba(20, 20, 40, 0.85);
    --bg-elevated: rgba(30, 30, 60, 0.95);
    --text-primary: #ffffff;
    --text-secondary: #e2e8f0;
    --text-muted: #94a3b8;
    --border-subtle: rgba(99, 102, 241, 0.1);
    --border-default: rgba(99, 102, 241, 0.2);
    --border-strong: rgba(99, 102, 241, 0.4);
    --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.25);
    --shadow-xl: 0 24px 48px rgba(0, 0, 0, 0.35);
    --shadow-glow: 0 0 32px rgba(99, 102, 241, 0.4);
    --radius-xl: 20px;
    --radius-2xl: 24px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.block-container {
    padding: 2rem 1rem 3rem;
    max-width: 1400px;
    margin: 0 auto;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.hero-section {
    background: linear-gradient(135deg, var(--border-subtle), rgba(168, 85, 247, 0.08));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: 3rem 2rem;
    margin: 1.5rem 0 3rem;
    border: 1px solid var(--border-default);
    text-align: center;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
    animation: fadeInDown 0.6s ease-out;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
    opacity: 0.7;
}

.hero-title {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    letter-spacing: -0.025em;
    line-height: 1.1;
}

.hero-subtitle {
    font-size: 1.125rem;
    color: var(--text-muted);
    line-height: 1.8;
    max-width: 900px;
    margin: 0 auto;
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.model-card {
    background: linear-gradient(135deg, var(--bg-card), var(--bg-elevated));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: 2rem;
    border: 1px solid var(--border-default);
    transition: var(--transition);
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out both;
    opacity: 0;
}

.model-card:nth-child(1) { animation-delay: 0.1s; }
.model-card:nth-child(2) { animation-delay: 0.2s; }
.model-card:nth-child(3) { animation-delay: 0.3s; }
.model-card:nth-child(4) { animation-delay: 0.4s; }

.model-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    opacity: 0;
    transition: var(--transition);
}

.model-card:hover {
    transform: translateY(-4px);
    border-color: var(--border-strong);
    box-shadow: var(--shadow-xl);
}

.model-card:hover::before {
    opacity: 1;
}

.model-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.model-icon {
    font-size: 3rem;
    width: 72px;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
    border-radius: 16px;
    border: 1px solid var(--border-subtle);
    flex-shrink: 0;
    transition: var(--transition);
}

.model-card:hover .model-icon {
    transform: scale(1.05) rotate(5deg);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.model-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.2;
}

.model-description {
    font-size: 0.9375rem;
    color: var(--text-muted);
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

.model-specs {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.spec-badge {
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    padding: 0.25rem 1rem;
    font-size: 0.875rem;
    color: var(--primary-light);
    font-weight: 500;
    transition: var(--transition);
}

.model-card:hover .spec-badge {
    background: rgba(99, 102, 241, 0.25);
    transform: translateY(-2px);
}

.best-for {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.1));
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 12px;
    padding: 0.5rem 1rem;
    margin-top: 1rem;
    display: inline-block;
    transition: var(--transition);
}

.model-card:hover .best-for {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.2);
}

.best-for-text {
    color: var(--success);
    font-weight: 600;
    font-size: 0.875rem;
}

.selection-card {
    background: linear-gradient(135deg, var(--border-subtle), rgba(168, 85, 247, 0.05));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: 2rem;
    border: 1px solid var(--border-strong);
    margin: 1.5rem 0;
    box-shadow: var(--shadow-lg);
    animation: fadeInUp 0.6s ease-out;
}

.selection-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.stSelectbox div[data-baseweb="select"] {
    background: linear-gradient(135deg, var(--bg-elevated), var(--bg-card)) !important;
    border-radius: 16px !important;
    border: 1px solid var(--border-default) !important;
    transition: var(--transition) !important;
}

.stSelectbox div[data-baseweb="select"]:hover {
    border-color: var(--border-strong) !important;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: transparent !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    padding: 1rem 1.5rem !important;
}

.comparison-section {
    background: linear-gradient(135deg, var(--bg-elevated), var(--bg-card));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: 2rem;
    border: 1px solid var(--border-subtle);
    margin: 1.5rem 0;
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.detail-card {
    background: linear-gradient(135deg, var(--bg-elevated), var(--bg-card));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: 2rem;
    border: 1px solid var(--border-subtle);
    margin: 1.5rem 0;
}

.detail-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
}

.detail-content {
    font-size: 0.9375rem;
    color: var(--text-secondary);
    line-height: 1.8;
}

.detail-content strong {
    color: var(--primary-light);
}

.cta-section {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: 3rem 1.5rem;
    margin: 3rem 0 2rem;
    text-align: center;
    border: 1px solid var(--border-strong);
    box-shadow: var(--shadow-lg);
    animation: fadeInUp 0.6s ease-out 0.4s both;
}

.cta-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
}

.cta-description {
    font-size: 1.125rem;
    color: var(--text-muted);
    margin-bottom: 2rem;
}

.stButton > button {
    border-radius: 16px;
    font-weight: 600;
    padding: 1rem 1.5rem;
    transition: var(--transition);
    border: 1px solid var(--border-default);
    background: linear-gradient(135deg, var(--bg-elevated), var(--bg-card));
    color: var(--text-secondary);
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.5s;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-glow);
    border-color: var(--primary);
    color: var(--text-primary);
    background: linear-gradient(135deg, var(--primary), var(--secondary));
}

.stAlert {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05)) !important;
    border-radius: var(--radius-xl) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
    padding: 1.5rem !important;
    margin: 1.5rem 0 !important;
}

hr {
    margin: 3rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-default), transparent);
}

@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .model-header { 
        flex-direction: column;
        text-align: center;
    }
    .model-icon { 
        width: 60px;
        height: 60px;
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Import header
from ui.components.header import render_header

# Render Header
render_header()

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-title">AI Models</div>
    <div class="hero-subtitle">
        Explore our curated collection of AI models powered by Groq, each optimized for different types 
        of learning challenges. Choose the perfect model for your doubt—whether it's 
        text-heavy, visual, or requires advanced reasoning.
    </div>
</div>
""", unsafe_allow_html=True)

# Models Information
models_info = {
    "llama-3.1-8b-instant": {
        "icon": "🦙",
        "title": "Llama 3.1 (8B) – Instant",
        "desc": "Meta's fast, reliable lightweight model. Excellent for math, language, science, and quick explanations.",
        "specs": ["8B parameters", "Very fast", "Text-only"],
        "best_for": "Quick text queries, math steps, grammar, and concept explanations"
    },
    "mistral": {
        "icon": "🌬️",
        "title": "Mistral 7B",
        "desc": "Balanced open-source model. Great for creative writing, summaries, and interdisciplinary topics.",
        "specs": ["7B parameters", "Balanced output", "Stable reasoning"],
        "best_for": "Creative writing, history, essays, and brainstorming"
    },
    "deepseek-r1": {
        "icon": "🔍",
        "title": "DeepSeek R1 – Reasoning",
        "desc": "Advanced reasoning model designed for logic, code explanations, and step-by-step STEM problems.",
        "specs": ["Deep reasoning", "STEM-focused", "Chain-of-thought"],
        "best_for": "Coding help, algorithm debugging, complex math & physics"
    },
    "hf-vision": {
        "icon": "🖼️",
        "title": "Qwen2-VL (Vision) – HuggingFace",
        "desc": "A multimodal model capable of understanding images, charts, diagrams, and screenshots. Uses the free HuggingFace Inference API.",
        "specs": ["Vision + Text", "Diagram analysis", "Screenshot understanding"],
        "best_for": "Image-based questions: diagrams, handwritten notes, screenshots"
    }
}

# Display model cards
st.markdown('<h3 style="text-align: center; color: var(--text-primary); font-size: 1.5rem; margin-bottom: 2rem;">🤖 Available Models</h3>')

for model_key, info in models_info.items():
    st.markdown(f"""
    <div class="model-card">
        <div class="model-header">
            <div class="model-icon">{info['icon']}</div>
            <div class="model-title">{info['title']}</div>
        </div>
        <div class="model-description">
            {info['desc']}
        </div>
        <div class="model-specs">
            {''.join([f'<span class="spec-badge">{spec}</span>' for spec in info['specs']])}
        </div>
        <div class="best-for">
            <span class="best-for-text">✨ Best for: {info['best_for']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Model Selection
st.markdown("""
<div class="selection-card">
    <div class="selection-title">🎯 Select Your Model</div>
</div>
""", unsafe_allow_html=True)

st.markdown("Choose your preferred model below. The selection will be saved and the badge in the header will update instantly.")

model_options = list(models_info.keys())
default_model = st.session_state.get("model_select_professional", "llama-3.1-8b-instant")
index = model_options.index(default_model) if default_model in model_options else 0

model_display_names = {
    "llama-3.1-8b-instant": "🦙 Llama 3.1 (8B) – Fast text responses",
    "mistral": "🌬️ Mistral – Creative & balanced",
    "deepseek-r1": "🔍 DeepSeek R1 – Advanced reasoning",
    "hf-vision": "🖼️ Qwen2-VL Vision – Image understanding"
}

selected_display = st.selectbox(
    "Choose your AI model",
    options=model_options,
    format_func=lambda x: model_display_names[x],
    index=index,
    help="Select a model based on your learning needs"
)

if selected_display != st.session_state.get("model_select_professional", "llama-3.1-8b-instant"):
    st.session_state["model_select_professional"] = selected_display
    st.success(f"✅ Successfully switched to **{models_info[selected_display]['title']}**!")
    st.balloons()
    st.rerun()

# Show current model info
st.markdown(f"""
<div class="detail-card">
    <div class="detail-title">📋 Current Model: {models_info[default_model]['title']}</div>
    <div class="detail-content">
        <strong>Best for:</strong> {models_info[default_model]['best_for']}  
        <br><br>
        Ready to start learning! Head back to the home page to begin chatting with your selected model.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Quick Comparison
st.markdown('<h3 style="text-align: center; color: var(--text-primary); font-size: 1.5rem; margin-bottom: 2rem;">📊 Quick Comparison</h3>')

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<h4 style="color: var(--primary); font-size: 1.125rem;">⚡ Speed</h4>')
    st.markdown('<div style="color: var(--text-secondary); line-height: 1.8;"><strong>Fastest:</strong> Llama 3.1 Instant<br><strong>Moderate:</strong> Mistral<br><strong>Thoughtful:</strong> DeepSeek R1<br><strong>Vision:</strong> Qwen2-VL (HF)</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<h4 style="color: var(--secondary); font-size: 1.125rem;">🎯 Specialization</h4>')
    st.markdown('<div style="color: var(--text-secondary); line-height: 1.8;"><strong>Text:</strong> Llama 3.1, Mistral<br><strong>Vision:</strong> HF Qwen2-VL<br><strong>Code/Logic:</strong> DeepSeek R1</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<h4 style="color: var(--accent); font-size: 1.125rem;">💡 Use Case</h4>')
    st.markdown('<div style="color: var(--text-secondary); line-height: 1.8;"><strong>Quick Answers:</strong> Llama 3.1<br><strong>Deep Learning:</strong> DeepSeek R1<br><strong>Creative:</strong> Mistral</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <div class="cta-title">🚀 Ready to Start?</div>
    <div class="cta-description">
        Your model is selected. Let's tackle those doubts together!
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    if st.button("🚀 Start Learning", use_container_width=True, type="primary"):
        st.switch_page("app.py")

with col2:
    if st.button("📖 How It Works", use_container_width=True):
        st.switch_page("pages/2_How_It_Works.py")

with col3:
    if st.button("ℹ️ About Us", use_container_width=True):
        st.switch_page("pages/1_About.py")

st.markdown("<br><br>", unsafe_allow_html=True)