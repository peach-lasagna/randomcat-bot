import logging
import httpx
from aiogram.types import InputFile
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from urllib.parse import urlparse



bot = Bot(token=getenv('TOKEN'))

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello! This bot can send u photos of random cats. List of commands:\n/meow")

@dp.message_handler(commands="meow")
async def meow(message: types.Message):
    url = "https://aws.random.cat/meow"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    url_meow = res.json()['file']
    file = InputFile.from_url(url_meow, filename=url_meow[url_meow.index('/i/')+3:])
    await message.answer_photo(file)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
