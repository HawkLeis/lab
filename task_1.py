class Automobile:
    """
    Базовый класс для автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор базового класса Automobile.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.brand = brand  # Публичный атрибут для марки автомобиля.
        self.model = model  # Публичный атрибут для модели автомобиля.
        self.year = year    # Публичный атрибут для года выпуска автомобиля.

    def get_age(self) -> int:
        """
        Возвращает возраст автомобиля в годах (предполагается текущий год как 2025).

        :return: Возраст автомобиля.
        """
        return 2025 - self.year

    def __str__(self) -> str:
        """
        Строковое представление объекта для пользователя.

        :return: Строка с описанием автомобиля.
        """
        return f"{self.brand} {self.model}, {self.year} года выпуска."

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта.

        :return: Строка с описанием объекта.
        """
        return f"Automobile(brand='{self.brand}', model='{self.model}', year={self.year})"


class PassengerCar(Automobile):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, seats: int):
        """
        Конструктор класса PassengerCar. Расширяет базовый класс добавлением количества мест.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param seats: Количество пассажирских мест.
        """
        super().__init__(brand, model, year)  # Вызываем конструктор базового класса.
        self._seats = seats  # Инкапсулируем количество мест (так как это внутренняя характеристика).

    def get_seats(self) -> int:
        """
        Возвращает количество мест.

        :return: Количество мест.
        """
        return self._seats

    def __str__(self) -> str:
        """
        Переопределяем метод __str__ для добавления информации о количестве мест.

        :return: Строка с описанием легкового автомобиля.
        """
        return f"{super().__str__()} ({self._seats} мест)"

    def __repr__(self) -> str:
        """
        Переопределяем метод __repr__ для более полного описания объекта.

        :return: Строка с описанием объекта.
        """
        return f"PassengerCar(brand='{self.brand}', model='{self.model}', year={self.year}, seats={self._seats})"

    def get_age(self) -> int:
        """
        Переопределяем метод get_age для добавления комментария о возрасте легкового автомобиля.
        Причина перегрузки: Для легковых автомобилей важно учитывать их возраст при продаже или обслуживании.

        :return: Возраст автомобиля.
        """
        age = super().get_age()
        return age


if __name__ == "__main__":
    # Создаем объект базового класса.
    car = Automobile(brand="Toyota", model="Corolla", year=2015)
    print(str(car))  # Toyota Corolla, 2015 года выпуска.
    print(repr(car))  # Automobile(brand='Toyota', model='Corolla', year=2015)

    # Создаем объект дочернего класса.
    passenger_car = PassengerCar(brand="Honda", model="Civic", year=2018, seats=5)
    print(str(passenger_car))  # Honda Civic, 2018 года выпуска. (5 мест)
    print(repr(passenger_car))  # PassengerCar(brand='Honda', model='Civic', year=2018, seats=5)

    # Вызываем метод get_age для обоих объектов.
    print(f"Возраст автомобиля: {car.get_age()} лет.")  # Возраст автомобиля: 10 лет.
    print(f"Возраст легкового автомобиля: {passenger_car.get_age()} лет.")  # Возраст легкового автомобиля: 7 лет.