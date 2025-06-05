@bot.message_handler(commands=['top10'])
def top10(message):
    c.execute("SELECT user_id, coins FROM users ORDER BY coins DESC LIMIT 10")
    top_users = c.fetchall()
    response = "🏆 **TOP 10 MINER** 🏆\n\n"
    for idx, (uid, coins) in enumerate(top_users, 1):
        response += f"{idx}. User {uid}: {coins} koin\n"
    bot.reply_to(message, response)