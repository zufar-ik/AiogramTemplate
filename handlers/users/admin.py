import asyncio

import pandas as pd
from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


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
async def send_ad_to_all():
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@BekoDev подписываемся")
        await asyncio.sleep(0.05)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("База очищена!")
