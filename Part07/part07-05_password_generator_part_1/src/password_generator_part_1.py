# Write your solution here

def generate_password(length: int):
    from string import ascii_lowercase
    from random import choice

    password = ""
    for i in range(length):
        password += choice(ascii_lowercase)
    
    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
