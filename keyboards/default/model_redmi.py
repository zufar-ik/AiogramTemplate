import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
listAll = openpyxl.open("D:\\CODE\\AiogramTemplate\\excel\\xiaomi_redmi.xlsx", read_only=True)
sheetX = listAll.active
sheets_1 = listAll.worksheets[0]
for i in range(3,sheets_1.max_row):
    model = sheets_1[i][0]
    print(model.value)
# В dict записывется названия моделей из БД
modelListX = ['space','space']
for i in range(3,sheets_1.max_row):
    modelxia = sheets_1[i][0]
    modelListX.append(modelxia.value)
#Для кнопок в боте с названиеями моделей
redminot9 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(3, 6):
    name = sheets_1[i][0]
    redminot9.insert(KeyboardButton(text=(name.value)))
redminot9.insert(KeyboardButton(text="Назад"))
redminot9.insert(KeyboardButton(text="Главное меню"))

redmi_a = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(6,8):
    name = sheets_1[i][0]
    redmi_a.insert(KeyboardButton(text=(name.value)))
redmi_a.insert(KeyboardButton(text="Назад"))
redmi_a.insert(KeyboardButton(text="Главное меню"))

redmi_k = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(8,11):
    name = sheets_1[i][0]
    redmi_k.insert(KeyboardButton(text=(name.value)))
redmi_k.insert(KeyboardButton(text="Назад"))
redmi_k.insert(KeyboardButton(text="Главное меню"))