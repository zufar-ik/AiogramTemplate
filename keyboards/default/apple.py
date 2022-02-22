import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

listAll = openpyxl.open("D:\\CODE\\AiogramTemplate\\excel\\iPhone.xlsx", read_only=True)
sheets_3 = listAll.active
modelList_apple = ['space', 'space']
for i in range(3, sheets_3.max_row):
    model = sheets_3[i][0]
    modelList_apple.append(model.value)

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
        [KeyboardButton(text="iPhone 13"),KeyboardButton(text="iPhone SE")],
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
for i in range(7,9):
    name = sheets_3[i][0]
    Apple_7.insert(KeyboardButton(text=name.value))
Apple_7.insert(KeyboardButton(text="Назад🔙"))
Apple_7.insert(KeyboardButton(text="Главное меню🏠"))
Apple_se = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(9,10):
    name = sheets_3[i][0]
    Apple_se.insert(KeyboardButton(text=name.value))
Apple_se.insert(KeyboardButton(text="Назад🔙"))
Apple_se.insert(KeyboardButton(text="Главное меню🏠"))
Apple_8 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(10,12):
    name = sheets_3[i][0]
    Apple_8.insert(KeyboardButton(text=name.value))
Apple_8.insert(KeyboardButton(text="Назад🔙"))
Apple_8.insert(KeyboardButton(text="Главное меню🏠"))
Apple_X = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(12,13):
    name = sheets_3[i][0]
    Apple_X.insert(KeyboardButton(text=name.value))
Apple_X.insert(KeyboardButton(text="Назад🔙"))
Apple_X.insert(KeyboardButton(text="Главное меню🏠"))
Apple_11 = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_12 = ReplyKeyboardMarkup(resize_keyboard=True)
Apple_13 = ReplyKeyboardMarkup(resize_keyboard=True)
