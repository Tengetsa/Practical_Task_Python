# 4. Задайте список из элементов, заполненных числами из промежутка [-N, N]. Задайте два числа - позиции(индексы) 
# в исходном списке это границы диапазона. Найдите произведение элементов списка в указанном диапазоне индексов
# Пример: N = 6 , Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5 ,    Произведение для [4, 1, 4, 1] равно 16
# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть, что они могут быть некорректными: 
# больше длины списка, меньше нуля, первый больше второго и т.п.

from random import randint

length_n = int(input('Задайте длину списка: '))
n = int(input('Введите число N: '))
n_list = []

for i in range(length_n):
    n_list.append(randint(-n, n))
print(n_list)

index_position_min = int(input('Задайте минимальную позицию (индекса): '))
index_position_max = int(input('Задайте максимальную позицию (индекса): '))
composition_element = 1
index_position_one = 0
s_list = []

if index_position_one > index_position_min:
    print('Некорректно задан диапазон индексов')
elif index_position_max > length_n:
    print('Некорректно задан диапазон индексов')
elif index_position_min > index_position_max:
    print('Некорректно задан диапазон индексов')
else:
    for item in range(length_n):
        if item >= index_position_min and item <= index_position_max:
            s_list.append(n_list[item])
            composition_element *= n_list[item]
    print(f'{s_list} = {composition_element}')
