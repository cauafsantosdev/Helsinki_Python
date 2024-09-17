# Write your solution here

def factorials(n: int):
    d = {}
    f = 1
    for i in range(1, n + 1):
        f *= i
        d[i] = f
    return d


if __name__ == "__main__":
    print(factorials())
