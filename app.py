from flask import Flask, request, jsonify
from models import db, Chat
from openai_integration import get_chat_response
import json

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_id = request.json.get('user_id')
    user_message = request.json.get('message')

    if not user_id or not user_message:
        return jsonify({"error": "Missing parameters"}), 400

    # Fetch previous chat conversation or create a new one
    chat = Chat.query.filter_by(user_id=user_id).first()
    if not chat:
        chat = Chat(id=user_id, user_id=user_id, messages=[])
        db.session.add(chat)
        db.session.commit()

    # Add the user message to the conversation
    messages = chat.messages
    messages.append({"role": "user", "content": user_message})

    # Get response from OpenAI
    bot_response = get_chat_response(messages)

    # Add the bot's response to the conversation
    messages.append({"role": "assistant", "content": bot_response})

    # Update the conversation in the database
    chat.messages = messages
    db.session.commit()

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)