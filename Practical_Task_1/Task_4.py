#  Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

nubmer = int(input('Введите номер четверти: '))

if nubmer < 1 or nubmer > 4:
    print('Введенно неверное число')
elif nubmer == 1:
    print('x > 0, y > 0')
elif nubmer == 2:
    print('x < 0, y > 0')
elif nubmer == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')
