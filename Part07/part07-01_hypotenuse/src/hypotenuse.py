# Write your solution here

def hypotenuse(leg1: float, leg2: float):
    from math import sqrt
    hypotenuse = leg1 ** 2 + leg2 ** 2
    hypotenuse = sqrt(hypotenuse)
    return hypotenuse


if __name__ == "__main__":
    print(hypotenuse(3,4))