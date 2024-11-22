import json
import random

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
    id = random.randint(0, 99999999)
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год книги: ")
    status = "в наличии"
    book = {
        "id": id,
        "title": title,
        "author": author,
        "year": year,
        "status": status,
    }
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
    except:
        books = []
    books.append(book)

    with open("data_base.json", "w", encoding="utf-8") as db:
        json.dump(books, db, indent=4, ensure_ascii=False)
    print("\nКнига была успешно записана\n")


def delete_book():
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
            user_input_id = int(input("Введите ID книги, которую хотите удалить: "))
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
                                      "3 - По году: \n"))

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
                    if book["title"] == user_input_author:
                        print(f'ID = {book["id"]}\n'
                              f'Название = {book["title"]}\n'
                              f'Автор = {book["author"]}\n'
                              f'Год = {book["year"]}\n'
                              f'Статус = {book["status"]}\n')
                    if found == False:
                        print("\nТакой книги нет в нашей библиотеке\n")
                main()

            if search_method == 3:
                user_input_year = input("Введите год: ")
                found = False
                for book in books:
                    if book["title"] == user_input_year:
                        print(f'ID = {book["id"]}\n'
                              f'Название = {book["title"]}\n'
                              f'Автор = {book["author"]}\n'
                              f'Год = {book["year"]}\n'
                              f'Статус = {book["status"]}\n')
                    if found == False:
                        print("\nТакой книги нет в нашей библиотеке\n")
                main()
            else:
                print('\nНесуществующее действие!!!\n')
                main()
    except:
        print("Не найдено книг в базе данных\n")


def show_all_books():
    with open("data_base.json", "r", encoding="utf-8") as db:
        books = json.load(db)
        for book in books:
            print(f'ID = {book["id"]}\n'
                  f'Название = {book["title"]}\n'
                  f'Автор = {book["author"]}\n'
                  f'Год = {book["year"]}\n'
                  f'Статус = {book["status"]}\n')


def change_book_status():
    try:
        with open("data_base.json", "r", encoding="utf-8") as db:
            books = json.load(db)
            user_input_id = int(input("Введите ID книги, статус которой надо поменять: "))
            found = False
            for book in books:
                if book["id"] == user_input_id:
                    user_input_status = input("Введите новый статус(в наличии/выдана): ")
                    with open("data_base.json", "w", encoding="utf-8") as db_status_changer:
                        book["status"] = user_input_status
                        json.dump(books, db_status_changer, ensure_ascii=False, indent=4)
                    print("\nСтатус был изменен\n")
                    found = True
            if found == False:
                print("\nТакой книги не найдено\n")
    except:
        print("\nНе найдено книг в базе данных\n")


if __name__ == "__main__":
    main()
