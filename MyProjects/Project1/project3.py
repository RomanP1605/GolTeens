import telebot
import requests
import datetime
from telebot import types

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

open_weather_token = 'f4e0ae6da5566b0a269e6c7ced02188f'

prices = {
    'Яйця': 'zero_img.jpg',
    'Хліб український': 'one_img.jpg',
    'Хліб бородинський': 'two_img.jpg',
    'Хліб фінський': 'three_img.jpg',
    'Міні-круасани': 'four_img.jpg',
    'Кока-кола': 'five_img.jpg',
    'Цукор': 'six_img.jpg',
    'Сіль': 'seven_img.jpg',
    'Шоколад': 'eight_img.jpg',
    'Молоко': 'nine_img.jpg'
}
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Погода')
    itembtn2 = types.KeyboardButton('Ціна на продукти')
    itembtn3 = types.KeyboardButton('Новини')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Привіт! я чат бот! Натисни кнопку яка тобі необхідна")


def price(message):
    text = message.text
    if text == 'Яйця':
        bot.send_message(message.chat.id, "ціна за 10 штук: 29 гривень 90 копійок")
    elif text == 'Хліб український':
        bot.send_message(message.chat.id, "37 гривень 90 копійок")
    elif text == 'Хліб бородинський':
        bot.reply_to(message, "20 гривень 99 копійок")
    elif text == 'Міні-круасани':
        bot.reply_to(message, "69 гривень 90 копійок")
    elif text == 'Кока-кола':
        bot.reply_to(message, "26 гривень 90 копійок за літр")
    elif text == 'Цукор':
        bot.reply_to(message, "33 гривні 00 копійок за кілограм")
    elif text == 'Сіль':
        bot.reply_to(message, "30 гривень 00 копійок за кілограм")
    elif text == 'Шоколад':
        bot.reply_to(message, "34 гривень 90 копійок")
    elif text == 'Молоко':
        bot.reply_to(message, "56 гривень 70 копійок за літр")

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Погода':
        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Хмарно \U00002601',
            'Drizzle': 'Дощ \U00002602'
        }
        data = get_weather('Dudarkiv')
        city = data['name']
        current_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Подивися у вікно \U00001F604'
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp((data['sys']['sunrise']))
        sunset = datetime.datetime.fromtimestamp((data['sys']['sunset']))
        bot.send_message(
            message.chat.id,
            f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f" Погода в місті: {city}\n Температура: {current_weather}C {wd}\n"
            f" Вологість: {humidity}%\n Атмосферний тиск: {pressure}мм.рт.ст. Вітер:{wind}\n"
            f" Схід сонця: {sunrise}\n Захід: {sunset}\n"
            f" Гарного дня!"
        )

#    elif message.text == 'Ціна на продукти':
#        bot.send_message(message.chat.id, "Введіть продукт (Обово'язково з великої букви!)")
#        price(message)
#        @bot.message_handler(content_types=['text'])
#        def price(message):
#            text = message.text
#            if text == 'Яйця':
#               bot.send_message(message.chat.id, "ціна за 10 штук: 29 гривень 90 копійок")
#            elif text == 'Хліб український':
#                bot.send_message(message.chat.id, "37 гривень 90 копійок")
#            elif text == 'Хліб бородинський':
#                bot.reply_to(message, "20 гривень 99 копійок")
#            elif text == 'Міні-круасани':
#                bot.reply_to(message, "69 гривень 90 копійок")
#            elif text == 'Кока-кола':
#                bot.reply_to(message, "26 гривень 90 копійок за літр")
#            elif text == 'Цукор':
#                bot.reply_to(message, "33 гривні 00 копійок за кілограм")
#            elif text == 'Сіль':
#                bot.reply_to(message, "30 гривень 00 копійок за кілограм")
#            elif text == 'Шоколад':
#                bot.reply_to(message, "34 гривень 90 копійок")
#            elif text == 'Молоко':
#                bot.reply_to(message, "56 гривень 70 копійок за літр")


    elif message.text == 'Новини':
        with open('news.txt', 'r') as n:
            news = n.read()
        bot.send_message(message.chat.id, news)

@bot.message_handler(func=lambda message: message.text == "Ціна на продукти")
def send_products_price(message):
    chat_id = message.chat.id

    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button = types.KeyboardButton('Відмінити')
    keyboard.add(button)

    bot.send_message(chat_id, "Напишіть назву продукту", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.chat.id

    if message.text.lower() == "яйця":
        eggs_price = 10
        bot.send_message(chat_id, f"Ціна на яйця: {eggs_price} грн")
    elif message.text.lower() == "шоколад":
        chocolate_price = 20
        bot.send_message(chat_id, f"Ціна на шоколад: {chocolate_price} грн")
    else:
        bot.send_message(chat_id, "Я не розумію, про що ви говорите")

@bot.message_handler(func=lambda message: message.text == "Відмінити")
def cancel_message(message):
    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button1 = types.KeyboardButton('Ціна на продукти')
    button2 = types.KeyboardButton('Погода')
    button3 = types.KeyboardButton('Новини')
    keyboard.add(button1, button2, button3)

    bot.send_message(chat_id, "Що ви б хотіли дізнатися?", reply_markup=keyboard)

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     itembtn1 = types.KeyboardButton('')
#     itembtn2 = types.KeyboardButton('Ціна на продукти')
#     itembtn3 = types.KeyboardButton('Новини')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(message.chat.id, "Привіт! я чат бот! Натисни кнопку яка тобі необхідна")
bot.polling(none_stop=True)
