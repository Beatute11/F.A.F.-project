import os
from dotenv import load_dotenv
from google import genai
import google.generativeai as genai

load_dotenv()

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

history = []

print("Bot: Hello, how can I help you?")

while True:

    user_input = input("You: ")
    if user_input == 'stop':
        print("Bot: Goodbye")
        break

    chat_session = model.start_chat(
        history = history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f'Bot: {model_response}')
    print()

    history.append({"role" : "user", "parts" : [user_input]})
    history.append({"role" : "model", "parts" : [model_response]})
