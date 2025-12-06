# ui/components/header.py
import streamlit as st

def render_header():
    """
    Render a professional, clean header for Doubt Tutor.
    
    Features:
    - Gradient brand title
    - Model badge display (selection handled on Models page)
    - Custom horizontal navigation bar (Home, About, How It Works, Models)
    - Styled export button
    - Subtle gradient divider
    """
    
    # Initialize model if not set (default for new sessions)
    model_key = "model_select_professional"
    if model_key not in st.session_state:
        st.session_state[model_key] = "llama3.2"
    
    selected_model = st.session_state[model_key]
    
    # Hide default Streamlit sidebar (for custom nav)
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)
    
    # Header layout with professional spacing
    header_container = st.container()
    with header_container:
        col_left, col_right = st.columns([1, 3])
        
        with col_left:
            # Professional brand with gradient text and subtle shadow
            st.markdown("""
            <div class="brand" style="
                font-size: 2.25rem;
                font-weight: 800;
                background: linear-gradient(135deg, #ffffff 0%, #818cf8 40%, #8b5cf6 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                letter-spacing: -0.025em;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-bottom: 0;
            ">
                Doubt Tutor
            </div>
            """, unsafe_allow_html=True)
        
        with col_right:
            # Professional model badge
            model_display = selected_model.upper().replace("-", " ").replace("LLAVA", "LLaVA").replace("DEEPSEEK R1", "DeepSeek")
            model_icons = {
                "llama3.2": "🦙",
                "llava": "🖼️",
                "mistral": "🌬️",
                "deepseek-r1": "🔍",
                "gpt-4o-mini": "⚡"
            }
            icon = model_icons.get(selected_model, "🤖")
            
            st.markdown(f"""
            <div class="model-badge" style="
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 10px 18px;
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%);
                border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 20px;
                font-weight: 600;
                font-size: 0.95rem;
                color: var(--text-primary);
                backdrop-filter: blur(12px);
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                box-shadow: 0 2px 8px rgba(99, 102, 241, 0.1);
                cursor: default;
                white-space: nowrap;
                margin-right: 1rem;
            "
            title="Current AI Model: {selected_model}. Change on Models page.">
                {icon} {model_display}
            </div>
            """, unsafe_allow_html=True)
            
            # Custom Horizontal Navigation Bar
            nav_pages = [
                ("🏠 Home", "app.py"),
                ("ℹ️ About", "pages/1_About.py"),
                ("🔄 How It Works", "pages/2_How_It_Works.py"),
                ("🤖 Models", "pages/3_Models.py")
            ]
            
            # Create small columns for nav buttons
            nav_cols = st.columns(len(nav_pages))
            for i, (label, page_path) in enumerate(nav_pages):
                with nav_cols[i]:
                    if st.button(label, key=f"nav_{i}", use_container_width=True, help=f"Go to {label}"):
                        st.switch_page(page_path)
            
            # Professional export button (beside nav)
            if st.button(
                "💾 Export",
                key="export_professional",
                use_container_width=False,
                help="Export chat history"
            ):
                st.session_state.export_chat = True
                st.success("✅ Chat exported successfully!", icon="✅")
                st.rerun()
    
    # Subtle professional divider
    st.markdown("""
    <div class="header-divider" style="
        height: 1px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(99, 102, 241, 0.4) 25%, 
            rgba(139, 92, 246, 0.2) 50%, 
            rgba(99, 102, 241, 0.4) 75%, 
            transparent 100%);
        margin: 1.5rem 0 2rem;
        border-radius: 1px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    "></div>
    """, unsafe_allow_html=True)