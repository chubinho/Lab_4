class Book:
    def __init__(self, title: str, author: str, year: str, genre: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        return f'Произведение "{self.title}", написанное автором {self.author} в {self.year}'
