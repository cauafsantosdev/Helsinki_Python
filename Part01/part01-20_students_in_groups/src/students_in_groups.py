# Write your solution here

students = int(input("How many students on the course? "))
groups = int(input("Desired group size? "))
number = students / groups

if number > int(number):
    number += 1
    number // 1

print(f"Number of groups formed: {number}")