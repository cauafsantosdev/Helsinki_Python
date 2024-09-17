# Write your solution here

from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth = datetime(year, month, day)
millenium = datetime(1999, 12, 31)
old = millenium - birth

if old.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {old.days} days old on the eve of the new millennium.")