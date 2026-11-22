
import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return "Astra AI Server is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")

        if not message.strip():
            return jsonify({"error": "Empty message"}), 400

        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions="You are Astra AI. Reply in Nepali or English.",
            input=message
        )

        return jsonify({
            "reply": response.output_text
        })

    except Exception:
        return jsonify({
            "error": "AI server error"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
