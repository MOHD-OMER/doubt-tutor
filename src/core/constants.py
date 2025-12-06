"""
Application-wide constants
"""
from enum import Enum

class SessionState:
    """Session state keys"""
    CHAT_HISTORY = "chat_history"
    USER_ID = "user_id"
    SELECTED_MODEL = "selected_model"
    ACADEMIC_INFO = "academic_info"
    UPLOADED_FILES = "uploaded_files"
    FILE_CONTENTS = "file_contents"

class UIConstants:
    """UI-related constants"""
    PAGE_TITLE = "🎓 Doubt Tutor - AI-Powered Learning Assistant"
    PAGE_ICON = "🎓"
    LAYOUT = "wide"
    
    # Sidebar
    SIDEBAR_TITLE = "🤖 AI Configuration"
    MODEL_SECTION = "Model Selection"
    SETTINGS_SECTION = "Settings"
    
    # Main sections
    ACADEMIC_FORM_TITLE = "📚 Academic Information"
    CHAT_TITLE = "💬 Ask Your Doubt"
    HISTORY_TITLE = "📜 Conversation History"
    
    # Messages
    WELCOME_MESSAGE = """
    Welcome to **Doubt Tutor**! 👋
    
    I'm your AI-powered learning assistant, here to help you with:
    - 📖 Detailed explanations of concepts
    - 🧮 Step-by-step problem solving
    - 📄 Document analysis (PDF, images, text files)
    - 🎯 Personalized learning guidance
    
    Get started by selecting your subject and asking your question!
    """
    
    ERROR_NO_QUESTION = "⚠️ Please enter your question"
    ERROR_FILE_PROCESSING = "❌ Error processing file"
    SUCCESS_RESPONSE = "✅ Response generated successfully"

class ModelConstants:
    """AI Model constants"""
    AVAILABLE_MODELS = {
        "llama3.2": {
            "name": "Llama 3.2",
            "description": "Fast and efficient for general queries",
            "context_length": 4096,
            "icon": "🦙"
        },
        "mistral": {
            "name": "Mistral 7B",
            "description": "Balanced performance and quality",
            "context_length": 8192,
            "icon": "🌊"
        },
        "deepseek-r1": {
            "name": "Deepseek R1",
            "description": "Best for complex reasoning tasks",
            "context_length": 16384,
            "icon": "🧠"
        }
    }
    
    DEFAULT_MODEL = "llama3.2"

class AcademicConstants:
    """Academic-related constants"""
    SUBJECTS = [
        "Mathematics", "Physics", "Chemistry", "Biology",
        "Computer Science", "Engineering", "Economics",
        "History", "Literature", "Other"
    ]
    
    PRIORITY_LEVELS = ["Beginner", "Intermediate", "Advanced", "Expert"]
    
    LEARNER_ROLES = [
        "High School Student",
        "Undergraduate Student",
        "Graduate Student",
        "Self-Learner",
        "Professional"
    ]

class FileConstants:
    """File processing constants"""
    MAX_FILE_SIZE_MB = 10
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
    
    ALLOWED_EXTENSIONS = {
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg'
    }
    
    OCR_CONFIGS = [
        r'--oem 3 --psm 6',  # Default
        r'--oem 3 --psm 3',  # Fully automatic page segmentation
        r'--oem 1 --psm 6'   # Legacy engine
    ]

class DatabaseConstants:
    """Database-related constants"""
    DEFAULT_DB_PATH = "data/doubt_tutor.db"
    BACKUP_DIR = "data/backups"
    LOG_DIR = "logs"