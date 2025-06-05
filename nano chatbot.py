
@bot.message_handler(commands=['transfer'])
def transfer(message):
    try:
        # Format: /transfer [user_id] [jumlah]
        args = message.text.split()
        recipient_id = int(args[1])
        amount = int(args[2])
        sender_id = message.from_user.id
        
        if amount <= 0:
            bot.reply_to(message, "❌ Jumlah harus positif")
            return
        
        # Cek saldo pengirim
        c.execute("SELECT coins FROM users WHERE user_id=?", (sender_id,))
        sender_coins = c.fetchone()[0]
        
        if sender_coins < amount:
            bot.reply_to(message, "❌ Saldo tidak cukup")
            return
        
        # Kurangi saldo pengirim
        c.execute("UPDATE users SET coins=coins-? WHERE user_id=?", 
                  (amount, sender_id))
                  
        # Tambah saldo penerima
        c.execute("INSERT OR IGNORE INTO users (user_id, coins) VALUES (?, 0)", (recipient_id,))
        c.execute("UPDATE users SET coins=coins+? WHERE user_id=?", 
                  (amount, recipient_id))
                  
        conn.commit()
        bot.reply_to(message, f"✅ Berhasil transfer {amount} koin ke user {recipient_id}")
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")