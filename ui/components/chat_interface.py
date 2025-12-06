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

    html_output = '<div class="message-attachments">'

    for file in files:
        name = html.escape(file.get("name", "file"))
        ftype = file.get("type", "")
        data = file.get("data", "")

        if "image" in ftype and data:
            html_output += f'''
            <div class="attachment-preview image-preview">
                <div class="preview-container">
                    <img src="data:{ftype};base64,{data}" alt="{name}" loading="lazy" />
                </div>
                <div class="attachment-info">
                    <span class="attachment-icon">🖼️</span>
                    <span class="attachment-name">{name}</span>
                </div>
            </div>
            '''

        elif "pdf" in ftype and data:
            html_output += f'''
            <div class="attachment-preview pdf-preview">
                <div class="preview-container">
                    <iframe src="data:application/pdf;base64,{data}"></iframe>
                </div>
                <div class="attachment-info">
                    <span class="attachment-icon">📄</span>
                    <span class="attachment-name">{name}</span>
                </div>
            </div>
            '''

        else:
            ext = ftype.split('/')[-1].upper()
            html_output += f'''
            <div class="attachment-pill">
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

    # Enhanced CSS for professional UI
    enhanced_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
        
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        .chat {
            max-width: 900px;
            margin: 0 auto;
            padding: 1.5rem 1rem;
            background: transparent;
        }
        
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: rgba(255, 255, 255, 0.5);
        }
        
        .empty-icon {
            font-size: 56px;
            margin-bottom: 1.25rem;
            opacity: 0.5;
        }
        
        .empty-title {
            font-size: 1.75rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            color: rgba(255, 255, 255, 0.9);
        }
        
        .empty-desc {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.5);
            max-width: 400px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .message-wrapper {
            display: flex;
            gap: 0.875rem;
            margin-bottom: 2rem;
            animation: fadeInUp 0.35s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(8px);
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
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            flex-shrink: 0;
            box-shadow: 0 3px 10px rgba(102, 126, 234, 0.25);
        }
        
        .bubble {
            max-width: 75%;
            border-radius: 14px;
            padding: 1rem 1.25rem;
            line-height: 1.65;
            word-wrap: break-word;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
            transition: all 0.2s ease;
        }
        
        .bubble:hover {
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.12);
        }
        
        .user-bubble {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #ffffff;
            border-bottom-right-radius: 4px;
        }
        
        .ai-bubble {
            background: rgba(255, 255, 255, 0.04);
            color: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-bottom-left-radius: 4px;
            backdrop-filter: blur(10px);
        }
        
        .bubble-content {
            font-size: 0.9375rem;
        }
        
        .bubble-content p {
            margin: 0 0 0.875rem 0;
        }
        
        .bubble-content p:last-child {
            margin-bottom: 0;
        }
        
        .bubble-content strong {
            font-weight: 600;
            color: #a78bfa;
        }
        
        .bubble-content ul, .bubble-content ol {
            margin: 0.875rem 0;
            padding-left: 1.5rem;
        }
        
        .bubble-content li {
            margin: 0.5rem 0;
        }
        
        .bubble-content code {
            background: rgba(0, 0, 0, 0.3);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.875rem;
            font-family: 'JetBrains Mono', 'Monaco', monospace;
        }
        
        .code-block-wrapper {
            margin: 1rem 0;
            border-radius: 10px;
            overflow: hidden;
            background: #1e1e1e;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        }
        
        .code-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 1rem;
            background: rgba(255, 255, 255, 0.04);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .code-lang {
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            color: #a78bfa;
            letter-spacing: 0.5px;
        }
        
        .copy-btn {
            background: rgba(167, 139, 250, 0.15);
            color: #a78bfa;
            border: none;
            padding: 0.375rem 0.75rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .copy-btn:hover {
            background: rgba(167, 139, 250, 0.25);
            transform: translateY(-1px);
        }
        
        .copy-btn:active {
            transform: translateY(0);
        }
        
        .highlight {
            margin: 0 !important;
            padding: 1rem !important;
            background: #1e1e1e !important;
            overflow-x: auto;
        }
        
        .highlight pre {
            margin: 0 !important;
            padding: 0 !important;
            background: transparent !important;
            font-size: 0.875rem;
            line-height: 1.6;
            font-family: 'JetBrains Mono', monospace;
        }
        
        .message-meta {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: 0.375rem;
            font-size: 0.75rem;
            color: rgba(255, 255, 255, 0.35);
        }
        
        .user-meta {
            justify-content: flex-end;
            margin-right: 43px;
        }
        
        .ai-meta {
            margin-left: 43px;
        }
        
        .timestamp {
            font-weight: 500;
        }
        
        .model-badge {
            background: rgba(167, 139, 250, 0.15);
            color: #a78bfa;
            padding: 3px 8px;
            border-radius: 10px;
            font-size: 0.6875rem;
            font-weight: 600;
            letter-spacing: 0.3px;
            text-transform: uppercase;
        }
        
        .message-attachments {
            display: flex;
            flex-wrap: wrap;
            gap: 0.875rem;
            margin-bottom: 0.875rem;
        }
        
        .attachment-preview {
            border-radius: 10px;
            overflow: hidden;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            max-width: 280px;
        }
        
        .preview-container img {
            width: 100%;
            height: auto;
            display: block;
        }
        
        .preview-container iframe {
            width: 100%;
            height: 360px;
            border: none;
        }
        
        .attachment-info {
            padding: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(0, 0, 0, 0.15);
        }
        
        .attachment-name {
            font-size: 0.8125rem;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.9);
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .attachment-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 0.625rem 1rem;
            border-radius: 16px;
            transition: all 0.2s ease;
        }
        
        .attachment-pill:hover {
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-2px);
        }
        
        .attachment-type {
            font-size: 0.6875rem;
            color: rgba(255, 255, 255, 0.45);
            font-weight: 600;
        }
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.04);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(167, 139, 250, 0.25);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(167, 139, 250, 0.4);
        }
    </style>
    <script>
        function copyCode(btn) {
            const codeBlock = btn.closest('.code-block-wrapper').querySelector('pre');
            const code = codeBlock.textContent;
            navigator.clipboard.writeText(code).then(() => {
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
                <div class="empty-title">Start a Conversation</div>
                <div class="empty-desc">Ask questions, upload documents, and get instant AI-powered answers</div>
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

        # Sanitization
        safe_text = re.sub(r"<script[\s\S]*?>[\s\S]*?</script>", "", raw_content, flags=re.IGNORECASE)
        safe_text = re.sub(r"<style[\s\S]*?>[\s\S]*?</style>", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r"<iframe[\s\S]*?>[\s\S]*?</iframe>", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r"&lt;script", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r"&lt;style", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r"&lt;iframe", "", safe_text, flags=re.IGNORECASE)
        safe_text = re.sub(r'\n\s*\n\s*\n+', '\n\n', safe_text).strip()

        time_str = format_timestamp(timestamp) if timestamp else ""

        # USER MESSAGE
        if role == "user":
            escaped_text = html.escape(safe_text)
            escaped_text = escaped_text.replace('\n', '<br>')
            file_html = render_file_attachments(files)

            chat_html += f'''
            <div class="message-wrapper user-message">
                {file_html}
                <div class="bubble user-bubble">
                    <div class="bubble-content">{escaped_text}</div>
                </div>
            </div>
            <div class="message-meta user-meta">
                <span class="timestamp">{time_str}</span>
            </div>
            '''

        # AI MESSAGE
        else:
            rendered_content = render_markdown_with_code(safe_text)
            model_badge = f'<span class="model-badge">{model}</span>' if model else ''

            chat_html += f'''
            <div class="message-wrapper ai-message">
                <div class="ai-avatar">🤖</div>
                <div class="bubble ai-bubble">
                    <div class="bubble-content">{rendered_content}</div>
                </div>
            </div>
            <div class="message-meta ai-meta">
                {model_badge}
                <span class="timestamp">{time_str}</span>
            </div>
            '''

    chat_html += '</div>'
    
    st.html(chat_html)