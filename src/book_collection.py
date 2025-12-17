from typing import Union
from src.book import Book


class BookCollection:
    """
    Пользовательская коллекция, которая хранит в себе список всех книг
    """

    def __init__(self) -> None:
        self.books: list = []

    def __getitem__(self, index: Union[int, slice]) -> Union[Book, list[Book]]:
        """
        Метод возвращает книгу по индексу в books или срез списка книг
        """
        if isinstance(index, int):
            return self.books[index]
        elif isinstance(index, slice):
            return self.books[index]

    def __iter__(self):
        """
        Метод позволяет использовать BookCollection в итерациях
        """
        return iter(self.books)

    def __len__(self) -> int:
        """Метод возвращает длину списка books"""
        return len(self.books)

    def append(self, book: Book) -> None:
        """Добавление элемента в конец списка books"""
        self.books.append(book)

    def insert(self, index: int, book: Book) -> None:
        """Вставка значения в список books по индексу"""
        self.books.insert(index, book)

    def remove_book(self, book: Book) -> None:
        """Удаление книги"""
        self.books.remove(book)

    def __delitem__(self, index: int) -> None:
        """Удаление книги по индексу в booksЫ"""
        del self.books[index]

    def __contains__(self, book: Book) -> bool:
        """позволяет использовать in """
        return book in self.books
