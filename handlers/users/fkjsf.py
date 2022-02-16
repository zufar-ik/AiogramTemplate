import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import tel,xiaomi,Redmi
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="RedmiNOTE9S")
async def getred(message:types.Message):
    calls = sheet['A3':'AU3']
    