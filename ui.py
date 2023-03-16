def show_menu():
    print('''
    \tCSV MANAGER
    1. создать .csv
    2. поиск элемента в файле
    3. сортировка данных
    4. добавление данных в файл
    5. удаление данных из файла
    6. добавление элементов в группу
    7. вывести файл
    ''')
def choice_menu():
    try:
        choice = int(input("введите номер пункта: "))
        if 1>choice or choice>7:
            raise ValueError("не корректные данные")
        else: return choice
    except Exception:
        raise ValueError("не корректные данные")

def show_data(input_str):
    for i in input_str.split('\n'):
        for j in i.split(';'):
            print(j, end="\t\t\t")
        print()

