# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01, 12.00]
result_list = []

for i in my_list:
    if i % 1 != 0:
        result_list.append(i % 1)
print(f'{my_list} => {round(max(result_list) - min(result_list), 2)}')
