# Write your solution here

from difflib import get_close_matches

def read_file(filename: str):
    word_list = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            word_list.append(line)

    return word_list


text = input("Write text: ").split()
word_list = read_file("wordlist.txt")

misspelled = []

for idx, word in enumerate(text):
    if word.lower() not in word_list:
        text[idx] = f"*{word}*"
        misspelled.append(word) 

print(" ".join(text))

print("suggestions: ")

for word in misspelled:
    close_matches = get_close_matches(word, word_list)
    close_matches = ", ".join(close_matches)
    print(f"{word}: {close_matches}")
