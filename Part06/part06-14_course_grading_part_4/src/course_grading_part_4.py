# tee ratkaisu tänne

def read_file(filename: str):
    with open(f"src/{filename}") as file:
        if 'students' in filename or 'exercises' in filename or 'exam_points' in filename:
            d = {}
            for line in file:
                line = line.strip()
                line = line.split(';')
                if line[0] == 'id':
                    continue
                d[line[0]] = line[1:]
            return d
        elif 'course' in filename:
            course_info = []
            for line in file:
                line = line.strip()
                line = line.split(':')
                course_info.append(line[1].strip())
            return course_info


def convert_int(d: dict):
    for v in d.values():
        for index, value in enumerate(v):
            v[index] = int(value)


def grade(points: int):
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5


def write_results(students: dict, exercises: dict, exams: dict, course: list):

    students_grade = []
    summary = (f"{course[0]}, {course[1]} credits\n")
    summary += "=" * 38 + "\n"
    summary += (f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n")

    for student, name in students.items():
        full_name = f"{name[0]} {name[1]}"
        exercise_total = sum(exercises[student])
        exercise_points = exercise_total // 4
        exam_points = sum(exams[student])
        total_points = exercise_points + exam_points
        student_grade = grade(total_points)

        students_grade.append([str(student), full_name, str(student_grade)])
        summary += (f"{full_name:<30}{exercise_total:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{student_grade:<10}\n")

    with open("results.txt", 'w') as txt_file:
        txt_file.write(summary)
    
    with open("results.csv", 'w') as csv_file:
        for record in students_grade:
            line = f"{';'.join(record)}\n"
            csv_file.write(line)

    print(f"Results written to files results.txt and results.csv")


def main():
    student_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
    exam_file = input("Exam points: ")
    course_file = input("Course information: ")
    
    students = read_file(student_file)
    exercises = read_file(exercises_file)
    exams = read_file(exam_file)
    course = read_file(course_file)

    convert_int(exercises)
    convert_int(exams)

    write_results(students, exercises, exams, course)


main()