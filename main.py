import telebot
from setting import *
from texts import *
bot = telebot.TeleBot(token)

if __name__ == "__main__":
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Старый Бог 💪 ")


    @bot.message_handler(commands=['message'])
    def info(message):
        bot.send_message(message.chat.id, f"{message}")


    @bot.message_handler(commands=['calculate'])
    def calculate(message):
        text = message.text[10:]
        text = text.strip()
        if '+' in text:
            text = text.split("+")
            bot.send_message(message.chat.id, f"{int(text[0]) + int(text[1])}")
        if '-' in text:
            text = text.split("-")
            bot.send_message(message.chat.id, f"{int(text[0]) - int(text[1])}")
        if '*' in text:
            text = text.split("*")
            bot.send_message(message.chat.id, f"{int(text[0]) * int(text[1])}")
        if '/' in text:
            text = text.split("/")
            bot.send_message(message.chat.id, f"{int(text[0]) / int(text[1])}")

    @bot.message_handler(commands=['help'])
    def calculate(message):
        bot.send_message(message.chat.id, f'{commands}')

    bot.polling(none_stop=True)
