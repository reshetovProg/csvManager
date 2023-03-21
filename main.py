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
            input()
            main()
    except Exception as ex:
        print(str(ex))
        input()
        main()

print("start program")
main()

