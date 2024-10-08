# WRITE YOUR SOLUTION HERE:

class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        return max(set(my_list), key=my_list.count)

    @classmethod
    def doubles(cls, my_list: list):
        doubles = list(set([n for n in my_list if my_list.count(n) > 1]))
        return len(doubles)
    

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))