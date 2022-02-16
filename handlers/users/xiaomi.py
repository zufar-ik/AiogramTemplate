import openpyxl

redmi = openpyxl.open("D:\\CODE\\AiogramTemplate\\excel\\xiaomi_redmi.xlsx", read_only=True)
sheet = redmi.active
calls = sheet['A4':'AU4']
for model, date, size, weight, frame, color, battery, price, tech, touch, colour, sized, square, hw, sc, sr, PPI, sp, other, camback, backab, backf, backrec, frontcam, frontab, frontf, frontrec, OS, chip, cpu, gpu, sdcard, RAM, Antutu9, Antutu8, Geek5s, Geek5m, sim, net, speed, gprs, edge, wifi, gps, nfc, usb, bluet in calls:
    print(f'Модель: {model.value}')
    print(f'Дата выхода: {date.value}')