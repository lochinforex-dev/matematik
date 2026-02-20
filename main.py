import telebot
import google.generativeai as genai
from flask import Flask
from threading import Thread
import os

# 1. KALITLAR
BOT_TOKEN = "8570831864:AAEY860HTdudiMpkG9-SZ0NM0HxNJI5cquc"
API_KEY = "AIzaSyBgpXPCLXpwTIPTqoHznkjrnmr4f9C3tq8"

# 2. SOZLAMALAR
bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=API_KEY)

# MODEL NOMINI TO'G'RILADIK
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Men Gemini botman. Savolingizni yozing.")

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        if response.text:
            bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Birozdan so'ng qayta urinib ko'ring.")

app = Flask('')
@app.route('/')
def home(): return "Bot ishlamoqda!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
