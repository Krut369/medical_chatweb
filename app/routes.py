from flask import Blueprint, render_template, request, jsonify
from .gemini_client import get_gemini_model

main_bp = Blueprint("main", __name__)

with open("app/prompts/system_prompt.txt") as f:
    SYSTEM_PROMPT = f.read()

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message")

    if not user_msg:
        return jsonify({"reply": "Please enter a message."})

    prompt = SYSTEM_PROMPT + "\nUser: " + user_msg

    model = get_gemini_model()
    response = model.generate_content(prompt)

    return jsonify({"reply": response.text})
