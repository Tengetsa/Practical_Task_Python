def start_menu():
    """
    Стартовое меню
    :return: None
    """
    print(f'\n'
          'Выбор \n'
          '1. Создать \n'
          '2. Считать \n'
          '3. Считать по id \n'
          '4. Удалить \n'
          '5. Экспорт по id \n'
          '6. Экспорт \n'
          '7. Импорт по id\n'
          '8. Импорт \n'
          '9. Выход \n'
          )


def new_id():
    """
    ввод id
    :return: None
    """
    return int(input('Введите id: '))


def new_rec():
    """
    Ввод данных
    """
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя:')
    group = input('Введите группу: ')
    return lastname, firstname, group


def choice_menu():
    return input("Выберите пункт меню: ")


def read(db):
    """
    Чтение базы данных
    :param db: база данных
    :return: печать db
    """
    return print(db)


def file_name():
    return input('Введите имя файла: ') + '.csv'


def input_error():
    print('Некорректно ввели')
