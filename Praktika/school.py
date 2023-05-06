import telebot
import time

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

users = []
@bot.message_handler(commands=['start'])
def say_hello(message):
    username = message.from_user.first_name
    users.append(username)
    print('Users who said hello:', users)
    users.remove(username)
    bot.send_message(message.chat.id, "Зачекай поки Роман налаштує бота, може зайняти ~30 секунд")
    abc=input("Введи слово для атаки")
    bbc=int(input("Введи кількість разів"))
    cbc=int(input("Введи затримку"))
    for i in range(bbc):
        time.sleep(cbc)
        bot.send_message(message.chat.id, abc)
    print("Все")

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Зачем ти мене офнув(((')
    bot.stop_polling()

bot.polling(none_stop=True, interval=0)

