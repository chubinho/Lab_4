from typing import Union
from book import Book


class IndexDict:
    def __init__(self) -> None:
        self.ISBN: dict[str, Book] = {}
        self.year: dict[int, Book] = {}
        self.author: dict[str, list[Book]] = {}
        self.genre: dict[str, list[Book]] = {}

    def add_book(self, book: Book) -> None:
        self.ISBN[book.isbn] = book

        if book.author in self.author:
            self.author[book.author].append(book)
        else:
            self.author[book.author] = [book]

        if book.year in self.year:
            self.year[book.year].append(book)
        else:
            self.year[book.year] = [book]

        if book.genre in self.genre:
            self.genre[book.genre].append(book)
        else:
            self.genre[book.year] = [book]

    def remove_book(self, book: Book) -> None:
        del self.ISBN[book.isbn]

        self.author[book.author].remove(book)
        if not self.author[book.author]:
            del self.author[book.author]

        self.year[book.year].remove(book)
        if not self.year[book.year]:
            del self.year[book.year]

        self.genre[book.genre].remove(book)
        if not self.genre[book.genre]:
            del self.genre[book.genre]

    def __getitem__(self, key: Union[int, str]) -> Union[Book, list[Book]]:
        if isinstance(key, int):
            if key in self.year:
                return self.year[key]
            else:
                raise KeyError(key)
        elif isinstance(key, str):
            if key in self.ISBN:
                return self.ISBN[key]
            elif key in self.author:
                return self.author[key]
            else:
                raise KeyError(key)
        else:
            raise KeyError(key)
