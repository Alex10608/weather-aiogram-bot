import httpx
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon import LEXICON
from utils import custom_weather_data

router = Router()


@router.message(CommandStart())
async def process_cmd_start(message: Message):
    await message.answer(text=LEXICON['start'])


@router.message(F.text)
async def find_city(message: Message):
    url = "http://127.0.0.1:8000/weather/" + message.text
    async with httpx.AsyncClient() as client:
        r = await client.get(url=url)
    await message.answer(text=custom_weather_data(r.json(), message.text))


