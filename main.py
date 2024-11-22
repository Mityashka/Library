import json
import os.path
import random

MIN_VALUE = 1
MAX_VALUE = 99999999

def main():
    while True:
        print("Управление библиотекой\n"
              "1 - Добавление книги\n"
              "2 - Удаление книги\n"
              "3 - Поиск книги\n"
              "4 - Отображение всех книг\n"
              "5 - Изменение статуса книги\n")
        user_input = int(input("Введите цифру действия: "))
        if user_input == 1:
            add_book()
        elif user_input == 2:
            delete_book()
        elif user_input == 3:
            search_book()
        elif user_input == 4:
            show_all_books()
        elif user_input == 5:
            change_book_status()
        else:
            print('\nНесуществующее действие!!!\n')
            main()


def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    while True:
        year = input("Введите год книги: ")
        if year.isdigit():
            year = int(year)
            break
        else:
            print("\nДолжно быть целое число")
    status = "в наличии"
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            try:
                books = json.load(db)
            except:
                books = []
    except FileNotFoundError:
        books = []

    used_id = [book["id"] for book in books]
    id = unique_id_generator()
    if len(books) == MAX_VALUE:
        raise Exception("База данных переполнена")
    while id in used_id:
        id = unique_id_generator()

    book = {
        "id": id,
        "title": title,
        "author": author,
        "year": year,
        "status": status,
    }
    books.append(book)

    with open("data_base.json", "w", encoding="utf-8") as db:
        json.dump(books, db, indent=4, ensure_ascii=False)
    print("\nКнига была успешно записана\n")


def delete_book():
    if not os.path.exists("data_base.json"):
        print("\nБаза данных пуста\n")
        main()
    while True:
        user_input_id = input("Введите ID книги, которую хотите удалить (для просмотра всех книг напишите show, "
                              "используйте exit для выхода): ")
        if user_input_id == "show":
            show_all_books()
        elif user_input_id == "exit":
            main()
        elif user_input_id.isdigit():
            break
        else:
            print("ID должен быть целым числом")
    user_input_id = int(user_input_id)
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
            found = False
            for book in books:
                if book["id"] == user_input_id:
                    books.remove(book)
                    with open("data_base.json", "w", encoding="utf-8") as db_eraser:
                        json.dump(books, db_eraser, ensure_ascii=False, indent=4)
                    print("\nКнига была удалена\n")
                    found = True
            if found == False:
                print("\nТакой книги не найдено\n")
    except:
        print("\nНе найдено книг в базе данных\n")


def search_book():
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
            print("Введите как хотите искать книгу: ")
            search_method = int(input("1 - По названию\n"
                                      "2 - По автору\n"
                                      "3 - По году \n"
                                      "4 - Выход в меню\n"))

            if search_method == 1:
                user_input_title = input("Введите название книги: ")
                found = False
                for book in books:
                    if book["title"] == user_input_title:
                        print(f'ID = {book["id"]}\n'
                              f'Название = {book["title"]}\n'
                              f'Автор = {book["author"]}\n'
                              f'Год = {book["year"]}\n'
                              f'Статус = {book["status"]}\n')
                        found = True
                if found == False:
                    print("\nТакой книги нет в нашей библиотеке\n")
                main()

            if search_method == 2:
                user_input_author = input('Введите автора книги: ')
                found = False
                for book in books:
                    if book["author"] == user_input_author:
                        print(f'ID = {book["id"]}\n'
                              f'Название = {book["title"]}\n'
                              f'Автор = {book["author"]}\n'
                              f'Год = {book["year"]}\n'
                              f'Статус = {book["status"]}\n')
                        found = True
                if found == False:
                    print("\nТакой книги нет в нашей библиотеке\n")
                main()

            if search_method == 3:
                while True:
                    user_input_year = input("Введите год: ")
                    if user_input_year.isdigit():
                        user_input_year = int(user_input_year)
                        break
                found = False
                for book in books:
                    if book["year"] == user_input_year:
                        print(f'ID = {book["id"]}\n'
                              f'Название = {book["title"]}\n'
                              f'Автор = {book["author"]}\n'
                              f'Год = {book["year"]}\n'
                              f'Статус = {book["status"]}\n')
                        found = True
                if found == False:
                    print("\nТакой книги нет в нашей библиотеке\n")
                main()
            elif search_method == 4:
                main()
            else:
                print('\nНесуществующее действие!!!\n')
                main()
    except:
        print("\nНе найдено книг в базе данных\n")


def show_all_books():
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
            for book in books:
                print(f'ID = {book["id"]}\n'
                      f'Название = {book["title"]}\n'
                      f'Автор = {book["author"]}\n'
                      f'Год = {book["year"]}\n'
                      f'Статус = {book["status"]}\n')
    except:
        print("\nКниг в базе данных не обнаружено\n")


def change_book_status():
    if not os.path.exists("data_base.json"):
        print("\nБаза данных пуста\n")
        main()
    while True:
        user_input_id = input("Введите ID книги, статус которой надо поменять (используйте exit для выхода): ")
        if user_input_id == "exit":
            main()
        elif user_input_id.isdigit():
            user_input_id = int(user_input_id)
            break
        print("ID должен быть целым числом\n")

    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
            found = False
            for book in books:
                if book["id"] == user_input_id:
                    user_input_status = input("Введите новый статус(в наличии/выдана): ")
                    if user_input_status != "в наличии" and user_input_status != "выдана":
                        print("\nТакого статуса не может быть\n")
                        main()
                    else:
                        with open("data_base.json", "w", encoding="utf-8") as db_status_changer:
                            book["status"] = user_input_status
                            json.dump(books, db_status_changer, ensure_ascii=False, indent=4)
                        print("\nСтатус был изменен\n")
                    found = True
            if found == False:
                print("\nТакой книги не найдено\n")
    except:
        print("\nНе найдено книг в базе данных\n")

def unique_id_generator():
    id = random.randint(MIN_VALUE, MAX_VALUE)
    return id

if __name__ == "__main__":
    main()
