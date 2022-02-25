@dp.message_handler(state=anketa.amout)
async def orqa1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        od = data.get('odi')
        cat = data.get('cat')
        nn = price[od]* int(n)
        if cat == 'Shashlik':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=Shashlik)
            idd = message.from_user.id
            with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='a') as fayl:
                fayl.write(f"{od} - {str(price[od])} x {n} = {str(nn)}\n")
            await anketa.product.set()
        elif cat == 'Baliq 🐠':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=balq)
            idd = message.from_user.id
            with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='a') as fayl:
                fayl.write(f"{od} - {str(price[od])} x {n} = {str(nn)}\n")
            await anketa.product.set()
        elif cat == "Холодные закуски":
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=zaquska)
            idd = message.from_user.id
            with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='a') as fayl:
                fayl.write(f"{od} - {str(price[od])} x {n} = {str(nn)}\n")
            await anketa.product.set()
        elif cat == "Salatlar":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=salat)
            idd = message.from_user.id
            with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='a') as fayl:
                fayl.write(f"{od} - {str(price[od])} x {n} = {str(nn)}\n")
            await anketa.product.set()
        elif cat == "Ichimliklar 🥤":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=water)
            idd = message.from_user.id
            with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='a') as fayl:
                fayl.write(f"{od} - {str(price[od])} x {n} = {str(nn)}\n")
            await anketa.product.set()
        elif cat == "Sho'rva":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=shorva)
            idd = message.from_user.id
            with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='a') as fayl:
                fayl.write(f"{od} - {str(price[od])} x {n} = {str(nn)}\n")
            await anketa.product.set()
    else:
        await message.answer("Faqat son kiriting!")
        await anketa.amout.set()