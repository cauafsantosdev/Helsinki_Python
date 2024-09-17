# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    option = int(input("Function: "))

    if option == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish};{english}\n")
        print("Dictionary entry added")

    elif option == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip()
                line = line.split(";")
                if search_term in line[0] or search_term in line[1]:
                    print(f"{line[0]} - {line[1]}")
                    
    elif option == 3:
        print("Bye!")
        break