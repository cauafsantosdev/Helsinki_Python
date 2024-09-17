# Write your solution here

def fractionate(amount: int):
    from fractions import Fraction

    fractions = []

    for i in range(amount):
        fractions.append(Fraction(1, amount))
        
    return fractions

if __name__ == "__main__":
    for p in fractionate(9):
        print(p)

    print()
    print(fractionate(44))