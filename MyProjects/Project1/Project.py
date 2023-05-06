import telebot
from telebot import types
import requests
import datetime

bot = telebot.TeleBot("6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI")
open_weather_token = 'f4e0ae6da5566b0a269e6c7ced02188f'

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button1 = types.KeyboardButton('Ціна на продукти')
    button2 = types.KeyboardButton('Погода')
    button3 = types.KeyboardButton('Новини')
    keyboard.add(button1, button2, button3)

    bot.send_message(chat_id, "Привіт! Я бот. Що ви б хотіли дізнатися?", reply_markup=keyboard)

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
        eggs_price = 38
        bot.send_message(chat_id, f"Ціна на яйця: {eggs_price} грн")
    elif message.text.lower() == "шоколад":
        chocolate_price = 23
        bot.send_message(chat_id, f"Ціна на шоколад: {chocolate_price} грн")
    elif message.text.lower() == "сахар":
        sugar = 33
        bot.send_message(chat_id, f"Ціна на сахар: {sugar} грн")
    elif message.text.lower() == "кока-кола":
        coca_cola = 27
        bot.send_message(chat_id, f"Ціна на кока-кола: {coca_cola} грн")
    elif message.text.lower() == "молоко":
        milk = 56
        bot.send_message(chat_id, f"Ціна на молоко: {milk} грн")


    elif message.text.lower() == "погода":
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
    elif message.text.lower() == "новини":
        with open('news.txt', 'r') as n:
            news = n.read()
        bot.send_message(message.chat.id, news)
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

bot.polling()