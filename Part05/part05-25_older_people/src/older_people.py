# Write your solution here

def older_people(people: list, year: int):
    name = []
    for i in range(len(people)): 
        if people[i][1] < year:
            name += [people[i][0]]
    return name


if __name__ == "__main__":
    p1 = ()
    p2 = ()
    p3 = ()
    p4 = ()
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)