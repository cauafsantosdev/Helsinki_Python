# write your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

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
        exercises[parts[0]] = (sum(parts[1:]) // 4)

exams = {}

with open(exam_data) as grades:
    for line in grades:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for i in range(1, len(parts)):
            parts[i] = int(parts[i])
        exams[parts[0]] = sum(parts[1:])


for i, j in names.items():
    print(f"{' '.join(j)} ", end="")
    grade = exercises[i] + exams[i]
    if grade < 15:
        print(0)
    elif grade < 18:
        print(1)
    elif grade < 21:
        print(2)
    elif grade < 24:
        print(3)
    elif grade < 28:
        print(4)
    else:
        print(5)