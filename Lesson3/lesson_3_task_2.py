from smartphone import Smartphone
catalog = []
phone_1 = Smartphone("Apple", "iPhone 8 Plus", "+79029651254")
phone_2 = Smartphone("NOKIA", "e50 without camera", "+79137238192")
phone_3 = Smartphone("Acer", "CloudMobile S500", "+79658460284")
phone_4 = Smartphone("SonyEricsson", "G700 Business Edition", "+79081053421")
phone_5 = Smartphone("Samsung", "Galaxy Note", "+79997652346")

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.number}")
