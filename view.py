def print_menu():
    print("Введите  команду ")
    print("1 - Добавить заметку ")
    print("2 - Получить список заметок ")
    print("3 - Прочитать заметку ")
    print("4 - Отредактировать заметку ")
    print("5 - Сохранить заметку ")
    print("6 - Удалить заметку ")
    print("0 - Завершение работы ")

def print_comand_not_exist():
    print("Команды с введенным номером не существует")

def print_note_in_list(note):
    # print(note)
    print(str(note[0]) + ' ' + note[1] + ' ' + str(note[3]) + ' ' + str(note[4]))