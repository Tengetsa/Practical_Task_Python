def dict_data(surname: str, name: str, tel: str, desc: str) -> dict:
    """
    Создаём словарь данных
    :param surname: фамилия
    :param name: имя
    :param tel: телефон
    :param desc: описание
    :return: Словарь данных
    """
    return {'surname': surname, 'name': name, 'tel': tel, 'desc': desc}


def export_csv_file(data: dict, filename: str, delimiter=","):
    """
    Запись данных в файл csv
    :param data: данные
    :param filename: имя файла
    :param delimiter: делитель
    :return:
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        for rec in data:
            file.write(delimiter.join(rec.values()))
            file.write(f'\n')


def import_csv_file(filename: str, delimiter=","):
    """
    Извлекаем данные из файла csv
    :param filename: имя файла
    :param delimiter: делитель
    :return:
    """
    temp = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for data in file:
            surname, name, tel, desc = data.strip().split(delimiter)
            temp.append({'surname': surname, 'name': name, 'tel': tel, 'desc': desc})

    return temp


def export_txt_file(data: dict, filename: str, delimiter=f'\n'):
    """
    Запись данных в файл txt
    :param data: данные
    :param filename: имя файла
    :param delimiter: делитель
    :return:
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        for rec in data:
            file.write(delimiter.join(rec.values()))
            file.write(delimiter)


def import_txt_file(filename: str, delimiter=','):
    """
    Извлекаем данные их файла txt
    :param filename: имя файла
    :param delimiter: делитель
    :return:
    """
    temp = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for data in file:
            temp += data.strip().split(delimiter)
    return temp


def transformations(temp: list):
    """
    Преобразовываем из списка в список словарей
    :param temp: список
    :return: список словарей
    """
    i = 0
    keeping = []
    data = []
    data1 = ['surname', 'name', 'tel', 'desc']
    while len(temp) > i:
        keeping.append(temp[i])
        keeping.append(temp[i + 1])
        keeping.append(temp[i + 2])
        keeping.append(temp[i + 3])
        dict1 = dict(zip(data1, keeping))
        i += 4
        data.append(dict1)
        keeping.clear()
    return data