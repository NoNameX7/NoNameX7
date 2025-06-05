import telebot
import time
import random
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")  # Simpan token di file .env
bot = telebot.TeleBot(TOKEN)

# Database sederhana (simpan di memory)
user_coin = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_coin[user_id] = 0
    bot.reply_to(message, "🔷 **Bot Mining Koin** 🔷\n\n"
                          "Gunakan perintah /mine setiap 1 jam untuk mining koin!\n"
                          "Cek koinmu: /mycoin")

@bot.message_handler(commands=['mine'])
def mine(message):
    user_id = message.from_user.id
    last_mine = user_coin.get(f"last_{user_id}", 0)
    
    if time.time() - last_mine < 3600:  # Cooldown 1 jam
        bot.reply_to(message, "⏳ Tunggu 1 jam sebelum mining lagi!")
        return

    coins_earned = random.randint(1, 5)  # Koin acak
    user_coin[user_id] = user_coin.get(user_id, 0) + coins_earned
    user_coin[f"last_{user_id}"] = time.time()
    
    bot.reply_to(message, f"⛏️ Kamu mendapat {coins_earned} koin!\n"
                          f"Total koin: {user_coin[user_id]}")

@bot.message_handler(commands=['mycoin'])
def mycoin(message):
    user_id = message.from_user.id
    coins = user_coin.get(user_id, 0)
    bot.reply_to(message, f"💰 Total koinmu: {coins}")

print("Bot berjalan...")
bot.polling()