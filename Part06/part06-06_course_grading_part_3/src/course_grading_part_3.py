# tee ratkaisu tänne

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
        exercises[parts[0]] = sum(parts[1:])

exams = {}

with open(exam_data) as grades:
    for line in grades:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for i in range(1, len(parts)):
            parts[i] = int(parts[i])
        exams[parts[0]] = sum(parts[1:])


print(f"{'name':<30}", end="")
print(f"{'exec_nbr':<10}", end="")
print(f"{'exec_pts.':<10}", end="")
print(f"{'exm_pts.':<10}", end="")
print(f"{'tot_pts.':<10}", end="")
print(f"{'grade':<10}")

for i, j in names.items():
    grade = (exercises[i] // 4) + exams[i]
    print(f"{' '.join(j):<29} ", end="")
    print(f"{exercises[i]:<10}", end="")
    print(f"{exercises[i] // 4:<10}", end="")
    print(f"{exams[i]:<10}", end="")
    print(f"{grade:<10}", end="")
    if grade < 15:
        print(f"{'0':<10}")
    elif grade < 18:
        print(f"{'1':<10}")
    elif grade < 21:
        print(f"{'2':<10}")
    elif grade < 24:
        print(f"{'3':<10}")
    elif grade < 28:
        print(f"{'4':<10}")
    else:
        print(f"{'5':<10}")