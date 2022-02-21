import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

listAll = openpyxl.open("excel\\DATABASE.xlsx", read_only=True)
sheetA = listAll.active
sheets_3 = listAll.worksheets[2]
modelListGalaxy = ['space', 'space']
for i in range(3, sheets_3.max_row):
    model = sheets_3[i][0]
    modelListGalaxy.append(model.value)

iphone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="iPhone")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

Apple_model = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="iPhone 6"), KeyboardButton(text="iPhone 7"), KeyboardButton(text="iPhone 8")],
        [KeyboardButton(text="iPhone X"), KeyboardButton(text="iPhone 11"), KeyboardButton(text="iPhone 12")],
        [KeyboardButton(text="iPhone 13")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

Apple_6 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(3, 7):
    name = sheets_3[i][0]
    Apple_6.insert(KeyboardButton(text=name.value))
Apple_6.insert(KeyboardButton(text="Назад🔙"))
Apple_6.insert(KeyboardButton(text="Главное меню🏠"))
Apple_7 = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_8 = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_X = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_11 = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_12 = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_13 = ReplyKeyboardMarkup(resize_keyboard=True)
