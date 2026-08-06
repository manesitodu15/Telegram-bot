import os
import threading
import time
import telebot

from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(TOKEN)

# Petit serveur pour Render (gratuit)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton("🔥 Surpresa 1", url="https://u6h749.me/v/2a0f823b8e")
    )
    markup.add(
        InlineKeyboardButton("😈 Surpresa 2", url="https://bmh0oc.me/v/3125c2401d")
    )
    markup.add(
        InlineKeyboardButton("💋 Surpresa 3", url="https://oj3p6c.me/v/25a555d545")
    )
    markup.add(
        InlineKeyboardButton("👀 Surpresa 4", url="https://o44jt0.me/v/05b31dbba5")
    )

    bot.send_message(
        message.chat.id,
        "Olá meu amor ❤️\n\nEscolhe aqui a tua surpresa e desfruta dela 👀",
        reply_markup=markup
    )


print("Bot online!")

while True:
    try:
        bot.infinity_polling(skip_pending=True, timeout=30, long_polling_timeout=30)
    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(5)
