from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.apple import Apple_model, iphone, Apple_6, Apple_8, Apple_7, Apple_X, Apple_11, Apple_12, \
    Apple_13
from keyboards.default.buttons import tel
from loader import dp
from states.state import Phone, iPhone


@dp.message_handler(text='Apple', state=Phone.category)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Apple", reply_markup=iphone)
    await iPhone.subcategory.set()


@dp.message_handler(text="iPhone", state=iPhone.subcategory)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов", reply_markup=Apple_model)
    await iPhone.product.set()


@dp.message_handler(text="iPhone 6", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone 6", reply_markup=Apple_6)
    await iPhone.subproduct.set()


@dp.message_handler(text="iPhone 7", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone 7", reply_markup=Apple_7)
    await iPhone.subproduct.set()


@dp.message_handler(text="iPhone 8", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone 8", reply_markup=Apple_8)
    await iPhone.subproduct.set()


@dp.message_handler(text="iPhone X", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone X", reply_markup=Apple_X)
    await iPhone.subproduct.set()


@dp.message_handler(text="iPhone 11", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone 11", reply_markup=Apple_11)
    await iPhone.subproduct.set()


@dp.message_handler(text="iPhone 12", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone 12", reply_markup=Apple_12)
    await iPhone.subproduct.set()


@dp.message_handler(text="iPhone 13", state=iPhone.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона iPhone 13", reply_markup=Apple_13)
    await iPhone.subproduct.set()


@dp.message_handler(text="Назад🔙", state=iPhone.subcategory)
async def back1(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=tel)
    await Phone.category.set()


@dp.message_handler(text="Назад🔙", state=iPhone.subproduct)
async def back1(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=iphone)
    await iPhone.product.set()


@dp.message_handler(text="Назад🔙", state=iPhone.product)
async def back1(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=iphone)
    await iPhone.subcategory.set()
