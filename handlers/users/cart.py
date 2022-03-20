import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from data.config import CHANNELS
from handlers.users.tel_price import get_price
from keyboards.default.buttons import menuAll, tel
from keyboards.inline.inn import user, contactnum, admin
from loader import dp, db
from states.state import Phone, Zakaz


@dp.message_handler(text='Корзинка 🛒')
async def korzina(message: types.Message):
    products1 = db.get_products(tg_id=message.from_user.id)
    if len(products1) != 0:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Заказать 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Ваши заказы\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} $\n"
        msg += f"\nОбщая сумма: {total} $"
        markup.row("Назад", "Очистить 🗑")
        await message.answer(msg, reply_markup=markup)
    else:
        await message.answer("Ваша корзинка еще пуста! Может быть это исправим?", reply_markup=tel)
        await Phone.category.set()


@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Name=product.strip())
    await message.answer(f"{product.strip()} Ваша корзинка удалена!", reply_markup=menuAll)


@dp.message_handler(text="Очистить 🗑")
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Ваша корзинка очищена!", reply_markup=menuAll)


@dp.message_handler(text="Назад")
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=menuAll)


@dp.message_handler(text="Заказать 🚚")
async def send(message: types.Message):
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    msg = "Ваши заказы\n\n"
    for product in products:
        price = get_price(product[1], product[2])
        total += price
        msg += f"{product[1]} x {product[2]} = {price} $\n"
    msg += f"\nОбщая сумма: {total} $"
    yes_no = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no.add("Да!")
    yes_no.add("Нет!")
    await message.answer(msg)
    await message.answer("Все верно?", reply_markup=yes_no)


@dp.message_handler(text="Да!")
async def yes(message: types.Message):
    await message.answer("Заполните нужные пункты пожалуйста", reply_markup=ReplyKeyboardRemove())
    await message.answer("Как вас зовут?")
    await Zakaz.name.set()


@dp.message_handler(state=Zakaz.name)
async def name(message: types.Message, state: FSMContext):
    id1 = message.from_user.id
    await state.update_data(
        {"id":id1}
    )
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Введите адрес доставки")
    await Zakaz.next()


@dp.message_handler(state=Zakaz.Adress)
async def adress(message: types.Message, state: FSMContext):
    adress1 = message.text
    await state.update_data(
        {"adress": adress1}
    )
    await message.answer("Введите основной номер!", reply_markup=contactnum)
    await Zakaz.next()


@dp.message_handler(content_types=['contact'], state=Zakaz.tel)
async def get_img(message: types.Message, state: FSMContext):
    phone = message.contact['phone_number']
    num = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    if re.match(num, phone):
        await state.update_data(
            {'phone': phone}
        )
        await message.answer("Введите второстепенный номер!\n"
                             "(если его нет отправьте любой знак)")
        await Zakaz.next()
    else:
        await message.answer("Вы ввели некорректный номер\n"
                             "Введите еще раз!")
        await Zakaz.tel


@dp.message_handler(state=Zakaz.tel2)
async def get_img(message: types.Message, state: FSMContext):
    tel2 = message.text
    await state.update_data(
        {'tel2': tel2}
    )
    data1 = await state.get_data()
    name = data1.get("name")
    adress1 = data1.get("adress")
    telnum1 = data1.get("phone")
    telnum2 = data1.get("tel2")
    Username = message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    username = data1.get("username")
    await message.answer(
        text=f"Имя и фамилия: {name}\n"
             f"Адрес: {adress1}\n"
             f"Основной номер: +{telnum1}\n"
             f"Username: @{Username}\n"
             f"Второстепенный: +{telnum2}", reply_markup=user
    )
    await message.answer("Этот раздел только для демонстрации наших сил😊", reply_markup=menuAll)
    await Zakaz.next()

@dp.callback_query_handler(text="cancel",state=Zakaz.confirmP)
async def back(call: types.CallbackQuery):
    await call.message.answer("Вы отменили заказ!", reply_markup=menuAll)
    await call.message.delete()


@dp.callback_query_handler(text="send_to_admin", state=Zakaz.confirmP)
async def sendadmin(call: types.CallbackQuery, state: FSMContext):
    data1 = await state.get_data()
    name = data1.get("name")
    adress1 = data1.get("adress")
    telnum1 = data1.get("phone")
    telnum2 = data1.get("tel2")
    id1 = data1.get("id")
    Username = call.message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    username = data1.get("username")
    products = db.get_products(tg_id=id1)
    total = 0
    msg = "Его заказы\n\n"
    for product in products:
        price = get_price(product[1], product[2])
        total += price
        msg += f"{product[1]} x {product[2]} = {price} $\n"
    msg += f"\nОбщая сумма: {total} $\n"
    await call.bot.send_message(chat_id=1297546327,
                                text=f"{msg}\n"
                                     f"Имя и фамилия: {name}\n"
                                     f"Адрес: {adress1}\n"
                                     f"Основной номер: +{telnum1}\n"
                                     f"Username: @{username}\n"
                                     f"Второстепенный: +{telnum2}", reply_markup=admin
                                )
    await call.message.answer("Ваш заказ не будет отправлен!\n"
                              "Этот раздел только для демонстрации наших сил😊", reply_markup=menuAll)

    db.clear_cart(tg_id=id1)

    await state.finish()

@dp.callback_query_handler(text="send_to_channel")
async def confirm_post(call:types.CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])

@dp.message_handler(text="Нет!")
async def no(message: types.Message):
    await message.answer("Вы отменили заказ!", reply_markup=menuAll)
