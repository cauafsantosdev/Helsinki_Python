# Write your solution here:

class Person:

    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        separated = self.name.split()
        first = separated[0]
        return first
    
    def return_last_name(self):
        separated = self.name.split()
        last = separated[1]
        return last


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())











