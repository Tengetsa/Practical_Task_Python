# 1. Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста

delete_text = 'абв'

def read_data(filename: str) -> list:
    with open(filename, mode = "r", encoding = "utf-8") as data:
        text = data.read().split()
        return text

text = read_data("my_file.txt")
print(f'{text}')

new_txt =' '.join([i for i in text if not delete_text in i])
print(f'{new_txt}'  )
