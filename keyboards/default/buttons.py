from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuAll = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Телефоны"),KeyboardButton(text="Ноутбуки")]
    ],
    resize_keyboard=True
)

tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Apple"), KeyboardButton(text='Samsung')],
        [KeyboardButton(text="Xiaomi"), KeyboardButton(text='VIVO')],
        [KeyboardButton(text="Главное меню")]
    ],
    resize_keyboard=True
)

xiaomi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Redmi"), KeyboardButton(text='POCO')],
        [KeyboardButton(text="MI"), KeyboardButton(text="MI MIX")],
        [KeyboardButton(text="Главное меню")]
    ],
    resize_keyboard=True
)

Redmi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Redmi Note 9/S/Pro"), KeyboardButton(text="Redmi Note 10/S/Pro")],
        [KeyboardButton(text="Redmi Note 11/S/Pro"), KeyboardButton(text="Redmi Note 12/S/Pro")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ],
    resize_keyboard=True,
)


# category -> subcategory -> product -> subproduct