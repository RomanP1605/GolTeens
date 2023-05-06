import telebot
from telebot import types

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

notes = {}

@bot.message_handler(commands=['remind'])
def remind(message):
    user_id = message.chat.id
    if user_id not in notes:
        bot.send_message(user_id, "Напиши слово")
    else:
        bot.send_message(user_id, notes[user_id])

@bot.message_handler(content_types=['text'])
def remember(message):
    user_id = message.chat.id
    notes[user_id] = message.text
    bot.send_message(user_id, "Я записав твоє повідомлення")
    print(notes)

bot.polling(none_stop=True, interval=0)