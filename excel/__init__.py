import openpyxl
book = openpyxl.open("xiaomi_redmi.xlsx",read_only=True)
sheet = book.active