import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Apple"), KeyboardButton(text='Samsung')],
        [KeyboardButton(text="Xiaomi"), KeyboardButton(text='VIVO')]
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
        [KeyboardButton(text="Главное меню")]
    ],
    resize_keyboard=True,
)
listAll = openpyxl.open("D:\\CODE\\AiogramTemplate\\excel\\xiaomi_redmi.xlsx", read_only=True)
sheet = listAll.active
redminot9 = ReplyKeyboardMarkup(resize_keyboard=True)

for i in range(3, 6):
    name = sheet[i][1]
    redminot9.insert(KeyboardButton(text=(name.value)))
redminot9.insert(KeyboardButton(text="Назад"))
redminot9.insert(KeyboardButton(text="Главное меню"))

redminot10 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(6, 9):
    name = sheet[i][1]
    redminot10.insert(KeyboardButton(text=(name.value)))
redminot10.insert(KeyboardButton(text="Назад"))
redminot10.insert(KeyboardButton(text="Главное меню"))

redminot11 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(9, 12):
    name = sheet[i][1]
    redminot11.insert(KeyboardButton(text=(name.value)))
redminot11.insert(KeyboardButton(text="Назад"))
redminot11.insert(KeyboardButton(text="Главное меню"))

redminot12 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(12, 15):
    name = sheet[i][1]
    redminot12.insert(KeyboardButton(text=(name.value)))
redminot12.insert(KeyboardButton(text="Назад"))
redminot12.insert(KeyboardButton(text="Главное меню"))
