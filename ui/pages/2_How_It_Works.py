# ui/pages/2_How_It_Works.py
import streamlit as st
from pathlib import Path

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="How It Works - Doubt Tutor",
    page_icon="📖",
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

# Enhanced professional styling for How It Works page (integrated with global vars)
st.markdown("""
<style>
/* Use global CSS variables for consistency */
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    --success: #10b981;
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
    font-size: var(--font-size-4xl);
    font-weight: 900;
    background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: var(--spacing-lg);
    letter-spacing: -0.025em;
    line-height: 1.1;
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

/* Step Cards */
.step-card {
    background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-2xl);
    padding: var(--spacing-xl) var(--spacing-lg);
    border: 1px solid var(--border-default);
    transition: var(--transition-base);
    text-align: center;
    height: 100%;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out;
    opacity: 0;
    transform: translateY(20px);
    animation-fill-mode: forwards;
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
    transition: var(--transition-base);
}

.step-card:hover {
    transform: translateY(-8px);
    border-color: var(--border-strong);
    box-shadow: var(--shadow-xl);
    background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
}

.step-card:hover::before {
    opacity: 1;
}

.step-number {
    width: 64px;
    height: 64px;
    border-radius: var(--radius-full);
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: var(--text-primary);
    font-size: 1.75rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto var(--spacing-lg) auto;
    box-shadow: var(--shadow-glow);
    transition: var(--transition-base);
    border: 2px solid var(--border-subtle);
}

.step-card:hover .step-number {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
}

.step-icon {
    font-size: 3rem;
    margin-bottom: var(--spacing-md);
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    transition: var(--transition-base);
}

.step-card:hover .step-icon {
    transform: scale(1.1);
}

.step-title {
    font-size: var(--font-size-xl);
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
    line-height: 1.3;
}

.step-description {
    font-size: var(--font-size-base);
    color: var(--text-muted);
    line-height: 1.7;
}

/* Arrow Between Steps */
.step-arrow {
    font-size: 2.5rem;
    color: var(--primary);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    font-weight: 300;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.6; }
    50% { opacity: 1; }
}

/* Detail Cards */
.detail-card {
    background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    border: 1px solid var(--border-subtle);
    margin: var(--spacing-lg) 0;
    transition: var(--transition-base);
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
    transition: var(--transition-base);
}

.detail-card:hover {
    border-color: var(--border-default);
    box-shadow: var(--shadow-md);
    transform: translateX(4px);
}

.detail-card:hover::before {
    opacity: 1;
}

.detail-title {
    font-size: var(--font-size-lg);
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}

.detail-content {
    font-size: var(--font-size-base);
    color: var(--text-secondary);
    line-height: 1.8;
}

.detail-content strong {
    color: var(--primary-light);
}

/* Pro Tip Box */
.pro-tip {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    border: 1px solid rgba(16, 185, 129, 0.3);
    margin: var(--spacing-xl) 0;
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.pro-tip-icon {
    font-size: 2rem;
    margin-bottom: var(--spacing-sm);
    color: var(--success);
}

.pro-tip-title {
    font-size: var(--font-size-lg);
    font-weight: 700;
    color: var(--success);
    margin-bottom: var(--spacing-md);
}

.pro-tip-content {
    font-size: var(--font-size-base);
    color: var(--text-secondary);
    line-height: 1.7;
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

/* Divider */
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

/* Override st.info for pro tip */
.stAlert {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05)) !important;
    border-radius: var(--radius-xl) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
    color: var(--text-secondary) !important;
    padding: var(--spacing-xl) !important;
    margin: var(--spacing-xl) 0 !important;
    box-shadow: var(--shadow-sm) !important;
}

.stAlert > div {
    color: var(--text-secondary) !important;
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
    
    .step-card {
        padding: var(--spacing-lg);
        margin-bottom: var(--spacing-md);
    }
}

@media (max-width: 768px) {
    .block-container {
        padding: var(--spacing-lg) var(--spacing-sm);
    }
    
    .step-card {
        margin-bottom: var(--spacing-lg);
    }
    
    .step-arrow {
        display: none !important;
    }
    
    [data-testid="column"] {
        padding: 0 var(--spacing-xs);
        margin-bottom: var(--spacing-md);
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
    <div class="hero-title">How It Works</div>
    <div class="hero-subtitle">
        Doubt Tutor simplifies learning with a seamless, 4-step workflow powered by 
        cutting-edge AI technology. Get instant answers to your questions in seconds.
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Workflow Steps
# --------------------------------------------------
st.markdown('<h3 style="text-align: center; color: var(--text-primary); font-size: var(--font-size-2xl); margin-bottom: var(--spacing-xl);">🔄 Simple 4-Step Process</h3>')
st.markdown("<br>", unsafe_allow_html=True)

# Create columns for steps with arrows
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

# --------------------------------------------------
# Detailed Breakdown
# --------------------------------------------------
st.markdown('<h3 style="text-align: center; color: var(--text-primary); font-size: var(--font-size-2xl); margin-bottom: var(--spacing-xl);">📝 Detailed Breakdown</h3>')

st.markdown("""
<div class="detail-card">
    <div class="detail-title">🎯 Step 1: Choose Your AI Model</div>
    <div class="detail-content">
        Start by selecting the right AI model for your needs. We offer multiple models, 
        each with unique capabilities:
        <br><br>
        • <strong>LLaMA 3.2</strong>: Fast, efficient text-based responses for quick questions<br>
        • <strong>LLaVA</strong>: Advanced vision capabilities for analyzing images and diagrams<br>
        • <strong>Gemma 2</strong>: Balanced performance for complex reasoning tasks<br>
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

# --------------------------------------------------
# Pro Tips
# --------------------------------------------------
st.markdown('<h3 style="text-align: center; color: var(--text-primary); font-size: var(--font-size-2xl); margin-bottom: var(--spacing-xl);">💡 Pro Tips for Best Results</h3>')

with st.container():
    st.markdown("""
    <div class="pro-tip">
        <div class="pro-tip-icon">💡</div>
        <div class="pro-tip-title">Model Selection Guide</div>
        <div class="pro-tip-content">
            **For Text Questions:** Start with LLaMA 3.2 for quick, accurate answers to conceptual questions, definitions, and problem-solving.<br><br>
            **For Visual Content:** Use LLaVA when you need to analyze diagrams, charts, handwritten notes, or any image-based content.<br><br>
            **For Complex Problems:** Try Gemma 2 for multi-step reasoning, mathematical proofs, or in-depth explanations.<br><br>
            **Upload Context:** Attach relevant PDFs, textbook pages, or assignment sheets to get more accurate, tailored responses.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------
# CTA Section
# --------------------------------------------------
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

# Add some bottom spacing
st.markdown("<br><br>", unsafe_allow_html=True)