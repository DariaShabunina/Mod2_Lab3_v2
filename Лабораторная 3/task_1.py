class Book:
    def __init__(self, name: str, author: str):
        self._name = None
        self.set_name(name)
        self._author = None
        self.set_author(author)

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть типа str")
        self._name = new_name

    def set_author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError("Поле автор должно быть типа str")
        self._author = new_author

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._author!r})'

    def __str__(self) -> str:
        return f'Книга "{self._name}"'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._author!r}, {self._pages})'


class EBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._author!r}, {self._duration})'


paperbook = PaperBook("Имя2", "Автор2", 3)
print(str(paperbook))
paperbook.pages = 5
paperbook.set_name("Имя1")
paperbook.set_author("Автор1")
print(repr(paperbook))
#end
