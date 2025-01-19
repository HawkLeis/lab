BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    # метод, возвращающий строку формата Книга "название_книги"
    def __str__(self):
        return f'Книга "{self.name}"'

    # метод, возвращающий валидную python строку
    def __repr__(self):
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'

# класс Library
class Library:
    def __init__(self, books=None):
        # если books не передан, инициализируем пустым списком
        self.books = books if books is not None else []

    def get_next_book_id(self):
        # если в библиотеке нет книг, следующий id будет 1
        if not self.books:
            return 1
        # если книги есть, возвращаем id последней книги + 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        # ищем индекс книги по id
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        # если книги с таким id нет, вызываем исключение
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
