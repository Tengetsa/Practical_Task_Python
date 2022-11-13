# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите день недели: '))

if number == 1: print('Понедельник')
elif number == 2: print('Вторник')  
elif number == 3: print('Среда') 
elif number == 4: print('Четверг')
elif number == 5: print('Пятница')
elif number == 6: print('Суббота, выходной')
elif number == 7: print('Воскресенье, выходной')
else: print("Введено некорректное число")
