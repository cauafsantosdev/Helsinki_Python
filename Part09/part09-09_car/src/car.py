# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, distance: int):
        for i in range(distance):
            if self.__petrol > 0:
                self.__odometer += 1
                self.__petrol -= 1
            else:
                break

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"
    

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)