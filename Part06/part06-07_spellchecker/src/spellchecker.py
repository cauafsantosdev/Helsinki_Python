# write your solution here

text = input("Input some text: ").split()
words = []

with open("src/wordlist.txt") as wordlist:
    for line in wordlist:
        words.append(line.strip())

    for i, j in enumerate(text):
        if j.lower() not in words:
            text[i] = f"*{text[i]}*"

print(" ".join(text))