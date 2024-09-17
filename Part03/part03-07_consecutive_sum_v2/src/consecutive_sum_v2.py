# Write your solution here

limit = int(input("Limit: "))
s = 0
n = 1

print("The consecutive sum: ", end="")

while s < limit:
    print(f"{n} ", end="")
    s += n
    n += 1
    if s < limit:
        print("+", end=" ")

print(f"= {s}")