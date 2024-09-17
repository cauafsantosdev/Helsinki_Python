# write your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

names = {}

with open(student_info) as students:
    for line in students:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for i in range(1, len(parts)):
            parts[i] = parts[i].strip()
        names[parts[0]] = parts[1:]

exercises = {}

with open(exercise_data) as grades:
    for line in grades:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for i in range(1, len(parts)):
            parts[i] = int(parts[i])
        exercises[parts[0]] = sum(parts[1:])

for i, j in names.items():
    print(f"{' '.join(j)} {exercises[i]}")