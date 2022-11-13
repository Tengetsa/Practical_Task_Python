# 1. Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200. Использовать comprehensions

length = int(input("Задайте число N: "))

# список нечетных целых чисел от 0 по N
# my_list = [i for i in range(1, length + 1) if i**2 < 200 and i%2 == 1]


# список нечетных целых чисел от 0 до N
my_list = [i for i in range(1, length, 2) if i**2 < 200]

print(my_list)

