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

# Professional styling for How It Works page
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

/* Step Cards */
.step-card {
    background: rgba(30, 30, 60, 0.5);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    border: 1px solid rgba(99, 102, 241, 0.2);
    transition: all 0.3s ease;
    text-align: center;
    height: 100%;
    position: relative;
    overflow: hidden;
}

.step-card::before {
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

.step-card:hover {
    transform: translateY(-8px);
    border-color: rgba(99, 102, 241, 0.5);
    box-shadow: 0 16px 40px rgba(99, 102, 241, 0.2);
    background: rgba(30, 30, 60, 0.7);
}

.step-card:hover::before {
    opacity: 1;
}

.step-number {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white;
    font-size: 1.75rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem auto;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
}

.step-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.step-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
}

.step-description {
    font-size: 1rem;
    color: #94a3b8;
    line-height: 1.7;
}

/* Arrow Between Steps */
.step-arrow {
    font-size: 2rem;
    color: rgba(99, 102, 241, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}

/* Detail Cards */
.detail-card {
    background: rgba(30, 30, 60, 0.4);
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid rgba(99, 102, 241, 0.15);
    margin: 1.5rem 0;
}

.detail-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.detail-content {
    font-size: 1rem;
    color: #cbd5e1;
    line-height: 1.8;
}

/* Pro Tip Box */
.pro-tip {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid rgba(16, 185, 129, 0.3);
    margin: 2rem 0;
}

.pro-tip-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.pro-tip-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #10b981;
    margin-bottom: 0.75rem;
}

.pro-tip-content {
    font-size: 1rem;
    color: #cbd5e1;
    line-height: 1.7;
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
st.markdown("### 🔄 Simple 4-Step Process")
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
st.markdown("### 📝 Detailed Breakdown")

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
st.markdown("### 💡 Pro Tips for Best Results")

st.info("""
**For Text Questions:** Start with LLaMA 3.2 for quick, accurate answers to conceptual questions, definitions, and problem-solving.

**For Visual Content:** Use LLaVA when you need to analyze diagrams, charts, handwritten notes, or any image-based content.

**For Complex Problems:** Try Gemma 2 for multi-step reasoning, mathematical proofs, or in-depth explanations.

**Upload Context:** Attach relevant PDFs, textbook pages, or assignment sheets to get more accurate, tailored responses.
""")

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