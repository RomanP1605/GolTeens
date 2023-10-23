import telebot

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

@bot.message_handler(commands=['start', 'help'])
def help(message):
    user=message.chat.id
    bot.send_message(user, "1")

@bot.message_handler(content_types=['text'])
def echo(message):
    user=message.chat.id
    text = message.text
    f = open("C:\Users\Roman\OneDrive\Рабочий стол\GolTeens\April\phrases.txt", "rb")
    bot.send_document(message.id, f)