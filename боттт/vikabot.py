import telebot
from telebot import types
import random
from configv import get_token
from vika import reqst
from decor import log_message


def main():
    bot = telebot.TeleBot(get_token())
    url = "https://www.funcookies.pl/en"
    reqst(url=url)

    @bot.message_handler(commands=['start'])
    def starting(message):
        markup = types.InlineKeyboardMarkup()
        button_chart = types.InlineKeyboardButton("my prediction", callback_data="send_text_predict")
        markup.add(button_chart)
        bot.send_message(message.chat.id, "Натисніть кнопку, щоб отримати передбачення",
                         reply_markup=markup)

    @log_message
    @bot.callback_query_handler(func=None)
    def callback(call):
        sent_predictions = set()
        file_path = "cookie"
        if call.data == "send_text_predict":
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = []
                    for line in file:
                        stripped_line = line.strip()
                        if stripped_line:
                            lines.append(stripped_line)
                    prediction = random.choice(lines)
                    sent_predictions.add(prediction)
                    bot.send_message(call.message.chat.id, prediction)
                starting(call.message)
    print("bot ready")
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()