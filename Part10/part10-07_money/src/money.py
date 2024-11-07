# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, __euros: int, __cents: int):
        self.__total = __euros * 100 + __cents

    def __str__(self):
        return f"{(self.__total / 100):.2f} eur"

    def __eq__(self, another):
        return self.__total == another.__total
    
    def __ne__(self, another):
        return self.__total != another.__total
    
    def __gt__(self, another):
        return self.__total > another.__total
    
    def __lt__(self, another):
        return self.__total < another.__total
    
    def __add__(self, another):
        values_sum = self.__total + another.__total
        euros = values_sum // 100
        cents = values_sum % 100
        
        return Money(euros, cents)
    
    def __sub__(self, another):
        difference = self.__total - another.__total

        if difference < 0:
            raise ValueError ("a negative result is not allowed")
        
        euros = difference // 100
        cents = difference % 100
        
        return Money(euros, cents)


if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1)
    print(e2)
    print(e1 == e2)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    print(e1)
    e1.euros = 1000
    print(e1)