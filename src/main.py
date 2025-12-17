import shlex
from src.library import Library
from src.book import FictionBook, NonFictionBook


def main():
    """Запуск взаимодействия с пользователем"""
    lib = Library()
    print("БИБЛИОТЕКА")
    print("Команды:")
    print('  add --fiction "<название>" "<автор>" <год> <жанр> <isbn> <страницы>')
    print('  add --nonfiction "<название>" "<автор>" <год> <жанр> <isbn> <страницы>')
    print("  remove <isbn>")
    print("  search author | genre | year <значение>")
    print("  list")
    print("  help")
    print("  exit")

    while True:
        try:
            line = input("> ").strip()
            if not line:
                continue

            parts = shlex.split(line)
            cmd = parts[0]

            if cmd == "exit":
                break

            elif cmd == "help":
                print("Примеры:")
                print('  add --fiction "Хоббит" "Толкин" 1937 Фэнтези isbn-123 310')
                print(
                    '  add --nonfiction "Краткая история времени" "Хокинг" 1988 Научпоп isbn-456 256')
                print(
                    '  add --fiction "Преступление и наказание" "Достоевский" 1866 Роман isbn-789 670')
                print("  remove isbn-123")
                print("  search author Толкин")
                print("  search genre Фэнтези")
                print("  search year 1937")
                print("  list")

            elif cmd == "add":
                if len(parts) != 8:
                    print("укажите тип (--fiction или --nonfiction) и 6 параметров")
                    print("заключайте названия и авторов с пробелами в кавычки")
                    continue

                flag = parts[1]
                title = parts[2]
                author = parts[3]
                try:
                    year = int(parts[4])
                    genre = parts[5]
                    isbn = parts[6]
                    pages = int(parts[7])
                except ValueError:
                    print("Ошибка: год и количество страниц должны быть целыми числами")
                    continue

                if flag == "--fiction":
                    book = FictionBook(title, author, year, genre, isbn, pages)
                elif flag == "--nonfiction":
                    book = NonFictionBook(
                        title, author, year, genre, isbn, pages)
                else:
                    print("Ошибка: укажите --fiction или --nonfiction")
                    continue

                lib.add_book(book)
                print(f"[+] {book}")

            elif cmd == "remove":
                if len(parts) != 2:
                    continue
                isbn = parts[1]
                try:
                    title = lib.index.ISBN[isbn].title
                    lib.remove_book(isbn)
                    print(f"[-] Книга: \"{title}\" удалена")
                except KeyError:
                    print("Книга с таким ISBN отсутствует")

            elif cmd == "search":
                if len(parts) != 3:
                    continue
                type, value = parts[1], parts[2]
                try:
                    if type == "author":
                        books = lib.find_by_author(value)
                    elif type == "genre":
                        books = lib.find_by_genre(value)
                    elif type == "year":
                        books = lib.find_by_year(int(value))
                    else:
                        print("Поддерживаемые типы: author, genre, year")
                        continue
                    if books:
                        for b in books:
                            print(f" {b}")
                    else:
                        print("Ничего не найдено")
                except Exception:
                    print("Ничего не найдено")

            elif cmd == "list":
                if not lib.books:
                    print("Библиотека пуста")
                else:
                    for book in lib.books:
                        print(f" -{book}")

            else:
                print("Неизвестная команда. Введите 'help'.")

        except KeyboardInterrupt:
            print("\nВыход")
            break
        except ValueError:
            print("Ошибка разбора команды. Убедитесь, что строки в кавычках")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
