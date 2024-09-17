# Write your solution here

s1 = input("Please type in string 1: ")
s2 = input("Please type in string 2: ")

if len(s1) > len(s2):
    print(f"{s1} is longer")
elif len(s2) > len(s1):
    print(f"{s2} is longer")
else:
    print("The strings are equally long")