import sys
import os
library = [
    {
    "название": "Введение в Python. Том 1",
    "автор": "Марк Лутц",
    "год": 2022
    },
    {
    "название": "Введение в Python. Том 2",
    "автор": "Марк Лутц",
    "год": 2023
    },
    {
    "название": "Введение в Python. Том 3",
    "автор": "Марк Лутц",
    "год": 2023
    }
]


def show_books():
    if not library:
        print("В библиотеке книг нет")
        return

    for book in library:
        show_book(book)
    input("нажмите энтер ")
    os.system("cls")


def show_book(book):
    print("номер на полке: ", library.index(book) + 1)
    for k, v in book.items():
        print(f"{k}: {v}")


def add_book() -> None:
    """
        добавляет уникальную книгу 
        если указаны названия год и автор
    """
    title = input("Введите название книги:")
    if not title:
       print("НЕТ НАЗВАНИЯ!")
       return

    author = input("Введите имя автора:")

    if not author:
       print("НЕТ АВТОРА!")
       return

    year = input("Введите год издания:")

    if year.isdigit():
       year = int(year)
    else:
       print("Год должен быть числом!")
       return

    book = {
    "название": title,
    "автор": author,
    "год": year,
    }
    if book in library:
       print("")
       print("такая книга уже есть!")
       print("")
       return

    library.append(book)
    print(f"книга {book['название']} успешно добавлена ")
    input("нажмите энтер ")
    os.system("cls")


def remove_book():
    """
    удаляет книгу по номеру
    """
    if not library:
        print("В библиотеке книг нет!")
        return

    num = input("введите порядковый номер книги для удаления: ")

    if num.isdigit():
       num = int(num)
    else:
       print("Вводите номер который больше нуля!")
       return

    idx = num - 1

    if idx < 0 or idx >= len(library):
        print("нет книги с таким номером!")
        return

    print(f"книга {library[idx]['название']} была успешно удалена")
    library.pop(idx)
    input("нажмите энтер ")
    os.system("cls")


def search_by_number():
    """
    выводит книгу на экран,если она нашлась по порядковому номеру
    """
    if not library:
        print("В библиотеке книг нет!")
        return

    num = input("введите порядковый номер книги для поиска её в библиотеке: ")

    if  not num.isdigit():
        print("Номер должен быть числом")
        return
    num = int(num)

    idx = num - 1

    if idx < 0:
        print("число должно быть положительным")
        return
    if idx >= len(library):
        print("нет книги с таким числом")
        return

    book = library[idx]

    print(f"номер на полке:, {num}")
    print(f"название:, {book['название']}")
    print(f"автор:, {book['автор']}")
    print(f"год:, {book['год']}")
    print(f"")
    input("нажмите энтер ")
    os.system("cls")

def search_book_by_key(user_key: str) -> None:
    """
    показывает на экране книгу если находит ее по порядковому номеру  
    """
    if not library:
        print("В библиотеке книг нет!")
        return

    user_value = input(f"введите {user_key}: ")

    if not user_value:
        print("нет данных для поиска")
        return
    if user_key == "год":
        if user_value.isdigit():
            user_value = int(user_value)

    if "название" or "год" or "автор" >= len(library):
        print("нет такой книги :(")
        return

    for book in library:
        if book[user_key] == user_value:
            show_book(book)

    input("нажмите энтер ")
    os.system("cls")


def close_library() -> None:
    """
    закрывает программу
    """
    print("Программа завершена. До скорых встречь!")
    sys.exit()

def show_menu():
    while True:
        options = [
            ("Показать все книги", lambda: show_books()),
            ("Добавить книгу", lambda: add_book()),
            ("Удалить книгу", lambda: remove_book()),
            ("Найти книгу по порядковому номеру на полке", lambda: search_by_number()),
            ("Найти книгу по названию", lambda: search_book_by_key('название')),
            ("Найти книгу по году", lambda: search_book_by_key('год')),
            ("Найти книгу по автору", lambda: search_book_by_key('автор')),
            ("Bыйти", lambda: close_library()),
        ]

        for i, option in enumerate(options, start=1):
            print(i, option[0])
        option_num = input("введите номер варианта и нажмите энтер ")
        idx = int(option_num) - 1
        options[idx][1]()
        

show_menu()
