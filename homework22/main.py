import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from os import getenv

botkey = getenv('BOT_TOKEN')
bot = Bot(token=botkey)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text='Информация', url='https://ru.wikipedia.org/wiki/Python'),
        types.InlineKeyboardButton(text='Литература', url='https://habr.com/ru/company/sberbank/blog/679852/')
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer('2 inline-кнопки', reply_markup=keyboard)


if __name__ == '__main__':
    print('Bot is starting')
    executor.start_polling(dp)
