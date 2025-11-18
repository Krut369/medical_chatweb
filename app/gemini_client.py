import google.generativeai as genai
from flask import current_app

def get_gemini_model():
    api_key = current_app.config["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")
