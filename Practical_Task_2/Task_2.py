# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input('Введите чилсо N: '))
number = 1

for i in range(n):
    i += 1
    number *= i
    print(f'{num}', end=' ')

# Изначальный вариант
# x = 1
# while number <= n:
#     x *= number
#     print(f'{x}', end=' ')
#     number += 1