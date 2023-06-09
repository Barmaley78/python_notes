import datetime
import csv
import os.path
from view import *

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
                if int(i[0]) >= id : id = int(i[0]) + 1
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        note = []
        note.append(id)
        note.append(note_name)
        note.append(note_text)
        note.append(datetime.datetime.now().strftime("%H:%M:%S"))
        note.append(datetime.date.today().strftime("%d.%m.%Y"))
        writer.writerow(note)

def read_note(path, id):
    note = []
    if os.stat(path).st_size > 0:
        with open(path, 'r') as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader:
                if int(i[0]) == id: 
                    note = i
    else:
        print("нет ни одной заметки")
    print_note(note)
    print()
    
def delete_note(path, id):
    notes = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            if int(i[0]) != id: notes.append(i)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for i in notes:
            writer.writerow(i)
        
def edit_note(path, id):
    notes = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            if int(i[0]) == id: 
                print("Заголовок заметки: " + i[1] + " если хотите изменить, введите новое значение или нажмине Enter")
                temp_title = input()
                if temp_title != '': i[1] = temp_title
                print("Текст заметки: " + i[2] + " если хотите изменить, введите новое значение или нажмине Enter")
                temp_text = input()
                if temp_text != '': i[2] = temp_text
                i[3] = datetime.datetime.now().strftime("%H:%M:%S")
                i[4] = datetime.date.today().strftime("%d %b %Y")
            notes.append(i)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for i in notes:
            writer.writerow(i)

def filter_by_date(path, date):
    notes = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            if i[4] == date:
                notes.append(i)
    return notes
