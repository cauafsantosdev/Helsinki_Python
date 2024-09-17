# Write your solution here

def remove_smallest(numbers: list):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
           smallest = i
    return numbers.remove(smallest)

if __name__ == "__main__":
    numbers = []
    remove_smallest(numbers)
    print(numbers)