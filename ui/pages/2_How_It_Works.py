# ui/pages/2_How_It_Works.py
import streamlit as st
from ..components.header import render_header  # Relative import for components

# Render shared header
render_header()

# How It Works page content
st.title("How It Works")
st.markdown("""
Doubt Tutor simplifies learning with a seamless, 4-step workflow powered by AI.

### Step 1: Select Your Model
Choose from our curated AI models (see [Models](/Models) page). Each is optimized for different doubt types—text, images, or code.

### Step 2: Ask Your Doubt
Type your question in the chat interface. Be specific for best results, e.g., "Explain photosynthesis with a diagram."

### Step 3: Get Instant Response
Our AI generates a clear, structured answer with explanations, examples, and follow-ups. Multimodal models can even analyze images!

### Step 4: Export & Learn More
Download your chat history or dive deeper with related resources. Repeat as needed.

""")

# Visual workflow diagram using Streamlit columns
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("### 1. Choose Model")
    st.write("🧠 Pick AI")
with col2:
    st.markdown("### 2. Ask Question")
    st.write("💬 Type doubt")
with col3:
    st.markdown("### 3. Receive Answer")
    st.write("✨ AI responds")
with col4:
    st.markdown("### 4. Export")
    st.write("💾 Save session")

st.info("Pro Tip: Start with Llama 3.2 for quick text queries or LLaVA for visual doubts.")

# Navigation links
st.markdown("[Back to Home →](/) | [Models →](/Models)")