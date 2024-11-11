# WRITE YOUR SOLUTION HERE:

def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as file:
        words_list = [word.strip().replace(".", "").replace(",", "") for line in file for word in line.split()]
        return {word: words_list.count(word) for word in words_list if words_list.count(word) >= lower_limit}


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))