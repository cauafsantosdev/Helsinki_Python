# tee ratkaisusi tänne

class CourseList:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, course: str, grade: int, credit: int):
        if course not in self.__courses:
            self.__courses[course] = [grade, credit]
        elif grade > self.__courses[course][0]:
            self.__courses[course][0] = grade
            
    def get_course_data(self, course: str):
        if course in self.__courses:
            return f"{course} ({self.__courses[course][1]} cr) grade {self.__courses[course][0]}"
        else:
            return "no entry for this course"
    
    def get_statistics(self):
        total_courses = len(self.__courses)
        total_grades = sum(value[0] for value in self.__courses.values())
        total_credits = sum(value[1] for value in self.__courses.values())
        mean = round(total_grades / total_courses, 1)
        grades = {
            5: "x" * sum(1 for valor in self.__courses.values() if valor[0] == 5),
            4: "x" * sum(1 for valor in self.__courses.values() if valor[0] == 4),
            3: "x" * sum(1 for valor in self.__courses.values() if valor[0] == 3),
            2: "x" * sum(1 for valor in self.__courses.values() if valor[0] == 2),
            1: "x" * sum(1 for valor in self.__courses.values() if valor[0] == 1),
        }

        print(f"{total_courses} completed courses, a total of {total_credits} credits\nmean {mean}\ngrade distribution")
        for key, value in grades.items():
            print(f"{key}: {value}")


class CourseRecordsApplication:
    def __init__(self):
        self.__course_list = CourseList()
    
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.__course_list.add_course(course, grade, credit)

    def search(self):
        course = input("course: ")
        print(self.__course_list.get_course_data(course))

    def menu(self):
        print("1 add course\n2 get course data\n3 statistics\n0 exit")

    def execute(self):
        self.menu()

        while True:
            command = int(input("\ncommand: "))
            if command == 0:
                break
            elif command == 1:
                self.add_course()
            elif command == 2:
                self.search()
            elif command == 3:
                self.__course_list.get_statistics()


course_records = CourseRecordsApplication()
course_records.execute()