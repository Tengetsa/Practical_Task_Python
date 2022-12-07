import view as v
import model as m


def start():
    global_mapping = {"lastname": "Фамилия", "firstname": "Имя", "group": "Класс"}
    db_main = dict()
    db = dict()
    while True:
        v.start_menu()
        choice = v.choice_menu()
        if choice == "1":
            db = m.update_record(db_main, v.new_id(), *(v.new_rec(), global_mapping))
        elif choice == "2":
            v.read(db)
        elif choice == "3":
            v.read(m.extract_record(db, v.new_id()))
        elif choice == "4":
            db.pop(v.new_id())
        elif choice == "5":
            m.export_csv_id(db, v.file_name())
            db.clear()
        elif choice == "6":
            m.export_csv(db, v.file_name())
        elif choice == "7":
            db = m.import_csv_id(db, v.file_name(), global_mapping)
        elif choice == "8":
            v.read(m.import_csv(v.file_name()))
        elif choice == "9":
            break
        else:
            v.input_error()