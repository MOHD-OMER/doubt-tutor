"""
Modern Theme Configuration for Doubt Tutor
Professional color schemes and design tokens
"""

class Theme:
    """Professional theme configuration"""
    
    # Primary Colors
    PRIMARY = "#6366f1"
    PRIMARY_DARK = "#4f46e5"
    PRIMARY_LIGHT = "#818cf8"
    SECONDARY = "#8b5cf6"
    ACCENT = "#ec4899"
    
    # Background Colors
    BG_PRIMARY = "#0f0f1e"
    BG_SECONDARY = "#1a1a2e"
    BG_CARD = "rgba(30, 30, 50, 0.6)"
    BG_HOVER = "rgba(30, 30, 50, 0.9)"
    
    # Text Colors
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#e2e8f0"
    TEXT_MUTED = "#94a3b8"
    TEXT_INVERSE = "#0f0f1e"
    
    # Border Colors
    BORDER_DEFAULT = "rgba(99, 102, 241, 0.15)"
    BORDER_FOCUS = "rgba(99, 102, 241, 0.6)"
    BORDER_HOVER = "rgba(99, 102, 241, 0.4)"
    
    # Semantic Colors
    SUCCESS = "#10b981"
    WARNING = "#f59e0b"
    ERROR = "#ef4444"
    INFO = "#3b82f6"
    
    # Shadows
    SHADOW_SM = "0 2px 8px rgba(0, 0, 0, 0.1)"
    SHADOW_MD = "0 4px 16px rgba(0, 0, 0, 0.2)"
    SHADOW_LG = "0 8px 32px rgba(0, 0, 0, 0.3)"
    SHADOW_XL = "0 12px 48px rgba(0, 0, 0, 0.4)"
    SHADOW_GLOW = "0 4px 20px rgba(99, 102, 241, 0.4)"
    
    # Gradients
    GRADIENT_PRIMARY = f"linear-gradient(135deg, {PRIMARY} 0%, {SECONDARY} 100%)"
    GRADIENT_SUCCESS = "linear-gradient(135deg, #10b981 0%, #059669 100%)"
    GRADIENT_WARNING = "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)"
    GRADIENT_ERROR = "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)"
    GRADIENT_BG = f"linear-gradient(135deg, {BG_PRIMARY} 0%, {BG_SECONDARY} 100%)"
    
    # Border Radius
    RADIUS_SM = "8px"
    RADIUS_MD = "12px"
    RADIUS_LG = "16px"
    RADIUS_XL = "24px"
    RADIUS_FULL = "9999px"
    
    # Spacing
    SPACE_XS = "0.25rem"
    SPACE_SM = "0.5rem"
    SPACE_MD = "1rem"
    SPACE_LG = "1.5rem"
    SPACE_XL = "2rem"
    SPACE_2XL = "3rem"
    SPACE_3XL = "4rem"
    
    # Typography
    FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    FONT_MONO = "'Fira Code', 'Courier New', monospace"
    
    FONT_SIZE_XS = "0.75rem"
    FONT_SIZE_SM = "0.875rem"
    FONT_SIZE_BASE = "1rem"
    FONT_SIZE_LG = "1.125rem"
    FONT_SIZE_XL = "1.25rem"
    FONT_SIZE_2XL = "1.5rem"
    FONT_SIZE_3XL = "1.875rem"
    FONT_SIZE_4XL = "2.25rem"
    
    FONT_WEIGHT_LIGHT = "300"
    FONT_WEIGHT_NORMAL = "400"
    FONT_WEIGHT_MEDIUM = "500"
    FONT_WEIGHT_SEMIBOLD = "600"
    FONT_WEIGHT_BOLD = "700"
    
    # Transitions
    TRANSITION_FAST = "all 0.15s ease"
    TRANSITION_BASE = "all 0.3s ease"
    TRANSITION_SLOW = "all 0.5s ease"
    
    # Z-Index Layers
    Z_BASE = "1"
    Z_DROPDOWN = "1000"
    Z_STICKY = "1010"
    Z_MODAL = "1020"
    Z_POPOVER = "1030"
    Z_TOOLTIP = "1040"
    
    @classmethod
    def get_css_variables(cls):
        """Get CSS custom properties"""
        return f"""
        :root {{
            /* Colors */
            --primary: {cls.PRIMARY};
            --primary-dark: {cls.PRIMARY_DARK};
            --primary-light: {cls.PRIMARY_LIGHT};
            --secondary: {cls.SECONDARY};
            --accent: {cls.ACCENT};
            
            --bg-primary: {cls.BG_PRIMARY};
            --bg-secondary: {cls.BG_SECONDARY};
            --bg-card: {cls.BG_CARD};
            
            --text-primary: {cls.TEXT_PRIMARY};
            --text-secondary: {cls.TEXT_SECONDARY};
            --text-muted: {cls.TEXT_MUTED};
            
            --border-default: {cls.BORDER_DEFAULT};
            --border-focus: {cls.BORDER_FOCUS};
            --border-hover: {cls.BORDER_HOVER};
            
            --success: {cls.SUCCESS};
            --warning: {cls.WARNING};
            --error: {cls.ERROR};
            --info: {cls.INFO};
            
            /* Shadows */
            --shadow-sm: {cls.SHADOW_SM};
            --shadow-md: {cls.SHADOW_MD};
            --shadow-lg: {cls.SHADOW_LG};
            --shadow-glow: {cls.SHADOW_GLOW};
            
            /* Border Radius */
            --radius-sm: {cls.RADIUS_SM};
            --radius-md: {cls.RADIUS_MD};
            --radius-lg: {cls.RADIUS_LG};
            --radius-xl: {cls.RADIUS_XL};
            
            /* Spacing */
            --space-xs: {cls.SPACE_XS};
            --space-sm: {cls.SPACE_SM};
            --space-md: {cls.SPACE_MD};
            --space-lg: {cls.SPACE_LG};
            --space-xl: {cls.SPACE_XL};
            
            /* Typography */
            --font-family: {cls.FONT_FAMILY};
            --font-mono: {cls.FONT_MONO};
            
            /* Transitions */
            --transition-base: {cls.TRANSITION_BASE};
        }}
        """
    
    @classmethod
    def get_component_styles(cls):
        """Get reusable component styles"""
        return """
        /* Button variants */
        .btn {
            padding: 0.75rem 1.5rem;
            border-radius: var(--radius-md);
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition-base);
            border: none;
            font-family: var(--font-family);
        }
        
        .btn-primary {
            background: var(--primary);
            color: white;
        }
        
        .btn-primary:hover {
            background: var(--primary-dark);
            transform: translateY(-2px);
            box-shadow: var(--shadow-glow);
        }
        
        /* Card styles */
        .card {
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-default);
            border-radius: var(--radius-lg);
            padding: var(--space-lg);
            transition: var(--transition-base);
        }
        
        .card:hover {
            border-color: var(--border-hover);
            transform: translateY(-4px);
            box-shadow: var(--shadow-md);
        }
        
        /* Input styles */
        .input {
            width: 100%;
            padding: 0.75rem 1rem;
            background: rgba(20, 20, 35, 0.9);
            border: 1px solid var(--border-default);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-family: var(--font-family);
            transition: var(--transition-base);
        }
        
        .input:focus {
            outline: none;
            border-color: var(--border-focus);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
        }
        
        /* Badge styles */
        .badge {
            display: inline-flex;
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-sm);
            font-size: var(--font-size-sm);
            font-weight: 600;
        }
        
        .badge-primary {
            background: var(--primary);
            color: white;
        }
        
        .badge-success {
            background: var(--success);
            color: white;
        }
        
        .badge-warning {
            background: var(--warning);
            color: white;
        }
        
        .badge-error {
            background: var(--error);
            color: white;
        }
        
        /* Alert styles */
        .alert {
            padding: 1rem 1.25rem;
            border-radius: var(--radius-md);
            margin: 1rem 0;
            border-left: 4px solid;
        }
        
        .alert-info {
            background: rgba(59, 130, 246, 0.1);
            border-color: var(--info);
            color: var(--text-secondary);
        }
        
        .alert-success {
            background: rgba(16, 185, 129, 0.1);
            border-color: var(--success);
            color: var(--text-secondary);
        }
        
        .alert-warning {
            background: rgba(245, 158, 11, 0.1);
            border-color: var(--warning);
            color: var(--text-secondary);
        }
        
        .alert-error {
            background: rgba(239, 68, 68, 0.1);
            border-color: var(--error);
            color: var(--text-secondary);
        }
        """


# Chart colors for data visualization
CHART_COLORS = [
    "#6366f1",  # Primary
    "#8b5cf6",  # Secondary
    "#ec4899",  # Accent
    "#10b981",  # Success
    "#f59e0b",  # Warning
    "#3b82f6",  # Info
    "#14b8a6",  # Teal
    "#f97316",  # Orange
]

# Status indicators
STATUS_COLORS = {
    "online": "#10b981",
    "offline": "#6b7280",
    "busy": "#ef4444",
    "away": "#f59e0b",
}

# Model colors (for AI model indicators)
MODEL_COLORS = {
    "llama3.2": "#6366f1",
    "mistral": "#8b5cf6",
    "deepseek-r1": "#ec4899",
}

# Subject colors
SUBJECT_COLORS = {
    "Mathematics": "#3b82f6",
    "Physics": "#10b981",
    "Chemistry": "#f59e0b",
    "Biology": "#10b981",
    "Computer Science": "#8b5cf6",
    "History": "#ef4444",
    "Literature": "#ec4899",
    "General": "#6366f1",
}

# Helper functions
def get_gradient(start_color, end_color):
    """Generate CSS gradient"""
    return f"linear-gradient(135deg, {start_color} 0%, {end_color} 100%)"

def get_shadow(size="md", glow=False):
    """Get shadow based on size"""
    shadows = {
        "sm": Theme.SHADOW_SM,
        "md": Theme.SHADOW_MD,
        "lg": Theme.SHADOW_LG,
        "xl": Theme.SHADOW_XL,
    }
    
    if glow:
        return f"{shadows.get(size, Theme.SHADOW_MD)}, {Theme.SHADOW_GLOW}"
    return shadows.get(size, Theme.SHADOW_MD)

def get_color_with_opacity(color, opacity):
    """Add opacity to hex color"""
    # Simple implementation - you can enhance this
    return f"{color}{int(opacity * 255):02x}"