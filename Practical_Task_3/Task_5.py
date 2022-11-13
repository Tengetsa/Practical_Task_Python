# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def nega_fibonacci(n):
    if n == 1: return 1                    
    elif n == 2: return -1                      
    else:
        a, b = 1, -1
        for i in range(2, n):
            a, b = b, a - b
        return b

my_list = [0]
k = int(input('Введите число: '))

for y in range(1, k + 1):
    my_list.append(fibonacci(y))
    my_list.insert(0, nega_fibonacci(y))
print(my_list)
