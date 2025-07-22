from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    bot_reply = get_bot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
