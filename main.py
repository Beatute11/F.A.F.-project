from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_bot_response
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/chat/<bot_name>")
def chat(bot_name):
    return render_template("chat.html", bot_name=bot_name)

@app.route("/get_response/<bot_name>", methods=["POST"])
def get_response(bot_name):
    user_input = request.json.get("message")
    bot_reply = get_bot_response(user_input, bot_name)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)