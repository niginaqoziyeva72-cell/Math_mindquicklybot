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
            # Foydalanuvchi yuborgan qismlarni ajratamiz
            qismlar = tekst.split("*")
            kod_qismi = qismlar[0] + "*"
            foydalanuvchi_javobi = qismlar[1]
            
            if kod_qismi in testlar:
                asl_javoblar = testlar[kod_qismi]
                # To'g'ri javoblarni hisoblash
                togri_soni = sum(1 for i, j in zip(asl_javoblar, foydalanuvchi_javobi) if i == j)
                xato_soni = len(asl_javoblar) - togri_soni
                
                bot.reply_to(message, f"📊 Test: {kod_qismi}\n✅ To'g'ri: {togri_soni}\n❌ Xato: {xato_soni}")
            else:
                bot.reply_to(message, "❌ Kod topilmadi.")
        except:
            bot.reply_to(message, "⚠️ Format: 2*bacdbaaccb")
    else:
        bot.reply_to(message, "💡 Testni tekshirish uchun kodni kiriting (Masalan: 2*bacdbaaccb)")

bot.infinity_polling()
