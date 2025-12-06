# ui/pages/3_Models.py
import streamlit as st

# Page config
st.set_page_config(page_title="Models", layout="wide")

from ui.components.header import render_header  # Absolute import fix

# Render shared header
render_header()

# Models page content
st.title("Available AI Models")
st.markdown("""
Before selecting a model, here's a quick overview of each one. All are integrated for educational use in Doubt Tutor.
Choose based on your doubt type—text-heavy, visual, or advanced reasoning.
""")

# Model descriptions
models_info = {
    "llama3.2": {
        "icon": "🦙",
        "title": "Llama 3.2",
        "desc": "Meta's efficient, open-source model excels at concise explanations for math, science, and language arts. Ideal for quick, accurate doubt resolution without fluff. (8B parameters, fast inference.)"
    },
    "llava": {
        "icon": "🖼️",
        "title": "LLaVA",
        "desc": "Multimodal powerhouse for visual doubts—upload diagrams, charts, or photos, and get step-by-step breakdowns. Perfect for biology sketches or physics graphs. (Vision-Language model.)"
    },
    "mistral": {
        "icon": "🌬️",
        "title": "Mistral",
        "desc": "Lightweight yet powerful for creative and interdisciplinary queries, like history timelines or literature analysis. Balances speed and depth for exploratory learning."
    },
    "deepseek-r1": {
        "icon": "🔍",
        "title": "DeepSeek R1",
        "desc": "Specialized for deep reasoning in coding, logic, and advanced STEM. Great for debugging algorithms or deriving proofs—thinks like a tutor with multiple angles."
    },
    "gpt-4o-mini": {
        "icon": "⚡",
        "title": "GPT-4o Mini",
        "desc": "OpenAI's speedy mini-version for broad topics. Handles everything from essay outlines to trivia with witty, engaging responses. (Cost-effective for frequent use.)"
    }
}

for model_key, info in models_info.items():
    with st.expander(f"{info['icon']} {info['title']}"):
        st.write(info['desc'])
        best_for = "text queries" if model_key != "llava" else "visual analysis"
        st.caption(f"Best for: {best_for}")

# Model Selection
st.subheader("Select Your Model")
st.markdown("Choose below—the badge in the header will update instantly.")

model_options = list(models_info.keys())
default_model = st.session_state.get("model_select_professional", "llama3.2")
index = model_options.index(default_model)
selected_model = st.selectbox(
    "Preferred Model",
    options=model_options,
    index=index,
    help="Pick a model to start tutoring."
)

if selected_model != default_model:
    st.session_state["model_select_professional"] = selected_model
    st.success(f"✅ Switched to {selected_model.upper()}!")
    st.rerun()

st.info("Model selected! Return to Home to start chatting.")

# Navigation
st.markdown("[How It Works →](/How_It_Works) | [About →](/About)")