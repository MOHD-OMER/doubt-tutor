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

# Hide default Streamlit sidebar
st.markdown("""
<style>
section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------
css_path = Path("ui/styles/style.css")
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Professional styling for Models page
st.markdown("""
<style>
/* Global improvements */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Hero Section */
.hero-section {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(168, 85, 247, 0.08));
    border-radius: 24px;
    padding: 4rem 3rem;
    margin: 2rem 0 3rem 0;
    border: 1px solid rgba(99, 102, 241, 0.15);
    text-align: center;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: #94a3b8;
    line-height: 1.8;
    max-width: 900px;
    margin: 0 auto;
    font-weight: 400;
}

/* Model Cards */
.model-card {
    background: rgba(30, 30, 60, 0.5);
    border-radius: 20px;
    padding: 2.5rem;
    border: 1px solid rgba(99, 102, 241, 0.2);
    transition: all 0.3s ease;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}

.model-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.model-card:hover {
    transform: translateY(-4px);
    border-color: rgba(99, 102, 241, 0.4);
    box-shadow: 0 12px 32px rgba(99, 102, 241, 0.2);
    background: rgba(30, 30, 60, 0.6);
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
    width: 70px;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
    border-radius: 16px;
    border: 1px solid rgba(99, 102, 241, 0.3);
}

.model-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #e2e8f0;
}

.model-description {
    font-size: 1.05rem;
    color: #94a3b8;
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

.model-specs {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.spec-badge {
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
    color: #a5b4fc;
    font-weight: 500;
}

.best-for {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.1));
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 12px;
    padding: 0.75rem 1.25rem;
    margin-top: 1rem;
    display: inline-block;
}

.best-for-text {
    color: #10b981;
    font-weight: 600;
    font-size: 0.95rem;
}

/* Selection Section */
.selection-card {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.05));
    border-radius: 20px;
    padding: 2.5rem;
    border: 1px solid rgba(99, 102, 241, 0.25);
    margin: 2rem 0;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
}

.selection-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
}

/* Comparison Table */
.comparison-section {
    background: rgba(30, 30, 60, 0.4);
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid rgba(99, 102, 241, 0.15);
    margin: 2rem 0;
}

/* CTA Section */
.cta-section {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
    border-radius: 24px;
    padding: 3rem 2rem;
    margin: 3rem 0 2rem 0;
    text-align: center;
    border: 1px solid rgba(99, 102, 241, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.cta-title {
    font-size: 2rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
}

.cta-description {
    font-size: 1.125rem;
    color: #94a3b8;
    margin-bottom: 2rem;
}

/* Button Improvements */
.stButton > button {
    border-radius: 12px;
    font-weight: 600;
    padding: 0.75rem 1.5rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(99, 102, 241, 0.3);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
}

/* Selectbox styling */
.stSelectbox {
    margin-top: 1rem;
}

/* Divider */
hr {
    margin: 3rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
}
</style>
""", unsafe_allow_html=True)

# Import header
from ui.components.header import render_header

# --------------------------------------------------
# Render Header
# --------------------------------------------------
render_header()

# --------------------------------------------------
# Hero Section
# --------------------------------------------------
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

# --------------------------------------------------
# Models Information
# --------------------------------------------------
models_info = {
    "llama-3.1-8b-instant": {
        "icon": "🦙",
        "title": "Llama 3.1 (8B) — Instant",
        "desc": "Meta’s fast, reliable lightweight model. Excellent for math, language, science, and quick explanations.",
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
        "title": "DeepSeek R1 — Reasoning",
        "desc": "Advanced reasoning model designed for logic, code explanations, and step-by-step STEM problems.",
        "specs": ["Deep reasoning", "STEM-focused", "Chain-of-thought"],
        "best_for": "Coding help, algorithm debugging, complex math & physics"
    },

    "hf-vision": {
        "icon": "🖼️",
        "title": "Qwen2-VL (Vision) — HuggingFace",
        "desc": "A multimodal model capable of understanding images, charts, diagrams, and screenshots. Uses the free HuggingFace Inference API.",
        "specs": ["Vision + Text", "Diagram analysis", "Screenshot understanding"],
        "best_for": "Image-based questions: diagrams, handwritten notes, screenshots"
    }
}

# Display model cards
st.markdown("### 🤖 Available Models")
st.markdown("<br>", unsafe_allow_html=True)

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

# --------------------------------------------------
# Model Selection
# --------------------------------------------------
st.markdown("""
<div class="selection-card">
    <div class="selection-title">🎯 Select Your Model</div>
</div>
""", unsafe_allow_html=True)

st.markdown("Choose your preferred model below. The selection will be saved and the badge in the header will update instantly.")

model_options = list(models_info.keys())
default_model = st.session_state.get("model_select_professional", "llama-3.1-8b-instant")
index = model_options.index(default_model) if default_model in model_options else 0

# Create a more descriptive display for the selectbox
model_display_names = {
    "llama-3.1-8b-instant": "🦙 Llama 3.1 (8B) — Fast text responses",
    "mistral": "🌬️ Mistral — Creative & balanced",
    "deepseek-r1": "🔍 DeepSeek R1 — Advanced reasoning",
    "hf-vision": "🖼️ Qwen2-VL Vision — Image understanding"
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
st.info(f"""
**Current Model:** {models_info[default_model]['title']}  
**Best for:** {models_info[default_model]['best_for']}  

Ready to start learning! Head back to the home page to begin chatting with your selected model.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------
# Quick Comparison
# --------------------------------------------------
st.markdown("### 📊 Quick Comparison")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### ⚡ Speed")
    st.write("**Fastest:** Llama 3.1 Instant")
    st.write("**Moderate:** Mistral")
    st.write("**Thoughtful:** DeepSeek R1")
    st.write("**Vision:** Qwen2-VL (HF Vision)")

with col2:
    st.markdown("#### 🎯 Specialization")
    st.write("**Text:** Llama 3.1, Mistral")
    st.write("**Vision:** HF Qwen2-VL")
    st.write("**Code/Logic:** DeepSeek R1")

with col3:
    st.markdown("#### 💡 Use Case")
    st.write("**Quick Answers:** Llama 3.1 Instant")
    st.write("**Deep Learning:** DeepSeek R1")
    st.write("**Creative:** Mistral")

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------
# CTA Section
# --------------------------------------------------
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

# Add some bottom spacing
st.markdown("<br><br>", unsafe_allow_html=True)