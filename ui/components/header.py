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
    }
    </style>
    """, unsafe_allow_html=True)

    # Enhanced header CSS
    st.markdown("""
    <style>
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --primary-light: #818cf8;
        --secondary: #8b5cf6;
        --accent: #ec4899;
        --success: #10b981;
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
        --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.25);
        --shadow-glow: 0 0 20px rgba(99, 102, 241, 0.3);
        --radius-lg: 16px;
        --radius-xl: 20px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        --header-height: 72px;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    .header-container { 
        padding: 1rem 0; 
        margin-bottom: 1.5rem;
        background: linear-gradient(180deg, rgba(15, 15, 30, 0.95) 0%, rgba(10, 10, 25, 0.92) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        border-bottom: 1px solid var(--border-default);
        position: sticky;
        top: 0;
        z-index: 1000;
        box-shadow: var(--shadow-md);
        animation: slideDown 0.4s ease-out;
    }
    
    .nav-button {
        background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-secondary) 100%) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-lg) !important;
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
        margin: 0 0.25rem !important;
        transition: var(--transition) !important;
        height: 44px !important;
        min-height: 44px !important;
        line-height: 1 !important;
        position: relative !important;
        overflow: hidden !important;
        font-size: 0.875rem !important;
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
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.15) 100%) !important;
        border-color: var(--primary) !important;
        color: var(--text-primary) !important;
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-lg) !important;
    }
    
    .nav-button:active {
        transform: translateY(0) !important;
    }
    
    .model-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.1));
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-xl);
        padding: 0.5rem 1rem;
        font-weight: 600;
        font-size: 0.875rem;
        backdrop-filter: blur(10px);
        box-shadow: var(--shadow-sm);
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        white-space: nowrap;
        line-height: 1.2;
        transition: var(--transition);
        max-width: 220px;
        overflow: hidden;
        text-overflow: ellipsis;
        cursor: help;
        position: relative;
    }
    
    .model-badge::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--primary-light), transparent);
        opacity: 0;
        transition: var(--transition);
    }
    
    .model-badge:hover {
        border-color: var(--primary);
        box-shadow: var(--shadow-glow);
        transform: translateY(-2px);
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.15));
    }
    
    .model-badge:hover::after {
        opacity: 1;
    }
    
    .model-icon {
        font-size: 1.125rem;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        transition: var(--transition);
    }
    
    .model-badge:hover .model-icon {
        transform: scale(1.1) rotate(5deg);
    }
    
    .export-button {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(16, 185, 129, 0.1)) !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
        color: var(--text-secondary) !important;
    }
    
    .export-button:hover {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.25), rgba(16, 185, 129, 0.15)) !important;
        border-color: rgba(34, 197, 94, 0.5) !important;
        color: var(--text-primary) !important;
        box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3) !important;
    }
    
    .export-button:disabled {
        opacity: 0.4 !important;
        cursor: not-allowed !important;
        transform: none !important;
    }
    
    .brand-title {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--text-primary) 0%, var(--primary-light) 60%, var(--secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        padding: 0;
        letter-spacing: -0.025em;
        line-height: 1;
        transition: var(--transition);
        display: flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;
        position: relative;
    }
    
    .brand-title::after {
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .brand-title:hover::after {
        transform: scaleX(1);
    }
    
    .brand-title:hover {
        transform: translateY(-1px);
        filter: brightness(1.1);
    }
    
    .brand-icon {
        font-size: 1.5rem;
        filter: drop-shadow(0 2px 6px rgba(99, 102, 241, 0.4));
        transition: var(--transition);
    }
    
    .brand-title:hover .brand-icon {
        transform: rotate(10deg) scale(1.1);
    }
    
    .header-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-default), transparent);
        margin: 1.5rem 0 1rem;
        position: relative;
    }
    
    .header-divider::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 40px;
        height: 40px;
        background: radial-gradient(circle, var(--primary) 10%, transparent 70%);
        opacity: 0.2;
        border-radius: 50%;
    }
    
    /* Button container alignment */
    [data-testid="column"] > div {
        display: flex;
        align-items: center;
        height: 100%;
    }
    
    /* Responsive adjustments */
    @media (max-width: 1024px) {
        .brand-title {
            font-size: 1.5rem;
        }
        .brand-icon {
            font-size: 1.25rem;
        }
        .model-badge {
            font-size: 0.75rem;
            padding: 0.375rem 0.75rem;
            max-width: 180px;
        }
        .nav-button {
            font-size: 0.75rem !important;
            padding: 0.375rem 0.75rem !important;
        }
    }
    
    @media (max-width: 768px) {
        .brand-title {
            font-size: 1.25rem;
        }
        .model-badge {
            max-width: 150px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Row
    col1, col2 = st.columns([1.2, 4])
    
    with col1:
        st.markdown("""
        <div class="brand-title">
            <span class="brand-icon">🤔</span>
            Doubt Tutor
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Create perfectly aligned horizontal navigation bar
        nav_container = st.container()
        with nav_container:
            cols = st.columns([2.5, 0.8, 0.8, 1.5, 0.8, 0.8])
            
            # Model Badge with icon
            model_display_names = {
                "llama-3.1-8b-instant": "LLaMA 3.1 • 8B Instant",
                "mistral": "Mistral 7B Instruct",
                "deepseek-r1": "DeepSeek R1 • Reasoning",
                "hf-vision": "Qwen2-VL • Vision"
            }

            model_display = model_display_names.get(selected_model, selected_model)

            # Icon selection
            model_icons = {
                "llama-3.1-8b-instant": "🦙",
                "mistral": "🌬️",
                "deepseek-r1": "🔍",
                "hf-vision": "🖼️"
            }
            
            icon = model_icons.get(selected_model, "🤖")

            with cols[0]:
                st.markdown(f"""
                <div class="model-badge" title="Current AI Model: {selected_model}&#10;Change model on the Models page">
                    <span class="model-icon">{icon}</span>
                    <span>{model_display}</span>
                </div>
                """, unsafe_allow_html=True)

            # Navigation Buttons
            nav_items = [
                ("Home", "app.py"),
                ("About", "pages/1_About.py"),
                ("How It Works", "pages/2_How_It_Works.py"),
                ("Models", "pages/3_Models.py")
            ]

            for i, (label, path) in enumerate(nav_items, 1):
                with cols[i]:
                    if st.button(label, key=f"nav_{label}", use_container_width=True, help=f"Navigate to {label}"):
                        st.switch_page(path)
            
            # Export button with conditional styling
            with cols[5]:
                has_messages = "messages" in st.session_state and st.session_state.messages
                
                if has_messages:
                    if st.button("💾 Export", key="export_btn", use_container_width=True, help="Export chat history as JSON"):
                        st.session_state["export_chat"] = True
                        st.rerun()
                else:
                    st.button("💾 Export", key="export_btn_disabled", disabled=True, use_container_width=True, help="No chat history to export yet")

    # Elegant divider
    st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)