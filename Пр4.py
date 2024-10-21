import telebot

TOKEN = '7630296862:AAHD4-8PNijEOr9TmMens0k5f6rcuFVKyNs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    print("Echo bot is running...")
    bot.polling()
