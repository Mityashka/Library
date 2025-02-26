# 📚 Library

## 🚀 Для запуска
1. Подтяните зависимости: `pip install -r requirements.txt`
2. Создайте свою базу данных PostgreSQL через pgAdmin или командой sql`CREATE DATABASE library`
3. Введите корректные данные в `configs.py`
4. Запустите файл `main.py`

## 📖 Библиотека, которая содержит функции:
1. **Добавление книги (add_book)**: Пользователь вводит `title`, `author` и `year`, после чего книга добавляется в библиотеку с уникальным `id` и статусом “в наличии”. 📗
2. **Удаление книги (delete_book)**: Пользователь вводит `id` книги, которую нужно удалить. 🗑️
3. **Поиск книги (search_book)**: Пользователь может искать книги по `title`, `author` или `year`. 🔍
4. **Отображение всех книг (show_all_books)**: Приложение выводит список всех книг с их `id`, `title`, `author`, `year` и `status`. 📋
5. **Изменение статуса книги (change_book_status)**: Пользователь вводит `id` книги и новый статус (“в наличии” или “выдана”). 🔄