import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
listAll = openpyxl.open("D:\\CODE\\AiogramTemplate\\excel\\xiaomi_redmi.xlsx", read_only=True)
sheet = listAll.active
#В dict записывется названия моделей из БД
modelList = ['space','space']
for i in range(3,sheet.max_row):
    model = sheet[i][1]
    modelList.append(model.value)
#Для кнопок в боте с названиеями моделей
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
