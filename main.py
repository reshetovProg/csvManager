import os
import file
import list_function
import ui
def main():
    os.system('cls')
    ui.show_menu()
    try:
        choice = ui.choice_menu()
        print(choice)
        if choice==7:
            ui.show_data(file.read_file('data.csv'))
        elif choice==2:
            category=ui.show_category('data.csv')
            element=input("введение значение для поиска: ")
            list = list_function.search_in_file('data.csv', category, element)
            ui.show_list(list)
        elif choice==4:
            list = ui.add_element('data.csv')
            file.write_line('data.csv', list)
            print("запись завершена")

        input()
        main()

    except Exception as ex:
        print(str(ex))
        input()
        main()


main()

