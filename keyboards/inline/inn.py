from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

donate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поддержать наш проект!", callback_data="get_donate")]
    ]
)

donate_version = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="QIWI", url="qiwi.com/n/ZUFARIK")],
        [InlineKeyboardButton(text="Юmoney", url="https://yoomoney.ru/to/4100117381464409/0")]
    ]
)
