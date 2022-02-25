from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuAll = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Телефоны📱"), KeyboardButton(text="Ноутбуки💻 (beta)")]
    ],
    resize_keyboard=True
)


tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Apple"), KeyboardButton(text='Samsung')],
        [KeyboardButton(text="Xiaomi"), KeyboardButton(text='Google')],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

xiaomi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Redmi"), KeyboardButton(text='POCO')],
        [KeyboardButton(text="MI"), KeyboardButton(text="MI MIX")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True
)

Redmi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Redmi Note")],
        [KeyboardButton(text="Redmi/Redmi A"), KeyboardButton(text="Redmi K")],
        [KeyboardButton(text="Назад🔙"), KeyboardButton(text="Главное меню🏠")]
    ],
    resize_keyboard=True,
)

# category -> subcategory -> product -> subproduct

count = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"),
         KeyboardButton(text="3")],
        [KeyboardButton(text="4"), KeyboardButton(text="5"),
         KeyboardButton(text="6")],
        [KeyboardButton(text="7"), KeyboardButton(text="8"),
         KeyboardButton(text="9")],
        [KeyboardButton(text="Отмена")]
    ],
    resize_keyboard=True
)
