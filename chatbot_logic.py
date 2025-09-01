import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("key.env")

GEMINI_API = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=GEMINI_API)

model = genai.GenerativeModel("gemini-2.5-flash")

history_dir = "chat_history"
max_history_length = 200

def load_history(bot_name: str) -> list[dict[str, str]]:
    """
    Load chat history for a given bot from its JSON file.

    Args:
        bot_name (str): The name of the bot whose history is requested.

    Returns:
        list[dict]: A list of message dictionaries with keys:
            - "role": Either "user" or "model".
            - "message": The text content of the message.
        Returns an empty list if no history file exists.
    """
    path = os.path.join(history_dir, f"{bot_name}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(bot_name: str, history: list[dict[str, str]]) -> None:
    """
    Save chat history to a JSON file, trimming it to the maximum allowed length.

    Args:
        bot_name (str): The name of the bot to associate with the history file.
        history (list[dict]): The chat history containing role/message pairs.

    Returns:
        None
    """
    path = os.path.join(history_dir, f"{bot_name}.json")
    trimmed_history = history[:max_history_length]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(trimmed_history, f, indent=2)

def get_bot_response(user_input: str, bot_name: str) -> str:
    """
    Generate a chatbot response using Google Gemini based on prior history and personality.

    The function:
      1. Loads prior chat history from JSON.
      2. Converts history into Gemini's expected input format.
      3. Applies a personality prefix depending on the chosen bot:
            - Flirty: playful compliments, avoids flower knowledge.
            - Angry: polite start, then responds angrily.
            - Funny: wraps every response with "haha".
      4. Sends input + personality to Gemini and retrieves a response.
      5. Updates history, enforces max length, and saves it back to JSON.

    Args:
        user_input (str): The user's message to the chatbot.
        bot_name (str): The selected chatbot personality (flirty, angry, funny).
    Returns:
        str: The chatbot's reply.
    """
    history = load_history(bot_name)

    # Format for Gemini
    history_form = []
    for msg in history:
        history_form.append({"role": msg["role"], "parts": [msg["message"]]})

    # Apply personality prefix based on bot type
    if bot_name == "flirty":
        prefix = """
        You are a flirty bot that responds to everything flirty and always gives a compliment,
        but knows nothing about flowers.
        """
    elif bot_name == "angry":
        prefix = """
        Respond to everything with angry tone, but first sentence is always nice.
        """
    elif bot_name == "funny":
        prefix = """
        You are a funny bot that responds to everything funny and always starts and finishes message with "haha".
        """
    else:
        prefix = ""

    # Generate response
    chat_session = model.start_chat(history=history_form)
    response = chat_session.send_message(prefix + user_input)
    reply = response.text

    # Update and persist history
    history.append({"role": "user", "message": user_input})
    history.append({"role": "model", "message": reply})
    if len(history) > max_history_length:
        del history[:5] # Drops oldest 5 to keep file size manageable
    print(history[:max_history_length])
    save_history(bot_name, history)

    return reply