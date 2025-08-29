from flask import Flask, request, jsonify, render_template, Response
from chatbot_logic import get_bot_response, load_history

app = Flask(__name__)
chat_history = {}

@app.route("/")
def home() -> str:
    """
    Render the main page with chatbot selection.

    Returns:
        str: Rendered HTML page for chatbot selection.
    """

    return render_template("page.html")

@app.route("/chat/<bot_name>")
def chat(bot_name: str) -> str:
    """
    Render the chat interface for a specific chatbot, including its history.

    Args:
        bot_name (str): The name of the selected chatbot personality.

    Returns:
        str: Rendered HTML page for chat interface with history passed in.
    """
    history = load_history(bot_name)
    return render_template("chat.html", bot_name=bot_name, history=history)

@app.route("/get_response/<bot_name>", methods=["POST"])
def get_response(bot_name: str) -> Response:
    """
    Handle an incoming chat message from the user.

    Args:
        bot_name (str): The name of the selected chatbot personality.

    Returns:
        Response: JSON response with the chatbot's reply, e.g. {"response": "<bot reply>"}
    """
    user_input = request.json.get("message")
    bot_reply = get_bot_response(user_input, bot_name)

    history = chat_history.setdefault(bot_name, [])
    history.append({"role": "you", "message": user_input})
    history.append({"role": bot_name, "message": bot_reply})

    return jsonify({"response": bot_reply})

@app.route('/clear/<bot_name>', methods=['POST'])
def clear(bot_name: str ) -> None:
    """
       Clear chat history for a specific chatbot, both in-memory and in JSON file.

       Args:
           bot_name (str): The name of the chatbot whose history will be cleared.

       Returns:
           None
    """
    json_path = f"chat_history/{bot_name}.json"

    try:
        # Remove JSON history file
        with open(json_path, "w", encoding="utf-8") as f:
            f.write("[]")
    except FileNotFoundError:
        pass  # If file doesn't exist, ignore

    chat_history.pop(bot_name, None)

if __name__ == "__main__":
    app.run(debug=True)