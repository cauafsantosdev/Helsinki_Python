# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))
    if option == 0:
        print("Bye now!")
        break
    elif option == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(f"{entry}\n")
            file.close()
        print("Diary saved")
        print()
    elif option == 2:
        print("Entries:")
        with open("diary.txt") as file:
            for line in file:
                print(line.strip())
            file.close()
        print()