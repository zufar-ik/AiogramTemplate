from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import menuAll, tel
from keyboards.default.forcart import add_product, count1
from keyboards.default.pixel import pixel4, pixel5, pixel6, pixelModel, modelListPixel, pixelmod, sheets_2
from keyboards.inline.inn import donate_version
from loader import dp, db
from states.state import Phone, Pixel


@dp.message_handler(text='Google', state=Phone.category)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Google", reply_markup=pixelmod)
    await Pixel.subcategory.set()


@dp.message_handler(text="Pixel", state=Pixel.subcategory)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Pixel", reply_markup=pixelModel)
    await Pixel.product.set()


@dp.message_handler(text="Google Pixel 4/XL/a", state=Pixel.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона Pixel 4", reply_markup=pixel4)
    await Pixel.subproduct.set()


@dp.message_handler(text="Google Pixel 5/a", state=Pixel.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона Pixel 5", reply_markup=pixel5)
    await Pixel.subproduct.set()


@dp.message_handler(text="Google Pixel 6/Pro", state=Pixel.product)
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона Pixel 6", reply_markup=pixel6)
    await Pixel.subproduct.set()


@dp.message_handler(text="Назад🔙", state=Pixel.subcategory)
async def back1(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=tel)
    await Phone.category.set()


@dp.message_handler(text="Назад🔙", state=Pixel.subproduct)
async def back1(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=pixelModel)
    await Pixel.product.set()


@dp.message_handler(text="Назад🔙", state=Pixel.product)
async def back1(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=pixelmod)
    await Pixel.subcategory.set()

@dp.message_handler(text="Главное меню🏠", state=Pixel)
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали Главное меню", reply_markup=menuAll)
    await state.finish()


@dp.message_handler(text=modelListPixel, state=Pixel.subproduct)
async def model_answer(message: types.Message, state: FSMContext):
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListPixel:
        if message.text == i:
            n = modelListPixel.index(i)
            n += 1
            answer_sheet = (sheets_2[f"B{n}:AV{n}"])
            for photo, date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, \
                sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, \
                cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, \
                usb, bluet in answer_sheet:
                await message.answer_photo(photo=photo.value)
                await message.answer(f'<b>•Общие Характеристики</b>•\n\n'
                                     f'•Дата выхода: {date.value}\n'
                                     f'•Размеры (ВxШxГ): {size.value}\n'
                                     f'•Вес: {weight.value}\n'
                                     f'•Корпус: {frame.value}\n'
                                     f'•Цвета: {color.value}\n'
                                     f'•Аккумулятор: {battery.value}\n'
                                     f'•Ориентировочная цена: {price.value}\n'
                                     f'\n\n<b>•Дисплей•</b>\n\n'
                                     f'•Технологии: {tech.value}\n'
                                     f'•Сенсорный экран: {touch.value}\n'
                                     f'•Глубина цвета: {colour.value}\n'
                                     f'•Размер(Диагональ): {sized.value}\n'
                                     f'•Площадь экрана: {square.value}\n'
                                     f'•Соотношение (высота:ширина): {hw.value}\n'
                                     f'•Соотношение (экран:корпус): {sc.value}\n'
                                     f'•Разрешение: {sr.value}\n'
                                     f'•Точек на дюйм : {PPI.value}\n'
                                     f'•Защита экрана: {sp.value}\n'
                                     f'•Другое: {other.value}\n'
                                     f'\n\n<b>•Камеры и видео•</b>\n\n'
                                     f'•Камера заднего, основная: {camback.value}\n'
                                     f'•Характеристики камеры: \n{backab.value}\n'
                                     f'•Функции: {backf.value}\n'
                                     f'•Запись видео: {backrec.value}\n'
                                     f'•Фронтальная камера, селфи: {frontcam.value}\n'
                                     f'•Характеристика: {frontab.value}\n'
                                     f'•Функции: {frontf.value}\n'
                                     f'•Запись видео: {frontrec.value}\n'
                                     f'\n\n<b>•Продуктивность•</b>\n\n'
                                     f'•Операционная система (OS): {OS.value}\n'
                                     f'•Чипсет: {chip.value}\n'
                                     f'•Центральный процессор (CPU): {cpu.value}\n'
                                     f'•Графический процессор (GPU): {gpu.value}\n'
                                     f'•Внешняя карта памяти: {sdcard.value}\n'
                                     f'•Внутренняя память: {RAM.value}\n'
                                     f'•Результат Antutu 9: {Antutu9.value}\n'
                                     f'•Результат Antutu 8: {Antutu8.value}\n'
                                     f'•Результат GeekBench 5 Single Core: {Geek5s.value}\n'
                                     f'•Результат GeekBench 5 Multi-Core: {Geek5m.value}\n'
                                     f'\n\n<b>•Сети•</b>\n\n'
                                     f'•Слоты: {sim.value}\n'
                                     f'•Сеть: {net.value}\n'
                                     f'•Скорость интернета: {speed.value}\n'
                                     f'•GPRS: {gprs.value}\n'
                                     f'•Edge: {edge.value}\n'
                                     f'•Wi-Fi: {wifi.value}\n'
                                     f'•GPS: {gps.value}\n'
                                     f'•NFC: {nfc.value}\n'
                                     f'•USB: {usb.value}\n'
                                     f'•Bluetooth: {bluet.value}\n', reply_markup=add_product)
                Price = price.value
                await state.update_data(
                    {"price": Price}
                )
                await Pixel.subproduct.set()


@dp.message_handler(text="Добавить в корзинку!", state=Pixel.subproduct)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Pixel.subproduct.set()


@dp.message_handler(text="Отмена", state=Pixel.subproduct)
async def get_donate(message: types.Message):
    await message.answer('Вы нажали отмена', reply_markup=pixelModel)
    await Pixel.product.set()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message_handler(state=Pixel.subproduct)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        dataall = await state.get_data()
        NAME = dataall.get("name")
        price = dataall.get("price")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n"
                             f"Кол-во: {n}, Цена за штуку: {price}", reply_markup=pixelModel)
    await Pixel.product.set()


@dp.callback_query_handler(text="donate", state=Pixel.subproduct)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Pixel.subproduct.set()



