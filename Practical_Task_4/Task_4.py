# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов многочлена и записать
#  в файл многочлен степени k. Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.

# Примечание Создать три функции:
# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином. Коэффициенты вычисляются случайными.
# Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
# В словаре степени будут ключами, в списке - индексами.
# Например k=3 => 6*x^3 + 4*x + 5. Словарь будет такой: {3:6, 2:0, 1:4, 0:5}. А список такой [5,4,0,6]
# 2) Функция формирование строки-полинома. Аргумент: полином (в вид словаря или списка).
# Возвращает строку вида '6*x^3 + 4*x + 5'
# Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
# Для формирования строки удобно использовать join
# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.

from random import randint

from function_forming_polynom import coefficients_polynomial_list
from function_forming_polynom import Print_power_equation

length = randint(1, 5)
max_coeffs = 100
coeffs = coefficients_polynomial_list(length + 1, max_coeffs)
print(coeffs)
first_coeff_section = Print_power_equation(coeffs)
print(first_coeff_section)

length = randint(1, 5)
coeffs = coefficients_polynomial_list(length + 1, max_coeffs)
print(coeffs)
second_coeff_section = Print_power_equation(coeffs)
print(second_coeff_section)