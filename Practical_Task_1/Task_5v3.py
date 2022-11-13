from math import sqrt

point_list = []
for i in range(4):
    point_list.append(int(input('Введите координаты точек: ')))

distance = sqrt((point_list[2] - point_list[0])**2 + (point_list[3] - point_list[1])**2)
print(f'Расстояние между точками с координатами {point_list[0], point_list[1]}, {point_list[2], point_list[3]}{distance:.3f}')
#                                 .3f  указывает сколько будет знаков после точки                             {distance:.3f}
#                                17  указывает сколько ячеек должно быть перед точкой                         {distance:17.3f} 