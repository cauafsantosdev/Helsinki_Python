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


def cheaters():
    start_list = read_csv("src/start_times.csv")
    submission_list = read_csv("src/submissions.csv")
    
    cheaters = []

    for name1, time1 in start_list:
        time1 = convert_time(time1)

        for name2, _, _, time2 in submission_list:
            if name1 == name2: 
                time2 = convert_time(time2)
                time_diff = time2 - time1

                if time_diff.total_seconds() > 10800:
                    if name1 not in cheaters:
                        cheaters.append(name1)
    
    return cheaters


if __name__ == "__main__":
    print(cheaters())
