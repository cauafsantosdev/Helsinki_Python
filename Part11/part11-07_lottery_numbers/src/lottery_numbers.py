# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week: int, drawn: list):
        self.__week = week
        self.__drawn = drawn

    def number_of_hits(self, numbers: list):
        return sum(1 for n in numbers if n in self.__drawn)
    
    def hits_in_place(self, numbers: list):
        return [n if n in self.__drawn else -1 for n in numbers]
    

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.number_of_hits(my_numbers))
    print(week8.hits_in_place(my_numbers))