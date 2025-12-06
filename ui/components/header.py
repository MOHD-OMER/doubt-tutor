# ui/components/header.py
import streamlit as st

def render_header():
    """Render enhanced professional header with better UI"""
    
    # Header container
    st.markdown('<div class="top-nav">', unsafe_allow_html=True)
    
    # Create columns for layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # Brand with gradient text
        st.markdown("""
        <div class="brand">
            <span style="font-size: 1.8rem;">🎓</span>
            <span>Doubt Tutor</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Navigation controls
        st.markdown('<div class="nav-controls">', unsafe_allow_html=True)
        
        # Model selector with better styling
        subcol1, subcol2 = st.columns([3, 1])
        
        with subcol1:
            model = st.selectbox(
                "AI Model",
                ["llama3.2", "llava", "mistral", "deepseek-r1"],
                key="model_select_top",
                label_visibility="collapsed",
                help="Select AI model for processing"
            )
            
            # Model badge
            model_colors = {
                "llama3.2": "🔵",
                "llava": "🟢",
                "mistral": "🟣",
                "deepseek-r1": "🔴"
            }
            st.markdown(
                f'<span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 0.5rem;">'
                f'{model_colors.get(model, "⚪")} {model.upper()}</span>',
                unsafe_allow_html=True
            )
        
        with subcol2:
            # Export button
            if st.button("💾 Export", help="Export chat history", key="export_toggle", use_container_width=True):
                st.session_state.export_chat = True
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Divider with gradient
    st.markdown("""
    <div style="height: 2px; background: linear-gradient(90deg, 
        transparent 0%, 
        rgba(99, 102, 241, 0.5) 50%, 
        transparent 100%); 
        margin-bottom: 0;">
    </div>
    """, unsafe_allow_html=True)