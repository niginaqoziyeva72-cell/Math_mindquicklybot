import telebot

TOKEN = "8296888507:AAGflQ3cNTsyq-8e6YDiCB3MqTMr-8COBTw"
bot = telebot.TeleBot(TOKEN)

# TESTLAR BAZASI
testlar = {
    "101": "abcda",
    "102": "cdabc",
    "2*": "bacdbaaccb"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot tayyor! ✅\nTestni tekshirish uchun format: 2*bacdbaaccb")

@bot.message_handler(func=lambda message: True)
def tekshirish(message):
    tekst = message.text.strip().lower()
    if "*" in tekst:
        try:
            kod, foydalanuvchi_javobi = tekst.split("*")
            kod = kod + "*"
            if kod in testlar:
                asl_javoblar = testlar[kod]
                togri_soni = sum(1 for i, j in zip(asl_javoblar, foydalanuvchi_javobi) if i == j)
                bot.reply_to(message, f"📊 Test: {kod}\n✅ To'g'ri: {togri_soni}\n❌ Xato: {len(asl_javoblar)-togri_soni}")
            else:
                bot.reply_to(message, "❌ Kod topilmadi.")
        except:
            bot.reply_to(message, "⚠️ Format: 2*bacdbaaccb")

bot.infinity_polling()
      
