import streamlit as st
from datetime import datetime
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
import re
import html


# --------------------------------------------------
# Markdown Rendering with Code Highlighting
# --------------------------------------------------
def render_markdown_with_code(text):
    """Render markdown with syntax highlighting for code blocks"""
    
    def highlight_code(match):
        code = match.group(2)
        lang = match.group(1) if match.group(1) else 'python'

        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except:
            try:
                lexer = guess_lexer(code)
            except:
                return f'<pre><code>{html.escape(code)}</code></pre>'

        formatter = HtmlFormatter(style='monokai', noclasses=True, cssclass='highlight')
        highlighted = highlight(code, lexer, formatter)
        return f'<div class="code-block-wrapper"><div class="code-header"><span class="code-lang">{lang}</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>{highlighted}</div>'

    # Handle code blocks first (before markdown processing)
    pattern = r'```([\w+-]*)\n([\s\S]*?)```'
    text = re.sub(pattern, highlight_code, text, flags=re.DOTALL)
    
    # Render markdown
    rendered_html = markdown.markdown(text, extensions=['extra', 'codehilite'])
    
    return rendered_html


# --------------------------------------------------
# Timestamp Formatter
# --------------------------------------------------
def format_timestamp(iso_timestamp):
    try:
        dt = datetime.fromisoformat(iso_timestamp)
        return dt.strftime("%I:%M %p")
    except:
        return ""


# --------------------------------------------------
# File Renderer
# --------------------------------------------------
def render_file_attachments(files):
    if not files:
        return ""

    html_output = '<div class="message-files">'

    for file in files:
        name = html.escape(file.get("name", "file"))
        ftype = file.get("type", "")
        data = file.get("data", "")

        if "image" in ftype and data:
            html_output += f'''
            <div class="message-file-item image-attachment">
                <img src="data:{ftype};base64,{data}" alt="{name}" class="attachment-image" loading="lazy" />
                <div class="attachment-overlay">
                    <span class="attachment-icon">🖼️</span>
                    <span class="attachment-name">{name}</span>
                </div>
            </div>
            '''

        elif "pdf" in ftype and data:
            html_output += f'''
            <div class="message-file-item pdf-attachment">
                <embed src="data:{ftype};base64,{data}" type="{ftype}" class="pdf-embed" />
                <div class="attachment-overlay">
                    <span class="attachment-icon">📄</span>
                    <span class="attachment-name">{name}</span>
                </div>
            </div>
            '''

        else:
            ext = ftype.split('/')[-1].upper() if '/' in ftype else "FILE"
            html_output += f'''
            <div class="message-file-item generic-attachment">
                <span class="attachment-icon">📎</span>
                <div class="attachment-details">
                    <span class="attachment-name">{name}</span>
                    <span class="attachment-type">{ext}</span>
                </div>
            </div>
            '''

    html_output += '</div>'
    return html_output


# --------------------------------------------------
# Professional Chat Renderer with Enhanced UI
# --------------------------------------------------
def render_chat(messages):
    """Render chat messages with professional, modern design"""

    # Enhanced CSS integrated with global theme
    enhanced_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');
        
        /* Use global CSS variables for consistency */
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --primary-light: #818cf8;
            --secondary: #8b5cf6;
            --accent: #ec4899;
            --bg-primary: #0a0a1a;
            --bg-secondary: #0f0f1e;
            --bg-card: rgba(20, 20, 40, 0.85);
            --bg-elevated: rgba(30, 30, 60, 0.95);
            --bg-input: rgba(15, 15, 30, 0.98);
            --text-primary: #ffffff;
            --text-secondary: #e2e8f0;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --text-link: #a5b4fc;
            --border-subtle: rgba(99, 102, 241, 0.1);
            --border-default: rgba(99, 102, 241, 0.2);
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.15);
            --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.2);
            --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.25);
            --radius-md: 12px;
            --radius-lg: 16px;
            --radius-xl: 20px;
            --transition-base: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --spacing-sm: 0.5rem;
            --spacing-md: 1rem;
            --spacing-lg: 1.5rem;
            --font-size-sm: 0.875rem;
            --font-size-base: 0.9375rem;
            --font-size-lg: 1.125rem;
        }
        
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        .chat {
            max-width: 1400px;
            margin: 0 auto;
            padding: var(--spacing-lg) var(--spacing-md);
            background: transparent;
            overflow-y: auto;
            height: calc(100vh - var(--header-height) - var(--input-height) - 140px);
            min-height: 500px;
        }
        
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
            animation: fadeInUp 0.6s ease-out;
        }
        
        .empty-icon {
            font-size: 4rem;
            margin-bottom: var(--spacing-lg);
            opacity: 0.6;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
        }
        
        .empty-title {
            font-size: var(--font-size-2xl);
            font-weight: 700;
            margin-bottom: var(--spacing-sm);
            color: var(--text-primary);
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .empty-desc {
            font-size: var(--font-size-base);
            color: var(--text-secondary);
            max-width: 500px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .message-wrapper {
            display: flex;
            gap: var(--spacing-md);
            margin-bottom: var(--spacing-xl);
            animation: fadeInUp 0.35s ease-out;
            opacity: 0;
            animation-fill-mode: forwards;
        }
        
        .message-wrapper:nth-child(even) {
            animation-delay: 0.1s;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .user-message {
            flex-direction: row-reverse;
        }
        
        .ai-message {
            flex-direction: row;
        }
        
        .ai-avatar {
            width: 40px;
            height: 40px;
            border-radius: var(--radius-full);
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: var(--font-size-lg);
            flex-shrink: 0;
            box-shadow: var(--shadow-md);
            transition: var(--transition-base);
            border: 2px solid var(--border-subtle);
        }
        
        .ai-avatar:hover {
            transform: scale(1.05);
            box-shadow: var(--shadow-lg);
        }
        
        .bubble {
            max-width: 75%;
            border-radius: var(--radius-xl);
            padding: var(--spacing-md) var(--spacing-lg);
            line-height: 1.65;
            word-wrap: break-word;
            transition: var(--transition-base);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(16px);
        }
        
        .bubble::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.02), transparent);
            opacity: 0;
            transition: var(--transition-base);
            pointer-events: none;
        }
        
        .bubble:hover::before {
            opacity: 1;
        }
        
        .user-bubble {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: var(--text-primary);
            border-bottom-right-radius: var(--radius-sm);
            box-shadow: var(--shadow-md);
        }
        
        .ai-bubble {
            background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
            color: var(--text-secondary);
            border: 1px solid var(--border-default);
            border-bottom-left-radius: var(--radius-sm);
            box-shadow: var(--shadow-sm);
        }
        
        .bubble-content {
            font-size: var(--font-size-base);
        }
        
        .bubble-content p {
            margin: 0 0 var(--spacing-sm) 0;
        }
        
        .bubble-content p:last-child {
            margin-bottom: 0;
        }
        
        .bubble-content strong {
            font-weight: 600;
            color: var(--primary-light);
        }
        
        .bubble-content ul, .bubble-content ol {
            margin: var(--spacing-sm) 0;
            padding-left: var(--spacing-lg);
        }
        
        .bubble-content li {
            margin: var(--spacing-xs) 0;
        }
        
        .bubble-content code {
            background: rgba(0, 0, 0, 0.3);
            padding: var(--spacing-xs) var(--spacing-sm);
            border-radius: var(--radius-sm);
            font-size: var(--font-size-sm);
            font-family: 'JetBrains Mono', 'Monaco', monospace;
            color: var(--text-primary);
        }
        
        .code-block-wrapper {
            margin: var(--spacing-md) 0;
            border-radius: var(--radius-lg);
            overflow: hidden;
            background: var(--bg-secondary);
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-subtle);
        }
        
        .code-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: var(--spacing-sm) var(--spacing-md);
            background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
            border-bottom: 1px solid var(--border-subtle);
        }
        
        .code-lang {
            font-size: var(--font-size-xs);
            font-weight: 600;
            text-transform: uppercase;
            color: var(--primary-light);
            letter-spacing: 0.05em;
        }
        
        .copy-btn {
            background: rgba(99, 102, 241, 0.15);
            color: var(--primary-light);
            border: 1px solid var(--border-default);
            padding: var(--spacing-xs) var(--spacing-sm);
            border-radius: var(--radius-sm);
            font-size: var(--font-size-xs);
            font-weight: 500;
            cursor: pointer;
            transition: var(--transition-base);
        }
        
        .copy-btn:hover {
            background: rgba(99, 102, 241, 0.25);
            transform: translateY(-1px);
            box-shadow: var(--shadow-sm);
        }
        
        .copy-btn:active {
            transform: translateY(0);
        }
        
        .highlight {
            margin: 0 !important;
            padding: var(--spacing-md) !important;
            background: var(--bg-secondary) !important;
            overflow-x: auto;
        }
        
        .highlight pre {
            margin: 0 !important;
            padding: 0 !important;
            background: transparent !important;
            font-size: var(--font-size-sm);
            line-height: 1.6;
            font-family: 'JetBrains Mono', monospace;
        }
        
        .message-meta {
            display: flex;
            align-items: center;
            gap: var(--spacing-sm);
            margin-top: var(--spacing-xs);
            font-size: var(--font-size-xs);
            color: var(--text-dim);
            padding: 0 var(--spacing-xs);
        }
        
        .user-meta {
            justify-content: flex-end;
            margin-right: 50px;
        }
        
        .ai-meta {
            margin-left: 50px;
        }
        
        .timestamp {
            font-weight: 500;
            opacity: 0.8;
        }
        
        .model-badge {
            padding: var(--spacing-xs) var(--spacing-sm);
            background: rgba(99, 102, 241, 0.15);
            color: var(--primary-light);
            border-radius: var(--radius-md);
            font-size: var(--font-size-xs);
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            border: 1px solid var(--border-subtle);
        }
        
        .message-files {
            display: flex;
            flex-direction: column;
            gap: var(--spacing-sm);
            margin-top: var(--spacing-sm);
        }
        
        .message-file-item {
            background: var(--bg-card);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-subtle);
            overflow: hidden;
            transition: var(--transition-base);
            position: relative;
            max-width: 100%;
        }
        
        .message-file-item:hover {
            border-color: var(--border-default);
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }
        
        .attachment-image, .pdf-embed {
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }
        
        .pdf-embed {
            background: var(--bg-secondary);
        }
        
        .attachment-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0,0,0,0.7));
            padding: var(--spacing-sm);
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: var(--spacing-xs);
        }
        
        .attachment-details {
            display: flex;
            flex-direction: column;
            flex: 1;
        }
        
        .attachment-name {
            font-size: var(--font-size-sm);
            font-weight: 500;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .attachment-type {
            font-size: var(--font-size-xs);
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .generic-attachment {
            display: flex;
            align-items: center;
            gap: var(--spacing-md);
            padding: var(--spacing-md);
        }
        
        .attachment-icon {
            font-size: var(--font-size-lg);
            flex-shrink: 0;
        }
        
        /* Custom Scrollbar */
        .chat::-webkit-scrollbar {
            width: 6px;
        }
        
        .chat::-webkit-scrollbar-track {
            background: var(--bg-secondary);
            border-radius: var(--radius-full);
        }
        
        .chat::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, var(--primary) 0%, var(--secondary) 100%);
            border-radius: var(--radius-full);
        }
        
        .chat::-webkit-scrollbar-thumb:hover {
            background: var(--primary-light);
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .chat {
                padding: var(--spacing-md);
                height: calc(100vh - var(--header-height) - var(--input-height) - 100px);
                min-height: 400px;
            }
            
            .bubble {
                max-width: 90%;
            }
            
            .message-wrapper {
                gap: var(--spacing-sm);
            }
            
            .user-meta, .ai-meta {
                margin-left: 0 !important;
                margin-right: 0 !important;
            }
            
            .ai-avatar {
                width: 36px;
                height: 36px;
                font-size: var(--font-size-base);
            }
        }
    </style>
    <script>
        function copyCode(btn) {
            const codeBlock = btn.closest('.code-block-wrapper').querySelector('pre');
            const code = codeBlock.textContent;
            navigator.clipboard.writeText(code).then(() => {
                const originalText = btn.textContent;
                btn.textContent = 'Copied!';
                btn.style.background = 'rgba(99, 102, 241, 0.25)';
                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.style.background = 'rgba(99, 102, 241, 0.15)';
                }, 1800);
            }).catch(() => {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = code;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                // Update button
                const originalText = btn.textContent;
                btn.textContent = 'Copied!';
                setTimeout(() => {
                    btn.textContent = originalText;
                }, 1800);
            });
        }
    </script>
    """

    if not messages:
        st.html(enhanced_css + """
        <div class="chat">
            <div class="empty-state">
                <div class="empty-icon">💬</div>
                <div class="empty-title">Ready to Learn?</div>
                <div class="empty-desc">Upload documents or ask a question to get started with AI-powered tutoring.</div>
            </div>
        </div>
        """)
        return

    chat_html = enhanced_css + '<div class="chat" id="chat-container">'

    for i, msg in enumerate(messages):
        role = msg.get("role", "user")
        raw_content = str(msg.get("content", ""))
        files = msg.get("files", [])
        timestamp = msg.get("timestamp", "")
        model = msg.get("model", "")

        # Enhanced sanitization
        safe_text = re.sub(r"<script[\s\S]*?>[\s\S]*?</script>", "", raw_content, flags=re.IGNORECASE | re.DOTALL)
        safe_text = re.sub(r"<style[\s\S]*?>[\s\S]*?</style>", "", safe_text, flags=re.IGNORECASE | re.DOTALL)
        safe_text = re.sub(r"<iframe[\s\S]*?>[\s\S]*?</iframe>", "", safe_text, flags=re.IGNORECASE | re.DOTALL)
        safe_text = re.sub(r"&lt;script", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r"&lt;style", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r"&lt;iframe", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r'\n\s*\n\s*\n+', '\n\n', safe_text).strip()

        time_str = format_timestamp(timestamp) if timestamp else ""
        file_html = render_file_attachments(files)

        # USER MESSAGE
        if role == "user":
            escaped_text = html.escape(safe_text)
            escaped_text = escaped_text.replace('\n', '<br>')

            chat_html += f'''
            <div class="message-wrapper user-message">
                <div class="bubble user-bubble">
                    <div class="bubble-content">{escaped_text}</div>
                    {file_html}
                </div>
            </div>
            <div class="message-meta user-meta">
                <span class="timestamp">{time_str}</span>
            </div>
            '''

        # AI MESSAGE
        else:
            rendered_content = render_markdown_with_code(safe_text)
            model_badge = f'<span class="model-badge">{model or "AI"}</span>' if model else ''

            chat_html += f'''
            <div class="message-wrapper ai-message">
                <div class="ai-avatar">🤖</div>
                <div class="bubble ai-bubble">
                    <div class="bubble-content">{rendered_content}</div>
                    {file_html}
                </div>
            </div>
            <div class="message-meta ai-meta">
                {model_badge}
                <span class="timestamp">{time_str}</span>
            </div>
            '''

    chat_html += '</div>'
    
    st.html(chat_html)