import telebot

# Botingiz tokini
TOKEN = "8296888507:AAGflQ3cNTsyq-8e6YDiCB3MqTMr-8COBTw"
# Sizning ID raqamingiz
ADMIN_ID = 8137610119 

bot = telebot.TeleBot(TOKEN)

# TESTLAR BAZASI
testlar = {
    "101": "abcda",
    "102": "cdabc",
    "2*": "bacdbaaccb"
}

@bot.message_handler(commands=['start'])
def start(message):
    matn = ("Salom! Testni tekshirish uchun kod va javoblarni yuboring.\n\n"
            "Format: KOD*JAVOBLAR\n"
            "Namuna: 2*abcd...")
    bot.send_message(message.chat.id, matn)

@bot.message_handler(func=lambda message: True)
def tekshirish(message):
    tekst = message.text.strip().lower()
    if "*" in tekst:
        try:
            qismlar = tekst.split("*")
            kod_qismi = qismlar[0] + "*"
            foydalanuvchi_javobi = qismlar[1]
            
            if kod_qismi in testlar:
                asl_javoblar = testlar[kod_qismi]
                togri_soni = sum(1 for i, j in zip(asl_javoblar, foydalanuvchi_javobi) if i == j)
                xato_soni = len(asl_javoblar) - togri_soni
                
                # O'quvchiga natija yuborish
                bot.reply_to(message, f"📊 Test: {kod_qismi}\n✅ To'g'ri: {togri_soni}\n❌ Xato: {xato_soni}")
                
                # ADMINGA (SIZGA) HISOBOT YUBORISH
                user = message.from_user
                ism = user.first_name if user.first_name else "Noma'lum"
                familiya = user.last_name if user.last_name else ""
                username = f"@{user.username}" if user.username else "Mavjud emas"
                
                hisobot = (f"🔔 YANGI NATIJA!\n\n"
                          f"👤 O'quvchi: {ism} {familiya}\n"
                          f"🆔 Username: {username}\n"
                          f"📝 Test kodi: {kod_qismi}\n"
                          f"📥 Javobi: {foydalanuvchi_javobi}\n"
                          f"✅ Natija: {togri_soni} ta to'g'ri")
                
                bot.send_message(ADMIN_ID, hisobot)
            else:
                bot.reply_to(message, "❌ Bunday kodli test topilmadi.")
        except Exception as e:
            bot.reply_to(message, "⚠️ Format xato! Namuna: 2*abcd...")
    else:
        bot.reply_to(message, "💡 Testni tekshirish uchun kodni kiriting (Masalan: 2*abcd...)")

bot.infinity_polling()
              
