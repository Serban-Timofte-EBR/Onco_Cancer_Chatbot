from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
from dotenv import load_dotenv
import os

load_dotenv()


def get_chat_response(messages):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=messages)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I couldn't process your request at this moment."