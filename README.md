# Лабораторная работа № 4: Симуляция с пользовательсĸими ĸоллеĸциями и псевдослучайной моделью

## Описание
Реализация системы управления библиотекой, включающей в себя классы Book(производные от Book - NonFictionBook и FictionBook), IndexDict, Library и функциями псевдослучайной симуляции и CLI(взаимодействие с пользователем).

## Структура проекта

```
Lab_4

├─ .pre-commit-config.yaml
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ src
│  ├─ book.py
│  ├─ book_collection.py
│  ├─ index_dict.py
│  ├─ library.py
│  ├─ main.py
│  ├─ simulation.py
│  └─ __init__.py
├─ tests
│  ├─ test_book.py
│  ├─ test_book_collection.py
│  ├─ test_generate_book.py
│  ├─ test_index_dict.py
│  ├─ test_library.py
│  └─ __init__.py
└─ uv.lock

```

## Запуск симуляции
```python src\simulation.py <steps> <seed>```

## Запуск Cli
``` src\main.py```

## Запуск тестов
1) Предустановка ```pip install pytest```
2) Для подробного вывода - ```pytest -v```
