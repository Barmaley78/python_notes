import datetime
import csv
import os.path

def create_notes_file(path):
    with open(path, 'w') as file:
        csv.writer(file)

def notes_file_exist(path):
    return not os.path.exists(path)

def notes_file_read(path):
    notes = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            notes.append(i)
    return notes

def add_note(path):
    note_name = input("Введите название заметки ")
    note_text = input("Введите содержание заметки ")
    id = 1
    if os.stat(path).st_size > 0:
        with open(path, 'r') as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader:
                if int(i[0] > id): id = int(i[0]) + 1
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        note = []
        note.append(id)
        note.append(note_name)
        note.append(note_text)
        note.append(datetime.datetime.now().strftime("%H:%M:%S"))
        note.append(datetime.date.today().strftime("%d %b %Y"))
        writer.writerow(note)