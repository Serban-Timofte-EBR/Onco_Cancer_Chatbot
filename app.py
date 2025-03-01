import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app, origins="http://localhost:3000", methods=["GET", "POST", "PUT", "DELETE"], allow_headers=["Content-Type", "Authorization"])


@app.route("/chat", methods=["POST"])
def chat():
    # Retrieve the message from the incoming request body
    user_message = request.json.get("message")
    
    # Check if message is provided
    if not user_message:
        return jsonify({"error": "Message is required"}), 400  # Send error response if message is missing

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle OpenAI API errors

if __name__ == "__main__":
    app.run(debug=True)