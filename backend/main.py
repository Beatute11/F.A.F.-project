from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/chat/<bot_name>")
def chat(bot_name):
    return render_template("chat.html", bot_name=bot_name)