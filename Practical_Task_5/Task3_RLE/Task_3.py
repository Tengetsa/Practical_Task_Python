# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:    ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
#            WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

def data_compression(initial_data):
    compression = ''
    count = 1
    if not initial_data:
        return ''
    for i in range(1, len(initial_data)):
        if initial_data[i] == initial_data[i - 1]:
            count += 1
        else :
            compression += str(count) + initial_data[i - 1]
            count = 1
    else:
        compression += str(count) + initial_data[i - 1]
    return compression

def data_recovery(data_output):
    recovery = ''
    count = ''
    for i in data_output:
        if i.isdigit():
            count += i
        else :
            temp = int(count) * i
            recovery += temp
            count = ''
    return recovery

def write_file(value, file):
    with open (file, 'w') as data:
        data.writelines(value)

initial_file = 'Initial_data.txt'
initial_data = ''
with open (initial_file, 'r') as data:
    initial_data = data.read()
print(f'Исходные данные: {initial_data}')

compression = data_compression(initial_data)
print(f'Данные в сжатом виде: {compression}')
compression_file = 'Data_compression.txt'
write_file(compression, compression_file)

recovery = data_recovery(compression)
recovery_file = 'Data_recovery.txt'
write_file(recovery, recovery_file)
print(f'Востоновление данных {recovery}')

