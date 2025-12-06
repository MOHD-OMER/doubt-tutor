# ui/pages/1_About.py
import streamlit as st

# Page config (optional, for tab title)
st.set_page_config(page_title="About Doubt Tutor", layout="wide")

from ui.components.header import render_header  # Absolute import fix

# Render shared header
render_header()

# About page content
st.title("About Doubt Tutor")
st.markdown("""
## Our Mission
Doubt Tutor is an innovative AI-driven platform designed to empower learners worldwide by providing instant, 
accurate resolutions to academic doubts. Founded in 2025, we believe that no question is too small, 
and every curiosity deserves a thoughtful answer. Our goal is to make education accessible, 
personalized, and engaging through cutting-edge language models.

## Why Doubt Tutor?
- **Instant Insights**: Get responses in seconds from specialized AI models.
- **Educational Focus**: All models are fine-tuned or prompted for clear, step-by-step explanations.
- **Privacy First**: Your queries stay private—no data is stored without consent.
- **Free & Open**: Basic access is free, with premium models for deeper analysis.

## Our Team
Built by educators and AI enthusiasts. We're passionate about bridging the gap between 
curiosity and clarity.

[Explore Models →](/Models) | [How It Works →](/How_It_Works)
""")

# Add metrics for engagement
col1, col2 = st.columns(2)
col1.metric("Users Helped", "10K+", delta="+20%")
col2.metric("Questions Answered", "50K+", delta="+15%")