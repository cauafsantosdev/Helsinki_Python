from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts: list):
    attempts = [i.credits for i in attempts]
    return reduce(lambda reduced_sum, item: reduced_sum + item, attempts)

def sum_of_passed_credits(attempts: list):
    passed = filter(lambda x: x.grade >= 1, attempts)
    passed = [i.credits for i in passed]
    return reduce(lambda reduced_sum, item: reduced_sum + item, passed)

def average(attempts: list):
    passed = filter(lambda x: x.grade >= 1, attempts)
    passed = [i.grade for i in passed]
    passed_sum = reduce(lambda reduced_sum, item: reduced_sum + item, passed)
    return passed_sum / len(passed)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)