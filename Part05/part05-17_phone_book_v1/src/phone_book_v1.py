# Write your solution here

book = {}

while True:
    x = int(input("Command (1 search, 2 add, 3 quit): "))
    if x == 1:
        search = input("Name: ")
        if search in book:
            print(book[search])
        else:
            print("no number")
    elif x == 2:
        name = input("Name: ")
        number = input("Number: ")
        book[name] = number
        print("ok!")
    elif x == 3:
        print("quitting...")
        break
    else:
        print(f"Invalid option!\n")