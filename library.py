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
def show_options(options):
    for num, option in enumerate(options):
        print(f"{num}. {option}")

def visit_hub():
    text = "вы на главной странице библиотеки "
    options = [
        "показать книги",
        "добавить книгу в библиотеку",
        "удалить книгу",
        "найти книгу по номеру",
        "найти книгу по автору, году, названию"
        ]
    print("")
    print(text)
    show_options(options)
    if options == 1:
        return show_books()
    elif options == 2:
        return add_book()
    elif options == 3:
        return remove_book()
    elif options == 4:
        return search_by_number()
    elif options == 5:
        return search_book_by_key(user_key)
    else:
        print("нет такого варианта")
    input("\n нажмите энтер для продолжения")


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

    for book in library:
        if book[user_key] == user_value:
            print(f"номер на полке:, {library.index(book) + 1}")
            print(f"название:, {book['название']}")
            print(f"автор:, {book['автор']}")
            print(f"год:, {book['год']}")
            print(f"")
        

visit_hub()
