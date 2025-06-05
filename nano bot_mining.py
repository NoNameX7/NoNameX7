import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ganti dengan token bot Anda
TOKEN = "TOKEN_BOT_ANDA"

# Inisialisasi logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Struktur data sederhana untuk menyimpan koin user
user_coin = {}

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Hai {user.first_name}! Selamat datang di Bot Mining Koin. Gunakan /mine untuk menambang koin!")

def mine(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    # Jika user belum ada, inisialisasi dengan 0
    if user_id not in user_coin:
        user_coin[user_id] = 0
    
    # Tambahkan 10 koin setiap kali mining
    user_coin[user_id] += 10
    update.message.reply_text(f"Kamu mendapatkan 10 koin! Total koin kamu: {user_coin[user_id]}")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("mine", mine))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()