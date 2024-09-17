# Write your solution here

limit = int(input("Limit: "))
s = c = n = 0

while s < limit:
    n += 1
    s += n
    c += 1

print(s)