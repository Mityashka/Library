from dbcontroller import connect


def main():
    while True:
        print("Управление библиотекой\n"
              "1 - Добавление книги\n"
              "2 - Удаление книги\n"
              "3 - Поиск книги\n"
              "4 - Отображение всех книг\n"
              "5 - Изменение статуса книги\n"
              "6 - Закрыть программу\n")
        user_input = input("Введите цифру действия: ")
        if not user_input.isdigit():
            print(f"\nНекорректный ввод\n")
            continue
        user_input = int(user_input)
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
        elif user_input == 6:
            break
        else:
            print('\nНесуществующее действие!!!\n')
            continue


def add_book():
    connection, cursor = connect()
    title = (input("Введите название книги: ")).lower()
    author = (input("Введите автора книги: ")).lower()
    while True:
        year = input("Введите год книги: ")
        if year.isdigit():
            year = int(year)
            break
        else:
            print("\nДолжно быть целое число")
    status = "в наличии"
    book = (title, author, year, status)
    print(type(book))
    try:
        cursor.execute("INSERT INTO books (title, author, year, status) VALUES (%s, %s, %s, %s)", book)
        print("\nКнига была успешно записана\n")
    except Exception as er:
        print(f"Ошибка при добавлении книги - {er}")
    finally:
        cursor.close()
        connection.close()


def delete_book():
    connection, cursor = connect()
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
        cursor.execute("DELETE FROM books WHERE book_id = %s", (user_input_id,))
        if cursor.rowcount > 0:
            print(f"\nКнига {user_input_id} успешна удалена\n")
        else:
            print(f"\nОшибка. Книга с таким id не найдена\n")
    except Exception as er:
        print(f"\nОшибка - {er}\n")
    finally:
        cursor.close()
        connection.close()


def search_book():
    connection, cursor = connect()
    try:
        print("Введите как хотите искать книгу: ")
        search_method = int(input("1 - По названию\n"
                                  "2 - По автору\n"
                                  "3 - По году \n"
                                  "4 - Выход в меню\n"))
        found = False
        if search_method == 1:
            user_input_title = (input("Введите название книги: ")).lower()
            cursor.execute(f"SELECT * FROM books WHERE title = %s", (user_input_title, ))
            detected_book = cursor.fetchall()

            if detected_book:
                print(f"{detected_book}")
                found = True

        elif search_method == 2:
            user_input_author = (input('Введите автора книги: ')).lower()
            cursor.execute(f"SELECT * FROM books where author = %s", (user_input_author, ))
            detected_book = cursor.fetchall()
            if detected_book:
                print(f"\n{detected_book}\n")
                found = True

        elif search_method == 3:
            while True:
                user_input_year = input("Введите год: ")
                if user_input_year.isdigit():
                    user_input_year = int(user_input_year)
                    break
            cursor.execute(f"SELECT * FROM books where year = %s", (user_input_year, ))
            detected_book = cursor.fetchall()
            if detected_book:
                print(f"\n{detected_book}\n")
                found = True

        elif search_method == 4:
            main()

        else:
            print('\nНесуществующее действие!!!\n')
            main()

        if found == False:
            print("\nТакой книги нет в нашей библиотеке\n")
            main()

    except Exception as er:
        print(f"\nОшибка - {er}\n")
    finally:
        cursor.close()
        connection.close()


def show_all_books():
    connection, cursor = connect()
    try:
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        if result:
            print(f"\n{result}\n")
        else:
            print(f"\nБаза данных пуста\n")
    except Exception as er:
        print(f"\nОшибка - {er}\n")
    finally:
        cursor.close()
        connection.close()

def change_book_status():
    connection, cursor = connect()
    while True:
        user_input_id = input("Введите ID книги, статус которой надо поменять (используйте exit для выхода): ")
        if user_input_id == "exit":
            main()
        elif user_input_id.isdigit():
            user_input_id = int(user_input_id)
            break
        print("ID должен быть целым числом\n")

    try:
        cursor.execute("SELECT * FROM books WHERE book_id = %s", (user_input_id,))
        if cursor.rowcount == 0:
            print("\nТакой книги не найдено\n")
            main()
        else:
            user_input_status = (input("Введите новый статус(в наличии/выдана): ")).lower()
            if user_input_status != "в наличии" and user_input_status != "выдана":
                print("\nТакого статуса не может быть\n")
                main()
            else:
                cursor.execute(f"UPDATE books SET status = %s WHERE book_id = %s", (user_input_status, user_input_id))
                print(f"\nСтатус книги {user_input_id} успешно изменен\n")
    except Exception as er:
        print(f"\nОшибка - {er}\n")
    finally:
        cursor.close()
        connection.close()
