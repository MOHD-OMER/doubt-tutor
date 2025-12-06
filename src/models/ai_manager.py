import requests
import re
import base64
import os
from src.utils.logger import setup_logger


class AIManager:
    def __init__(self):
        self.logger = setup_logger()

        # API endpoints
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

        # API keys (Set these in your environment)
        self.groq_key = os.getenv("GROQ_API_KEY", "")
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")

    # ------------------------------------------------------
    # Ultra HTML Sanitizer (Safe for UI renderer)
    # ------------------------------------------------------
    def _strip_all_html(self, text):
        if not text:
            return ""

        text = str(text)

        # Remove HTML tags
        text = re.sub(r"<[^>]*>", "", text)

        # Remove HTML entities
        html_entities = {
            "&lt;": "<", "&gt;": ">", "&amp;": "&",
            "&quot;": '"', "&apos;": "'", "&nbsp;": " ",
            "&#39;": "'", "&#34;": '"',
        }
        for ent, val in html_entities.items():
            text = text.replace(ent, val)

        # Remove leftover entities
        text = re.sub(r"&[a-zA-Z0-9#]+;", "", text)

        # Remove CSS/UI classes accidentally injected
        ui_terms = [
            "bubble", "message", "wrapper", "timestamp",
            "meta", "ai-bubble", "user-bubble"
        ]
        for term in ui_terms:
            text = text.replace(term, "")

        # Clean whitespace
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # ------------------------------------------------------
    # Gemini (Vision + Text)
    # ------------------------------------------------------
    def _call_gemini(self, prompt, files):
        try:
            contents = [{"role": "user", "parts": []}]

            # Add text prompt
            contents[0]["parts"].append({"text": prompt})

            # Add image/pdf files
            for f in files:
                # FIX #1: Changed from "mime_type" to "type" to match Streamlit uploader
                mime = f.get("type", "")
                data = f.get("data", "")

                contents[0]["parts"].append({
                    "inline_data": {
                        "mime_type": mime,
                        "data": data
                    }
                })

            url = f"{self.gemini_url}?key={self.gemini_key}"

            response = requests.post(
                url,
                json={"contents": contents},
                timeout=60
            )

            if response.status_code != 200:
                self.logger.error(response.text)
                return f"❌ Gemini Error: {response.text}"

            data = response.json()

            # Extract text
            try:
                reply = data["candidates"][0]["content"]["parts"][0]["text"]
            except:
                reply = "⚠️ Gemini returned an unexpected response."

            return reply

        except Exception as e:
            self.logger.error(str(e))
            return f"❌ Gemini Error: {str(e)}"

    # ------------------------------------------------------
    # Groq (Text-only)
    # ------------------------------------------------------
    def _call_groq(self, prompt, model):
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
                "temperature": 0.7
            }

            response = requests.post(
                self.groq_url,
                json=payload,
                headers=headers,
                timeout=60
            )

            if response.status_code != 200:
                self.logger.error(response.text)
                return f"❌ Groq Error: {response.text}"

            data = response.json()
            reply = data["choices"][0]["message"]["content"]

            return reply

        except Exception as e:
            self.logger.error(str(e))
            return f"❌ Groq Error: {str(e)}"

    # ------------------------------------------------------
    # Public method -> auto-selects model
    # ------------------------------------------------------
    def generate_response(self, question, model, temperature=0.7, files=None):
        try:
            prompt = question.strip()
            files = files or []

            # FIX #3: Add API key validation
            if model != "gemini-flash" and not self.groq_key:
                return "❌ Missing GROQ_API_KEY in your .env"

            if model == "gemini-flash" and not self.gemini_key:
                return "❌ Missing GEMINI_API_KEY in your .env"

            # Choose provider
            if model == "gemini-flash":
                reply = self._call_gemini(prompt, files)

            else:
                # Groq models cannot view images → warn user
                if files:
                    prompt = (
                        "Note: This model cannot see uploaded files. "
                        "Only answer using the text below:\n\n" + prompt
                    )
                reply = self._call_groq(prompt, model)

            # Final sanitize
            reply = self._strip_all_html(reply)

            return reply or "⚠️ AI returned an empty response."

        except Exception as e:
            self.logger.error(str(e))
            return f"❌ AI Error: {str(e)}"