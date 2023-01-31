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
    }

]


def show_books():
    if not library:
        print("В библиотеке книг нет")
        return

    for num, book in enumerate(library, 1):
        """
        выводит на экран все книги: номер, автора , год, название.
        """
        print(f"номер на полке:, {num}")
        print(f"название:, {book['название']}")
        print(f"автор:, {book['автор']}")
        print(f"год:, {book['год']}")
        print(f"")


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
       print("Вводите цифры!")
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
    print(f"книга {library['название']} успешно добавлена ")

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
    

def search_by_number():
    """
    выводит книгу на экран,если она нашлась по порядковому номеру
    """
    if not library:
        print("В библиотеке книг нет!")
        return

    num = input("введите порядковый номер книги для поиска её в библиотеке: ")

    if num.isdigit():
       num = int(num)
    else:
       print("Вводите номер который больше нуля!")
       return

    idx = num - 1

    if idx < 0 or idx >= len(library):
        print("нет книги с таким номером!")
        return

    print(f"номер на полке:, {num}")
    print(f"название:, {library[idx]['название']}")
    print(f"автор:, {library[idx]['автор']}")
    print(f"год:, {library[idx]['год']}")
    print(f"")



def search_by_title():
    if not library:
        print("В библиотеке книг нет!")
        return
show_books()
search_by_number()
