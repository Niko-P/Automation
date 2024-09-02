# Високосный год

def is_year_leap(year):
    if (year % 4 == 0):
        return print('Год ' + str(year) + ': True')
    else:
        return print('Год ' + str(year) + ': False')


year_to_check = int(input("Введите год для проверки: "))

is_year_leap(year_to_check)
