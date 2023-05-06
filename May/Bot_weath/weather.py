from config import open_weather_token
import requests
from pprint import pprint
import datetime

def get_weather(city,open_weather_token):
    code_to_smile={
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Хмарно \U00002601',
        'Drizzle': 'Дощ \U00002602'
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city=data['name']
        current_weather=data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd=code_to_smile[weather_description]
        else:
            wd='Подивися у вікно \U00001F604'
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        wind=data['wind']['speed']
        sunrise=datetime.datetime.fromtimestamp((data['sys']['sunrise']))
        sunset = datetime.datetime.fromtimestamp((data['sys']['sunset']))
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f" Погода в місті: {city}\n Температура: {current_weather}C {wd}\n"
              f" Вологість: {humidity}%\n Атмосферний тиск: {pressure}мм.рт.ст. Вітер:{wind}\n"
              f" Схід сонця: {sunrise}\n Захід: {sunset}\n"
              f" Гарного дня!"
              )
    except Exception as ex:
        print(ex)
        print('error')
    pass

def main():
    city = input('enter city')
    get_weather(city,open_weather_token)

if __name__=='__main__':
    main()
