# Write your solution here

from datetime import date


def list_years(dates: list):
    years = []

    for i in dates:
        years.append(i.year)
    
    years.sort()
    return years


if __name__ == "__main__":
    date1 = date(2010, 2, 3)
    date2 = date(2009, 10, 10)
    date3 = date(2004, 5, 9)
    date4 = date(2000, 5, 9)

    years = list_years([date1, date2, date3, date4])
    print(years)
