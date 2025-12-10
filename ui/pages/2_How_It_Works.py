# ui/pages/2_How_It_Works.py
import streamlit as st
from pathlib import Path

import sys
from pathlib import Path

# Add project root to PYTHONPATH so "src" and "ui" imports work
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))


# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="How It Works - Doubt Tutor",
    page_icon="📖",
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

@keyframes pulse {
    0%, 100% { opacity: 0.6; }
    50% { opacity: 1; }
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

.section-heading {
    text-align: center;
    color: var(--text-primary);
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.step-card {
    background: linear-gradient(135deg, var(--bg-card), var(--bg-elevated));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: 2rem 1.5rem;
    border: 1px solid var(--border-default);
    transition: var(--transition);
    text-align: center;
    height: 100%;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out both;
    opacity: 0;
}

.step-card:nth-child(1) { animation-delay: 0.1s; }
.step-card:nth-child(3) { animation-delay: 0.2s; }
.step-card:nth-child(5) { animation-delay: 0.3s; }
.step-card:nth-child(7) { animation-delay: 0.4s; }

.step-card::before {
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

.step-card:hover {
    transform: translateY(-8px);
    border-color: var(--border-strong);
    box-shadow: var(--shadow-xl);
}

.step-card:hover::before {
    opacity: 1;
}

.step-number {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: var(--text-primary);
    font-size: 1.75rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    box-shadow: var(--shadow-glow);
    transition: var(--transition);
    border: 2px solid var(--border-subtle);
}

.step-card:hover .step-number {
    transform: scale(1.1) rotate(360deg);
}

.step-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    transition: var(--transition);
}

.step-card:hover .step-icon {
    transform: scale(1.15);
}

.step-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    line-height: 1.3;
}

.step-description {
    font-size: 0.9375rem;
    color: var(--text-muted);
    line-height: 1.7;
}

.step-arrow {
    font-size: 2.5rem;
    color: var(--primary);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    animation: pulse 2s infinite;
}

.detail-card {
    background: linear-gradient(135deg, var(--bg-elevated), var(--bg-card));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: 2rem;
    border: 1px solid var(--border-subtle);
    margin: 1.5rem 0;
    transition: var(--transition);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out;
}

.detail-card::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background: linear-gradient(180deg, var(--primary), var(--secondary));
    opacity: 0;
    transition: var(--transition);
}

.detail-card:hover {
    border-color: var(--border-default);
    transform: translateX(4px);
}

.detail-card:hover::before {
    opacity: 1;
}

.detail-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.detail-content {
    font-size: 0.9375rem;
    color: var(--text-secondary);
    line-height: 1.8;
}

.detail-content strong {
    color: var(--primary);
}

.pro-tip {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: 2rem;
    border: 1px solid rgba(16, 185, 129, 0.3);
    margin: 2rem 0;
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.pro-tip-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    color: var(--success);
}

.pro-tip-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--success);
    margin-bottom: 1rem;
}

.pro-tip-content {
    font-size: 0.9375rem;
    color: var(--text-secondary);
    line-height: 1.7;
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

hr {
    margin: 3rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-default), transparent);
}

@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .step-arrow { display: none !important; }
    .step-card { margin-bottom: 1.5rem; }
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
    <div class="hero-title">How It Works</div>
    <div class="hero-subtitle">
        Doubt Tutor simplifies learning with a seamless, 4-step workflow powered by 
        cutting-edge AI technology. Get instant answers to your questions in seconds.
    </div>
</div>
""", unsafe_allow_html=True)

# Workflow Steps
st.markdown('<div class="section-heading">🔄 Simple 4-Step Process</div>', unsafe_allow_html=True)

cols = st.columns([3, 0.5, 3, 0.5, 3, 0.5, 3])

with cols[0]:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">1</div>
        <div class="step-icon">🧠</div>
        <div class="step-title">Select Your Model</div>
        <div class="step-description">
            Choose from our curated AI models. Each is optimized for different 
            doubt types—text, images, or code.
        </div>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="step-arrow">→</div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">2</div>
        <div class="step-icon">💬</div>
        <div class="step-title">Ask Your Question</div>
        <div class="step-description">
            Type your question in the chat interface. Be specific for best results, 
            and upload files if needed.
        </div>
    </div>
    """, unsafe_allow_html=True)

with cols[3]:
    st.markdown('<div class="step-arrow">→</div>', unsafe_allow_html=True)

with cols[4]:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">3</div>
        <div class="step-icon">✨</div>
        <div class="step-title">Get Instant Response</div>
        <div class="step-description">
            Our AI generates a clear, structured answer with explanations, 
            examples, and follow-ups.
        </div>
    </div>
    """, unsafe_allow_html=True)

with cols[5]:
    st.markdown('<div class="step-arrow">→</div>', unsafe_allow_html=True)

with cols[6]:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">4</div>
        <div class="step-icon">💾</div>
        <div class="step-title">Export & Continue</div>
        <div class="step-description">
            Download your chat history or dive deeper with related resources. 
            Repeat as needed.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Detailed Breakdown
st.markdown('<div class="section-heading">🔍 Detailed Breakdown</div>', unsafe_allow_html=True)

st.markdown("""
<div class="detail-card">
    <div class="detail-title">🎯 Step 1: Choose Your AI Model</div>
    <div class="detail-content">
        Start by selecting the right AI model for your needs. We offer multiple models, 
        each with unique capabilities:
        <br><br>
        • <strong>LLaMA 3.1</strong>: Fast, efficient text-based responses for quick questions<br>
        • <strong>GPT OSS 20B</strong>: Powerful open-source model for comprehensive explanations<br>
        • <strong>Qwen2-VL Vision</strong>: Advanced vision capabilities for analyzing images and diagrams<br>
        <br>
        Navigate to the Models page to learn more about each option and their use cases.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="detail-card">
    <div class="detail-title">💭 Step 2: Ask Your Doubt</div>
    <div class="detail-content">
        Type your question clearly in the chat interface. For best results:
        <br><br>
        • Be specific: "Explain photosynthesis with a diagram" instead of "what is photosynthesis"<br>
        • Upload supporting materials: PDFs, images, or text files<br>
        • Provide context: Include relevant details about what you're learning<br>
        • Ask follow-ups: Dive deeper into concepts that need clarification<br>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="detail-card">
    <div class="detail-title">⚡ Step 3: Receive Your Answer</div>
    <div class="detail-content">
        Within seconds, our AI analyzes your question and generates a comprehensive response:
        <br><br>
        • <strong>Clear explanations</strong>: Step-by-step breakdowns of complex concepts<br>
        • <strong>Visual analysis</strong>: For image-based questions, get detailed interpretations<br>
        • <strong>Examples</strong>: Real-world applications and practice problems<br>
        • <strong>Related concepts</strong>: Suggestions for deeper learning<br>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="detail-card">
    <div class="detail-title">📤 Step 4: Export & Learn More</div>
    <div class="detail-content">
        Save your learning session for future reference:
        <br><br>
        • <strong>Export chat history</strong>: Download conversations as JSON files<br>
        • <strong>Review anytime</strong>: Access your saved sessions whenever needed<br>
        • <strong>Continue learning</strong>: Ask follow-up questions or explore new topics<br>
        • <strong>Share knowledge</strong>: Help others by sharing your learning journey<br>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Pro Tips
st.markdown('<div class="section-heading">💡 Pro Tips for Best Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pro-tip">
    <div class="pro-tip-icon">💡</div>
    <div class="pro-tip-title">Model Selection Guide</div>
    <div class="pro-tip-content">
        <strong>For Quick Questions:</strong> Start with LLaMA 3.1 for fast, accurate answers to conceptual questions, definitions, and problem-solving.<br><br>
        <strong>For Comprehensive Answers:</strong> Use GPT OSS 20B when you need detailed, in-depth explanations and multi-step reasoning.<br><br>
        <strong>For Visual Content:</strong> Use Qwen2-VL Vision when you need to analyze diagrams, charts, handwritten notes, or any image-based content.<br><br>
        <strong>Upload Context:</strong> Attach relevant PDFs, textbook pages, or assignment sheets to get more accurate, tailored responses.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <div class="cta-title">🚀 Ready to Start Learning?</div>
    <div class="cta-description">
        Try Doubt Tutor now and experience the future of AI-powered education.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    if st.button("🚀 Start Learning", use_container_width=True, type="primary"):
        st.switch_page("app.py")

with col2:
    if st.button("🤖 Explore Models", use_container_width=True):
        st.switch_page("pages/3_Models.py")

with col3:
    if st.button("ℹ️ About Us", use_container_width=True):
        st.switch_page("pages/1_About.py")

st.markdown("<br><br>", unsafe_allow_html=True)
