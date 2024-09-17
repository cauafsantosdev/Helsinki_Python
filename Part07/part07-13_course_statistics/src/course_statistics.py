# Write your solution here

import urllib.request
import json
from math import floor


def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(request.read())

    courses = []

    for course in data:
        if course['enabled'] == True:
            add = course['fullName'], course['name'], course['year'], sum(course['exercises'])
            courses.append(add)
    
    return courses


def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.loads(request.read())

    weeks = len(data)
    students = []
    hours = []
    exercises = []

    for week in data.values():
        students.append(week['students'])
        hours.append(week['hour_total'])
        exercises.append(week['exercise_total'])

    students = max(students)
    hours = sum(hours)
    exercises = sum(exercises)
    hours_average = floor(hours / students)
    exercises_average = floor(exercises / students)

    course_data = {'weeks': weeks, 
        'students': students, 
        'hours': hours, 
        'hours_average': hours_average, 
        'exercises': exercises, 
        'exercises_average': exercises_average
    }
   
    return course_data


if __name__ == "__main__":
    print(retrieve_course("docker2019"))
