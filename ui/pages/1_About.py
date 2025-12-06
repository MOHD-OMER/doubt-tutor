# ui/pages/1_About.py
import streamlit as st
from ..components.header import render_header  # Relative import for components

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
Built by educators and AI enthusiasts at xAI-inspired labs. We're passionate about bridging the gap between 
curiosity and clarity.

[Explore Models →](/Models) | [How It Works →](/How_It_Works)
""")

# Add an image or metric if available (e.g., from assets)
# st.image("assets/doubt_tutor_logo.png", caption="Doubt Tutor in Action")
st.metric("Users Helped", "10K+", delta="+20%")
st.metric("Questions Answered", "50K+", delta="+15%")