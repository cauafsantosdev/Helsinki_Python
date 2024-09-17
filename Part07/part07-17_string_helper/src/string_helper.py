# Write your solution here

import string

def change_case(orig_string: str):
    orig_string = orig_string.split()
    new_string = ""
    
    for word in orig_string:
        for letter in word:
            if letter in string.ascii_lowercase:
                new_string += letter.upper()
            elif letter in string.ascii_uppercase:
                new_string += letter.lower()
        new_string += " "

    return new_string.strip()


def split_in_half(orig_string: str):
    half = len(orig_string) // 2

    first_half = orig_string[:half]
    second_half = orig_string[half:]

    return first_half, second_half


def remove_special_characters(orig_string: str):
    orig_string = orig_string.split()
    new_string = ""
    
    for word in orig_string:
        for letter in word:
            if letter.isalnum():
                new_string += letter
        new_string += " "
    
    return new_string.strip()

    