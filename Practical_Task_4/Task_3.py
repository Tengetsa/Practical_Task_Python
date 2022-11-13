# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from random import randint

def random_list(size_list,n, m):
    return [randint(n, m) for i in range(size_list)]

def non_recurring_list(origin):
    return [i for i in set(origin)]

size_list = 15
min_number = 1
max_number = 20

my_list = random_list(size_list, min_number, max_number)
print(my_list)
print(non_recurring_list(my_list))