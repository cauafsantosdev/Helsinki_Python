# Write your solution here

def double_items(numbers: list):
    new = []
    for i in numbers:
        new.append(i * 2)
    return new


if __name__ == "__main__":
    numbers = []
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)