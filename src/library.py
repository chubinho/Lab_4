from src.book_collection import BookCollection
from src.index_dict import IndexDict
from src.book import Book


class Library:
    def __init__(self) -> None:
        self.books: BookCollection = BookCollection()
        self.index: IndexDict = IndexDict()

    def add_book(self, book: Book) -> None:
        """
        Добавление книги как в BookCollection
        так и  в словарную коллекцию
        IndexDict
        Если книга существует, то дубликат не добавляется
        """
        if book.isbn in self.index.ISBN:
            return
        self.books.append(book)
        self.index.add_book(book)

    def remove_book(self, isbn: str) -> None:
        """
        Удаление книги из BookCollection
        и IndexDict
        """
        try:
            book: Book = self.index[isbn]
            self.index.remove_book(book)

            for i, b in enumerate(self.books):
                if b.isbn == isbn:
                    del self.books[i]
                    break
        except KeyError:
            print("Книга не найдена")

    def find_by_isbn(self, isbn: str) -> Book:
        """Поиск книги по isbn"""
        book: Book = self.index[isbn]
        return book

    def find_by_author(self, author: str) -> list[Book]:
        """Поиск книги по автору"""
        books: list[Book] = self.index[author]
        return books

    def find_by_year(self, year: int) -> list[Book]:
        """Поиск книги по дате выпуска"""
        books: list[Book] = self.index[year]
        return books

    def find_by_genre(self, genre: str):
        """Поиск книги по жанру"""
        return [book for book in self.books if book.genre == genre]
