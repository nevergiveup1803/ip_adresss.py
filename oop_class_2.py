# Создание класса Date
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f'{self.day}, {self.month}, {self.year}'

    # Статический метод @classmethod
    @classmethod
    def mileniym_1(cls, day, month):
        return cls(day, month, 2000)

    # Статический метод @staticmethod
    @staticmethod
    def milenium_2(day, month):
        return Date(day, month, 2000)


d_1 = Date.mileniym_1(18, 3)
d_2 = Date.milenium_2(18, 3)
print(d_1.display())
print(d_2.display())


# Создание класса DateTime наследника класса Date.
class DateTime(Date):
    def display(self):
        return f'{self.day}, {self.month}, {self.year}, 00:00AM'


dt1 = DateTime(18, 3, 2010)
dt2 = DateTime.mileniym_1(18, 3)
print(dt1.display())
print(dt2.display())
