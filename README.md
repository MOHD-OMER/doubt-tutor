# 🎓 Doubt Tutor

> An AI-powered educational platform that provides instant, accurate answers to academic questions using multiple state-of-the-art language models.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Available Models](#available-models)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🌟 Overview

**Doubt Tutor** is an innovative AI-driven platform designed to empower learners worldwide by providing instant, accurate resolutions to academic doubts. Whether you're struggling with math problems, need help understanding complex diagrams, or want explanations for coding challenges, Doubt Tutor has you covered.

### Why Doubt Tutor?

- **⚡ Instant Insights**: Get responses in seconds from specialized AI models
- **🎓 Educational Focus**: All models fine-tuned for clear, step-by-step explanations
- **🔒 Privacy First**: Your queries stay private—no data stored without consent
- **🌍 Free & Open**: Basic access is free for all learners
- **📚 Multi-Format Support**: Upload PDFs, images, and text files
- **🤖 Multiple AI Models**: Choose from specialized models for different tasks

---

## ✨ Features

### Core Features

- **Multiple AI Models**: Choose from 4 specialized models (LLaMA 3.2, LLaVA, Mistral, DeepSeek R1)
- **Multimodal Support**: Upload and analyze PDFs, images (JPG, PNG), and text files
- **Real-time Chat Interface**: Beautiful, responsive chat UI with message history
- **File Preview**: View uploaded files before sending queries
- **Export Conversations**: Download chat history as JSON for future reference
- **Model Switching**: Seamlessly switch between models during conversations
- **Dark Theme**: Modern, eye-friendly dark interface

### Technical Features

- **Secure File Handling**: Files processed in-memory with size validation
- **Content Sanitization**: Protection against XSS and injection attacks
- **Error Handling**: Graceful error recovery with user-friendly messages
- **Session Management**: Persistent state across page navigation
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile

---

## 🎬 Demo

### Screenshots

**Home Page**
```
[Chat interface with file upload and model selection]
```

**About Page**
```
[Mission statement and feature highlights]
```

**Models Page**
```
[Model cards with specifications and selection]
```

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git (optional, for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/doubt-tutor.git
cd doubt-tutor
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv edu
edu\Scripts\activate

# macOS/Linux
python3 -m venv edu
source edu/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Configuration

1. Copy the example environment file:
```bash
cp config/.env.example .env
```

2. Edit `.env` and add your API keys (if needed):
```env
OLLAMA_BASE_URL=http://localhost:11434
MODEL_DEFAULT=llama3.2
MAX_FILE_SIZE_MB=10
```

### Step 5: Install Ollama (Required for local models)

Download and install Ollama from [ollama.ai](https://ollama.ai)

Pull the required models:
```bash
ollama pull llama3.2
ollama pull llava
ollama pull mistral
ollama pull deepseek-r1
```

---

## 💻 Usage

### Running the Application

```bash
streamlit run ui/app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using Doubt Tutor

1. **Select a Model**: Choose from the available AI models in the header dropdown
2. **Upload Files** (Optional): Click the 📎 icon to upload PDFs, images, or text files
3. **Ask Your Question**: Type your doubt in the input field
4. **Get Instant Answer**: Receive AI-powered explanations in seconds
5. **Export Chat**: Save your conversation history using the export button

### Best Practices

- **Be Specific**: Ask clear, detailed questions for better answers
- **Choose the Right Model**:
  - Use **LLaMA 3.2** for quick text-based questions
  - Use **LLaVA** for image analysis and diagrams
  - Use **Mistral** for creative or interdisciplinary topics
  - Use **DeepSeek R1** for coding and advanced reasoning
- **Upload Context**: Attach relevant files to get more accurate responses

---

## 🤖 Available Models

| Model | Icon | Best For | Specs |
|-------|------|----------|-------|
| **LLaMA 3.2** | 🦙 | Quick text queries, math problems | 8B parameters, Fast inference |
| **LLaVA** | 🖼️ | Visual content, diagrams, charts | Vision-Language, Multimodal |
| **Mistral** | 🌬️ | Creative writing, history analysis | 7B parameters, Versatile |
| **DeepSeek R1** | 🔍 | Coding, algorithms, complex proofs | Advanced reasoning, Code-focused |

---

## 📁 Project Structure

```
doubt-tutor/
├── config/
│   ├── .env.example          # Environment variables template
│   ├── auth_config.yaml      # Authentication settings
│   ├── config.yaml           # Main configuration
│   └── models_config.yaml    # Model specifications
├── data/
│   ├── exports/              # Exported chat histories
│   ├── processed/            # Processed uploads
│   └── uploads/              # Temporary file storage
├── docs/
│   ├── API.md               # API documentation
│   ├── CHANGELOG.md         # Version history
│   ├── CONTRIBUTING.md      # Contribution guidelines
│   ├── README.md            # This file
│   └── SETUP.md             # Detailed setup guide
├── logs/                    # Application logs
├── src/
│   ├── core/
│   │   ├── config.py        # Configuration loader
│   │   ├── constants.py     # App constants
│   │   └── exceptions.py    # Custom exceptions
│   ├── models/
│   │   └── ai_manager.py    # AI model interface
│   └── utils/
│       ├── decorators.py    # Utility decorators
│       ├── helpers.py       # Helper functions
│       └── logger.py        # Logging setup
├── ui/
│   ├── assets/              # Static assets
│   ├── components/
│   │   ├── chat_interface.py  # Chat UI component
│   │   └── header.py          # Header component
│   ├── pages/
│   │   ├── 1_About.py         # About page
│   │   ├── 2_How_It_Works.py  # Tutorial page
│   │   └── 3_Models.py        # Models page
│   ├── styles/
│   │   ├── style.css          # Main stylesheet
│   │   └── animations.js      # UI animations
│   └── app.py                 # Main application
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434

# Model Settings
MODEL_DEFAULT=llama3.2
TEMPERATURE_DEFAULT=0.7

# File Upload Settings
MAX_FILE_SIZE_MB=10
ALLOWED_EXTENSIONS=pdf,jpg,jpeg,png,txt

# Application Settings
LOG_LEVEL=INFO
EXPORT_FORMAT=json
```

### Model Configuration

Edit `config/models_config.yaml` to customize model settings:

```yaml
models:
  llama3.2:
    enabled: true
    context_length: 8192
    temperature: 0.7
  llava:
    enabled: true
    supports_vision: true
  mistral:
    enabled: true
  deepseek-r1:
    enabled: true
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t doubt-tutor:latest .
```

### Run Container

```bash
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  --env-file .env \
  doubt-tutor:latest
```

### Docker Compose

```yaml
version: '3.8'
services:
  doubt-tutor:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    env_file:
      - .env
    restart: unless-stopped
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write unit tests for new features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support

### Documentation

- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [API Documentation](docs/API.md) - API reference
- [Changelog](docs/CHANGELOG.md) - Version history

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/doubt-tutor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/doubt-tutor/discussions)
- **Email**: support@doubttutor.com

### FAQ

**Q: Which model should I use?**  
A: Use LLaMA 3.2 for text, LLaVA for images, Mistral for creative tasks, and DeepSeek R1 for coding.

**Q: Can I use this offline?**  
A: Yes! All models run locally via Ollama, no internet required after installation.

**Q: Is my data stored?**  
A: No, all processing happens in-memory. Files are not permanently stored.

**Q: How do I add more models?**  
A: Pull new models with Ollama and update the configuration files.

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io) - Web framework
- [Ollama](https://ollama.ai) - Local LLM runtime
- [Meta AI](https://ai.meta.com) - LLaMA models
- [Mistral AI](https://mistral.ai) - Mistral models
- [DeepSeek](https://www.deepseek.com) - DeepSeek models

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/doubt-tutor?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/doubt-tutor?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/doubt-tutor?style=social)

---

<div align="center">

**Built with ❤️ by educators and AI enthusiasts**

[Website](https://doubttutor.com) • [Documentation](docs/) • [Report Bug](https://github.com/yourusername/doubt-tutor/issues) • [Request Feature](https://github.com/yourusername/doubt-tutor/issues)

</div>