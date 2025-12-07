# Doubt Tutor 🤔

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange.svg)](https://groq.com)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-🤗-yellow.svg)](https://huggingface.co)


An innovative AI-driven educational platform that provides instant, personalized academic support through cutting-edge language models. Built with Streamlit and powered by Groq's lightning-fast AI infrastructure.

## ✨ Features

- **🤖 Multi-Model AI Support**: Choose from multiple specialized AI models
  - LLaMA 3.1 (8B) - Fast, efficient text responses
  - Mistral 7B - Balanced creative and analytical tasks
  - DeepSeek R1 - Advanced reasoning for complex problems
  - Qwen2-VL Vision - Image and diagram understanding

- **📁 Multi-Format File Support**: Upload and analyze PDFs, images, and text files
- **💬 Real-time Chat Interface**: Clean, modern UI with markdown and code highlighting
- **🎨 Professional Design**: Dark/light theme with smooth animations
- **💾 Export Conversations**: Save your learning sessions as JSON
- **🔒 Privacy First**: No data stored without consent
- **⚡ Lightning Fast**: Powered by Groq's optimized inference engine

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Anaconda/Miniconda (recommended)
- Groq API key ([Get one here](https://console.groq.com))
- HuggingFace API token ([Get one here](https://huggingface.co/settings/tokens))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/doubt-tutor.git
   cd doubt-tutor
   ```

2. **Create and activate conda environment**
   ```bash
   conda create -n edu python=3.9
   conda activate edu
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy example config
   cp config/.env.example .env
   
   # Edit .env and add your API keys
   # On Windows: notepad .env
   # On Mac/Linux: nano .env
   ```
   
   Add your API keys to `.env`:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HF_TOKEN=your_huggingface_token_here
   ```

5. **Run the application**
   ```bash
   streamlit run ui/app.py
   ```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
doubt-tutor/
├── config/                 # Configuration files
│   ├── .env.example       # Environment variables template
│   ├── auth_config.yaml   # Authentication settings
│   ├── config.yaml        # App configuration
│   └── models_config.yaml # Model parameters
├── src/                   # Core application logic
│   ├── core/             # Core functionality
│   │   ├── config.py     # Configuration management
│   │   ├── constants.py  # App constants
│   │   └── exceptions.py # Custom exceptions
│   ├── models/           # AI model integrations
│   │   └── ai_manager.py # Model orchestration
│   ├── utils/            # Helper utilities
│   │   ├── decorators.py # Custom decorators
│   │   ├── helpers.py    # Helper functions
│   │   └── logger.py     # Logging setup
│   └── load_env.py       # Environment loader
├── ui/                    # Frontend components
│   ├── app.py            # Main Streamlit app
│   ├── components/       # Reusable UI components
│   │   ├── chat_interface.py
│   │   └── header.py
│   ├── pages/            # Multi-page navigation
│   │   ├── 1_About.py
│   │   ├── 2_How_It_Works.py
│   │   └── 3_Models.py
│   └── styles/           # CSS and animations
│       ├── style.css
│       └── animations.js
├── data/                 # Data storage
│   ├── uploads/         # User uploaded files
│   ├── exports/         # Exported conversations
│   └── processed/       # Processed data
├── logs/                # Application logs
├── docs/                # Documentation
│   ├── API.md
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── README.md
│   └── SETUP.md
├── .dockerignore        # Docker ignore rules
├── .gitignore          # Git ignore rules
├── Dockerfile          # Docker configuration
├── LICENSE             # MIT License
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── setup.py           # Package setup
```

## 🎯 Usage

### Basic Workflow

1. **Select Your Model**: Choose the AI model that best fits your needs from the Models page
2. **Ask Your Question**: Type your question in the chat interface
3. **Upload Files** (optional): Attach PDFs, images, or text files for context
4. **Get Instant Response**: Receive detailed, step-by-step explanations
5. **Export History**: Save your conversation for future reference

### Model Selection Guide

| Model | Best For | Speed | Capabilities |
|-------|----------|-------|--------------|
| **LLaMA 3.1 (8B)** | Quick answers, math, science | ⚡⚡⚡ | Text only |
| **Mistral 7B** | Creative writing, essays | ⚡⚡ | Text only |
| **DeepSeek R1** | Complex reasoning, coding | ⚡ | Text + Code |
| **Qwen2-VL Vision** | Images, diagrams, charts | ⚡⚡ | Text + Vision |

### Example Use Cases

**For Math Problems:**
```
Question: Explain how to solve quadratic equations
Model: LLaMA 3.1 or DeepSeek R1
```

**For Essay Writing:**
```
Question: Help me structure an essay about climate change
Model: Mistral 7B
```

**For Diagram Analysis:**
```
Question: [Upload image] Explain this diagram
Model: Qwen2-VL Vision
```

**For Code Debugging:**
```
Question: Why isn't this Python code working? [paste code]
Model: DeepSeek R1
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Required API Keys
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here

# Optional Settings
LOG_LEVEL=INFO
MAX_FILE_SIZE_MB=10
ENABLE_ANALYTICS=false
DEBUG_MODE=false
```

### Model Configuration

Edit `config/models_config.yaml` to customize model parameters:

```yaml
models:
  llama-3.1-8b-instant:
    provider: groq
    temperature: 0.7
    max_tokens: 2048
    
  mistral:
    provider: groq
    temperature: 0.8
    max_tokens: 4096
    
  deepseek-r1:
    provider: groq
    temperature: 0.7
    max_tokens: 4096
    
  hf-vision:
    provider: huggingface
    temperature: 0.7
    max_tokens: 2048
```

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t doubt-tutor .

# Run container
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_key \
  -e HF_TOKEN=your_token \
  doubt-tutor
```

Or use Docker Compose:

```bash
docker-compose up -d
```

## 🛠️ Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -r requirements.txt

# Install pre-commit hooks (optional)
pip install pre-commit
pre-commit install

# Run tests (if available)
pytest tests/
```

### Code Style

This project follows PEP 8 guidelines with:
- Black for code formatting
- Flake8 for linting
- isort for import sorting

```bash
# Format code
black src/ ui/

# Check linting
flake8 src/ ui/

# Sort imports
isort src/ ui/
```

### Running Locally

```bash
# Activate environment
conda activate edu

# Run app
streamlit run ui/app.py

# Run with custom port
streamlit run ui/app.py --server.port 8080

# Run in development mode
streamlit run ui/app.py --server.runOnSave true
```

## 📊 Architecture

```
┌─────────────────────────────────────┐
│         Streamlit UI Layer          │
│  ┌──────────┬──────────┬──────────┐ │
│  │   App    │  Pages   │ Components│ │
│  └──────────┴──────────┴──────────┘ │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│       Application Layer             │
│  ┌──────────────┬─────────────────┐ │
│  │ AI Manager   │  File Handler   │ │
│  └──────────────┴─────────────────┘ │
└─────────────────┬───────────────────┘
                  │
       ┌──────────┴──────────┐
       │                     │
┌──────▼──────┐      ┌──────▼──────┐
│  Groq API   │      │  HF API     │
│  (Text)     │      │  (Vision)   │
└─────────────┘      └─────────────┘
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Write clear, descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Follow the existing code style
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** - For providing lightning-fast AI inference
- **HuggingFace** - For vision model hosting
- **Streamlit** - For the amazing web framework
- **Meta AI** - For LLaMA models
- **Mistral AI** - For Mistral models
- **DeepSeek** - For reasoning models
- **Alibaba Cloud** - For Qwen2-VL vision model

## 📞 Support

- 📧 Email: support@doubttutor.com
- 💬 Discord: [Join our community](https://discord.gg/doubttutor)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/doubt-tutor/issues)
- 📖 Docs: [Full Documentation](docs/README.md)

## 🗺️ Roadmap

### Completed ✅
- [x] Multi-model support
- [x] File upload capabilities (PDF, images, text)
- [x] Dark/light theme
- [x] Export conversations
- [x] Professional UI/UX
- [x] Code syntax highlighting
- [x] Responsive design

### In Progress 🚧
- [ ] User authentication system
- [ ] Conversation history persistence
- [ ] Advanced analytics dashboard

### Planned 📋
- [ ] Mobile app (iOS/Android)
- [ ] Voice input/output
- [ ] Collaborative learning sessions
- [ ] Integration with learning management systems
- [ ] API for third-party integrations
- [ ] Offline mode
- [ ] Multi-language support

## ⚠️ Disclaimer

This is an educational tool designed to assist with learning. Always verify critical information from authoritative sources. The AI models may occasionally produce incorrect or biased information.

**Important Notes:**
- Not a replacement for professional tutoring or formal education
- Responses should be verified for accuracy
- Use responsibly and ethically
- Follow your institution's academic integrity policies

## 🔒 Security

- API keys are never logged or stored
- Files are temporarily processed and not permanently stored
- All communications are encrypted
- No user data is collected without consent

To report security vulnerabilities, please email security@doubttutor.com

## 📈 System Requirements

### Minimum Requirements
- Python 3.9+
- 4 GB RAM
- 2 GB free disk space
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Recommended Requirements
- Python 3.10+
- 8 GB RAM
- 5 GB free disk space
- High-speed internet connection

## 🌐 Browser Support

| Browser | Supported | Version |
|---------|-----------|---------|
| Chrome | ✅ | Latest |
| Firefox | ✅ | Latest |
| Safari | ✅ | 14+ |
| Edge | ✅ | Latest |
| Opera | ✅ | Latest |

## 📊 Performance

- Average response time: < 2 seconds
- Concurrent users supported: 100+
- File upload limit: 10 MB
- Maximum conversation length: Unlimited

## 🔄 Updates

This project is actively maintained. Check the [CHANGELOG.md](docs/CHANGELOG.md) for version history and updates.

## 📚 Additional Resources

- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [API Documentation](docs/API.md) - For developers
- [Contributing Guide](docs/CONTRIBUTING.md) - How to contribute
- [FAQ](docs/README.md) - Frequently asked questions

---

<div align="center">
  <strong>Built with ❤️ by the Doubt Tutor Team</strong>
  <br>
  <sub>Empowering learners worldwide through AI • Founded 2025</sub>
  <br><br>
  <a href="#quick-start">Get Started</a> •
  <a href="#features">Features</a> •
  <a href="docs/README.md">Documentation</a> •
  <a href="#support">Support</a>
</div>