# Write your solution here

def filter_solutions():
    open('incorrect.csv', 'w').close()
    open('correct.csv', 'w').close()
    
    with open("correct.csv", "a") as correct:
        with open("incorrect.csv", "a") as incorrect:

            with open("src/solutions.csv") as solutions:
                for line in solutions:
                    line = line.split(";")

                    if "+" in line[1]:
                        problem = line[1].split("+")
                        problem = int(problem[0]) + int(problem[1])
                        if problem == int(line[2]):
                            correct.write(f"{line[0]};{line[1]};{line[2]}")
                        else:
                            incorrect.write(f"{line[0]};{line[1]};{line[2]}")

                    if "-" in line[1]:
                        problem = line[1].split("-")
                        problem = int(problem[0]) - int(problem[1])
                        if problem == int(line[2]):
                            correct.write(f"{line[0]};{line[1]};{line[2]}")
                        else:
                            incorrect.write(f"{line[0]};{line[1]};{line[2]}")


if __name__ == "__main__":
    filter_solutions()