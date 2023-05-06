import telebot
import time

from telebot import types
bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')

CHANNEL_NAME = '@GoITeens_BotTest'
f = open('phrases.txt', 'r', encoding='UTF-8')
phrase_read = f.read().split('\n')
f.close()
for phrase in phrase_read:
    bot.send_message(message.chat.id, phrase)
    time.sleep(0)
bot.send_message(CHANNEL_NAME, "Фрази закінчились :-(")

