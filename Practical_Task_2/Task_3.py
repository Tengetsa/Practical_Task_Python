# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример: - Для n=4 [2, 2.25, 2.37, 2.44]       Сумма 9.06

n = int(input('Введите число n = '))
summa = 0
n_list = []
for i in range(n):
    i += 1
    number_n = round(float((1 + 1 / i)**i), 2)
    n_list.append(number_n)
    summa += number_n
print(n_list, end= ' = ')
print(summa)