import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("/home/beata/Projektas/static/key.env")

GEMINI_API = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=GEMINI_API)

model = genai.GenerativeModel("gemini-2.5-flash"),

chat_session = model.start_chat(history=[])

print("Bot: Hello, how can I help you?")

def get_bot_response(user_input, bot_name):

    if bot_name == "flirty":
        prefix = """
        You are a flirty bot that responds to everything flirty and always gives a compliment,
        but knows nothing about flowers
        """
    # elif bot_name == "":
    #     prefix = "Respond in a friendly and encouraging tone: "
    # elif bot_name == "sarcastic":
    #     prefix = "Respond sarcastically: "

    response = chat_session.send_message(prefix + user_input)
    return response.text
