# 1. Вычислить число pi c заданной точностью d. Число d находится в интервале [1e-1, 1e-10]
# Пример: - при d = 0.001, pi = 3.141.
# Примечание:
# Использовать только итерационные алгоритмы вычисления числа pi. Любой на ваш выбор.
# Написать функцию, которая принимает аргумент: точность вычисления числа pi
# Возвращает:
# 1. Вычисленное число pi
# 2. Количество выполненных итераций
# 3. Погрешность вычисления
# Пример вызова функции: - vallis(1e-4) -> (3.141392685883853, 3928, -0.00019996770594010727)

def pi_function (accuracy):
    d = 10** -accuracy
    my_pi = 3
    number = 4
    result = 1
    iterations = 0
    while d < abs(result):
        result = 4 / number / (number - 1) / (number - 2)
        if number % 4 != 0:
            result *= -1 
            iterations += 1
        my_pi += result
        number += 2
    return round(my_pi, accuracy), iterations

accuracy = int(input('Введите количество цифр после запятой, для определения числе пи: '))
my_pi = pi_function(accuracy)
iterations = my_pi[1]

from decimal import *

pi = 3.141592653589793
getcontext().prec = 10
difference_pi = Decimal(my_pi[0]) - Decimal(pi)

print(f'Пи с точностью {10 ** -accuracy}  = {my_pi[0]}')
print(f'Количество выполненных итераций {iterations}, погрешность вычисления {difference_pi}')
