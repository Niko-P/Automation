# Площадь квадрата

import math


def square(side):
    # Вычисляем площадь квадрата
    area = side * side

    # Округляем площадь до целого числа
    return math.ceil(area)


# Примеры использования функции
side = 6.2
result = square(side)
print(f'Площадь квадрата со стороной {side} = {result}')

side = 2
result = square(side)
print(f'Площадь квадрата со стороной {side} = {result}')

side = 11
result = square(side)
print(f'Площадь квадрата со стороной {side} = {result}')

side = 3.3
result = square(side)
print(f'Площадь квадрата со стороной {side} = {result}')
