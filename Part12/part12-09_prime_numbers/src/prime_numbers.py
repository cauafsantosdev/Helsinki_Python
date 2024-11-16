# Write your solution here

def prime_numbers():
    n = 2

    while True:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            yield n

        n += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))