from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import menuAll, tel
from keyboards.default.forcart import add_product, count1
from keyboards.default.galaxy import galaxymod, modelListGalaxy, sheets_4, GalaxyS10, GalaxyS20, GalaxyS21, GalaxyS22, \
    galaxyModelS, galaxyModelN, GalaxyNote10, GalaxyNote20, galaxyModelZ, GalaxyFold, GalaxyFlip, galaxyModelA, \
    GalaxyA01, GalaxyA10, GalaxyA20, GalaxyA30, GalaxyA40, GalaxyA50, GalaxyA70
from keyboards.inline.inn import donate, donate_version
from loader import dp, db
from states.state import Phone
from states.state import Samsung


@dp.message_handler(text="Samsung", state=Phone.category)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Samsung", reply_markup=galaxymod)
    await Samsung.subcategory.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subcategory)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=tel)
    await Phone.category.set()


@dp.message_handler(text='Galaxy S', state=Samsung.subcategory)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона Galaxy S", reply_markup=galaxyModelS)
    await Samsung.productS.set()


@dp.message_handler(text="Назад🔙", state=Samsung.productS)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxymod)
    await Samsung.subcategory.set()


@dp.message_handler(text="Galaxy S10/Lite/e/+", state=Samsung.productS)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов S10", reply_markup=GalaxyS10)
    await Samsung.subproductS.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subproductS)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxyModelS)
    await Samsung.productS.set()


@dp.message_handler(text="Galaxy S20/+/Ultra/FE", state=Samsung.productS)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов S20", reply_markup=GalaxyS20)
    await Samsung.subproductS.set()


@dp.message_handler(text="Galaxy S21/+/Ultra/FE", state=Samsung.productS)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов S21", reply_markup=GalaxyS21)
    await Samsung.subproductS.set()


@dp.message_handler(text="Galaxy S22/+/Ultra", state=Samsung.productS)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов S22", reply_markup=GalaxyS22)
    await Samsung.subproductS.set()


@dp.message_handler(text='Galaxy Note', state=Samsung.subcategory)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона Galaxy Note", reply_markup=galaxyModelN)
    await Samsung.productN.set()


@dp.message_handler(text="Назад🔙", state=Samsung.productN)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxymod)
    await Samsung.subcategory.set()


@dp.message_handler(text="Galaxy Note 10/Lite/+", state=Samsung.productN)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Note 10", reply_markup=GalaxyNote10)
    await Samsung.subproductN.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subproductN)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxyModelN)
    await Samsung.productN.set()


@dp.message_handler(text="Galaxy Note 20/Ultra", state=Samsung.productN)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Note 20", reply_markup=GalaxyNote20)
    await Samsung.subproductN.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subproductS)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxymod)
    await Samsung.productS.set()


@dp.message_handler(text='Galaxy Z', state=Samsung.subcategory)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона Galaxy Z", reply_markup=galaxyModelZ)
    await Samsung.productZ.set()


@dp.message_handler(text="Galaxy Z Fold", state=Samsung.productZ)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy Z", reply_markup=GalaxyFold)
    await Samsung.subproductZF.set()


@dp.message_handler(text="Galaxy Z Flip", state=Samsung.productZ)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy Z", reply_markup=GalaxyFlip)
    await Samsung.subproductZFI.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subproductZFI)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxyModelZ)
    await Samsung.productZ.set()


@dp.message_handler(text="Назад🔙", state=Samsung.productZ)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxymod)
    await Samsung.subcategory.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subproductZF)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxyModelZ)
    await Samsung.productZ.set()


@dp.message_handler(text='Galaxy A', state=Samsung.subcategory)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона Galaxy A", reply_markup=galaxyModelA)
    await Samsung.productA.set()


@dp.message_handler(text="Назад🔙", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxymod)
    await Samsung.subcategory.set()


@dp.message_handler(text="Galaxy A01-A09", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A01-A09", reply_markup=GalaxyA01)
    await Samsung.subproductA.set()


@dp.message_handler(text="Назад🔙", state=Samsung.subproductA)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=galaxyModelA)
    await Samsung.productA.set()


@dp.message_handler(text="Galaxy A10-A19", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A10-A19", reply_markup=GalaxyA10)
    await Samsung.subproductA.set()


@dp.message_handler(text="Galaxy A20-A29", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A20-A29", reply_markup=GalaxyA20)
    await Samsung.subproductA.set()


@dp.message_handler(text="Galaxy A30-A39", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A30-A39", reply_markup=GalaxyA30)
    await Samsung.subproductA.set()


@dp.message_handler(text="Galaxy A40-A49", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A40-A49", reply_markup=GalaxyA40)
    await Samsung.subproductA.set()


@dp.message_handler(text="Galaxy A50-A59", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A50-A59", reply_markup=GalaxyA50)
    await Samsung.subproductA.set()


@dp.message_handler(text="Galaxy A70-A79", state=Samsung.productA)
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов Galaxy A70-A79", reply_markup=GalaxyA70)
    await Samsung.subproductA.set()


@dp.message_handler(text=modelListGalaxy, state=Samsung.subproductS)
async def model_answer(message: types.Message,state:FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListGalaxy:
        if message.text == i:
            n = modelListGalaxy.index(i)
            n += 1
            answer_sheet = (sheets_4[f"B{n}:AV{n}"])
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
                    {"price":Price}
                )
                await Samsung.subproductS.set()


@dp.message_handler(text="Добавить в корзинку!", state=Samsung.subproductS)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Samsung.subproductS.set()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@dp.message_handler(state=Samsung.subproductS)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        dataall = await state.get_data()
        NAME = dataall.get("name")
        price = dataall.get("price")
        idname = message.from_user.id
        product = db.check_product(tg_id = message.from_user.id,Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n"
                             f"Кол-во: {n}, Цена за штуку: {price}",reply_markup=galaxyModelS)
    await Samsung.productS.set()


@dp.message_handler(text=modelListGalaxy, state=Samsung.subproductZFI)
async def model_answer(message: types.Message,state:FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListGalaxy:
        if message.text == i:
            n = modelListGalaxy.index(i)
            n += 1
            answer_sheet = (sheets_4[f"B{n}:AV{n}"])
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
                    {"price":Price}
                )
                await Samsung.subproductZFI.set()


@dp.message_handler(text="Добавить в корзинку!", state=Samsung.subproductZFI)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Samsung.subproductZFI.set()

@dp.message_handler(state=Samsung.subproductZFI)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        dataall = await state.get_data()
        NAME = dataall.get("name")
        price = dataall.get("price")
        idname = message.from_user.id
        product = db.check_product(tg_id = message.from_user.id,Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n"
                             f"Кол-во: {n}, Цена за штуку: {price}",reply_markup=galaxyModelZ)
    await Samsung.productZ.set()


@dp.message_handler(text=modelListGalaxy, state=Samsung.subproductZF)
async def model_answer(message: types.Message,state:FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListGalaxy:
        if message.text == i:
            n = modelListGalaxy.index(i)
            n += 1
            answer_sheet = (sheets_4[f"B{n}:AV{n}"])
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
                    {"price":Price}
                )
                await Samsung.subproductZF.set()


@dp.message_handler(text="Добавить в корзинку!", state=Samsung.subproductZF)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Samsung.subproductZF.set()

@dp.message_handler(state=Samsung.subproductZF)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        dataall = await state.get_data()
        NAME = dataall.get("name")
        price = dataall.get("price")
        idname = message.from_user.id
        product = db.check_product(tg_id = message.from_user.id,Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n"
                             f"Кол-во: {n}, Цена за штуку: {price}",reply_markup=galaxyModelZ)
    await Samsung.productZ.set()


@dp.message_handler(text=modelListGalaxy, state=Samsung.subproductA)
async def model_answer(message: types.Message,state:FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListGalaxy:
        if message.text == i:
            n = modelListGalaxy.index(i)
            n += 1
            answer_sheet = (sheets_4[f"B{n}:AV{n}"])
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
                    {"price":Price}
                )
                await Samsung.subproductA.set()


@dp.message_handler(text="Добавить в корзинку!", state=Samsung.subproductA)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Samsung.subproductA.set()

@dp.message_handler(state=Samsung.subproductA)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        dataall = await state.get_data()
        NAME = dataall.get("name")
        price = dataall.get("price")
        idname = message.from_user.id
        product = db.check_product(tg_id = message.from_user.id,Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n"
                             f"Кол-во: {n}, Цена за штуку: {price}",reply_markup=galaxyModelA)
    await Samsung.productA.set()


@dp.message_handler(text=modelListGalaxy, state=Samsung.subproductN)
async def model_answer(message: types.Message,state:FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListGalaxy:
        if message.text == i:
            n = modelListGalaxy.index(i)
            n += 1
            answer_sheet = (sheets_4[f"B{n}:AV{n}"])
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
                    {"price":Price}
                )
                await Samsung.subproductN.set()


@dp.message_handler(text="Добавить в корзинку!", state=Samsung.subproductN)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Samsung.subproductN.set()

@dp.message_handler(state=Samsung.subproductN)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        dataall = await state.get_data()
        NAME = dataall.get("name")
        price = dataall.get("price")
        idname = message.from_user.id
        product = db.check_product(tg_id = message.from_user.id,Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n"
                             f"Кол-во: {n}, Цена за штуку: {price}",reply_markup=galaxyModelN)
    await Samsung.productN.set()


@dp.message_handler(text='Главное меню🏠', state=Samsung)
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали Главное меню", reply_markup=menuAll)
    await state.finish()


@dp.callback_query_handler(text="donate", state=Samsung.subproductN)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Samsung.subproductN.set()


@dp.callback_query_handler(text="donate", state=Samsung.subproductS)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Samsung.subproductS.set()


@dp.callback_query_handler(text="donate", state=Samsung.subproductZFI)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Samsung.subproductZFI.set()


@dp.callback_query_handler(text="donate", state=Samsung.subproductZF)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Samsung.subproductZF.set()


@dp.callback_query_handler(text="donate", state=Samsung.subproductA)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Samsung.subproductA.set()


@dp.callback_query_handler(text="donate", state=Samsung.subproductN)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Samsung.subproductN.set()
