# Write your solution here:

def word_generator(characters: str, length: int, amount: int):
    return (characters[i: i + length] for i in range(amount))

if __name__ == "__main__":
    substrings = ("abcdefghijklmnopqrstuvwxyz"[i : i + 3] for i in range(24))

    for i in range(10):
        print(next(substrings))
