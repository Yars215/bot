
import asyncio
import re
import os
import Levenshtein
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

API_TOKEN = os.getenv("BOT_TOKEN")  # Получаем токен из переменной окружения

def is_similar_to_aeronavtyka(word):
    return Levenshtein.distance(word.lower(), "аеронавтика") <= 2

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    text = message.text.lower()
    words = re.findall(r'\w+', text)

    if "когда" in words:
        for word in words:
            if is_similar_to_aeronavtyka(word):
                await message.answer("Завтра")
                break

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
