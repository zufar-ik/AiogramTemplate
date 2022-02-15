from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заполнить анкету")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

anketa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Найти работу"),KeyboardButton(text="Найти помощника")],
        [KeyboardButton(text="Нужен сотрудник")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
contactnum = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поделиться номером", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)