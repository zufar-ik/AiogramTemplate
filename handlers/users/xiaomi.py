from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import tel, xiaomi, Redmi, menuAll
from keyboards.default.model_redmi import redminot9, redminot10, redminot11, redminot12, modelList
from loader import dp
from keyboards.default.model_redmi import sheet
@dp.message_handler(text="Телефоны")
async def go(message:types.Message):
    await message.answer("Выберите Марку Смартфонов",reply_markup=tel)

@dp.message_handler(text='Xiaomi')
async def key(message: types.Message):
    await message.answer("Выберите линейку смартфонов", reply_markup=xiaomi)


@dp.message_handler(text='Redmi')
async def key(message: types.Message):
    await message.answer("Выберите серию смартфона Redmi", reply_markup=Redmi)


@dp.message_handler(text='Redmi Note 9/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot9)


@dp.message_handler(text='Redmi Note 10/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot10)


@dp.message_handler(text="Назад")
async def back(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад", reply_markup=Redmi)


@dp.message_handler(text='Главное меню')
async def mainmenu(message: types.Message):
    await message.answer("Вы нажали Главное меню", reply_markup=menuAll)


@dp.message_handler(text='Redmi Note 11/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot11)


@dp.message_handler(text='Redmi Note 12/S/Pro')
async def key(message: types.Message):
    await message.answer("Выберите модель смартфона Redmi", reply_markup=redminot12)


@dp.message_handler(text=modelList)
async def model_answer(message: types.Message):
    for i in modelList:
        if message.text == i:
            n = modelList.index(i)
            n += 1
            answersheet = (sheet[f"C{n}:AV{n}"])
            for date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, usb, bluet in answersheet:
                await message.answer(f'<b>•Общие Характеристики</b>•\n\n\n'
                                     f'•Дата выхода: \n{date.value}\n'
                                     f'•Размеры (ВxШxГ):\n{size.value}\n'
                                     f'•Вес: \n{weight.value}\n'
                                     f'•Корпус: \n{frame.value}\n'
                                     f'•Цвета: \n{color.value}\n'
                                     f'•Аккумулятор: \n{battery.value}\n'
                                     f'•Ориентировочная цена: \n{price.value}\n\n'
                                     f'•Дислпей•\n'
                                     f'•Технологии: \n{tech.value}\n'
                                     f'•Сенсорный экран: \n{touch.value}\n'
                                     f'•Глубина цвета: \n{colour.value}\n'
                                     f'•Размер(Диагональ): \n{sized.value}\n'
                                     f'•Площадь экрана: \n{square.value}\n'
                                     f'•Соотношение (высота:ширина): \n{hw.value}\n'
                                     f'•Соотношение (экран:корпус): \n{sc.value}\n'
                                     f'•Разрешение: \n{sr.value}\n'
                                     f'•Точек на дюйм : \n{PPI.value}\n'
                                     f'•Защита экрана: \n{sp.value}\n'
                                     f'•Другое: \n{other.value}\n'
                                     f'•Камеры и видео•'
                                     f'•Камера заднего, основная: \n{camback.value}\n'
                                     f'•Характеристики камеры: \n{backab.value}\n'
                                     f'•Функции: \n{backf.value}\n'
                                     f'•Запись видео: \n{backrec.value}\n'
                                     f'•Фронтальная камера, селфи: \n{frontcam.value}\n'
                                     f'•Характеристика: \n{frontab.value}\n'
                                     f'•Функции: \n{frontf.value}\n'
                                     f'•Запись видео: \n{frontrec.value}\n'
                                     f'•Продуктивность•'
                                     f'•Операционная система (OS): \n{OS.value}\n'
                                     f'•Чипсет: \n{chip.value}\n'
                                     f'•Центральный процессор (CPU): \n{cpu.value}\n'
                                     f'•Графический процессор (GPU): \n{gpu.value}\n'
                                     f'•Внешняя карта памяти: \n{sdcard.value}\n'
                                     f'•Внутренняя память: \n{RAM.value}\n'
                                     f'•Результат Antutu 9: \n{Antutu9.value}\n'
                                     f'•Результат Antutu 8: \n{Antutu8.value}\n'
                                     f'•Результат GeekBench 5 Single Core: \n{Geek5s.value}\n'
                                     f'•Результат GeekBench 5 Multi-Core: \n{Geek5m.value}\n'
                                     f'•Cети•'
                                     f'•Слоты: \n{sim.value}\n'
                                     f'•Сеть: \n{net.value}\n'
                                     f'•Скорость интернета: \n{speed.value}\n'
                                     f'•GPRS: \n{gprs.value}\n'
                                     f'•Edge: \n{edge.value}\n'
                                     f'•Wi-Fi: \n{wifi.value}\n'
                                     f'•GPS: \n{gps.value}\n'
                                     f'•NFC: \n{nfc.value}\n'
                                     f'•USB: \n{usb.value}\n'
                                     f'•Bluetooth: \n{bluet.value}\n')
