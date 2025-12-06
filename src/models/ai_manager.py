"""
AI Manager — Handles communication with Ollama Local LLM (Vision + Text SAFE)
"""

import requests
import re
from src.utils.logger import setup_logger


class AIManager:
    def __init__(self):
        self.logger = setup_logger()
        self.ollama_url = "http://localhost:11434/api/generate"

    def _strip_all_html(self, text):
        """Aggressively strip ALL HTML tags and entities from text"""
        if not text:
            return ""
        
        # Convert to string if not already
        text = str(text)
        
        # Remove ALL HTML tags (including malformed ones)
        text = re.sub(r'<[^>]*>', '', text)
        text = re.sub(r'<[^>]*$', '', text)  # Remove incomplete tags
        text = re.sub(r'^[^<]*>', '', text)  # Remove closing tags at start
        
        # Remove HTML entities
        html_entities = {
            '&lt;': '<',
            '&gt;': '>',
            '&amp;': '&',
            '&quot;': '"',
            '&apos;': "'",
            '&nbsp;': ' ',
            '&#39;': "'",
            '&#34;': '"',
        }
        for entity, char in html_entities.items():
            text = text.replace(entity, char)
        
        # Remove any remaining HTML entity patterns
        text = re.sub(r'&[a-zA-Z0-9#]+;', '', text)
        
        # Remove common CSS class patterns that might appear
        text = re.sub(r'class\s*=\s*["\'][^"\']*["\']', '', text)
        text = re.sub(r'style\s*=\s*["\'][^"\']*["\']', '', text)
        
        # Remove div, span, and other container references
        unwanted_terms = [
            'bubble-user-bubble', 'bubble-content', 'message-meta', 
            'user-meta', 'ai-bubble', 'message-wrapper', 'timestamp',
            'user-bubble', 'ai-message', 'user-message'
        ]
        for term in unwanted_terms:
            text = text.replace(term, '')
        
        # Clean up excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        
        return text.strip()

    def generate_response(self, question: str, model: str, temperature: float = 0.7, files=None):
        """
        Send prompt + optional files to Ollama and return response safely.

        Supports:
        - Text-only models (LLaMA, Mistral, DeepSeek)
        - Vision models (LLaVA)
        """

        try:
            prompt = question.strip()
            files = files or []

            has_images = any("image" in f.get("type", "") for f in files)
            has_files = len(files) > 0

            # -------------------------
            # MODEL CAPABILITIES
            # -------------------------
            vision_model = "llava" in model.lower()

            # ❌ text-only model received files
            if has_files and not vision_model:
                prompt = (
                    "The user uploaded files but this model cannot read them.\n"
                    "Answer only the text question.\n\n"
                    + prompt
                )

            # -------------------------
            # BUILD PAYLOAD
            # -------------------------
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature
                }
            }

            # -------------------------
            # ATTACH IMAGES (VISION)
            # -------------------------
            if vision_model and has_images:
                payload["images"] = [
                    f["data"] for f in files if "image" in f.get("type", "")
                ]

                payload["prompt"] = (
                    "Analyze the image(s) carefully and answer the question.\n\n"
                    + prompt
                )

            # -------------------------
            # SEND REQUEST
            # -------------------------
            response = requests.post(
                self.ollama_url,
                json=payload,
                timeout=300
            )

            # -------------------------
            # ERROR HANDLING
            # -------------------------
            if response.status_code != 200:
                self.logger.error(response.text)
                raise Exception("Ollama returned non-200 response")

            data = response.json()
            reply = data.get("response", "").strip()

            if not reply:
                return "⚠️ AI returned an empty reply."

            # -------------------------
            # ✅ ULTRA-AGGRESSIVE HTML STRIPPING
            # -------------------------
            reply = self._strip_all_html(reply)
            
            # Final safety check - if still contains HTML tags, strip them again
            if '<' in reply and '>' in reply:
                reply = re.sub(r'<[^>]*>', '', reply)
            
            return reply.strip() if reply.strip() else "⚠️ AI response was empty after sanitization."

        except requests.exceptions.ConnectionError:
            self.logger.error("Ollama not running")
            return "❌ Ollama server is not running. Please start Ollama."

        except requests.exceptions.Timeout:
            self.logger.error("Timeout")
            return "⏳ AI took too long to respond. Try again."

        except Exception as e:
            self.logger.error(f"Ollama Error: {str(e)}")
            return f"❌ AI Error: {str(e)}"