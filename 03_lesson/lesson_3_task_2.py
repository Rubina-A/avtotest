from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone", "+79111111111"),
    Smartphone("Samsung", "Galaxy", "+7922222222"),
    Smartphone("Xiaomi", "Redmi", "+79345678901"),
    Smartphone("Google", "Pixel", "+79456789012"),
    Smartphone("OnePlus", "11 Pro", "+79567890123"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
