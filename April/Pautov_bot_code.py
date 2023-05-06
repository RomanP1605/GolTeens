import telebot

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привіт":
        bot.send_message(message.from_user.id, "Привіт")
    elif message.text == "Хто ти?":
        bot.send_message(message.from_user.id, "Я чат-бот")
    elif message.text == "Як тебе звати?":
        bot.send_message(message.from_user.id, "Мене звати Pautov_Bot")
    elif message.text == "Що ти вмієш?":
        bot.send_message(message.from_user.id, "Тільки вітатися")
    elif message.text == "Хто твій власник?":
        bot.send_message(message.from_user.id, "Мій власник Роман, ось його аккаунт якщо вам потрібно до нього звернутись: Roman068")
    elif message.text == "Який курс долара до гривні?":
        bot.send_message(message.from_user.id, "На даний момент курс 1 долару становить 36 гривень 96 копійок")
    elif message.text == "Порекомендуй місця для туристів неподалік від Києва":
        bot.send_message(message.from_user.id, "1. Софіївський парк - парк культури і відпочинку, який розташований у селі Умань Черкаської області. 2.Печерські лаври - історичний комплекс монастирів, що складається з Києво-Печерської лаври та Миколаївської церкви, які знаходяться у Києві. 3.Тростянець - містечко на Чернігівщині зі старовинним замком та музеєм млинів. 4.Яготинський парк ''Дубовий гай'' - парк зі старими дубами та іншими рідкісними деревами, що розташований неподалік")
    elif message.text == "Яка погода буде в Києві ближчих 10 днів?":
        bot.send_message(message.from_user.id, "Температура буде від 5°С до 17°С, вірогідність опадів 69%, вітер досягатиме 3.7 м/с.")
    elif message.text == "Які найпопулярніші доставки їжі зараз працюють?":
        bot.send_message(message.from_user.id, "Зараз у Києві є багато популярних сервісів доставки їжі, таких як Glovo, Uber Eats, Menu.ua, Raketa та інші.")
    else:
        bot.send_message(message.from_user.id, "Вибач, але цієї команди не існує! Якщо є ідеї для команд напиши моєму власнику: @Roman_068")


bot.polling(none_stop=True, interval=0)
