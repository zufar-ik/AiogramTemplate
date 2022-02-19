from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import tel, xiaomi, Redmi, menuAll
from keyboards.default.model_redmi import redminot9, sheetX, modelListX, redmi_a, redmi_k, MI, POCO, mi_mi10, sheets_1
from loader import dp
from states.state import Phone


@dp.message_handler(text="Телефоны")
async def go(message: types.Message):
    await message.answer("Выберите Марку Смартфонов", reply_markup=tel)
    await Phone.category.set()

@dp.message_handler(text="Назад", state=Phone.category)
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=menuAll)
    await state.finish()

@dp.message_handler(text='Xiaomi', state=Phone.category)
async def key(message: types.Message, state: FSMContext):
    await message.answer("Выберите линейку смартфонов", reply_markup=xiaomi)
    await Phone.subcategory.set()

@dp.message_handler(text="Назад", state=Phone.subcategory)
async def key(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=tel)
    await Phone.category.set()


@dp.message_handler(text='Redmi', state=Phone.subcategory)
async def key(message: types.Message, state: FSMContext):
    await message.answer("Выберите серию смартфона Redmi", reply_markup=Redmi)
    await Phone.productR.set()

@dp.message_handler(text="Назад", state=Phone.productR)
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()

@dp.message_handler(text='MI', state=Phone.subcategory)
async def key(message: types.Message, state: FSMContext):
    await message.answer("Выберите серию смартфона MI", reply_markup=MI)
    await Phone.productMI.set()

@dp.message_handler(text="MI 10",state=Phone.productMI)
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона MI 10", reply_markup=mi_mi10)
    await Phone.subproductMI.set()

@dp.message_handler(text="Назад",state=Phone.subproductMI)
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=MI)
    await Phone.productMI.set()

@dp.message_handler(text="Назад", state=Phone.productMI)
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()

@dp.message_handler(text='POCO', state=Phone.subcategory)
async def key(message: types.Message, state: FSMContext):
    await message.answer("Выберите серию смартфона POCO", reply_markup=POCO)
    await Phone.productP.set()

@dp.message_handler(text="Назад", state=Phone.productP)
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=xiaomi)
    await Phone.subcategory.set()

@dp.message_handler(text="")


@dp.message_handler(text='Redmi Note 9/S/Pro', state=Phone.productR)
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot9)
    await Phone.subproductR.set()

@dp.message_handler(text="Назад",state=Phone.subproductR)
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=Redmi)
    await Phone.productR.set()

@dp.message_handler(text="Redmi/Redmi A", state=Phone.productR)
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redmi_a)
    await Phone.subproductR.set()


@dp.message_handler(text="Redmi K", state=Phone.productR)
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redmi_k)
    await Phone.subproductR.set()




@dp.message_handler(text='Главное меню',state=Phone)
async def mainmenu(message: types.Message,state:FSMContext):
    await message.answer("Вы нажали Главное меню", reply_markup=menuAll)
    await state.finish()

# @dp.message_handler(text='Redmi Note 11/S/Pro', state=Phone.product)
# async def key(message: types.Message):
#     await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot11)
#     await Phone.subproduct.set()
#
#
# @dp.message_handler(text='Redmi Note 12/S/Pro', state=Phone.product)
# async def key(message: types.Message):
#     await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot12)
#     await Phone.subproduct.set()


@dp.message_handler(text=modelListX, state=Phone.subproductR)
async def model_answer(message: types.Message):
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answersheet = (sheets_1[f"B{n}:AV{n}"])
            for photo,date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, usb, bluet in answersheet:
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
                                     f'\n\n<b>•Cети•</b>\n\n'
                                     f'•Слоты: {sim.value}\n'
                                     f'•Сеть: {net.value}\n'
                                     f'•Скорость интернета: {speed.value}\n'
                                     f'•GPRS: {gprs.value}\n'
                                     f'•Edge: {edge.value}\n'
                                     f'•Wi-Fi: {wifi.value}\n'
                                     f'•GPS: {gps.value}\n'
                                     f'•NFC: {nfc.value}\n'
                                     f'•USB: {usb.value}\n'
                                     f'•Bluetooth: {bluet.value}\n')
                await Phone.subproductR.set()


@dp.message_handler(text=modelListX, state=Phone.subproductMI)
async def model_answer(message: types.Message):
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answersheet = (sheets_1[f"B{n}:AV{n}"])
            for photo,date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, usb, bluet in answersheet:
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
                                     f'\n\n<b>•Cети•</b>\n\n'
                                     f'•Слоты: {sim.value}\n'
                                     f'•Сеть: {net.value}\n'
                                     f'•Скорость интернета: {speed.value}\n'
                                     f'•GPRS: {gprs.value}\n'
                                     f'•Edge: {edge.value}\n'
                                     f'•Wi-Fi: {wifi.value}\n'
                                     f'•GPS: {gps.value}\n'
                                     f'•NFC: {nfc.value}\n'
                                     f'•USB: {usb.value}\n'
                                     f'•Bluetooth: {bluet.value}\n')
                await Phone.subproductMI.set()


@dp.message_handler(text=modelListX, state=Phone.subproductMIX)
async def model_answer(message: types.Message):
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answersheet = (sheets_1[f"B{n}:AV{n}"])
            for photo,date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, usb, bluet in answersheet:
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
                                     f'\n\n<b>•Cети•</b>\n\n'
                                     f'•Слоты: {sim.value}\n'
                                     f'•Сеть: {net.value}\n'
                                     f'•Скорость интернета: {speed.value}\n'
                                     f'•GPRS: {gprs.value}\n'
                                     f'•Edge: {edge.value}\n'
                                     f'•Wi-Fi: {wifi.value}\n'
                                     f'•GPS: {gps.value}\n'
                                     f'•NFC: {nfc.value}\n'
                                     f'•USB: {usb.value}\n'
                                     f'•Bluetooth: {bluet.value}\n')
                await Phone.subproductMIX.set()

@dp.message_handler(text=modelListX, state=Phone.subproductP)
async def model_answer(message: types.Message):
    for i in modelListX:
        if message.text == i:
            n = modelListX.index(i)
            n += 1
            answersheet = (sheets_1[f"B{n}:AV{n}"])
            for photo,date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, usb, bluet in answersheet:
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
                                     f'\n\n<b>•Cети•</b>\n\n'
                                     f'•Слоты: {sim.value}\n'
                                     f'•Сеть: {net.value}\n'
                                     f'•Скорость интернета: {speed.value}\n'
                                     f'•GPRS: {gprs.value}\n'
                                     f'•Edge: {edge.value}\n'
                                     f'•Wi-Fi: {wifi.value}\n'
                                     f'•GPS: {gps.value}\n'
                                     f'•NFC: {nfc.value}\n'
                                     f'•USB: {usb.value}\n'
                                     f'•Bluetooth: {bluet.value}\n')
                await Phone.subproductP.set()