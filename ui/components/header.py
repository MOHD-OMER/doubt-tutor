# ui/components/header.py
import streamlit as st

def render_header():
    # Initialize model
    model_key = "model_select_professional"
    if model_key not in st.session_state:
        st.session_state[model_key] = "llama-3.1-8b-instant"
    
    selected_model = st.session_state.get(model_key, "llama-3.1-8b-instant")

    # Hide default sidebar
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
    </style>
    """, unsafe_allow_html=True)

    # Enhanced header CSS with global vars
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
        --bg-elevated: rgba(30, 30, 60, 0.95);
        --text-primary: #ffffff;
        --text-secondary: #e2e8f0;
        --text-muted: #94a3b8;
        --border-subtle: rgba(99, 102, 241, 0.1);
        --border-default: rgba(99, 102, 241, 0.2);
        --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.15);
        --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.2);
        --radius-lg: 16px;
        --radius-xl: 20px;
        --transition-base: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        --spacing-sm: 0.5rem;
        --spacing-md: 1rem;
        --spacing-lg: 1.5rem;
        --font-size-xl: 1.25rem;
        --font-size-2xl: 1.5rem;
        --font-size-3xl: 2rem;
        --header-height: 72px;
    }
    
    .header-container { 
        padding: var(--spacing-md) 0; 
        margin-bottom: var(--spacing-lg);
        background: linear-gradient(180deg, rgba(15, 15, 30, 0.95) 0%, rgba(10, 10, 25, 0.92) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        border-bottom: 1px solid var(--border-default);
        position: sticky;
        top: 0;
        z-index: 1000;
        box-shadow: var(--shadow-md);
    }
    
    .nav-button {
        background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-secondary) 100%) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-lg) !important;
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
        padding: var(--spacing-sm) var(--spacing-md) !important;
        margin: 0 var(--spacing-xs) !important;
        transition: var(--transition-base) !important;
        height: 44px !important;
        min-height: 44px !important;
        line-height: 1 !important;
        position: relative !important;
        overflow: hidden !important;
        font-size: var(--font-size-sm) !important;
    }
    
    .nav-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .nav-button:hover::before {
        left: 100%;
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.12) 100%) !important;
        border-color: var(--border-default) !important;
        color: var(--text-primary) !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    .model-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.1));
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-xl);
        padding: var(--spacing-sm) var(--spacing-md);
        font-weight: 600;
        font-size: var(--font-size-sm);
        backdrop-filter: blur(10px);
        box-shadow: var(--shadow-sm);
        display: inline-flex;
        align-items: center;
        gap: var(--spacing-xs);
        white-space: nowrap;
        line-height: 1.2;
        transition: var(--transition-base);
        max-width: 200px;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    .model-badge:hover {
        border-color: var(--border-default);
        box-shadow: var(--shadow-md);
        transform: translateY(-1px);
    }
    
    .export-button {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(16, 185, 129, 0.1)) !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
        color: var(--text-secondary) !important;
    }
    
    .export-button:hover {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.25), rgba(16, 185, 129, 0.15)) !important;
        border-color: rgba(34, 197, 94, 0.4) !important;
        color: var(--text-primary) !important;
    }
    
    .export-button:disabled {
        opacity: 0.5 !important;
        cursor: not-allowed !important;
    }
    
    /* Brand styling */
    .brand-title {
        font-size: var(--font-size-3xl);
        font-weight: 800;
        background: linear-gradient(135deg, var(--text-primary) 0%, var(--primary-light) 60%, var(--secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        padding: 0;
        letter-spacing: -0.025em;
        line-height: 1;
        transition: var(--transition-base);
        display: flex;
        align-items: center;
        gap: var(--spacing-xs);
    }
    
    .brand-title:hover {
        transform: translateY(-1px);
        filter: brightness(1.05);
    }
    
    .brand-icon {
        font-size: var(--font-size-2xl);
    }
    
    /* Divider */
    .header-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-default), transparent);
        margin: var(--spacing-lg) 0 var(--spacing-md);
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Row
    col1, col2 = st.columns([1.2, 4])
    
    with col1:
        st.markdown(f"""
        <div class="brand-title">
            <span class="brand-icon">🤔</span>
            Doubt Tutor
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Create perfectly aligned horizontal bar
        nav_container = st.container()
        with nav_container:
            cols = st.columns([2.5, 0.8, 0.8, 1.5, 0.8, 0.8])  # Adjusted for longer model text: model, Home, About, How It Works, Models, Export
            
            # Model Badge (clean & professional)

            # Proper model name mapping (aligned with models.py)
            model_display_names = {
                "llama-3.1-8b-instant": "LLaMA 3.1 • 8B Instant",
                "mistral": "Mistral 7B Instruct",
                "deepseek-r1": "DeepSeek R1 • Reasoning",
                "hf-vision": "Qwen2-VL • Vision"
            }

            # Use mapped name or fall back to raw value
            model_display = model_display_names.get(selected_model, selected_model)

            # Icon selection (aligned with models.py)
            if "llama" in selected_model.lower():
                icon = "🦙"
            elif "mistral" in selected_model.lower():
                icon = "🌬️"
            elif "deepseek" in selected_model.lower():
                icon = "🔍"
            elif "hf-vision" in selected_model or "vision" in selected_model.lower():
                icon = "🖼️"
            else:
                icon = "🤖"

            with cols[0]:
                st.markdown(f"""
                <div class="model-badge" title="Current AI Model: {selected_model}. Change on Models page.">
                    {icon} {model_display}
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
            
            # Export button (last column) - Fixed to use 'messages' for consistency
            with cols[5]:
                if "messages" in st.session_state and st.session_state.messages:
                    # Trigger export in main app
                    if st.button("💾 Export", key="export_btn", use_container_width=True, help="Export chat history"):
                        st.session_state["export_chat"] = True
                        st.rerun()
                else:
                    st.button("💾 Export", key="export_btn_disabled", disabled=True, use_container_width=True, help="No chat history to export")

    # Clean divider
    st.markdown("""
    <div class="header-divider"></div>
    """, unsafe_allow_html=True)