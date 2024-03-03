import Lib


# Программа
while True:
    print("\nМеню:")
    print("1. Создать заметку")
    print("2. Показать список всех заметок")
    print("3. Поиск заметки")
    print("4. Удаление заметки")
    print("5. Редактирование заметки")
    print("6. Выборка заметок за конкретную дату")
    #print("7. Просмотр заметки")
    print("7. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        Lib.create_note()
    elif choice == "2":
        Lib.list_notes()
    elif choice == "3":
        note_title = input("Введите заголовок заметки : ")
        Lib.search_note(note_title)
        while True:
            command = input('Хотите посмотреть заметку y/n: ')
            command = command.lower()
            if command == 'y':
                note_id = int(input("Выберите id заметки которую хотите посмотреть: "))
                Lib.review_notes(note_title, note_id)
                break
            elif command == "n" :
                break
    elif choice == "4":
        note_title = input("Введите название заметки для удаления: ")
        Lib.search_note(note_title)
        note_id = int(input("Выберите id заметки которую хотите удалить: "))
        Lib.delete_note(note_id)
    elif choice == "5":
        note_title = input("Введите название заметки для редактирования: ")
        Lib.search_note(note_title)
        note_id = int(input("Выберите id заметки которую хотите отредактировать: "))
        Lib.edit_note(note_id)
    elif choice == "6":
        current_date = input("За какую дату хотите посмотреть заметки: ")
        Lib.view_notes(current_date)
    elif choice == "7":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")