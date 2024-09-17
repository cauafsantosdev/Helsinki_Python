# Write your solution here

import csv
from datetime import datetime, timedelta


def read_csv(filename: str):
    data_list = []

    with open(filename) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=";")
        for line in csv_data:
            data_list.append(line)
    
    return data_list


def convert_time(time_str: str):
    return datetime.strptime(time_str, "%H:%M")


def final_points():
    start_list = read_csv("src/start_times.csv")
    submission_list = read_csv("src/submissions.csv")

    student_scores = {}

    for name1, time1 in start_list:
        time1 = convert_time(time1)

        for name2, task, points, time2 in submission_list:
            if name1 == name2: 
                time2 = convert_time(time2)
                time_diff = time2 - time1            

                if time_diff.total_seconds() > 10800:
                    continue 
                
                student_name = name2
                task_number = int(task)
                task_points = int(points)

                if student_name not in student_scores:
                    student_scores[student_name] = [0] * 8
                
                if task_points > student_scores[student_name][task_number - 1]:  
                    student_scores[student_name][task_number - 1] = task_points
        
    final_scores = {}

    for student, task_scores in student_scores.items():
        final_scores[student] = sum(task_scores)  
    
    return final_scores


if __name__ == "__main__":
    print(final_points())