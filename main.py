import telebot

# Tokeningizni shu yerga yozdim
TOKEN = "8296888507:AAGflQ3cNTsyq-8e6YDiCB3MqTMr-8COBTw"
bot = telebot.TeleBot(TOKEN)

# Test javoblari (Baza)
testlar = {
    "101": "1-A, 2-B, 3-C, 4-D, 5-A",
    "102": "1-C, 2-D, 3-A, 4-B, 5-C"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men test yechuvchi botman. Test raqamini yuboring (Masalan: 101)")

@bot.message_handler(func=lambda message: True)
def yechim(message):
    test_kodi = message.text.strip()
    if test_kodi in testlar:
        bot.reply_to(message, f"✅ {test_kodi}-test javoblari:\n{testlar[test_kodi]}")
    else:
        bot.reply_to(message, "❌ Bunday test kodi topilmadi.")

bot.infinity_polling()
