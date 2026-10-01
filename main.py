import os
import telebot
from telebot import types

# Token va Admin ID ni to'g'ridan-to'g'ri kiritamiz
TOKEN = "8852515416:AAG1QYBGKXA1xCwp3gqtaP5HgFS1"
ADMIN_ID = 8859818281

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(
        message, 
        f"Assalomu alaykum, {user_name}! 'KALIT UY' real estate botiga xush kelibsiz. Uy-joy sotish va ijaraga berish xizmatidan foydalanish uchun kerakli bo'limni tanlang:"
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Xabaringiz qabul qilindi! Tez orada administratorlarimiz siz bilan bog'lanishadi.")

# Render uchun muhim qism (Webhooks o'rniga oddiy Polling ishlatamiz)
if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
