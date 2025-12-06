"""
Doubt Tutor - AI-Powered Educational Platform
Setup configuration for package installation and distribution
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
requirements_file = this_directory / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Package metadata
setup(
    name="doubt-tutor",
    version="1.0.0",
    author="Doubt Tutor Team",
    author_email="support@doubttutor.com",
    description="AI-powered educational platform for instant academic doubt resolution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/doubt-tutor",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/doubt-tutor/issues",
        "Documentation": "https://github.com/yourusername/doubt-tutor/docs",
        "Source Code": "https://github.com/yourusername/doubt-tutor",
    },
    
    # Package discovery
    packages=find_packages(exclude=["tests", "tests.*", "docs", "logs", "data"]),
    
    # Package data
    package_data={
        "ui": [
            "styles/*.css",
            "styles/*.js",
            "assets/*",
        ],
        "config": [
            "*.yaml",
            ".env.example",
        ],
    },
    include_package_data=True,
    
    # Python version requirement
    python_requires=">=3.9",
    
    # Dependencies
    install_requires=requirements,
    
    # Optional dependencies for development
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
            'pre-commit>=3.0.0',
        ],
        'docs': [
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.2.0',
            'sphinx-autodoc-typehints>=1.22.0',
        ],
        'docker': [
            'docker>=6.0.0',
        ],
    },
    
    # Entry points for command-line scripts
    entry_points={
        'console_scripts': [
            'doubt-tutor=ui.app:main',
        ],
    },
    
    # Classifiers for PyPI
    classifiers=[
        # Development status
        "Development Status :: 4 - Beta",
        
        # Intended audience
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        
        # Topic
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Python versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        
        # Operating systems
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        
        # Framework
        "Framework :: Streamlit",
        
        # Natural Language
        "Natural Language :: English",
    ],
    
    # Keywords for easier discovery
    keywords=[
        "ai",
        "education",
        "tutor",
        "learning",
        "llm",
        "chatbot",
        "doubt-resolution",
        "academic",
        "streamlit",
        "ollama",
        "machine-learning",
        "nlp",
        "multimodal",
    ],
    
    # Minimum versions for critical dependencies
    zip_safe=False,
    
    # Additional metadata
    platforms=["any"],
    license="MIT",
    
    # Data files to include
    data_files=[
        ('config', [
            'config/config.yaml',
            'config/models_config.yaml',
            'config/auth_config.yaml',
            'config/.env.example',
        ]),
    ],
)