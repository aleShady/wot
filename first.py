from flask import Flask, render_template, request

import os
import telegram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():
    bot = telegram.Bot(token=os.environ["from flask import Flask, render_template, request

import os
import telegram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():
    bot = telegram.Bot(token=os.environ["1815441409:AAE22OLP3DOblzIWWk2IvjN0Q_TcniS2YSo"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id     = update.effective_chat.id
        text        = update.message.text
        first_name  = update.effective_chat.first_name
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=f"{text} {first_name}")
        return 'ok'
    return 'error'

def index():
    return webhook()"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id     = update.effective_chat.id
        text        = update.message.text
        first_name  = update.effective_chat.first_name
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=f"{text} {first_name}")
        return 'ok'
    return 'error'

def index():
    return webhook()