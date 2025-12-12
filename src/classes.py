class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self):
        return f'Произведение "{self.title}", написанное автором {self.author} в {self.year}'


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

    def append(self, book):
        self.books.append(book)

    def insert(self, index, book):
        self.books.insert(index, book)

    def remove_book(self, book):
        self.books.remove(book)

    def __delitem__(self, index):
        del self.books[index]


class IndexDict:
    def __init__(self):
        self.ISBN = {}
        self.year = {}
        self.author = {}

    def add_book(self, book):
        self.ISBN[book.isbn] = book

        if book.author in self.author:
            self.author[book.author].append(book)
        else:
            self.author[book.author] = [book]

        if book.year in self.year:
            self.year[book.year].append(book)
        else:
            self.year[book.year] = [book]

    def remove_book(self, book):
        del self.ISBN[book.isbn]

        self.author[book.author].remove(book)
        if not self.author[book.author]:
            del self.author[book.author]

        self.year[book.year].remove(book)
        if not self.year[book.year]:
            del self.year[book.year]

    def __getitem__(self, key):
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


class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()

    def add_book(self, book):
        if book.isbn in self.index.ISBN:
            return
        self.books.append(book)
        self.index.add_book(book)

    def remove_book(self, isbn):
        try:
            book = self.index[isbn]
            self.index.remove_book(book)

            for i, b in enumerate(self.books):
                if b.isbn == isbn:
                    del self.books[i]
                    break
        except KeyError:
            print("Книга не найдена")

    def find_by_isbn(self, isbn):
        return self.index[isbn]

    def find_by_author(self, author):
        return self.index[author]

    def find_by_year(self, year):
        return self.index[year]

b = Book("Война и мир", "Толстой", 1869, "Роман", "isbn-123")
lib = Library()
lib.add_book(b)
print(lib.books[0])
lib.add_book(b)
