import random
import re

entertainments = ['піти в кіно', 'відвідати музей', 'пограти в ігри на вулиці', 'піти в театр', 'прогулятися в парку']

def get_recommendation(text):
    if re.search('розваги|розважальні заходи|що зробити', text):
        return f'Якщо ви хочете розважитися, можливо вам сподобається {random.choice(entertainments)}.'
    else:
        return 'Ви можете задавати мені запитання про розваги, та я дам вам рекомендації!'
def chat():
    print('Привіт! Я можу дати вам рекомендації про розважальні заходи!')
    while True:
        text = input('Введіть ваше запитання: ')
        if text == 'вийти':
            print('До побачення!')
            break
        response = get_recommendation(text)
        print(response)

chat()