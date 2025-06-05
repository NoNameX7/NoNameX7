
import sqlite3

# Tambahkan di awal script
conn = sqlite3.connect('mining.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (user_id INTEGER PRIMARY KEY, 
              coins INTEGER, 
              last_mine_time REAL)''')
conn.commit()

# Modifikasi fungsi mine
@bot.message_handler(commands=['mine'])
def mine(message):
    user_id = message.from_user.id
    c.execute("SELECT coins, last_mine_time FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    
    if not user:
        # User baru
        coins = 0
        last_mine = 0
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, 0, 0))
    else:
        coins, last_mine = user

    if time.time() - last_mine < 3600:
        bot.reply_to(message, "⏳ Tunggu 1 jam sebelum mining lagi!")
        return

    coins_earned = random.randint(1, 5)
    new_balance = coins + coins_earned
    
    # Update database
    c.execute("UPDATE users SET coins=?, last_mine_time=? WHERE user_id=?", 
              (new_balance, time.time(), user_id))
    conn.commit()
    
    bot.reply_to(message, f"⛏️ Kamu mendapat {coins_earned} koin!\n💰 Total: {new_balance}")