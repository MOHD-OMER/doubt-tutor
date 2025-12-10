# ui/pages/1_About.py
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
    page_title="About Doubt Tutor",
    page_icon="ℹ️",
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
    min-width: 0 !important;
    max-width: 0 !important;
    opacity: 0 !important;
    transform: translateX(-100%) !important;
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

.section-header {
    font-size: 2rem;
    font-weight: 800;
    color: var(--text-primary);
    margin: 3rem 0 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.section-header::before {
    content: '';
    width: 4px;
    height: 36px;
    background: linear-gradient(180deg, var(--primary), var(--secondary));
    border-radius: 2px;
}

.feature-card {
    background: linear-gradient(135deg, var(--bg-card), var(--bg-elevated));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: 2rem 1.5rem;
    border: 1px solid var(--border-default);
    height: 100%;
    transition: var(--transition);
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    opacity: 0;
    transition: var(--transition);
}

.feature-card:hover {
    transform: translateY(-4px);
    border-color: var(--border-strong);
    box-shadow: var(--shadow-xl);
}

.feature-card:hover::before {
    opacity: 1;
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1.5rem;
    display: block;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    transition: var(--transition);
}

.feature-card:hover .feature-icon {
    transform: scale(1.1) rotate(5deg);
}

.feature-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    line-height: 1.3;
}

.feature-description {
    font-size: 0.9375rem;
    color: var(--text-muted);
    line-height: 1.8;
}

.mission-card {
    background: linear-gradient(135deg, var(--border-subtle), rgba(168, 85, 247, 0.05));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: 2rem;
    border: 1px solid var(--border-default);
    margin: 1.5rem 0;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out;
}

.mission-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    opacity: 0.6;
}

.mission-text {
    font-size: 1.125rem;
    color: var(--text-secondary);
    line-height: 1.9;
    text-align: justify;
}

.team-card {
    background: linear-gradient(135deg, var(--bg-elevated), var(--bg-card));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: 2rem;
    border: 1px solid var(--border-subtle);
    margin: 1.5rem 0;
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.team-text {
    font-size: 0.9375rem;
    color: var(--text-secondary);
    line-height: 1.8;
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

[data-testid="column"] {
    padding: 0 0.5rem;
}

@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .section-header { font-size: 1.5rem; }
    .feature-card { padding: 1.5rem; }
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
    <div class="hero-title">About Doubt Tutor</div>
    <div class="hero-subtitle">
        Empowering learners worldwide with instant, AI-powered academic support powered by Groq.
        No question is too small, every curiosity deserves a thoughtful answer.
    </div>
</div>
""", unsafe_allow_html=True)

# Mission Section
st.markdown('<div class="section-header">🎯 Our Mission</div>', unsafe_allow_html=True)

st.markdown("""
<div class="mission-card">
    <div class="mission-text">
        Doubt Tutor is an innovative AI-driven platform designed to make education accessible, 
        personalized, and engaging through cutting-edge language models powered by Groq. Founded in 2025, 
        we believe in bridging the gap between curiosity and clarity by providing instant, 
        accurate resolutions to academic doubts. Our goal is to democratize education and 
        ensure that every learner has access to quality explanations, regardless of their 
        location or background.
    </div>
</div>
""", unsafe_allow_html=True)

# Why Choose Section
st.markdown('<div class="section-header">⭐ Why Choose Doubt Tutor?</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">⚡</span>
        <div class="feature-title">Instant Insights</div>
        <div class="feature-description">
            Get responses in seconds from specialized AI models. No waiting, 
            no delays—just immediate answers when you need them most.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🔒</span>
        <div class="feature-title">Privacy First</div>
        <div class="feature-description">
            Your queries stay private—no data is stored without consent. 
            We respect your academic journey and personal information.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🎓</span>
        <div class="feature-title">Educational Focus</div>
        <div class="feature-description">
            All models are fine-tuned for clear, step-by-step explanations. 
            We prioritize learning over simple answers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📚</span>
        <div class="feature-title">Multi-Format Support</div>
        <div class="feature-description">
            Upload PDFs, images, and text files. Our AI can read and 
            understand content from various sources.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🌍</span>
        <div class="feature-title">Free & Open</div>
        <div class="feature-description">
            Completely free access for all learners, powered by Groq's fast AI infrastructure.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🤖</span>
        <div class="feature-title">Smart AI Models</div>
        <div class="feature-description">
            Powered by Groq, choose from multiple AI models optimized for different tasks—
            from quick answers to in-depth analysis and vision support.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Team Section
st.markdown('<div class="section-header">👥 Our Team</div>', unsafe_allow_html=True)

st.markdown("""
<div class="team-card">
    <div class="team-text">
        Built by educators, AI enthusiasts, and lifelong learners who are passionate 
        about making quality education accessible to everyone. Our diverse team combines 
        expertise in artificial intelligence, pedagogy, and user experience design to 
        create an intuitive learning platform that truly understands student needs.
        <br><br>
        We're constantly improving our models, expanding our capabilities, and listening 
        to feedback from our community of learners. Your success is our success.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <div class="cta-title">🚀 Ready to Get Started?</div>
    <div class="cta-description">
        Join thousands of learners who are already using Doubt Tutor to ace their studies.
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
    if st.button("📖 How It Works", use_container_width=True):
        st.switch_page("pages/2_How_It_Works.py")

st.markdown("<br><br>", unsafe_allow_html=True)
