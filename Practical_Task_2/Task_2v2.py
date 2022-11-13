# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

n = int(input('Введите чилсо N: '))

# for i in range(n):
#     i += 1
#     print(f'{math.factorial(i)}', end= " ")


def fartorial(n):
    for i in range(n):
        i += 1
        n_list.append(math.factorial(i))
    return n_list
    
n_list= []   
print(fartorial(n))
print(math.factorial(n))