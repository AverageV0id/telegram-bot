import telebot
from math import *
from matplotlib import pyplot as plt
from diagrams import *
from setting import *
from texts import *

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Старый Бог 💪\n {commands}")


@bot.message_handler(commands=['get_message'])
def get_message(message):
    bot.send_message(message.chat.id, f"{message}")


@bot.message_handler(commands=['calculate'])
def calculate(message):
    try:
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
    except ZeroDivisionError:
        bot.send_message(message.chat.id, f'Ошибка: Нельзя делить на ноль!')
    except ValueError:
        bot.send_message(message.chat.id, f'Ошибка: Можно вводить только числа!')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')


@bot.message_handler(commands=['echo'])
def echo(message):
    text = message.text[5:]
    try:
        bot.send_message(message.chat.id, f'{text}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')


@bot.message_handler(commands=['help', 'info', 'commands'])
def help(message):
    bot.send_message(message.chat.id, f'{commands}')


@bot.message_handler(commands=['evaluate'])
def evaluate(message):
    try:
        text = message.text[9:]
        bot.send_message(message.chat.id, f'{eval(text)}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')


@bot.message_handler(commands=['bar'])
def bar(message):
    text = message.text[4:]
    text = text.split()
    categories = []
    text = list(map(int, text))
    for i in range(len(text)):
        categories.append(str(i+1))
    plt.figure(figsize=(10, 5))
    plt.bar(categories, text)
    plt.show()


@bot.message_handler(commands=['graph'])
def create_graph(message):
    try:
        text = message.text[6:]
        text = text.split(',')

        val = text[0].strip()
        nam = text[1].strip()

        val = val.split(" ")
        nam = nam.split(" ")

        val = list(map(int, val))

        save_bar(nam, val, 'bar.png')

        with open('bar.png', "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')


@bot.message_handler(content_types=['text'])
def another_message(message):
    if 'эхо' in message.text:
        try:
            text = message.text
            text = text.replace('эхо', '')
            bot.send_message(message.chat.id, f'{text}')
        except telebot.apihelper.ApiTelegramException:
            bot.send_message(message.chat.id, f'Ошибка: Сообщение пусто')
        except Exception as e:
            bot.send_message(message.chat.id, f'Ошибка: {e}')
    else:
        bot.send_message(message.chat.id, f'{invalid_message}')
