# Write your solution here

def words(n: int, beginning: str):
    from random import sample

    found = []

    with open("src/words.txt") as words:
        for line in words:
            line = line.strip()
            if line.startswith(beginning):
                found.append(line)

    random_found = sample(found, n)
    
    return random_found


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)