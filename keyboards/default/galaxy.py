import openpyxl
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

listAll = openpyxl.open("excel/samsung.xlsx", read_only=True)
sheets_4 = listAll.active
modelListGalaxy = ['space', 'space']
for i in range(3, sheets_4.max_row):
    model = sheets_4[i][0]
    modelListGalaxy.append(model.value)
GalaxyA01 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(3, 6):
    name = sheets_4[i][0]
    GalaxyA01.insert(KeyboardButton(text=name.value))
GalaxyA01.insert(KeyboardButton(text="Назад🔙"))
GalaxyA01.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyA10 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(6,10):
    name = sheets_4[i][0]
    GalaxyA10.insert(KeyboardButton(text=name.value))
GalaxyA10.insert(KeyboardButton(text="Назад🔙"))
GalaxyA10.insert(KeyboardButton(text="Главное меню🏠"))


GalaxyA20 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(10,15):
    name = sheets_4[i][0]
    GalaxyA20.insert(KeyboardButton(text=name.value))
GalaxyA20.insert(KeyboardButton(text="Назад🔙"))
GalaxyA20.insert(KeyboardButton(text="Главное меню🏠"))


GalaxyA30 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(15,18):
    name = sheets_4[i][0]
    GalaxyA30.insert(KeyboardButton(text=name.value))
GalaxyA30.insert(KeyboardButton(text="Назад🔙"))
GalaxyA30.insert(KeyboardButton(text="Главное меню🏠"))

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

GalaxyA40 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(18,21):
    name = sheets_4[i][0]
    GalaxyA40.insert(KeyboardButton(text=name.value))
GalaxyA40.insert(KeyboardButton(text="Назад🔙"))
GalaxyA40.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyA50 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(21,26):
    name = sheets_4[i][0]
    GalaxyA50.insert(KeyboardButton(text=name.value))
GalaxyA50.insert(KeyboardButton(text="Назад🔙"))
GalaxyA50.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyA70 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(26,32):
    name = sheets_4[i][0]
    GalaxyA70.insert(KeyboardButton(text=name.value))
GalaxyA70.insert(KeyboardButton(text="Назад🔙"))
GalaxyA70.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyFold = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(32,35):
    name = sheets_4[i][0]
    GalaxyFold.insert(KeyboardButton(text=name.value))
GalaxyFold.insert(KeyboardButton(text="Назад🔙"))
GalaxyFold.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyNote10 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(35,38):
    name = sheets_4[i][0]
    GalaxyNote10.insert(KeyboardButton(text=name.value))
GalaxyNote10.insert(KeyboardButton(text="Назад🔙"))
GalaxyNote10.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyNote20 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(38,40):
    name = sheets_4[i][0]
    GalaxyNote20.insert(KeyboardButton(text=name.value))
GalaxyNote20.insert(KeyboardButton(text="Назад🔙"))
GalaxyNote20.insert(KeyboardButton(text="Главное меню🏠"))


GalaxyS10 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(40,44):
    name = sheets_4[i][0]
    GalaxyS10.insert(KeyboardButton(text=name.value))
GalaxyS10.insert(KeyboardButton(text="Назад🔙"))
GalaxyS10.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyS20 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(44,48):
    name = sheets_4[i][0]
    GalaxyS20.insert(KeyboardButton(text=name.value))
GalaxyS20.insert(KeyboardButton(text="Назад🔙"))
GalaxyS20.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyS21 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(48,52):
    name = sheets_4[i][0]
    GalaxyS21.insert(KeyboardButton(text=name.value))
GalaxyS21.insert(KeyboardButton(text="Назад🔙"))
GalaxyS21.insert(KeyboardButton(text="Главное меню🏠"))

GalaxyS22 = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(52,55):
    name = sheets_4[i][0]
    GalaxyS22.insert(KeyboardButton(text=name.value))
GalaxyS22.insert(KeyboardButton(text="Назад🔙"))
GalaxyS22.insert(KeyboardButton(text="Главное меню🏠"))


GalaxyFlip = ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(55,57):
    name = sheets_4[i][0]
    GalaxyFlip.insert(KeyboardButton(text=name.value))
GalaxyFlip.insert(KeyboardButton(text="Назад🔙"))
GalaxyFlip.insert(KeyboardButton(text="Главное меню🏠"))
