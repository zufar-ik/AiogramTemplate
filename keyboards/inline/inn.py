from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from keyboards.default.model_redmi import sheets_1

donate_callback = CallbackData('donation', 'sum')

donate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поддержать наш проект!", callback_data='donate')]
    ]
)

donate_version = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="QIWI", url="https://qiwi.com/n/ZUFARIK")],
        [InlineKeyboardButton(text="Юmoney", url="https://yoomoney.ru/to/4100117381464409")],
    ]
)

modeluu = ["", ""]
# Корзинка товаров
cart = InlineKeyboardMarkup(row_width=1)
for i in range(1, 2):
    modelxia = sheets_1[i][48]
    modeluu.append(modelxia.value)
    cart.insert(InlineKeyboardButton(text='Добавить в корзину', callback_data=modelxia.value))
    cart.insert(InlineKeyboardButton(text="Отмена", callback_data="back"))
