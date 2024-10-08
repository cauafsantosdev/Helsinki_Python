# Write your solution here:

class Item:

    def __init__(self, name: str, weight: int = 0):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:

    def __init__(self, max_weight: int):
        self.__items = []
        self.__max_weight = max_weight
        self.__actual_weight = 0
    
    def add_item(self, item: Item):
        if item.weight() + self.__actual_weight <= self.__max_weight:
            self.__items.append(item)
            self.__actual_weight += item.weight()

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.__actual_weight
    
    def heaviest_item(self):
        return max(self.__items, key=lambda item: item.weight())
    
    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.__actual_weight} kg)"
        else:
            return f"{len(self.__items)} items ({self.__actual_weight} kg)"
  

class CargoHold:

    def __init__(self, max_weight: int):
        self.__suitcases = []
        self.__max_weight = max_weight
        self.__actual_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__actual_weight <= self.__max_weight:
            self.__suitcases.append(suitcase)
            self.__actual_weight += suitcase.weight()

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        if len(self.__suitcases) == 1:
            return f"1 suitcase, space for {self.__max_weight - self.__actual_weight} kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.__actual_weight} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()