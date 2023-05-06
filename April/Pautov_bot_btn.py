import telebot
from telebot import types
bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Фраза дня', url='https://www.google.com/')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton(text='Гороскоп', url='https://www.google.com/')
    markup.add(btn2)
    bot.send_message(message.from_user.id, "По кнопці можна перейти на сайт", reply_markup=markup)


bot.polling(none_stop=True, interval=0)