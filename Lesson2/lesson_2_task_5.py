# Месяц — сезон

def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Такого месяца не существует"


# Примеры использования функции
print(month_to_season(2))   # Зима
print(month_to_season(4))   # Весна
print(month_to_season(7))   # Лето
print(month_to_season(10))  # Осень
print(month_to_season(13))  # Такого месяца не существует
