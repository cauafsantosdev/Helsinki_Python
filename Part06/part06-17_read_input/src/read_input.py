# Write your solution here

def read_input(msg: str, start: int, end: int):
    while True:
        try:
            n = int(input(msg))
            if n >= start and n <= end:
                return n
        except:
            pass
        
        print(f"You must type in an integer between {start} and {end}")


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print(f"You typed in: {number}")
