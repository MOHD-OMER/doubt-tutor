# ui/components/header.py
import streamlit as st

def render_header():
    # Initialize model
    model_key = "model_select_professional"
    if model_key not in st.session_state:
        st.session_state[model_key] = "llama3.2"
    
    selected_model = st.session_state[model_key]

    # Hide default sidebar
    st.markdown("<style>section[data-testid='stSidebar'] {display: none !important;}</style>", unsafe_allow_html=True)

    # Main header
    st.markdown("""
    <style>
        .header-container { 
            padding: 1rem 0; 
            margin-bottom: 1.5rem;
        }
        .nav-button {
            background: rgba(99, 102, 241, 0.15) !important;
            border: 1px solid rgba(99, 102, 241, 0.3) !important;
            border-radius: 16px !important;
            color: white !important;
            font-weight: 500 !important;
            padding: 10px 20px !important;
            margin: 0 6px !important;
            transition: all 0.2s ease !important;
        }
        .nav-button:hover {
            background: rgba(139, 92, 246, 0.25) !important;
            transform: translateY(-1px);
        }
        .model-badge {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.1));
            border: 1px solid rgba(139, 92, 246, 0.4);
            border-radius: 20px;
            padding: 10px 20px;
            font-weight: 600;
            font-size: 0.85rem;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.15);
            display: inline-flex;
            align-items: center;
            gap: 4px;
            white-space: nowrap;
            line-height: 1.2;
        }
        .export-button {
            background: rgba(34, 197, 94, 0.2) !important;
            border: 1px solid rgba(34, 197, 94, 0.4) !important;
            color: white !important;
        }
        .export-button:hover {
            background: rgba(34, 197, 94, 0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header Row
    col1, col2 = st.columns([1.2, 4])
    
    with col1:
        st.markdown("""
        <h1 style="
            font-size: 2.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #e0e7ff 0%, #818cf8 50%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0;
            padding: 0;
        ">Doubt Tutor</h1>
        """, unsafe_allow_html=True)

    with col2:
        # Create perfectly aligned horizontal bar
        nav_container = st.container()
        with nav_container:
            cols = st.columns([2.5, 0.8, 0.8, 1.5, 0.8, 0.8])  # Adjusted for longer model text: model, Home, About, How It Works, Models, Export
            
            # Model Badge with full text (clean & professional)
            model_display = selected_model.upper().replace("LLAMA", "LLaMA").replace("-", " ").replace("LLAVA", "LLaVA").replace("DEEPSEEK R1", "DeepSeek")
            if "llama" in selected_model.lower():
                icon = "🦙"
            elif "llava" in selected_model.lower():
                icon = "🖼️"
            elif "mistral" in selected_model.lower():
                icon = "🌬️"
            elif "deepseek" in selected_model.lower():
                icon = "🔍"
            elif "gpt" in selected_model.lower():
                icon = "⚡"
            else:
                icon = "🤖"

            with cols[0]:
                st.markdown(f"""
                <div class="model-badge" title="Current AI Model: {selected_model}. Change on Models page.">
                    {icon} Current active model: {model_display}
                </div>
                """, unsafe_allow_html=True)

            # Navigation Buttons (including Home)
            nav_items = [
                ("Home", "app.py"),
                ("About", "pages/1_About.py"),
                ("How It Works", "pages/2_How_It_Works.py"),
                ("Models", "pages/3_Models.py")
            ]

            for i, (label, path) in enumerate(nav_items, 1):
                with cols[i]:
                    if st.button(label, key=f"nav_{label}", use_container_width=True, help=f"Go to {label}"):
                        st.switch_page(path)
            
            # Export button (last column)
            with cols[5]:
                if "chat_history" in st.session_state and len(st.session_state.chat_history) > 0:
                    st.download_button(
                        label="Export",
                        data="\n".join(st.session_state.chat_history),
                        file_name="chat_export.txt",
                        mime="text/plain",
                        key="export_btn",
                        use_container_width=True,
                        help="Download chat history"
                    )
                else:
                    st.button("Export", key="export_btn_disabled", disabled=True, use_container_width=True)


    # Clean divider
    st.markdown("""
    <div style="height: 1px; background: linear-gradient(90deg, transparent, rgba(139,92,246,0.4), transparent); margin: 2rem 0 1.5rem;"></div>
    """, unsafe_allow_html=True)