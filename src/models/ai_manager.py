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
    # HuggingFace Text Model (Phi-3-mini-4k-instruct)
    # ------------------------------------------------------
    def _call_hf_text(self, prompt, temperature=0.7, max_tokens=1024):
        try:
            if not self.hf_token:
                raise ValueError("HF_TOKEN missing in .env")

            headers = {
                "Authorization": f"Bearer {self.hf_token}",
                "Content-Type": "application/json"
            }

            # Use Phi-3 Mini model from HuggingFace Router
            payload = {
                "model": "microsoft/Phi-3-mini-4k-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
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
            return f"❌ HuggingFace Text Error: {str(e)}"

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
            
            # Debug logging
            self.logger.info(f"🔍 Model selected: {model}")
            self.logger.info(f"📝 Prompt length: {len(prompt)} chars")
            self.logger.info(f"📎 Files attached: {len(files)}")

            # ------------- PHI-3 MINI MODEL (HuggingFace) --------------
            if model == "phi-3-mini":
                self.logger.info("✅ Routing to HuggingFace Phi-3 Mini")
                if not self.hf_token:
                    return "❌ Missing HF_TOKEN in your .env"
                
                if files:
                    prompt = (
                        "⚠️ Note: This model cannot see uploaded files.\n"
                        "Only answering based on text:\n\n" + prompt
                    )
                
                reply = self._call_hf_text(prompt, temperature, max_tokens)
                return self._strip_all_html(reply)

            # ------------- VISION MODEL (HuggingFace) --------------
            if model == "hf-vision":
                self.logger.info("✅ Routing to HuggingFace Vision")
                if not self.hf_token:
                    return "❌ Missing HF_TOKEN in your .env"
                
                if not files:
                    return "⚠️ Please upload an image for the vision model."
                
                reply = self._call_hf_vision(prompt, files, temperature, max_tokens)
                return self._strip_all_html(reply)

            # ------------- GROQ MODELS --------------
            # Only Groq-supported models go in this map
            groq_model_map = {
                "llama-3.1-8b-instant": "llama-3.1-8b-instant",
            }
            
            if model in groq_model_map:
                self.logger.info(f"✅ Routing to Groq: {groq_model_map[model]}")
                if not self.groq_key:
                    return "❌ Missing GROQ_API_KEY in your .env"
                
                real_model = groq_model_map[model]
                
                if files:
                    prompt = (
                        "⚠️ Note: This model cannot see uploaded files.\n"
                        "Only answering based on text:\n\n" + prompt
                    )
                
                reply = self._call_groq_text(prompt, real_model, temperature, max_tokens)
                return self._strip_all_html(reply)

            # ------------- UNKNOWN MODEL --------------
            self.logger.error(f"❌ Unknown model: {model}")
            return f"❌ Unknown model selected: {model}"

        except Exception as e:
            return f"❌ AI Error: {str(e)}"
