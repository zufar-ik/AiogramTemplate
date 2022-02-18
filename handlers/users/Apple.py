from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.state import Phone


@dp.message_handler(text='Apple', state=Phone.category)
async def key(message: types.Message, state: FSMContext):
    await message.answer("Выберите линейку смартфонов")
    await Phone.subcategory.set()
