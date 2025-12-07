# ui/pages/1_About.py
import streamlit as st
from pathlib import Path

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="About Doubt Tutor",
    page_icon="ℹ️",
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

# Professional styling for About page
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
    max-width: 800px;
    margin: 0 auto;
    font-weight: 400;
}

/* Section Headers */
.section-header {
    font-size: 2rem;
    font-weight: 700;
    color: #e2e8f0;
    margin: 3rem 0 1.5rem 0;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.section-header::before {
    content: '';
    width: 4px;
    height: 32px;
    background: linear-gradient(180deg, #6366f1, #a855f7);
    border-radius: 2px;
}

/* Content Cards */
.content-card {
    background: rgba(30, 30, 60, 0.4);
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid rgba(99, 102, 241, 0.15);
    margin-bottom: 1.5rem;
    transition: all 0.3s ease;
}

.content-card:hover {
    border-color: rgba(99, 102, 241, 0.3);
    background: rgba(30, 30, 60, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.1);
}

/* Feature Cards */
.feature-card {
    background: rgba(30, 30, 60, 0.5);
    border-radius: 16px;
    padding: 2.5rem 2rem;
    border: 1px solid rgba(99, 102, 241, 0.2);
    height: 100%;
    transition: all 0.3s ease;
    margin-bottom: 1.5rem;
}

.feature-card:hover {
    transform: translateY(-4px);
    border-color: rgba(99, 102, 241, 0.4);
    box-shadow: 0 12px 32px rgba(99, 102, 241, 0.15);
    background: rgba(30, 30, 60, 0.6);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1.5rem;
    display: block;
}

.feature-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
    line-height: 1.3;
}

.feature-description {
    font-size: 1rem;
    color: #94a3b8;
    line-height: 1.8;
}

/* Mission Card */
.mission-card {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.05));
    border-radius: 20px;
    padding: 2.5rem;
    border: 1px solid rgba(99, 102, 241, 0.2);
    margin: 2rem 0;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
}

.mission-text {
    font-size: 1.125rem;
    color: #cbd5e1;
    line-height: 1.9;
    text-align: justify;
}

/* Team Card */
.team-card {
    background: rgba(30, 30, 60, 0.4);
    border-radius: 16px;
    padding: 2.5rem;
    border: 1px solid rgba(99, 102, 241, 0.15);
    margin: 2rem 0;
}

.team-text {
    font-size: 1.1rem;
    color: #cbd5e1;
    line-height: 1.8;
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

/* Divider styling */
hr {
    margin: 3rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
}

/* Column spacing */
[data-testid="column"] {
    padding: 0 0.75rem;
}

/* Additional spacing for feature grid */
.stColumn {
    padding: 0 0.75rem !important;
}

/* Section spacing */
.section-wrapper {
    margin: 3.5rem 0;
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
    <div class="hero-title">About Doubt Tutor</div>
    <div class="hero-subtitle">
        Empowering learners worldwide with instant, AI-powered academic support powered by Groq.
        No question is too small, every curiosity deserves a thoughtful answer.
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Mission Section
# --------------------------------------------------
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

# --------------------------------------------------
# Why Choose Section
# --------------------------------------------------
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

# --------------------------------------------------
# Team Section
# --------------------------------------------------
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

# --------------------------------------------------
# CTA Section
# --------------------------------------------------
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

# Add some bottom spacing
st.markdown("<br><br>", unsafe_allow_html=True)