from Address import Address
from Mailing import Mailing


to_address = Address("222222", "Новосибирск", "Куропаткина", "10", "222")
from_address = Address("333333", "Пенза", "Пушкина", "20", "333")

mailing = Mailing(to_address, from_address, 500, "123456789")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
