# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if len(self.numbers) > 0:
            return sum(self.numbers) / len(self.numbers)
        
        return 0
    
    def get_sum_of_evens(self):
        evens = [n for n in self.numbers if n % 2 == 0]
        return sum(evens)
    
    def get_sum_of_odds(self):
        odds = [n for n in self.numbers if n % 2 != 0]
        return sum(odds)
    

stats = NumberStats()
print("Please type in integer numbers:")

while True:
    n = int(input())
    if n == -1:
        break
    else:
        stats.add_number(n)

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.get_sum_of_evens())
print("Sum of odd numbers:", stats.get_sum_of_odds())
