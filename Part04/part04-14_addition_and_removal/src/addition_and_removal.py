# Write your solution here

list = []
while True:
    print(f"The list is now {list}")
    selection = input("a(d)d, (r)emove or e(x)it:")
    if selection == "d":
        item = len(list) + 1
        list.append(item)
    elif selection == "r":
        list.pop(len(list) - 1)
    elif selection == "x":
        break
    
print("Bye!")