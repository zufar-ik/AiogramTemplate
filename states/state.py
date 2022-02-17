from aiogram.dispatcher.filters.state import State, StatesGroup


class Phone(StatesGroup):
    category = State()
    subcategory = State()
    product = State()
    subproduct = State()
