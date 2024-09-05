from address import Address
from mailing import Mailing

to_address = Address("644045", "Омск", "Гагарина", "2", "13")
from_address = Address("10023", "New York", "Central Park W", "25", 3305)
mailing = Mailing(to_address, from_address, 10000, "SIMA32143244")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment}"
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
