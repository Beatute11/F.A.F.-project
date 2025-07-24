import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("/backend/key.env")

GEMINI_API = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=GEMINI_API)

model = genai.GenerativeModel("gemini-2.5-flash")

chat_session = model.start_chat(history=[])

print("Bot: Hello, how can I help you?")

def get_bot_response(user_input):
    response = chat_session.send_message(user_input)
    return response.text
