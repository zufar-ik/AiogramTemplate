import asyncio

import pandas as pd
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from states.state import Reklama


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[0])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    df = pd.DataFrame(data)
    # print(df)
    await message.answer(df)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await message.answer("Введите текст рекламы")
    await Reklama.reklama.set()


@dp.message_handler(state=Reklama.reklama)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    reklama_text = message.text
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=reklama_text)
        await asyncio.sleep(0.05)
        await state.finish()


@dp.message_handler(text="/cleandb", user_id=[1297546327])
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("База данных очищена!")


@dp.message_handler(text="/cleanct", user_id=[1297546327])
async def get_all_cart(message: types.Message):
    db.delete_cart()
    await message.answer("База данных корзины очищена!")
