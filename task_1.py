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

        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        """
        Симулирует чтение книги.

        Return:
            str: Сообщение о процессе чтения.

        >>> book = Book("Python Basics", "John Doe", 300)
        >>> book.read()
        'Reading the book: Python Basics.'
        """
        return f"Reading the book: {self.title}."

class Car:
    """
    Абстрактный класс, описывающий автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int):
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Year must be 1886 or later")

        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        """
        Симулирует вождение автомобиля.

        Return:
            str: Сообщение о процессе вождения.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.drive()
        'Driving a Toyota Corolla.'
        """
        return f"Driving a {self.brand} {self.model}."

class Chair:
    """
    Абстрактный класс, описывающий стул.
    """

    def __init__(self, material: str, legs: int):
        if not isinstance(material, str):
            raise TypeError("Material must be a string")
        if not isinstance(legs, int) or legs <= 0:
            raise ValueError("Legs must be a positive integer")

        self.material = material
        self.legs = legs

    def sit(self):
        """
        Симулирует сидение на стуле.

        Return:
            str: Сообщение о процессе использования стула.

        >>> chair = Chair("wood", 4)
        >>> chair.sit()
        'Sitting on a chair made of wood.'
        """
        return f"Sitting on a chair made of {self.material}."

if __name__ == "__main__":
    import doctest
    doctest.testmod()