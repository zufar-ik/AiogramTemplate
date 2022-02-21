import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

listAll = openpyxl.open("excel\\DATABASE.xlsx", read_only=True)
sheetX = listAll.active
sheets_1 = listAll.worksheets[0]
# В dict приходят названия моделей из БД
modelListX = ['space', 'space']
for i in range(3, sheets_1.max_row):
    modelxia = sheets_1[i][0]
    modelListX.append(modelxia.value)
# Для кнопок в боте с названиями моделей
redminot = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(3, 12):
    name = sheets_1[i][0]
    redminot.insert(KeyboardButton(text=name.value))
redminot.insert(KeyboardButton(text="Назад🔙"))
redminot.insert(KeyboardButton(text="Главное меню🏠"))

redmi_a = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(12, 15):
    name = sheets_1[i][0]
    redmi_a.insert(KeyboardButton(text=name.value))
redmi_a.insert(KeyboardButton(text="Назад🔙"))
redmi_a.insert(KeyboardButton(text="Главное меню🏠"))

redmi_k = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(15, 22):
    name = sheets_1[i][0]
    redmi_k.insert(KeyboardButton(text=name.value))
redmi_k.insert(KeyboardButton(text="Назад🔙"))
redmi_k.insert(KeyboardButton(text="Главное меню🏠"))

MI = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="MI 10/T"), KeyboardButton(text="MI 11/T")],
        [KeyboardButton(text="MI 12/T"), KeyboardButton(text="Black Shark")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

POCO = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="POCO X"), KeyboardButton(text="POCO M")],
        [KeyboardButton(text="POCO F"), KeyboardButton(text="POCO C")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

black_shark = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(22, 28):
    name = sheets_1[i][0]
    black_shark.insert(KeyboardButton(text=name.value))
black_shark.insert(KeyboardButton(text="Назад🔙"))
black_shark.insert(KeyboardButton(text="Главное меню🏠"))

mi_mi10 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(28, 37):
    name = sheets_1[i][0]
    mi_mi10.insert(KeyboardButton(text=name.value))
mi_mi10.insert(KeyboardButton(text="Назад🔙"))
mi_mi10.insert(KeyboardButton(text="Главное меню🏠"))

mi_mi11 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(37, 43):
    name = sheets_1[i][0]
    mi_mi11.insert(KeyboardButton(text=name.value))
mi_mi11.insert(KeyboardButton(text="Назад🔙"))
mi_mi11.insert(KeyboardButton(text="Главное меню🏠"))

poco_c = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(43, 44):
    name = sheets_1[i][0]
    poco_c.insert(KeyboardButton(text=name.value))
poco_c.insert(KeyboardButton(text="Назад🔙"))
poco_c.insert(KeyboardButton(text="Главное меню🏠"))

poco_f = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(44, 47):
    name = sheets_1[i][0]
    poco_f.insert(KeyboardButton(text=name.value))
poco_f.insert(KeyboardButton(text="Назад🔙"))
poco_f.insert(KeyboardButton(text="Главное меню🏠"))

poco_m = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(47, 51):
    name = sheets_1[i][0]
    poco_m.insert(KeyboardButton(text=name.value))
poco_m.insert(KeyboardButton(text="Назад🔙"))
poco_m.insert(KeyboardButton(text="Главное меню🏠"))

poco_x = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(51, 56):
    name = sheets_1[i][0]
    poco_x.insert(KeyboardButton(text=name.value))
poco_x.insert(KeyboardButton(text="Назад🔙"))
poco_x.insert(KeyboardButton(text="Главное меню🏠"))

mi_mi12 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(56, 59):
    name = sheets_1[i][0]
    mi_mi12.insert(KeyboardButton(text=name.value))
mi_mi12.insert(KeyboardButton(text="Назад🔙"))
mi_mi12.insert(KeyboardButton(text="Главное меню🏠"))

MI_MIX = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="MIX")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)


mi_mix = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(59, 62):
    name = sheets_1[i][0]
    mi_mix.insert(KeyboardButton(text=name.value))
mi_mix.insert(KeyboardButton(text="Назад🔙"))
mi_mix.insert(KeyboardButton(text="Главное меню🏠"))
