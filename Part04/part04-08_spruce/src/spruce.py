# Write your solution here
# You can test your function by calling it within the following block

def spruce(a):
    print("a spruce!")
    for i in range(1, a + 1):
        space = a - i
        chars = 2 * i - 1
        print(" " * space + "*" * chars)
    print(" " * (a - 1) + "*")


if __name__ == "__main__":
    spruce(5)