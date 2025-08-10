import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get("BOT_TOKEN")  # هتحطه في Render كمتغير بيئة
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is required")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/" + TOKEN, methods=["POST"])
def telegram_webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    text = (message.text or "").strip()
    if text == "السلام عليكم":
        bot.send_message(message.chat.id, "وعليكم السلام")
    else:
        bot.send_message(message.chat.id, "ما فهمتش الرسالة 🙃")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
