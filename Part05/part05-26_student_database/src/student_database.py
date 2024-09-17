# Write your solution here

def add_student(db: dict, name: str):
    #Adiciona um estudante com nenhum curso completado.
    db[name] = ["no completed courses"]


def add_course(db: dict, name: str, course: tuple):
    #Adiciona um curso ao estudante. Substitui o curso se a nova nota for maior.
    if course[1] > 0:
        if name in db:
            if db[name] == ["no completed courses"]:
                db[name] = [course]
            else:
                for i, existing_course in enumerate(db[name]):
                    if existing_course[0] == course[0]:
                        if existing_course[1] < course[1]:
                            db[name][i] = course
                        return
                db[name].append(course)
        else:
            print(f"{name}: no such person in the database")


def print_student(db: dict, name: str):
    #Mostra o resumo de um estudante, incluindo cursos e média de notas.
    if name in db:
        print(f"{name}:")
        courses = db[name]
        if courses == ["no completed courses"]:
            print(" no completed courses")
        else:
            print(f" {len(courses)} completed courses:")
            grades = count = 0
            for course_name, grade in courses:
                print(f"  {course_name} {grade}")
                grades += grade
                count += 1
            avg = grades / count
            print(f" average grade {avg:.1f}")
    else:
        print(f"{name}: no such person in the database")


def summary(db: dict):
    #Mostra o resumo geral: número de estudantes, quem completou mais cursos e melhor média."""
    total_students = len(db)
    most_courses = 0
    best_avg = 0
    most_courses_student = ""
    best_avg_student = ""

    for student, courses in db.items():
        if courses == ["no completed courses"]:
            continue

        count = len(courses)
        if count > most_courses:
            most_courses = count
            most_courses_student = student

        grades = sum(grade for _, grade in courses)
        avg = grades / count
        if avg > best_avg:
            best_avg = avg
            best_avg_student = student

    print(f"students {total_students}")
    print(f"most courses completed {most_courses} {most_courses_student}")
    print(f"best average grade {best_avg:.1f} {best_avg_student}")


if __name__ == "__main__":
    students = {}

    add_student(students, "Peter")
    add_student(students, "Josh")
    add_student(students, "John")
    add_student(students, "Marty")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    add_course(students, "Josh", ("Advanced Course in Programming", 2))

    print_student(students, "Peter")
    print()
    summary(students)
    print()
    print(students)
    