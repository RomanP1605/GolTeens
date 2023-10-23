import telebot

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! я бот який може анонімно відправити любе повідомлення людині яку ти вкажеш ;)")

@bot.message_handler(content_types=['text'])
def echo(message):
    username = 