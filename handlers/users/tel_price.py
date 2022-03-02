price = {
    "Redmi Note 9": 150,
    "Redmi Note 9S": 199,
    "Redmi Note 9 Pro": 250,
    "Redmi Note 10": 190,
    "Redmi Note 10S": 210,
    "Redmi Note 10 Pro": 280,
    "Redmi Note 11": 180,
    "Redmi Note 11S": 280,
    "Redmi Note 11 Pro": 300,
    "Redmi 9": 130,
    "Redmi 9A": 100,
    "Redmi 10": 180,
    "Redmi K30": 240,
    "Redmi K30 Pro": 440,
    "Redmi K30 Ultra": 280,
    "Redmi K30S": 370,
    "Redmi K40": 310,
    "Redmi K40 PRO": 400,
    "Redmi K40 Gaming": 290,
    "Black Shark 3": 550,
    "Black Shark 3 Pro": 830,
    "Black Shark 3S": 670,
    "Black Shark 4": 580,
    "Black Shark 4S": 400,
    "Black Shark 4S Pro": 720,
    "MI 10": 900,
    "MI 10 Lite": 300,
    "MI 10 Pro": 950,
    "MI 10 Ultra": 720,
    "MI 10 Youth": 400,
    "MI 10T": 560,
    "MI 10T Lite": 340,
    "MI 10T Pro": 560,
    "Note 10 Lite": 300,
    "MI 11": 720,
    "11T": 560,
    "11T Pro": 730,
    "MI 11 Lite": 340,
    "MI 11 Pro": 830,
    "MI 11 Ultra": 1300,
    "POCO C3": 90,
    "POCO F2 Pro": 450,
    "POCO F3": 350,
    "POCO F3 GT": 340,
    "POCO M2": 150,
    "POCO M2 Pro": 190,
    "POCO M3": 230,
    "POCO M3 Pro": 290,
    "POCO X2": 230,
    "POCO X3": 230,
    "POCO X3 NFC": 230,
    "POCO X3 GT": 390,
    "POCO X3 Pro": 230,
    "Mi 12": 570,
    "Mi 12 Pro": 730,
    "Mi 12X": 500,
    "Mix Fold": 1450,
    "Mix 3": 630,
    "Mix 4": 740,
    "Galaxy A01": 110,
    "Galaxy A02s": 150,
    "Galaxy A03s": 150,
    "Galaxy A10": 140,
    "Galaxy A10s": 140,
    "Galaxy A11": 180,
    "Galaxy A12": 170,
    "Galaxy A20": 230,
    "Galaxy A20s": 170,
    "Galaxy 21": 220,
    "Galaxy A21s": 220,
    "Galaxy A22": 220,
    "Galaxy A30": 280,
    "Galaxy A30s": 340,
    "Galaxy A31": 250,
    "Galaxy A40": 250,
    "Galaxy A41": 340,
    "Galaxy A42 5G": 400,
    "Galaxy A50": 280,
    "Galaxy A50s": 440,
    "Galaxy A51": 280,
    "Galaxy A51 5G": 500,
    "Galaxy A52": 380,
    "Galaxy A70": 370,
    "Galaxy A70s": 430,
    "Galaxy A71": 450,
    "Galaxy A71 5G": 474,
    "Galaxy A72": 450,
    "Galaxy A73": 450,
    "Galaxy Fold": 1950,
    "Galaxy Z Fold2 5G": 2225,
    "Galaxy Z Fold3 5G": 1799,
    "Galaxy Note 10": 1050,
    "Galaxy Note 10+": 1250,
    "Galaxy Note 10 Lite": 670,
    "Galaxy Note 20": 1050,
    "Galaxy Note 20 Ultra": 1390,
    "Galaxy S10": 1040,
    "Galaxy S10+": 1170,
    "Galaxy S10e": 870,
    "Galaxy S10 Lite": 730,
    "Galaxy S20 5G": 1000,
    "Galaxy S20 FE": 500,
    "Galaxy S20 Ultra 5G": 1500,
    "Galaxy S20+ 5G": 1200,
    "Galaxy S21 5G": 800,
    "Galaxy S21+ 5G": 970,
    "Galaxy S21 Ultra 5G": 960,
    "Galaxy S21 FE 5G": 840,
    "Galaxy S22+ 5G": 1000,
    "Galaxy S22 Ultra 5G": 1200,
    "Galaxy S22 5G": 800,
    "Galaxy Z Flip": 1670,
    "Galaxy Z Flip 3": 1000,
    "Google Pixel 4": 840,
    "Google Pixel 4 XL": 1000,
    "Google Pixel 4a": 380,
    "Google Pixel 5": 780,
    "Google Pixel 5a 5G": 630,
    "Google Pixel 6": 730,
    "Google Pixel 6 Pro": 1000,
    "iPhone 6": 400,
    "iPhone 6 Plus": 470,
    "iPhone 6S": 560,
    "iPhone 6S PLUS": 520,
    "iPhone 7": 620,
    "iPhone7 PLUS": 780,
    "iPhone SE": 340,
    "iPhone SE (2020)": 540,
    "iPhone 8": 780,
    "iPhone 8 Plus": 860,
    "iPhone X": 1120,
    "iPhone XR": 950,
    "iPhone XS": 1280,
    "iPhone XS Max": 1390,
    "iPhone 11": 890,
    "iPhone 11 Pro": 1280,
    "iPhone 11 Pro Max": 1390,
    "iPhone 12": 980,
    "iPhone 12 mini": 770,
    "iPhone 12 Pro": 1250,
    "iPhone 12 Pro Max": 1360,
    "iPhone 13": 1000,
    "iPhone 13 mini": 890,
    "iPhone 13 Pro": 1280,
    "iPhone 13 Pro Max": 1390
}


def get_price(name, amount):
    narx = price[name]
    return int(narx) * int(amount)
