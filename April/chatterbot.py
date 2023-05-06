import telebot
import os
from fuzzywuzzy import fuzz
from telebot import types

bot = telebot.TeleBot('6198567091:AAG07gB3O0IBKznT4MyEluKnbHIyuC1TSnI')



mas=[]
if os.path.exists('chatterbox.txt'):
    f=open('chatterbox.txt', 'r', encoding='UTF-8')
    for x in f:
        if (len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()
print(mas)

def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('chatterbox.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    aa=(fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn+1]
            return s
        else:
            return 'Помилка'
    except:
        return 'Помилка'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Я на зв'язку. Напиши привіт")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    f=open(str(message.chat.id) + 'log.txt', 'a', encoding='UTF-*=8')
    s=answer(message.text)
    f.write('u: ' + message.text + '\n' + s + '\n')
    f.close()
    bot.send_message(message.chat.id, s)
bot.polling(none_stop=True, interval=0)