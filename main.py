import telebot
import uuid
import os
from datetime import datetime

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 1964734222

bot = telebot.TeleBot(BOT_TOKEN)
users_db = {}

def get_user(uid, fname):
    if uid not in users_db:
        users_db[uid] = {
            "id": uid,
            "name": fname,
            "first": fname,
            "code": uuid.uuid4().hex[:8],
            "balance": 170.00,
            "orders": 25,
            "deposits": 18,
            "joined": datetime.now().strftime("%Y-%m-%d")
        }
    return users_db[uid]

@bot.message_handler(commands=['start'])
def start(m):
    u = get_user(m.from_user.id, m.from_user.first_name)
    bot.send_message(m.chat.id, f"||💎 Admin Kaviya Id Top Up Center 💎||\n\nHey {u['first']}!\nUse /wallet")

@bot.message_handler(commands=['wallet'])
def wallet(m):
    u = get_user(m.from_user.id, m.from_user.first_name)
    text = (
        f"┌──────────────────┐\n"
        f"│ 👤 USER PROFILE │\n"
        f"└──────────────────┘\n\n"
        f"├─ 🆔 ID: {u['id']}\n"
        f"├─ 👤 Name: {u['name']}\n"
        f"├─ 💰 Balance: {u['balance']:.2f} LKR\n"
        f"├─ 📦 Orders: {u['orders']}\n"
        f"└─ 📥 Deposits: {u['deposits']}"
    )
    bot.send_message(m.chat.id, text)

@bot.message_handler(commands=['products'])
def products(m):
    bot.send_message(m.chat.id, "✨ Jomiya Streams ✨\nWeekly Lite => 120 LKR\nWeekly => 560 LKR\nMonthly => 2700 LKR\n\n25=>100\n100=>315\n310=>920\n520=>1530\n1060=>3010\n2180=>6150\n5600=>14900\n11500=>29900")

@bot.message_handler(commands=['deposit'])
def deposit(m):
    bot.send_message(m.chat.id, "┌─ 💳 DEPOSIT MENU ─┐\n└──────────────────┘\n\nMin: 200 LKR\nMax: 50000 LKR\n\nEZ Cash - 0768747350\nWhatsApp - 076544308\nBinance - 774894425")

@bot.message_handler(commands=['id'])
def id_cmd(m):
    args = m.text.split()
    if len(args) < 2:
        bot.send_message(m.chat.id, "Use: /id GAME_ID")
        return
    u = get_user(m.from_user.id, m.from_user.first_name)
    bot.send_message(m.chat.id, f"{u['code']}\n{args[1]} 🆔✅")

@bot.message_handler(commands=['verify'])
def verify(m):
    rn = m.text.split()[1] if len(m.text.split())>1 else "20260810023756"
    dep_id = uuid.uuid4().hex[:12]
    bot.send_message(m.chat.id, f"┌─ ✅ DEPOSIT REQUESTED ─┐\n└────────────────────────┘\n\n📄 RN Number: {rn}\n🆔 Deposit ID: {dep_id}\n🏦 Method: RN\n\n⏳ Pending")

print("BOT RUNNING ON RENDER!")
bot.infinity_polling()
