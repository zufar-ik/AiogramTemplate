import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# listAll = openpyxl.open("excel\\samsung.xlsx", read_only=True)
# sheetG = listAll.active
# sheets_4 = listAll.worksheets[3]
# modelListGalaxy = ['space', 'space']
# for i in range(3, sheets_4.max_row):
#     model = sheets_4[i][0]
#     modelListGalaxy.append(model.value)
# GalaxyS = ReplyKeyboardMarkup(resize_keyboard=True)
# for i in range(3, 6):
#     name = sheets_4[i][0]
#     GalaxyS.insert(KeyboardButton(text=name.value))
# GalaxyS.insert(KeyboardButton(text="Назад🔙"))
# GalaxyS.insert(KeyboardButton(text="Главное меню🏠"))
#
# GalaxyN = ReplyKeyboardMarkup(resize_keyboard=True)
# for i in range(3, 6):
#     name = sheets_4[i][0]
#     GalaxyN.insert(KeyboardButton(text=name.value))
# GalaxyN.insert(KeyboardButton(text="Назад🔙"))
# GalaxyN.insert(KeyboardButton(text="Главное меню🏠"))
#
#
# GalaxyA = ReplyKeyboardMarkup(resize_keyboard=True)
# for i in range(3, 6):
#     name = sheets_4[i][0]
#     GalaxyA.insert(KeyboardButton(text=name.value))
# GalaxyA.insert(KeyboardButton(text="Назад🔙"))
# GalaxyA.insert(KeyboardButton(text="Главное меню🏠"))
#
#
# GalaxyZ = ReplyKeyboardMarkup(resize_keyboard=True)
# for i in range(3, 6):
#     name = sheets_4[i][0]
#     GalaxyZ.insert(KeyboardButton(text=name.value))
# GalaxyZ.insert(KeyboardButton(text="Назад🔙"))
# GalaxyZ.insert(KeyboardButton(text="Главное меню🏠"))

galaxymod = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy S"), KeyboardButton(text="Galaxy Note")],
        [KeyboardButton(text="Galaxy Z"), KeyboardButton(text="Galaxy A")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

galaxyModelS = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy S10/Lite/e/+"), KeyboardButton(text="Galaxy S20/+/Ultra/FE")],
        [KeyboardButton(text="Galaxy S21/+/Ultra/FE"), KeyboardButton(text="Galaxy S22/+/Ultra")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

galaxyModelN = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy Note 10/Lite/+"), KeyboardButton(text="Galaxy Note 20/Ultra")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

galaxyModelZ = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy Z Fold"), KeyboardButton(text="Galaxy Z Flip")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

galaxyModelA = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy A01-A09"), KeyboardButton(text="Galaxy A10-A19"),
         KeyboardButton(text="Galaxy A20-A29")],
        [KeyboardButton(text="Galaxy A30-A39"), KeyboardButton(text="Galaxy A40-A49"),
         KeyboardButton(text="Galaxy A50-A59")],
        [KeyboardButton(text="Galaxy A70-A79"), KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)
