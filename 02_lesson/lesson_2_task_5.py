def month_to_season(month):
    if not 1 <= month <= 12:
        return "Некорректный номер месяца"
    if month <= 2 or month == 12:
        return "Зима"
    elif month <= 5:
        return "Весна"
    elif month <= 8:
        return "Лето"
    else:
        return "Осень"
