from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Surpresa 1", url="https://u6h749.me/v/2a0f823b8e")],
        [InlineKeyboardButton("😈 Surpresa 2", url="https://bmh0oc.me/v/3125c2401d")],
        [InlineKeyboardButton("💋 Surpresa 3", url="https://oj3p6c.me/v/25a555d545")],
        [InlineKeyboardButton("👀 Surpresa 4", url="https://o44jt0.me/v/05b31dbba5")]
    ]

    await update.message.reply_text(
        "Olá meu amor ❤️\n\nEscolhe aqui a tua surpresa e desfruta dela 👀",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot online!")
    app.run_polling()

if __name__ == "__main__":
    main()
