class Book:
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        return f'Произведение "{self.title}", написанное автором {self.author} в {self.year}'


class NonFictionBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, pages: int) -> None:
        super().__init__(title, author, year, genre, isbn)
        self.pages: int = pages

    def __repr__(self) -> str:
        return f'Нехудожественное произведение "{self.title}", написанное автором {self.author} в {self.year} году имеет {self.pages} страниц'


class FictionBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, pages: int) -> None:
        super().__init__(title, author, year, genre, isbn)
        self.pages = pages

    def __repr__(self) -> str:
        return f'Художественное произведение "{self.title}", написанное автором {self.author} в {self.year} году имеет {self.pages} страниц'
