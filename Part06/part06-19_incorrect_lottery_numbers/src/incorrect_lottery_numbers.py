# Write your solution here

def week_valid(week: str):
    try:
        week = int(week)
        return True
    except:
        return False

def numbers_valid(numbers: list):
    try:
        numbers = numbers.split(',')

        if len(numbers) != 7:
            return False
        
        for num in numbers:
            number = int(num)
            if number < 1 or number > 39 or numbers.count(num) > 1:
                return False
            
        return True
    
    except:
        return False

def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    correct_file = open('correct_numbers.csv', 'a')

    with open("lottery_numbers.csv") as lottery:
        for line in lottery:
            original_line = line
            line = line.strip()
            line = line.split(';')

            week = line[0].split(' ')
            numbers = line[1]

            if week_valid(week[1]) and numbers_valid(numbers):
                correct_file.write(original_line)
