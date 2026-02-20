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

# MODEL NOMINI YANGILADIK (Xatolikni to'g'rilaydi)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Men Gemini sun'iy intellekt botiman. Savolingizni yozing.")

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        # Sun'iy intellektdan javob olish
        response = model.generate_content(message.text)
        if response.text:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "Kechirasiz, javob bera olmadim.")
    except Exception as e:
        print(f"Xatolik: {e}")
        bot.reply_to(message, "Hozircha javob bera olmayman, birozdan so'ng qayta urinib ko'ring.")

# Render serveri botni o'chirib qo'ymasligi uchun Flask server
app = Flask('')

@app.route('/')
def home():
    return "Bot muvaffaqiyatli ishlamoqda!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    print("Bot yoqildi...")
    bot.infinity_polling()
