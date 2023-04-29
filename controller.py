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
                add_note("notes.csv")
            case 2:
                notes = notes_file_read("notes.csv")
                if len(notes) != 0:
                    for i in notes:
                        print_note_in_list(i)
                else:
                    print("Список заметок пуст")
            case 3:
                id = int(input("Введите номер заметки для чтения "))
                read_note("notes.csv", id)
            case 4:
                id = int(input("Введите номер заметки для редактирования "))
            case 5:
                id = int(input("Введите номер заметки для удаления "))
                delete_note("notes.csv", id)
            case 0:
                break
            case _:
                print_comand_not_exist()