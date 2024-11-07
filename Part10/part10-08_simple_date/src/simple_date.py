# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        if day < 0 or day > 30 or month < 0 or month > 12 or year < 0:
            raise ValueError ("Invalid date")

        self.__day = day
        self.__month = month
        self.__year = year

    def __value(self):
        return self.__day + (self.__month * 30) + (self.__year * 360)

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __gt__(self, another: "SimpleDate"):
        return self.__value() > another.__value()
    
    def __lt__(self, another: "SimpleDate"):
        return self.__value() < another.__value()

    def __eq__(self, another: "SimpleDate"):
        return self.__value() == another.__value()

    def __ne__(self, another: "SimpleDate"):
        return self.__value() != another.__value()

    def __add__(self, increment: int):
        day = self.__day + increment
        month = self.__month
        year = self.__year

        while day > 30:
            day -= 30
            month += 1
            if month > 12:
                month = 1
                year += 1

        return SimpleDate(day, month, year)
    
    def __sub__(self, another):
        return abs(self.__value() - another.__value())


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)