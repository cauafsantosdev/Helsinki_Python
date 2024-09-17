# Write your solution here

import string
from random import choice, shuffle


def chars(numbers: bool, special: bool):
    chars = string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special:
        chars += "!?=+-()#"
    
    return chars


def generate_strong_password(length: int, numbers: bool, special: bool):
    char_list = chars(numbers, special)
    password = [choice(string.ascii_lowercase)]

    if numbers:
        password.append(choice(string.digits))
    if special:
        password.append(choice("!?=+-()#"))

    for i in range(len(password), length):
        password.append(choice(char_list))
    
    shuffle(password)
    
    return "".join(password)


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, False, True))
