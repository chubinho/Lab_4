from book_collection import BookCollection
from index_dict import IndexDict
from book import Book


class Library:
    def __init__(self) -> None:
        self.books: BookCollection = BookCollection()
        self.index: IndexDict = IndexDict()

    def add_book(self, book: Book) -> None:
        if book.isbn in self.index.ISBN:
            return
        self.books.append(book)
        self.index.add_book(book)

    def remove_book(self, isbn: str) -> None:
        try:
            book = self.index[isbn]
            self.index.remove_book(book)

            for i, b in enumerate(self.books):
                if b.isbn == isbn:
                    del self.books[i]
                    break
        except KeyError:
            print("Книга не найдена")

    def find_by_isbn(self, isbn: str) -> Book:
        return self.index[isbn]

    def find_by_author(self, author: str) -> list[Book]:
        return self.index[author]

    def find_by_year(self, year: int) -> list[Book]:
        return self.index[year]

    def find_by_genre(self, genre: str):
        return [book for book in self.books if book.genre == genre]
