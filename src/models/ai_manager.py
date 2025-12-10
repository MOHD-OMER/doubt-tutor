import requests
import re
import base64
import os
import html
from src.utils.logger import setup_logger


class AIManager:
    def __init__(self):
        self.logger = setup_logger()

        # API endpoints
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.hf_url = "https://router.huggingface.co/v1/chat/completions"

        # API keys
        self.groq_key = os.getenv("GROQ_API_KEY", "")
        self.hf_token = os.getenv("HF_TOKEN", "")  # Required for Router API

    # ------------------------------------------------------
    # Ultra HTML Sanitizer
    # ------------------------------------------------------
    def _strip_all_html(self, text):
        if not text:
            return ""

        text = str(text)

        # Remove HTML tags
        text = re.sub(r"<[^>]*>", "", text)

        # Decode safe HTML entities
        text = html.unescape(text)

        # Clean whitespace
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # ------------------------------------------------------
    # Groq Text-only Models
    # ------------------------------------------------------
    def _call_groq_text(self, prompt, model, temperature=0.7, max_tokens=2048):
        try:
            headers = {
                "Authorization": f"Bearer {self.groq_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens
            }

            response = requests.post(
                self.groq_url,
                json=payload,
                headers=headers,
                timeout=60
            )

            if response.status_code != 200:
                return f"❌ Groq Error: {response.text}"

            data = response.json()
            return data["choices"][0]["message"]["content"]

        except Exception as e:
            return f"❌ Groq Error: {str(e)}"

    # ------------------------------------------------------
    # HuggingFace Vision (Qwen2.5-VL via Router API)
    # ------------------------------------------------------
    def _call_hf_vision(self, prompt, files, temperature=0.7, max_tokens=1024):
        try:
            if not self.hf_token:
                raise ValueError("HF_TOKEN missing in .env")

            headers = {
                "Authorization": f"Bearer {self.hf_token}",
                "Content-Type": "application/json"
            }

            # Expecting only 1 file at a time
            f = files[0]
            image_b64 = f["data"]  # Base64 image string

            # Use data URI for base64 image (assuming JPEG; adjust mime type if needed)
            image_data_uri = f"data:image/jpeg;base64,{image_b64}"

            payload = {
                "model": "Qwen/Qwen2.5-VL-7B-Instruct:hyperbolic",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_data_uri
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": max_tokens,
                "temperature": temperature
            }

            res = requests.post(self.hf_url, headers=headers, json=payload, timeout=60)
            
            if res.status_code != 200:
                return f"❌ HF Response Error: {res.status_code} - {res.text}"

            out = res.json()
            return out["choices"][0]["message"]["content"]

        except Exception as e:
            return f"❌ HuggingFace Vision Error: {str(e)}"

    # ------------------------------------------------------
    # Public method: Auto-select model
    # ------------------------------------------------------
    def generate_response(self, question, model, temperature=0.7, max_tokens=2048, files=None):
        try:
            prompt = question.strip()
            files = files or []

            # UI → model resolver - FIXED MODEL NAMES
            model_map = {
                "llama-3.1-8b-instant": "llama-3.1-8b-instant",
                "gemma2-9b-it": "gemma2-9b-it",  # Gemma2 model
                "hf-vision": "hf-vision",  # Custom mode
            }

            # Validate keys
            if not self.groq_key:
                return "❌ Missing GROQ_API_KEY in your .env"

            real_model = model_map.get(model)

            # --------------------------
            # VISION MODEL (HF)
            # --------------------------
            if model == "hf-vision":
                if not files:
                    return "⚠️ Please upload an image for the vision model."

                reply = self._call_hf_vision(prompt, files, temperature, max_tokens)
                return self._strip_all_html(reply)

            # --------------------------
            # TEXT MODELS (GROQ)
            # --------------------------
            if files:
                prompt = (
                    "⚠️ Note: This model cannot see uploaded files.\n"
                    "Only answering based on text:\n\n" + prompt
                )

            reply = self._call_groq_text(prompt, real_model, temperature, max_tokens)
            return self._strip_all_html(reply)

        except Exception as e:
            return f"❌ AI Error: {str(e)}"
