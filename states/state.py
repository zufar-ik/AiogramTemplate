from aiogram.dispatcher.filters.state import State, StatesGroup


class Phone(StatesGroup):
    category = State()
    subcategory = State()
    productR = State()
    productMIX = State()
    productP = State()
    productMI = State()
    subproductR = State()
    subproductMIX = State()
    subproductP = State()
    subproductMI = State()
    goods = State()


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
    subproductA = State()
    subproductZF = State()
    subproductZFI = State()
    subproductN = State()

class Question(StatesGroup):
    questionad = State()

class Reklama(StatesGroup):
    reklama = State()