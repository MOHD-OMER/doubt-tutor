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
        self.hf_url = "https://api-inference.huggingface.co/models/Qwen/Qwen2-VL-7B-Instruct"

        # API keys
        self.groq_key = os.getenv("GROQ_API_KEY", "")
        self.hf_token = os.getenv("HF_TOKEN", "")  # Optional, HF works without token

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
    # HuggingFace Vision (Qwen2-VL)
    # ------------------------------------------------------
    def _call_hf_vision(self, prompt, files):
        try:
            headers = (
                {"Authorization": f"Bearer {self.hf_token}"}
                if self.hf_token else {}
            )

            # Expecting only 1 file at a time
            f = files[0]

            payload = {
                "inputs": {
                    "prompt": prompt,
                    "image": f["data"]  # Base64 image string
                }
            }

            res = requests.post(self.hf_url, headers=headers, json=payload, timeout=60)
            out = res.json()

            try:
                return out[0]["generated_text"]
            except:
                return str(out)

        except Exception as e:
            return f"❌ HuggingFace Vision Error: {str(e)}"

    # ------------------------------------------------------
    # Public method: Auto-select model
    # ------------------------------------------------------
    def generate_response(self, question, model, temperature=0.7, max_tokens=2048, files=None):
        try:
            prompt = question.strip()
            files = files or []

            # UI → model resolver
            model_map = {
                "llama-3.1-8b-instant": "llama-3.1-8b-instant",
                "mistral": "mistral-7b-instruct",
                "deepseek-r1": "deepseek-r1-distill-qwen-32b",
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

                reply = self._call_hf_vision(prompt, files)
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
