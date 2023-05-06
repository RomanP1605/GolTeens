import telebot

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

images = {
    '0': 'zero_img.jpg',
    '1': 'one_img.jpg',
    '2': 'two_img.jpg',
    '3': 'three_img.jpg',
    '4': 'four_img.jpg',
    '5': 'five_img.jpg',
    '6': 'six_img.jpg',
    '7': 'seven_img.jpg',
    '8': 'eight_img.jpg',
    '9': 'nine_img.jpg'
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напишіть будь-яку цифру від 0 до 9, щоб отримати подарунок!")


@bot.message_handler(func=lambda message: True)
def send_image(message):
    text = message.text
    if text in images.keys():
        with open(images[text], 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    else:
        bot.reply_to(message, "Ви ввели неправильне число! Введіть будь-ласка цифру від 0 до 9.")


bot.polling(none_stop=True, interval=0)
