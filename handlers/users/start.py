import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.buttons import tel, redminot9, xiaomi, Redmi, redminot10, redminot11, redminot12
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Добавляем пользователей в базу
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Добро пожаловать! {name}", reply_markup=tel)
        # Оповещаем админа
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу пользователей.\nВ базе есть {count} людей."
        await bot.send_message(chat_id=ADMINS[0], text=msg)


    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} в базе имелся раньше")
        await message.answer(f"Добро пожаловать! {name}, выберите марку смартфона", reply_markup=tel)


@dp.message_handler(text='Xiaomi')
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов", reply_markup=xiaomi)


@dp.message_handler(text='Redmi')
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона Redmi", reply_markup=Redmi)


@dp.message_handler(text='Redmi Note 9/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot9)


@dp.message_handler(text='Redmi Note 10/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot10)


@dp.message_handler(text="Назад")
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=Redmi)


@dp.message_handler(text='Главное меню')
async def mainmenu(message: types.Message):
    await message.answer("Вы нажали Главное меню", reply_markup=tel)


@dp.message_handler(text='Redmi Note 11/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot11)


@dp.message_handler(text='Redmi Note 12/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot12)
