import json
import os
from datetime import datetime
import datetime
import secrets



# Функция для создания новой заметки
def create_note():
    print(f" \n")
    notes = load_notes()
    new_note = {}
    new_note["id"] = secrets.randbelow(10000)
    new_note["title"] = input("Введите заголовок заметки: ")
    new_note["title"] = new_note["title"].lower()
    new_note["body"] = input("Введите текст заметки: ")
    new_note["body"] = new_note["body"].lower()
    new_note["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно создана!")
    
# Функция для загрузки списка заметок
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

# Функция для сохранения списка заметок
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


# Функция для вывода списка всех заметок
def list_notes():
    print(f" \n")
    notes = load_notes()
    for note in notes:
        print(f"{note['id']}. {note['title']} - {note['date']}")


# Функция для редактирования заметки
def edit_note(note_id):
    print(f" \n")
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["title"] = note["title"].lower()
            note["body"] = input("Введите новый текст заметки: ")
            note["body"] = note["body"].lower()
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с таким id не найдена.")


# Функция для удаления заметки
def delete_note(note_id):
    print(f" \n")
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена!")

    
# Функция поиска заметки по названию
def search_note(note_title):
    print(f" \n")
    notes = load_notes()
    note_found = False
    for note in notes:
        if note["title"] == note_title:
            print(f"id: {note['id']}\nЗаголовок: {note['title']}\nСоздана: {note['date']}\n")
            note_found = True
    if not note_found:
        print("Заметка с таким названием не найдена.")
        
# Функция выборки заметок за конкретную дату
def view_notes(current_date):
    print(f" \n")
    notes = load_notes()
    current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d').date()
    found_notes = False
    for note in notes:
        date_of_creation = datetime.datetime.strptime(note['date'], '%Y-%m-%d').date()
        if current_date == date_of_creation:
            print(f"id: {note['id']}\nЗаголовок: {note['title']}\nСодержание: {note['body']}\nСоздана: {note['date']}\n")
            found_notes = True
    if not found_notes:
        print("Заметок за выбранную дату нет!")
        
def review_notes(note_title, note_id):
    print(f" \n")
    notes = load_notes()
    note_found = False
    for note in notes:
        if note["title"] == note_title and note["id"] == note_id:
            print(f"id: {note['id']}\nЗаголовок: {note['title']}\nСодержание: {note['body']}\nСоздана: {note['date']}\n")
            note_found = True
            input('Для возврата в основное меню нажмите Enter')
    if not note_found:
        print("Заметка с таким названием не найдена.")