from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuAll = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Телефоны📱"), KeyboardButton(text="Ноутбуки💻 (beta)")],
        [KeyboardButton(text="Корзинка 🛒"),KeyboardButton(text="Связаться с администратором⁉️")]
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

