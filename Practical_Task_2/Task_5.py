# 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно.

import random

n = int(input('Введите число N: '))

n_list = []
for i in range(n):
    n_list.append(random.randrange(-n, n))
print(n_list)

for i in range(len(n_list)):
    j = random.randint(0, i + 1)
    n_list[i], n_list[j] = n_list[j], n_list[i]
print(n_list)

