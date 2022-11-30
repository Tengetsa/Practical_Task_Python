def start_menu():
    """
    Меню выбора действия
    :return: None
    """
    print('\n'
          'Выберите пункт меню: \n'
          "1 - новая запись;\n"
          "2 - вывод всего справочника в терминал;\n"
          "3 - экспорт справочника;\n"
          "4 - импорт справочника; \n"
          "5 - выход из программы")


def surname():
    return input('Фамилия: ')


def name():
    return input('Имя: ')


def tel_number():
    return input('Номер телефона: ')


def description():
    return input('Описание: ')


def menu_selection():
    return input('Выберите пункт меню: ')


def menu_export():
    print('\n'
          'Выбор экспорта: \n'
          "1 - Экспорта в файл csv;\n"
          "2 - Экспорта в файл txt; \n"
          "3 - Возврат в меню")


def menu_import():
    print('\n'
          'Выбор экспорта: \n'
          "1 - Импорт из файла csv;\n"
          "2 - Импорт из файла txt; \n"
          "3 - Возврат в меню")


def file_name():
    return input('Введите имя файла: ')


def data_output(data):
    print(data)


def input_error():
    print('Некорректно ввели')