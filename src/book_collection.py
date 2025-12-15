from typing import Union
from book import Book


class BookCollection:
    def __init__(self) -> None:
        self.books: list = []

    def __getitem__(self, index: Union[int,slice]) -> Union[Book, list[Book]]:
        if isinstance(index, int):
            return self.books[index]
        elif isinstance(index, slice):
            return self.books[index]

    def __iter__(self):
        return iter(self.books)

    def __len__(self) -> int:
        return len(self.books)

    def append(self, book: Book) -> None:
        self.books.append(book)

    def insert(self, index: int, book: Book) -> None:
        self.books.insert(index, book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def __delitem__(self, index: int) -> None:
        del self.books[index]
