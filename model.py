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
    with open(path) as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            notes.append("Список заметок пуст")
    return notes