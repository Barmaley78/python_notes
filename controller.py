from  model import *
from view import *

def app():
    command_number = 10
    if notes_file_exist("notes.csv"):
        create_notes_file("notes.csv")
    
    
    while command_number != 0:
        print_menu()
        command_number = int(input())
        match command_number:
            case 1:
                notes = notes_file_read("notes.csv")
                if len(notes) != 0:
                    for i in notes:
                        print(i)
                else:
                    print("Список заметок пуст")
            case 2:
                print(2)
            case 3:
                print(3)
            case 4:
                print(4)
            case 5:
                print(5)
            case 0:
                break
            case _:
                print_comand_not_exist()