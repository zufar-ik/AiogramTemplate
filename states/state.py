from aiogram.dispatcher.filters.state import State, StatesGroup


class Anketa(StatesGroup):
    ism = State()
    familiya = State()
    phone = State()
    texnologia = State()
    region = State()
    price = State()
    prof = State()
    timew = State()
    purpose = State()

class Pomosh(StatesGroup):
    ism = State()
    familiya = State()
    phone = State()
    texnologia = State()
    region = State()
    price = State()
    prof = State()
    timew = State()
    purpose = State()

class Xodim(StatesGroup):
    idora = State()
    phone = State()
    texnologia = State()
    region = State()
    price = State()
    prof = State()
    timew = State()
    timework = State()
    purpose = State()