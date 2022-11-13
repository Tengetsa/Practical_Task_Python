# (Усложненное). Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# Выделите необходимые действия, этапы алгоритма. Посмотрите какие из них уже решены в предыдущей задаче.
# Оформите необходимые функции в виде модуля и импортируйте.
# Примечание Многочлены в файлах могут быть разной степени


from random import randint

from function_forming_polynom import coefficients_polynomial_list
from function_forming_polynom import Print_power_equation

length = randint(1, 2)
max_coeffs = 100
coeffs = coefficients_polynomial_list(length + 1, max_coeffs)

first_coeffs_section = Print_power_equation(coeffs)
print(f'{first_coeffs_section} {coeffs}')

length = randint(1, 5)
coeffs = coefficients_polynomial_list(length + 1, max_coeffs)

second_coeffs_section = Print_power_equation(coeffs)
print(f'{second_coeffs_section} {coeffs}')

first_file = 'First_coeffs_section.txt'
with open(first_file, 'w') as data:
    data.writelines(first_coeffs_section)

second_file = 'Second_coeffs_section.txt'
with open(second_file, 'w') as data:
    data.writelines(second_coeffs_section)

