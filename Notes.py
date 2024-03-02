import Lib


# Программа
while True:
    print("\nМеню:")
    print("1. Создать заметку")
    print("2. Показать список всех заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        Lib.create_note()
    elif choice == "2":
        Lib.list_notes()
    elif choice == "3":
        note_id = int(input("Введите id заметки для редактирования: "))
        Lib.edit_note(note_id)
    elif choice == "4":
        note_id = int(input("Введите id заметки для удаления: "))
        Lib.delete_note(note_id)
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")