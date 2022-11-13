# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];

number = int(input("Введите число: "))

def simple_number(number):
    y = 2 
    my_list = []
    natural_number = number

    while y <= number:
        if number % y == 0:
            my_list.append(y)
            number //= y
            y = 2
        else:
            y += 1
    return (my_list)

print(f"Simple_number {number}  => {simple_number(number)}")