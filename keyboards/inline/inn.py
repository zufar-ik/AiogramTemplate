from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

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
