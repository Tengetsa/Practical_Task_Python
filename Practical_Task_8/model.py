import csv


def update_record(db: dict, rec_id: int, data1: list, mapping: dict):
    """
    Создание и обновление словарь словарей
    :param db: база данных
    :param rec_id: increment
    :param data: данные ученика
    :param mapping: отображение данных
    :return: словарь словарей
    """
    db[rec_id] = {name: value for name, value in zip(mapping.keys(), data1)}
    return db


def delete_id(db: dict, id: int):
    """
    Удаление записи по id
    :param db: база данных
    :param id: id студента которого нужно удалить
    :return: обновлённая база данных
    """
    db.pop(id)
    return db


def extract_record(db: dict, id: int):
    """
    Извлечение по id
    :param db:
    :param id:
    :return:
    """
    record = db[id]
    return record



def export_csv_id(data: dict, filename: str):
    """
    Запись данных в файл csv с id
    :param data: данные
    :param filename: имя файла
    :return:
    """
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter="#")
        for key, value in data.items():
            rec = []
            rec.append(key)
            for item in value.values():
                rec.append(item)
            file_writer.writerow(rec)


def export_csv(db: dict, filename: str, delimiter='#'):
    """
    Запись данных в файл csv без id
    :param db: данные
    :param filename: имя файла
    :param delimiter: делитель
    :return:
    """
    with open(filename, mode='a', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter="#")
        for key, value in db.items():
            rec = []
            for v in value.values():
                rec.append(v)
            file_writer.writerow(rec)


def import_csv_id(db: dict, file_name: str, mapping, delimiter="#"):
    """
    Импорт данных с id
    :param db: база данных
    :param file_name: имя файла
    :param delimiter: делитель
    :return:
    """
    with open(file_name, mode='r', encoding='utf-8') as file:
        rec = []
        for data in file:
            id_1, lastname, firstname, group = data.strip().split(delimiter)
            id = int(id_1)
            rec.append(lastname), rec.append(firstname), rec.append(group)
            update_record(db, id, rec, mapping)
            rec.clear()
    return db


def import_csv(file_name: str, delimiter="#"):
    """
    Импорт данных без id
    :param file_name:
    :param delimiter:
    :return:
    """
    with open(file_name, mode='r', encoding='utf-8') as file:
        rec = []
        for data in file:
            lastname, firstname, group = data.strip().split(delimiter)
            rec.append({'lastname': lastname, 'firstname': firstname, 'group': group})
    return rec

