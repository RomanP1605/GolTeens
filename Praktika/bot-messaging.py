import telebot

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

@bot.message_handler(commands=['start'])
def messaging(message):
    bot.send_message(message.chat.id, "бота запущено")

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Зачем ти мене офнув(((')
    bot.stop_polling()
