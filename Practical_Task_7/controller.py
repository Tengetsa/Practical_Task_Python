import view as v
import model as m


def start():
    data = []
    while True:
        v.start_menu()
        choice = v.menu_selection()
        if choice == "1":
            r = m.dict_data(v.surname(), v.name(), v.tel_number(), v.description())
            data.append(r)
        elif choice == "2":
            v.data_output(data)
        elif choice == "3":
            export(data)
            data.clear()
        elif choice == "4":
            data = import_file()
        elif choice == "5":
            break
        else:
            v.input_error()


def export(data):
    while True:
        v.menu_export()
        choice_export = v.menu_selection()
        if choice_export == "1":
            name_file = v.file_name() + '.csv'
            m.export_csv_file(data, name_file)
        elif choice_export == "2":
            name_file = v.file_name() + '.txt'
            m.export_txt_file(data, name_file)
        elif choice_export == "3":
            break


def import_file():
    while True:
        v.menu_import()
        choice_import = v.menu_selection()
        if choice_import == "1":
            name_file = v.file_name() + '.csv'
            data = m.import_csv_file(name_file)
        elif choice_import == "2":
            name_file = v.file_name() + '.txt'
            data = m.import_txt_file(name_file)
        elif choice_import == "3":
            break
        return data