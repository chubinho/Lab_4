import random
from src.book import NonFictionBook, FictionBook
from src.library import Library


titles = ["Хоббит", "Преступление и наказание",
          "Гарри Поттер и философский камень", "Краткая история времени", "Большая советская экономика"]
authors = ["Дж. Р. Р. Толкин", "Ф. М. Достоевский",
           "Дж. К. Роулинг", "Стивен Хокинг", "Алексей Сафронов"]
genres = ["Фэнтези", "Роман", "Фэнтези", "Научпоп", "Публицистика"]
years = [1937, 1866, 1997, 1988, 2025]


def generate_book():
    """
    Создание рандомной книги для дальнейшей симуляции
    """
    idx = random.randint(0, len(titles) - 1)
    title = titles[idx]
    author = authors[idx]
    genre = genres[idx]
    year = years[idx]
    isbn = f"isbn-{random.randint(1000, 9999)}"
    pages = random.randint(50, 600)

    if title == "Краткая история времени" or title == "Большая советская экономика":
        """
        Проверяем, является ли книга худ. литературой
        """
        return NonFictionBook(title, author, year, genre, isbn, pages)
    else:
        return FictionBook(title, author, year, genre, isbn, pages)


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        """
        Если seed передается, то выводится такая же
        последовательность логов
        """
        random.seed(seed)

    library = Library()
    actions = [
        "add_book",
        "remove_book",
        "search",
        "update_index",
        "try_get_book"
    ]

    for step in range(1, steps + 1):
        """
        последовательно создаем книги и выполняем рандомные действия с ними
        """
        event = random.choice(actions)
        print(f"Шаг {step}: ", end="")

        if event == "add_book":
            book = generate_book()
            library.add_book(book)
            print(f"Добавлена книга: {book}")

        elif event == "remove_book":
            if len(library.books) == 0:
                print("Нет книг для удаления")
            else:
                isbn = random.choice(list(library.index.ISBN.keys()))
                title = library.find_by_isbn(isbn).title
                library.remove_book(isbn)
                print(f'Удалена книга: "{title}"')

        elif event == "search":
            choice = random.choice(["author", "genre", "year"])
            if choice == "author" and library.index.author:
                author = random.choice(list(library.index.author.keys()))
                books = library.find_by_author(author)
                print(
                    f"Поиск по автору '{author}': найдено {len(books)} книг(и)")
            elif choice == "genre":
                genre = random.choice(genres)
                books = library.find_by_genre(genre)
                print(
                    f"Поиск по жанру '{genre}': найдено {len(books)} книг(и)")
            elif choice == "year" and library.index.year:
                year = random.choice(list(library.index.year.keys()))
                books = library.find_by_year(year)
                print(
                    f"Поиск по году {year}: найдено {len(books)} книг(и)")
            else:
                print("Поиск: нет данных")

        elif event == "update_index":
            print("Индекс синхронизирован")

        elif event == "try_get_book":
            fake_isbn = f"invalid-{random.randint(1, 9999)}"
            try:
                library.find_by_isbn(fake_isbn)
                print(
                    f"найдена несуществующая книга с ISBN {fake_isbn}")
            except KeyError:
                print(
                    f"Попытка найти несуществующую книгу (ISBN: {fake_isbn}) - не найдена")

    print("Симуляция завершена")


run_simulation()
