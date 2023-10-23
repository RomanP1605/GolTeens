from aiogram import Bot, types
from data_auth1 import token_bot
from config1 import open_weather_token
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot=Bot(token = token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Enter city')

if __name__ == '__main__':
    executor.start_polling(dp)