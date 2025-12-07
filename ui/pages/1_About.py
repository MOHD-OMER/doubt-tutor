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

# Immediately hide sidebar to prevent any flash
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
    transition: all 0s !important;
}
[role="complementary"], .css-1d391kg, .css-1v3f6k1 {
    display: none !important;
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

# Enhanced professional styling for About page (integrated with global vars)
st.markdown("""
<style>
/* Use global CSS variables for consistency */
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    --bg-primary: #0a0a1a;
    --bg-secondary: #0f0f1e;
    --bg-card: rgba(20, 20, 40, 0.85);
    --bg-elevated: rgba(30, 30, 60, 0.95);
    --text-primary: #ffffff;
    --text-secondary: #e2e8f0;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
    --text-link: #a5b4fc;
    --border-subtle: rgba(99, 102, 241, 0.1);
    --border-default: rgba(99, 102, 241, 0.2);
    --border-strong: rgba(99, 102, 241, 0.4);
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.15);
    --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.2);
    --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.25);
    --shadow-xl: 0 24px 48px rgba(0, 0, 0, 0.35);
    --shadow-glow: 0 0 32px rgba(99, 102, 241, 0.4);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
    --radius-2xl: 24px;
    --transition-base: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --font-size-sm: 0.875rem;
    --font-size-base: 0.9375rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;
    --font-size-2xl: 1.5rem;
    --font-size-3xl: 2rem;
    --font-size-4xl: 3rem;
    --header-height: 72px;
}

/* Global improvements */
.block-container {
    padding-top: var(--spacing-xl);
    padding-bottom: var(--spacing-section);
    max-width: 1400px;
    margin: 0 auto;
}

/* Hero Section */
.hero-section {
    background: linear-gradient(135deg, var(--border-subtle), rgba(168, 85, 247, 0.08));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: var(--spacing-section) var(--spacing-xl);
    margin: var(--spacing-xl) 0 var(--spacing-section) 0;
    border: 1px solid var(--border-default);
    text-align: center;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
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
    font-size: var(--font-size-4xl);
    font-weight: 900;
    background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: var(--spacing-lg);
    letter-spacing: -0.025em;
    line-height: 1.1;
    animation: fadeInDown 0.6s ease-out;
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-subtitle {
    font-size: var(--font-size-lg);
    color: var(--text-muted);
    line-height: 1.8;
    max-width: 900px;
    margin: 0 auto;
    font-weight: 400;
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Section Headers */
.section-header {
    font-size: var(--font-size-3xl);
    font-weight: 800;
    color: var(--text-primary);
    margin: var(--spacing-section) 0 var(--spacing-lg) 0;
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    position: relative;
}

.section-header::before {
    content: '';
    width: 4px;
    height: 36px;
    background: linear-gradient(180deg, var(--primary), var(--secondary));
    border-radius: 2px;
    flex-shrink: 0;
}

/* Content Cards */
.content-card {
    background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    border: 1px solid var(--border-subtle);
    margin-bottom: var(--spacing-lg);
    transition: var(--transition-base);
    position: relative;
    overflow: hidden;
}

.content-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    opacity: 0;
    transition: var(--transition-base);
}

.content-card:hover {
    border-color: var(--border-strong);
    background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
    transform: translateY(-2px);
    box-shadow: var(--shadow-xl);
}

.content-card:hover::before {
    opacity: 1;
}

/* Feature Cards */
.feature-card {
    background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl) var(--spacing-lg);
    border: 1px solid var(--border-default);
    height: 100%;
    transition: var(--transition-base);
    margin-bottom: var(--spacing-lg);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
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
    transition: var(--transition-base);
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
    margin-bottom: var(--spacing-lg);
    display: block;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    transition: var(--transition-base);
}

.feature-card:hover .feature-icon {
    transform: scale(1.05);
}

.feature-title {
    font-size: var(--font-size-xl);
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
    line-height: 1.3;
}

.feature-description {
    font-size: var(--font-size-base);
    color: var(--text-muted);
    line-height: 1.8;
    flex-grow: 1;
}

/* Mission Card */
.mission-card {
    background: linear-gradient(135deg, var(--border-subtle), rgba(168, 85, 247, 0.05));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: var(--spacing-xl);
    border: 1px solid var(--border-default);
    margin: var(--spacing-lg) 0;
    box-shadow: var(--shadow-md);
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
    font-size: var(--font-size-lg);
    color: var(--text-secondary);
    line-height: 1.9;
    text-align: justify;
}

/* Team Card */
.team-card {
    background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    border: 1px solid var(--border-subtle);
    margin: var(--spacing-lg) 0;
    box-shadow: var(--shadow-sm);
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.team-text {
    font-size: var(--font-size-base);
    color: var(--text-secondary);
    line-height: 1.8;
}

/* CTA Section */
.cta-section {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: var(--spacing-section) var(--spacing-lg);
    margin: var(--spacing-section) 0 var(--spacing-xl) 0;
    text-align: center;
    border: 1px solid var(--border-strong);
    box-shadow: var(--shadow-lg);
    animation: fadeInUp 0.6s ease-out 0.4s both;
}

.cta-title {
    font-size: var(--font-size-2xl);
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
}

.cta-description {
    font-size: var(--font-size-lg);
    color: var(--text-muted);
    margin-bottom: var(--spacing-xl);
}

/* Button Improvements */
.stButton > button {
    border-radius: var(--radius-lg);
    font-weight: 600;
    padding: var(--spacing-md) var(--spacing-lg);
    transition: var(--transition-base);
    border: 1px solid var(--border-default);
    background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
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
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
}

.stButton > button[type="primary"] {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
    color: var(--text-primary) !important;
    border-color: var(--primary) !important;
}

.stButton > button[type="primary"]:hover {
    background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%) !important;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
}

/* Divider styling */
hr {
    margin: var(--spacing-section) 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-default), transparent);
    position: relative;
}

hr::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 40px;
    height: 40px;
    background: radial-gradient(circle, var(--primary) 20%, transparent 70%);
    opacity: 0.3;
    border-radius: 50%;
}

/* Column spacing */
[data-testid="column"] {
    padding: 0 var(--spacing-sm);
}

/* Additional spacing for feature grid */
.stColumn {
    padding: 0 var(--spacing-sm) !important;
}

/* Section spacing */
.section-wrapper {
    margin: var(--spacing-section) 0;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
    .hero-section, .cta-section {
        padding: var(--spacing-lg) var(--spacing-md);
        margin: var(--spacing-lg) 0;
    }
    
    .hero-title {
        font-size: var(--font-size-3xl);
    }
    
    .feature-card {
        padding: var(--spacing-lg);
    }
}

@media (max-width: 768px) {
    .block-container {
        padding: var(--spacing-lg) var(--spacing-sm);
    }
    
    .section-header {
        font-size: var(--font-size-2xl);
    }
    
    .content-card, .mission-card, .team-card {
        padding: var(--spacing-lg);
    }
    
    [data-testid="column"] {
        padding: 0 var(--spacing-xs);
    }
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