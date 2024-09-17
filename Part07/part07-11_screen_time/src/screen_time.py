# Write your solution here

from datetime import datetime, timedelta

def format_date(start: str):
    try:
        date = datetime.strptime(start, "%d.%m.%Y")
    except ValueError:
        date = datetime.strptime(start, "%d.%m.%y")

    start_formatted = date.strftime("%d.%m.%Y")
    return date, start_formatted


def screen_time(date: str, period: int):
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    
    dictionary = {}

    for i in range(period):
        formatted_date = date.strftime("%d.%m.%Y")
        
        tv, computer, mobile = input(f"Screen time {formatted_date}: ").split()
        screen_time = int(tv), int(computer), int(mobile)
        dictionary[formatted_date] = screen_time

        date += timedelta(days = 1)
    
    return dictionary, formatted_date


def sum_avg(d: dict):
    total = 0

    for i in d.values():
        total += sum(i)

    avg = total / len(d)

    return total, avg


def write_stats(filename: str, start: str, end: str, total: int, average: float, dictionary: dict):
    with open(filename, "w") as file:
        file.write(f"Time period: {start}-{end}\n")
        file.write(f"Total minutes: {total}\n")
        file.write(f"Average minutes: {average}\n")
        for i, j in dictionary.items():
            file.write(f"{i}: {j[0]}/{j[1]}/{j[2]}\n")


def main():
    filename = input("Filename: ")
    start = input("Starting date: ")
    days_period = int(input("How many days: "))

    date, start_formatted = format_date(start)
    dictionary, formatted_date = screen_time(date, days_period)
    total, avg = sum_avg(dictionary)
    write_stats(filename, start_formatted, formatted_date, total, avg, dictionary)


main()
