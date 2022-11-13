# import math
from math import sqrt

point_list = []
for i in range(4):
    point_list.append(int(input('Введите координаты точек: ')))

distance = sqrt((point_list[2] - point_list[0])**2 + (point_list[3] - point_list[1])**2)
print(round((distance), 2))