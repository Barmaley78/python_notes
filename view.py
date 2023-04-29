def print_menu():
    print("Введите  команду ")
    print("1 - Добавить заметку ")
    print("2 - Получить список заметок ")
    print("3 - Прочитать заметку ")
    print("4 - Отредактировать заметку ")
    print("5 - Удалить заметку ")
    print("0 - Завершение работы ")
    print()

def print_comand_not_exist():
    print("Команды с введенным номером не существует")
    print()

def print_note_not_exist():
    print("Заметки с введенным номером не существует")
    print()

def print_note_in_list(note):
    print(str(note[0]) + ' ' + note[1] + ' ' + str(note[3]) + ' ' + str(note[4]))

def print_note(note):
    print("--- Start of message ---")
    print("ID: " + note[0])
    print("Заголовок заметки: " + note[1])
    print("Текст заметки: " + note[2])
    print("Время изменения заметки: " + note[3])
    print("Дата изменения заметки: " + note[4])
    print("--- End of message ---")
    print()