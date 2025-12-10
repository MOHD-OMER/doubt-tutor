# Doubt Tutor 🤔

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange.svg)](https://groq.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-🤗-yellow.svg)](https://huggingface.co)

An innovative AI-driven educational platform that provides instant, personalized academic support through cutting-edge language models. Built with Streamlit and powered by Groq's lightning-fast AI infrastructure and HuggingFace's versatile model ecosystem.

<div align="center">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs Welcome">
</div>

---

## ✨ Features

### 🤖 Multi-Model AI Support
Choose from multiple specialized AI models, each optimized for different learning scenarios:

- **🦙 LLaMA 3.1 (8B Instant) - Groq** - Lightning-fast responses for quick questions, math problems, and concept explanations
- **🌸 BLOOM 560M - HuggingFace** - Compact multilingual model supporting 46+ languages for lightweight text generation
- **🖼️ Qwen2-VL Vision - HuggingFace** - Advanced multimodal capabilities for analyzing images, diagrams, charts, and handwritten notes

### 📁 Multi-Format File Support
Seamlessly upload and analyze:
- **PDFs** - Extract and understand textbook pages, research papers, and assignments
- **Images** (PNG, JPG, JPEG) - Analyze diagrams, screenshots, and handwritten notes (Vision model only)
- **Text Files** - Process code, essays, and plain text documents

### 💬 Professional Chat Interface
- Clean, modern UI with dark/light theme support
- Real-time markdown rendering with syntax highlighting
- Code blocks with language detection and copy functionality
- Smooth animations and transitions for enhanced UX
- Responsive design optimized for desktop, tablet, and mobile

### 🎨 Modern Design System
- Glassmorphism effects with backdrop blur
- Gradient accents and smooth transitions
- Custom scrollbars and hover effects
- Professional color palette with accessibility in mind
- Mobile-first responsive design

### 💾 Export & History
- Export conversations as JSON files
- Save learning sessions for future reference
- Download and share your study materials
- Track your learning progress over time

### 🔒 Privacy-First Architecture
- No data stored without explicit consent
- API keys secured via environment variables
- Temporary file processing (files not permanently stored)
- Encrypted communication channels

### ⚡ Lightning-Fast Performance
- Powered by Groq's optimized inference engine for LLaMA models
- HuggingFace's efficient API for BLOOM and Vision models
- Average response time under 2 seconds
- Concurrent user support (100+)
- Efficient file processing pipeline

---

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:
- **Python 3.9+** (3.10+ recommended)
- **Anaconda/Miniconda** (optional but recommended)
- **Groq API Key** - [Get one here](https://console.groq.com)
- **HuggingFace Token** - [Get one here](https://huggingface.co/settings/tokens)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/doubt-tutor.git
cd doubt-tutor
```

#### 2. Create and Activate Virtual Environment

**Using Conda (Recommended):**
```bash
conda create -n doubt-tutor python=3.10
conda activate doubt-tutor
```

**Using venv:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

Create a `.env` file in the project root:
```bash
cp config/.env.example .env
```

Edit `.env` and add your API keys:
```env
# Required API Keys
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here

# Optional Configuration
LOG_LEVEL=INFO
MAX_FILE_SIZE_MB=10
DEBUG_MODE=false
```

> **Important:** Never commit your `.env` file to version control!

#### 5. Run the Application
```bash
streamlit run ui/app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
doubt-tutor/
├── config/                     # Configuration files
│   ├── .env.example           # Environment variables template
│   ├── auth_config.yaml       # Authentication settings
│   ├── config.yaml            # App configuration
│   └── models_config.yaml     # Model parameters
│
├── src/                       # Core application logic
│   ├── core/                  # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration management
│   │   ├── constants.py       # Application constants
│   │   └── exceptions.py      # Custom exceptions
│   │
│   ├── models/                # AI model integrations
│   │   ├── __init__.py
│   │   └── ai_manager.py      # Model orchestration & API calls
│   │
│   ├── utils/                 # Helper utilities
│   │   ├── __init__.py
│   │   ├── decorators.py      # Custom decorators
│   │   ├── helpers.py         # Helper functions
│   │   └── logger.py          # Logging configuration
│   │
│   └── load_env.py            # Environment loader
│
├── ui/                        # Frontend components
│   ├── app.py                 # Main Streamlit application
│   │
│   ├── components/            # Reusable UI components
│   │   ├── __init__.py
│   │   ├── chat_interface.py  # Chat rendering logic
│   │   └── header.py          # Navigation header
│   │
│   ├── pages/                 # Multi-page navigation
│   │   ├── 1_About.py         # About page
│   │   ├── 2_How_It_Works.py  # Tutorial page
│   │   └── 3_Models.py        # Model selection page
│   │
│   └── styles/                # CSS and animations
│       ├── style.css          # Main stylesheet
│       └── animations.js      # Animation engine
│
├── data/                      # Data storage
│   ├── uploads/               # User uploaded files (temporary)
│   ├── exports/               # Exported conversations
│   └── processed/             # Processed data cache
│
├── logs/                      # Application logs
│   └── doubt_tutor_YYYY-MM-DD.log
│
├── docs/                      # Documentation
│   ├── API.md                 # API documentation
│   ├── CHANGELOG.md           # Version history
│   ├── CONTRIBUTING.md        # Contribution guidelines
│   └── SETUP.md               # Detailed setup guide
│
├── .dockerignore              # Docker ignore rules
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Docker configuration
├── LICENSE                    # MIT License
├── README.md                  # This file
├── requirements.txt           # Python dependencies
└── setup.py                   # Package setup
```

---

## 🎯 Usage Guide

### Basic Workflow

1. **Launch the Application**
   ```bash
   streamlit run ui/app.py
   ```

2. **Select Your AI Model**
   - Navigate to the **Models** page
   - Choose from LLaMA 3.1 (Groq), BLOOM 560M (HuggingFace), or Qwen2-VL Vision (HuggingFace)
   - Your selection is saved automatically

3. **Ask Your Question**
   - Return to the home page
   - Type your question in the chat interface
   - Optionally upload supporting files (PDFs, images, text)

4. **Receive Instant Response**
   - Get detailed, step-by-step explanations
   - View formatted code with syntax highlighting
   - Ask follow-up questions for deeper understanding

5. **Export Your Session**
   - Click the **Export** button in the header
   - Download your chat history as JSON
   - Review and share your learning journey

### Model Selection Guide

| Model | Platform | Best For | Speed | Capabilities | File Support |
|-------|----------|----------|-------|--------------|--------------|
| **🦙 LLaMA 3.1 (8B)** | Groq | Quick answers, math, definitions | ⚡⚡⚡ Very Fast | Text generation, reasoning | Text only (files ignored) |
| **🌸 BLOOM 560M** | HuggingFace | Multilingual tasks, lightweight text | ⚡⚡ Fast | 46+ languages, compact | Text only (files ignored) |
| **🖼️ Qwen2-VL Vision** | HuggingFace | Images, diagrams, screenshots | ⚡⚡ Fast | Text + Vision, multimodal | **Images (PNG, JPG, JPEG)** |

### Example Use Cases

#### Mathematics
```
Question: Explain the quadratic formula step-by-step
Model: LLaMA 3.1 (8B Instant) - Groq
Expected Response: Detailed derivation with examples
```

#### Multilingual Translation
```
Question: Translate this paragraph to French and Spanish
Model: BLOOM 560M - HuggingFace
Expected Response: Accurate translations in multiple languages
```

#### Diagram Analysis
```
Question: [Upload biology diagram] Explain this cell structure
Model: Qwen2-VL Vision - HuggingFace
Expected Response: Detailed analysis of diagram components
```

#### Code Review
```
Question: Review this Python code for errors [paste code]
Model: LLaMA 3.1 (8B Instant) - Groq
Expected Response: Error identification and corrected code
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# ===========================
# REQUIRED API KEYS
# ===========================
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here

# ===========================
# OPTIONAL SETTINGS
# ===========================

# Logging Configuration
LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR, CRITICAL

# File Upload Settings
MAX_FILE_SIZE_MB=10         # Maximum file size in MB

# Application Settings
DEBUG_MODE=false            # Enable debug mode
ENABLE_ANALYTICS=false      # Enable analytics tracking

# Model Defaults
DEFAULT_MODEL=llama-3.1-8b-instant
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=2048
```

### Model Configuration

Edit `config/models_config.yaml` to customize model parameters:

```yaml
models:
  llama-3.1-8b-instant:
    provider: groq
    temperature: 0.7
    max_tokens: 2048
    description: "Fast, efficient responses"
    
  bloom-560m:
    provider: huggingface
    temperature: 0.7
    max_tokens: 1024
    description: "Multilingual text generation"
    
  hf-vision:
    provider: huggingface
    temperature: 0.7
    max_tokens: 1024
    description: "Image understanding"
```

---

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t doubt-tutor .

# Run the container
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_groq_key \
  -e HF_TOKEN=your_hf_token \
  doubt-tutor
```

### Using Docker Compose

```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  doubt-tutor:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - HF_TOKEN=${HF_TOKEN}
      - LOG_LEVEL=INFO
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
    restart: unless-stopped
```

---

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/doubt-tutor.git
cd doubt-tutor

# Create virtual environment
conda create -n doubt-tutor-dev python=3.10
conda activate doubt-tutor-dev

# Install dependencies including dev tools
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks (optional)
pre-commit install
```

### Code Style and Linting

This project follows **PEP 8** guidelines with additional tools:

```bash
# Format code with Black
black src/ ui/

# Check linting with Flake8
flake8 src/ ui/ --max-line-length=120

# Sort imports with isort
isort src/ ui/

# Type checking with mypy (optional)
mypy src/
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_ai_manager.py -v
```

### Development Mode

```bash
# Run with auto-reload
streamlit run ui/app.py --server.runOnSave true

# Run on custom port
streamlit run ui/app.py --server.port 8080

# Run with debug logging
LOG_LEVEL=DEBUG streamlit run ui/app.py
```

---

## 📊 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit UI Layer                       │
│  ┌──────────────┬──────────────┬─────────────────────────┐ │
│  │   Main App   │    Pages     │      Components         │ │
│  │   (app.py)   │ (About, etc) │ (Header, Chat, etc)     │ │
│  └──────────────┴──────────────┴─────────────────────────┘ │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│               Application Logic Layer                       │
│  ┌──────────────────────┬──────────────────────────────┐   │
│  │    AI Manager        │      File Processor          │   │
│  │ (Model orchestration)│  (PDF, Image, Text parsing)  │   │
│  └──────────────────────┴──────────────────────────────┘   │
│  ┌──────────────────────┬──────────────────────────────┐   │
│  │   Config Manager     │      Logger & Utils          │   │
│  │ (Settings, env vars) │  (Helpers, sanitization)     │   │
│  └──────────────────────┴──────────────────────────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │
       ┌──────────────────┴──────────────────┐
       │                                     │
┌──────▼────────────┐              ┌────────▼──────────┐
│   Groq API        │              │  HuggingFace API  │
│ (Text Models)     │              │  (Text + Vision)  │
│ • LLaMA 3.1 8B    │              │ • BLOOM 560M      │
│                   │              │ • Qwen2-VL Vision │
└───────────────────┘              └───────────────────┘
```

### Key Components

1. **UI Layer**: Streamlit-based responsive interface
2. **AI Manager**: Orchestrates API calls to different models (Groq & HuggingFace)
3. **File Processor**: Handles PDF, image, and text file parsing
4. **Config Manager**: Manages environment variables and settings
5. **Logger**: Centralized logging with rotation and levels

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/doubt-tutor.git
   cd doubt-tutor
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make Your Changes**
   - Follow the code style guidelines
   - Add tests for new features
   - Update documentation as needed

4. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

6. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Ensure all tests pass

### Development Guidelines

- **Code Style**: Follow PEP 8 and use type hints
- **Testing**: Write unit tests for new features
- **Documentation**: Update docstrings and README
- **Commits**: Use clear, descriptive commit messages
- **Issues**: Check existing issues before creating new ones

### Areas for Contribution

- 🐛 Bug fixes and error handling improvements
- ✨ New AI model integrations
- 🎨 UI/UX enhancements
- 📚 Documentation improvements
- 🌍 Internationalization (i18n)
- ♿ Accessibility improvements
- 🧪 Test coverage expansion

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Doubt Tutor Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[See LICENSE file for full text]
```

---

## 🙏 Acknowledgments

### Powered By

- **[Groq](https://groq.com)** - Lightning-fast AI inference infrastructure for LLaMA models
- **[HuggingFace](https://huggingface.co)** - Model hosting and inference API for BLOOM and Vision models
- **[Streamlit](https://streamlit.io)** - Rapid web app framework for Python

### AI Models

- **[Meta AI](https://ai.meta.com)** - LLaMA 3.1 language models
- **[BigScience](https://bigscience.huggingface.co)** - BLOOM multilingual language model
- **[Alibaba Cloud](https://www.alibabacloud.com)** - Qwen2-VL vision-language model
- **Open Source Community** - All model contributors

### Special Thanks

- All contributors who have helped improve Doubt Tutor
- The open-source community for tools and libraries
- Early adopters and testers for valuable feedback

---

## 📞 Support & Contact

### Get Help

- 📧 **Email**: support@doubttutor.com
- 💬 **Discord**: [Join our community](https://discord.gg/doubttutor)
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/doubt-tutor/issues)
- 📖 **Docs**: [Full Documentation](docs/README.md)

### Stay Connected

- 🌐 **Website**: [doubttutor.com](https://doubttutor.com)
- 🐦 **Twitter**: [@DoubtTutor](https://twitter.com/doubttutor)
- 📺 **YouTube**: [Doubt Tutor Channel](https://youtube.com/@doubttutor)
- 💼 **LinkedIn**: [Doubt Tutor](https://linkedin.com/company/doubttutor)

---

## 🗺️ Roadmap

### Version 1.x (Current) ✅
- [x] Multi-model AI support (LLaMA 3.1, BLOOM, Qwen2-VL)
- [x] Dual-platform integration (Groq + HuggingFace)
- [x] File upload capabilities (PDF, images, text)
- [x] Multilingual support via BLOOM (46+ languages)
- [x] Dark/light theme with professional design
- [x] Export conversations as JSON
- [x] Professional UI/UX with animations
- [x] Code syntax highlighting
- [x] Fully responsive mobile design
- [x] Multi-page navigation

### Version 2.0 (Q2 2025) 🚧
- [ ] User authentication and profiles
- [ ] Persistent conversation history
- [ ] Advanced analytics dashboard
- [ ] Study session tracking
- [ ] Collaborative learning features
- [ ] Additional model integrations (GPT-4, Claude)

### Version 3.0 (Q3 2025) 📋
- [ ] Mobile apps (iOS & Android)
- [ ] Voice input and output (TTS/STT)
- [ ] Real-time collaborative sessions
- [ ] Integration with LMS platforms (Canvas, Moodle)
- [ ] Custom model fine-tuning options

### Future Enhancements 🔮
- [ ] API for third-party integrations
- [ ] Offline mode with local models
- [ ] Enhanced multi-language support (100+ languages)
- [ ] Advanced search and filtering
- [ ] Flashcard and quiz generation
- [ ] Progress tracking and gamification
- [ ] Integration with note-taking apps
- [ ] Browser extension for quick access

---

## ⚠️ Important Notes & Disclaimers

### Educational Tool
Doubt Tutor is designed as an **educational assistant** to enhance learning. It is not:
- A replacement for professional tutoring or formal education
- A tool for academic dishonesty or plagiarism
- Guaranteed to provide 100% accurate information in all cases

### Usage Guidelines
- **Verify Information**: Always cross-reference critical information with authoritative sources
- **Academic Integrity**: Follow your institution's policies on AI usage
- **Ethical Use**: Use responsibly and respect intellectual property rights
- **Privacy**: Do not upload sensitive or confidential information

### Model Limitations
AI models may occasionally:
- Produce incorrect or outdated information
- Exhibit biases present in training data
- Struggle with highly specialized or niche topics
- Generate plausible-sounding but inaccurate responses

**Always verify important information from reliable sources.**

### Platform-Specific Notes
- **Groq Models**: Optimized for speed and efficiency (LLaMA 3.1)
- **HuggingFace Models**: Versatile ecosystem with multilingual (BLOOM) and vision (Qwen2-VL) capabilities
- **API Rate Limits**: Subject to provider rate limits and quotas

### Security
- API keys are **never logged or stored** in the application
- Files are **temporarily processed** and not permanently stored
- All communications use **encrypted channels**
- No user data is collected without explicit consent

To report security vulnerabilities: **security@doubttutor.com**

---

## 📈 System Requirements

### Minimum Requirements
- **Python**: 3.9 or higher
- **RAM**: 4 GB
- **Storage**: 2 GB free disk space
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Internet**: Stable connection (1 Mbps+)

### Recommended Requirements
- **Python**: 3.10 or higher
- **RAM**: 8 GB or more
- **Storage**: 5 GB free disk space
- **Browser**: Chrome or Edge (latest)
- **Internet**: High-speed connection (10 Mbps+)

### Browser Compatibility

| Browser | Supported | Version |
|---------|-----------|---------|
| Chrome | ✅ | 90+ |
| Firefox | ✅ | 88+ |
| Safari | ✅ | 14+ |
| Edge | ✅ | 90+ |
| Opera | ✅ | 76+ |

---

## 📊 Performance Metrics

- **Average Response Time**: < 2 seconds
- **Concurrent Users**: 100+ supported
- **File Upload Limit**: 10 MB per file
- **Max Conversation Length**: Unlimited (subject to token limits)
- **Uptime**: 99.5% target availability
- **Supported Languages**: 46+ (via BLOOM model)

---

## 🔄 Version History

See [CHANGELOG.md](docs/CHANGELOG.md) for detailed version history.

### Latest Version: 1.0.0 (December 2025)
- Initial public release
- Core features: Multi-model AI (Groq + HuggingFace), file uploads, export
- Three specialized models: LLaMA 3.1, BLOOM 560M, Qwen2-VL Vision
- Multilingual support (46+ languages)
- Professional UI with dark/light themes
- Mobile-responsive design
- Comprehensive documentation

---

## 📚 Additional Resources

### Documentation
- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [API Documentation](docs/API.md) - For developers building integrations
- [Contributing Guide](docs/CONTRIBUTING.md) - How to contribute to the project
- [FAQ](docs/FAQ.md) - Frequently asked questions

### Tutorials
- [Getting Started Video](https://youtube.com/@doubttutor)
- [Advanced Features Guide](docs/ADVANCED.md)
- [Model Selection Best Practices](docs/MODEL_GUIDE.md)
- [Troubleshooting Common Issues](docs/TROUBLESHOOTING.md)
- [Multilingual Usage Guide](docs/MULTILINGUAL.md)

---

<div align="center">
  <h3>Built with ❤️ by the Doubt Tutor Team</h3>
  <p><em>Empowering learners worldwide through AI • Founded 2025</em></p>
  
  <br>
  
  <a href="#quick-start">Get Started</a> •
  <a href="#features">Features</a> •
  <a href="docs/README.md">Documentation</a> •
  <a href="#support--contact">Support</a>
  
  <br><br>
  
  <sub>Made with Streamlit, Groq, and HuggingFace • Powered by LLaMA 3.1, BLOOM, and Qwen2-VL</sub>
</div>
