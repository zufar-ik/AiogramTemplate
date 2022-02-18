from aiogram.dispatcher.filters.state import State, StatesGroup


class Phone(StatesGroup):
    category = State()
    subcategory = State()
    product = State()
    subproduct = State()


class Pixel(StatesGroup):
    subcategory = State()
    product = State()
    subproduct = State()


class iPhone(StatesGroup):
    subcategory = State()
    product = State()
    subproduct = State()

class Samsung(StatesGroup):
    subcategory = State()
    productS = State()
    productA = State()
    productZ = State()
    productN = State()
    subproductS = State()
    subproductA= State()
    subproductZ = State()
    subproductN = State()
