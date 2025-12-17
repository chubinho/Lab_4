from typing import Union
from src.book import Book


class IndexDict:
    """Класс индексации книг"""
    def __init__(self) -> None:
        self.ISBN: dict[str, Book] = {}
        self.year: dict[int, list[Book]] = {}
        self.author: dict[str, list[Book]] = {}

    def add_book(self, book: Book) -> None:
        """Метод добавления книги"""
        self.ISBN[book.isbn] = book

        if book.author in self.author:
            self.author[book.author].append(book)
        else:
            self.author[book.author] = [book]

        if book.year in self.year:
            self.year[book.year].append(book)
        else:
            self.year[book.year] = [book]


    def remove_book(self, book: Book) -> None:
        """Метод удаления книги"""
        del self.ISBN[book.isbn]

        self.author[book.author].remove(book)
        if not self.author[book.author]:
            del self.author[book.author]

        self.year[book.year].remove(book)
        if not self.year[book.year]:
            del self.year[book.year]


    def __getitem__(self, key: Union[int, str]) -> Union[Book, list[Book]]:
        """
        Магический метод, возвращающий
        книгу по ключу
        """
        if isinstance(key, int):
            if key in self.year:
                return self.year[key]
            else:
                raise KeyError("Данные по переданному ключу не найдены")
        elif isinstance(key, str):
            if key in self.ISBN:
                return self.ISBN[key]
            elif key in self.author:
                return self.author[key]
            else:
                raise KeyError("Данные по переданному ключу не найдены")
        else:
            raise KeyError("Передан неверный ключ")

    def __len__(self):
        """ВОзвращает длину словаря книг"""
        return len(self.ISBN)

    def __contains__(self, isbn: str) -> bool:
        """Позволяет использовать len"""
        return isbn in self.ISBN
