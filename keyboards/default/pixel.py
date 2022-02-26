import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

listAll = openpyxl.open("excel/google.xlsx", read_only=True)
sheets_2 = listAll.active
modelListPixel = ['space', 'space']
for i in range(3, sheets_2.max_row):
    model = sheets_2[i][0]
    modelListPixel.append(model.value)
pixel4 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(3, 6):
    name = sheets_2[i][0]
    pixel4.insert(KeyboardButton(text=name.value))
pixel4.insert(KeyboardButton(text="Назад🔙"))
pixel4.insert(KeyboardButton(text="Главное меню🏠"))
pixel5 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(6, 8):
    name = sheets_2[i][0]
    pixel5.insert(KeyboardButton(text=name.value))
pixel5.insert(KeyboardButton(text="Назад🔙"))
pixel5.insert(KeyboardButton(text="Главное меню🏠"))
pixel6 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(8, 10):
    name = sheets_2[i][0]
    pixel6.insert(KeyboardButton(text=name.value))
pixel6.insert(KeyboardButton(text="Назад🔙"))
pixel6.insert(KeyboardButton(text="Главное меню🏠"))

pixelmod = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Pixel")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

pixelModel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Google Pixel 4/XL/a"), KeyboardButton(text="Google Pixel 5/a")],
        [KeyboardButton(text="Google Pixel 6/Pro")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)
