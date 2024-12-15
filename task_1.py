from typing import Union

class Book:
    """
    Абстрактный класс, описывающий книгу.
    """

    def __init__(self, title: str, author: str, pages: int):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer")

        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.pages = pages  # Количество страниц

    def read(self):
        """
        Симулирует чтение книги.

        Returns:
            str: Сообщение о процессе чтения.

        >>> book = Book("Python Basics", "John Doe", 300)
        >>> book.read()
        'Reading the book: Python Basics.'
        """
        return f"Reading the book: {self.title}."

    def bookmark_page(self, page: int):
        """
        Закладывает закладку на указанной странице.

        Args:
            page (int): Номер страницы для закладки.

        Raises:
            ValueError: Если номер страницы вне диапазона.

        >>> book = Book("Python Basics", "John Doe", 300)
        >>> book.bookmark_page(50)
        'Bookmarked page 50 in Python Basics.'
        """
        if page <= 0 or page > self.pages:
            raise ValueError("Page number must be within the range of the book")
        return f"Bookmarked page {page} in {self.title}."


class Car:
    """
    Абстрактный класс, описывающий автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int):
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        if not isinstance(year, int) or year < 1886:  # Первый автомобиль был создан в 1886 году
            raise ValueError("Year must be 1886 or later")

        self.brand = brand  # Бренд автомобиля
        self.model = model  # Модель автомобиля
        self.year = year  # Год выпуска

    def drive(self):
        """
        Симулирует вождение автомобиля.

        Returns:
            str: Сообщение о процессе вождения.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.drive()
        'Driving a Toyota Corolla.'
        """
        return f"Driving a {self.brand} {self.model}."

    def honk(self):
        """
        Симулирует сигнал автомобиля.

        Returns:
            str: Звук сигнала.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.honk()
        'Beep beep!'
        """
        return "Beep beep!"


class Chair:
    """
    Абстрактный класс, описывающий стул.
    """

    def __init__(self, material: str, legs: int):
        if not isinstance(material, str):
            raise TypeError("Material must be a string")
        if not isinstance(legs, int) or legs <= 0:
            raise ValueError("Legs must be a positive integer")

        self.material = material  # Материал стула
        self.legs = legs  # Количество ножек

    def sit(self):
        """
        Симулирует сидение на стуле.

        Returns:
            str: Сообщение о процессе использования стула.

        >>> chair = Chair("wood", 4)
        >>> chair.sit()
        'Sitting on a chair made of wood.'
        """
        return f"Sitting on a chair made of {self.material}."

    def move(self, distance: float):
        """
        Симулирует перемещение стула на указанное расстояние.

        Args:
            distance (float): Расстояние перемещения в метрах.

        Raises:
            ValueError: Если расстояние меньше или равно нулю.

        >>> chair = Chair("wood", 4)
        >>> chair.move(2.5)
        'Moved the chair 2.5 meters.'
        """
        if distance <= 0:
            raise ValueError("Distance must be positive")
        return f"Moved the chair {distance} meters."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
