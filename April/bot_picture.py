import telebot

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

@bot.message_handler(commands=['start', 'help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Привіт, напиши слово")

@bot.message_handler(content_types=['text'])
def echo(message):
    text=message.text
    user=message.chat.id
    bot.send_photo(user, "https://val.ua/uploads/news/full/5eb5b0975f211.jpeg")
    bot.send_message(user,text)
bot.polling(none_stop=True, interval=0)