import telebot
from telebot import types
import random

bot = telebot.TeleBot("6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Фраза дня')
    itembtn2 = types.KeyboardButton('Гороскоп')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Виберіть опцію:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Фраза дня":
        with open('phrases.txt', 'r', encoding='UTF-8') as f:
            phrases = f.readlines()
            phrase = random.choice(phrases)
            bot.send_message(message.chat.id, phrase)
    elif message.text == "Гороскоп":
        with open('horoscopes.txt', 'r', encoding='UTF-8') as f:
            horoscopes = f.readlines()
            print(horoscopes)
            bot.send_message(message.chat.id, horoscopes)

bot.polling(none_stop=True, interval=0)
