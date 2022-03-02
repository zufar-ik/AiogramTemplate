from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import tel, xiaomi, Redmi, menuAll
from keyboards.default.forcart import add_product, count1
from keyboards.default.model_redmi import redminot, modelListX, redmi_a, redmi_k, MI, POCO, mi_mi10, sheets_1, \
    black_shark, mi_mi11, mi_mi12, poco_x, poco_c, poco_m, poco_f, MI_MIX, mi_mix
from keyboards.inline.inn import donate_version
from loader import dp, db, bot
from states.state import Phone, Question


@dp.message_handler(text="Телефоны📱")
async def all_brand(message: types.Message):
    await message.answer("Выберите Марку Смартфонов", reply_markup=tel)
    await Phone.category.set()


@dp.message_handler(text="Ноутбуки💻 (beta)")
async def all_brand(message: types.Message):
    await message.answer("Этот раздел еще в разработке!")


@dp.message_handler(text="Связаться с администратором⁉️")
async def all_brand(message: types.Message, state: FSMContext):
    await message.answer("Задайте вопрос!")
    await Question.questionad.set()

@dp.message_handler(state=Question.questionad)
async def get_price(message: types.Message, state: FSMContext):
    que = message.text
    await state.update_data(
        {"vopros": que}
    )
    data = await state.get_data()
    vopros = data.get("vopros")
    username = message.from_user.username
    iduser = message.from_user.id
    await bot.send_message(chat_id=1297546327,text=f"Вопрос: {vopros}\nНикнейм: @{username}\nID Пользователя: {iduser}")
    await message.answer("Ваш вопрос отправлен!\n"
                         "Спасибо за помощь по улучшению нашего бота!",reply_markup=menuAll)
    await state.finish()
@dp.message_handler(text="Назад🔙", state=Phone.category)
async def back(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=menuAll)
    await state.finish()


@dp.message_handler(text='Xiaomi', state=Phone.category)
async def Xiaomi_menu(message: types.Message):
    await message.answer("Выберите линейку смартфонов Xiaomi", reply_markup=xiaomi)
    await Phone.subcategory.set()


@dp.message_handler(text="Назад🔙", state=Phone.subcategory)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=tel)
    await Phone.category.set()


@dp.message_handler(text='Redmi', state=Phone.subcategory)
async def Redmi_menu(message: types.Message):
    await message.answer("Выберите серию смартфона Redmi", reply_markup=Redmi)
    await Phone.productR.set()


@dp.message_handler(text="Назад🔙", state=Phone.productR)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()


@dp.message_handler(text='MI MIX', state=Phone.subcategory)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона MI MIX", reply_markup=MI_MIX)
    await Phone.productMIX.set()


@dp.message_handler(text='MIX', state=Phone.productMIX)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона MIX", reply_markup=mi_mix)
    await Phone.subproductMIX.set()


@dp.message_handler(text='MI', state=Phone.subcategory)
async def MI_menu(message: types.Message):
    await message.answer("Выберите серию смартфона MI", reply_markup=MI)
    await Phone.productMI.set()


@dp.message_handler(text="Назад🔙", state=Phone.subproductMIX)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=MI_MIX)
    await Phone.productMIX.set()


@dp.message_handler(text="Назад🔙", state=Phone.productMIX)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()


@dp.message_handler(text="MI 10/T", state=Phone.productMI)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона MI 10/T", reply_markup=mi_mi10)
    await Phone.subproductMI.set()


@dp.message_handler(text="MI 11/T", state=Phone.productMI)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона MI 11/T", reply_markup=mi_mi11)
    await Phone.subproductMI.set()


@dp.message_handler(text="MI 12/T", state=Phone.productMI)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона MI 12/T", reply_markup=mi_mi12)
    await Phone.subproductMI.set()


@dp.message_handler(text="Black Shark", state=Phone.productMI)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона Black Shark", reply_markup=black_shark)
    await Phone.subproductMI.set()


@dp.message_handler(text="Назад🔙", state=Phone.subproductMI)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=MI)
    await Phone.productMI.set()


@dp.message_handler(text="Назад🔙", state=Phone.productMI)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()


@dp.message_handler(text='POCO', state=Phone.subcategory)
async def POCO_menu(message: types.Message):
    await message.answer("Выберите серию смартфона POCO", reply_markup=POCO)
    await Phone.productP.set()


@dp.message_handler(text="POCO X", state=Phone.productP)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона POCO X", reply_markup=poco_x)
    await Phone.subproductP.set()


@dp.message_handler(text="POCO C", state=Phone.productP)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона POCO C", reply_markup=poco_c)
    await Phone.subproductP.set()


@dp.message_handler(text="POCO F", state=Phone.productP)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона POCO F", reply_markup=poco_f)
    await Phone.subproductP.set()


@dp.message_handler(text="POCO M", state=Phone.productP)
async def MI10_menu(message: types.Message):
    await message.answer("Выберите модель смартфона POCO M", reply_markup=poco_m)
    await Phone.subproductP.set()


@dp.message_handler(text="Назад🔙", state=Phone.subproductP)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=POCO)
    await Phone.productP.set()


@dp.message_handler(text="Назад🔙", state=Phone.productP)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()


@dp.message_handler(text="Назад🔙", state=Phone.subproductR)
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=Redmi)
    await Phone.productR.set()


@dp.message_handler(text="Redmi/Redmi A", state=Phone.productR)
async def Redmi_A_menu(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi/Redmi A", reply_markup=redmi_a)
    await Phone.subproductR.set()


@dp.message_handler(text="Redmi K", state=Phone.productR)
async def Redmi_K_menu(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi K", reply_markup=redmi_k)
    await Phone.subproductR.set()


@dp.message_handler(text="Redmi Note", state=Phone.productR)
async def Redmi_K_menu(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi Note", reply_markup=redminot)
    await Phone.subproductR.set()


@dp.message_handler(text='Главное меню🏠', state=Phone)
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали Главное меню", reply_markup=menuAll)
    await state.finish()


@dp.message_handler(text=modelListX, state=Phone.subproductR)
async def model_answer(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answer_sheet = (sheets_1[f"B{n}:AV{n}"])
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
                await Phone.subproductR.set()


@dp.message_handler(text="Добавить в корзинку!", state=Phone.subproductR)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Phone.subproductR.set()


@dp.message_handler(text="🔙Назад", state=Phone.subproductR)
async def addtocart(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=Redmi)
    await Phone.productR.set()


@dp.message_handler(text="Отмена", state=Phone.subproductR)
async def get_donate(message: types.Message):
    await message.answer('Вы нажали отмена', reply_markup=Redmi)
    await Phone.productR.set()


@dp.message_handler(state=Phone.subproductR)
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
                             f"Кол-во: {n}, Цена за штуку: {price}", reply_markup=Redmi)
    await Phone.productR.set()


@dp.message_handler(text=modelListX, state=Phone.subproductMI)
async def model_answer(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answer_sheet = (sheets_1[f"B{n}:AV{n}"])
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
                                     f'\n\n<b>• Сети •</b>\n\n'
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
                await Phone.subproductMI.set()


@dp.message_handler(text="Добавить в корзинку!", state=Phone.subproductMI)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Phone.subproductMI.set()


@dp.message_handler(text="🔙Назад", state=Phone.subproductMI)
async def addtocart(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=MI)
    await Phone.productMI.set()


@dp.message_handler(text="Отмена", state=Phone.subproductMI)
async def get_donate(message: types.Message):
    await message.answer('Вы нажали отмена', reply_markup=MI)
    await Phone.productMI.set()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message_handler(state=Phone.subproductMI)
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
                             f"Кол-во: {n}, Цена за штуку: {price}", reply_markup=MI)
    await Phone.productMI.set()


@dp.message_handler(text=modelListX, state=Phone.subproductMIX)
async def model_answer(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answer_sheet = (sheets_1[f"B{n}:AV{n}"])
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
                await Phone.subproductMIX.set()


@dp.message_handler(text="Добавить в корзинку!", state=Phone.subproductMIX)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Phone.subproductMIX.set()


@dp.message_handler(text="🔙Назад", state=Phone.subproductMIX)
async def addtocart(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=MI_MIX)
    await Phone.productMIX.set()


@dp.message_handler(text="Отмена", state=Phone.subproductMIX)
async def get_donate(message: types.Message):
    await message.answer('Вы нажали отмена', reply_markup=MI_MIX)
    await Phone.productMIX.set()


@dp.message_handler(state=Phone.subproductMIX)
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
                             f"Кол-во: {n}, Цена за штуку: {price}", reply_markup=MI_MIX)
    await Phone.productMIX.set()


@dp.message_handler(text=modelListX, state=Phone.subproductP)
async def model_answer(message: types.Message, state: FSMContext):
    namex = message.text
    await state.update_data(
        {"name": namex}
    )
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answer_sheet = (sheets_1[f"B{n}:AV{n}"])
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
                await Phone.subproductP.set()


@dp.message_handler(text="Добавить в корзинку!", state=Phone.subproductP)
async def addtocart(message: types.Message):
    await message.answer("Сколько смартфонов хотите купить?", reply_markup=count1)
    await Phone.subproductP.set()


@dp.message_handler(text="🔙Назад", state=Phone.subproductP)
async def addtocart(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=POCO)
    await Phone.productP.set()


@dp.message_handler(text="Отмена", state=Phone.subproductP)
async def get_donate(message: types.Message):
    await message.answer('Вы нажали отмена', reply_markup=POCO)
    await Phone.productP.set()


@dp.message_handler(state=Phone.subproductP)
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
                             f"Кол-во: {n}, Цена за штуку: {price}", reply_markup=POCO)
    await Phone.productP.set()


@dp.callback_query_handler(text="donate", state=Phone.subproductR)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Phone.subproductR.set()


@dp.callback_query_handler(text="donate", state=Phone.subproductP)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Phone.subproductP.set()


@dp.callback_query_handler(text="donate", state=Phone.subproductMI)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Phone.subproductMI.set()


@dp.callback_query_handler(text="donate", state=Phone.subproductMIX)
async def get_donate(call: types.CallbackQuery):
    await call.message.answer('Выберите удобный способ поддержки!', reply_markup=donate_version)
    await Phone.subproductMIX.set()
