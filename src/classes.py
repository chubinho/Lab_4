class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn


class BookCollection:
    def __init__(self):
        self.books = []

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.books[index]
        elif isinstance(index, slice):
            return self.books[index]

    def __iter__(self):
        return iter(self.books)

    def __len__(self):
        return len(self.books)

    def append(self, value):
        self.books.append(value)

    def insert(self, index, value):
        self.books.insert(index, value)

    def __delitem__(self, index):
        del self.books[index]


class IndexDict:
    def __init__(self):
        self.ISBN = {}
        self.year = {}
        self.author = {}

    def __getitem__(self, key):
        if isinstance(key, int):
            if key in self.year:
                return self.year[key]
            else:   
                raise KeyError
        elif isinstance(key, str):
            if key in self.ISBN:
                return self.ISBN[key]
            elif key in self.author:
                return self.author[key]
            else:
                raise KeyError
        else:
            raise KeyError


