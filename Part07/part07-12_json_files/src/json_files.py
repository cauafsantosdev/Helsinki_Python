# Write your solution here

def read_json(filename: str):
    import json

    with open(filename) as file:
        data = file.read()
    
    people = json.loads(data)
    return people


def print_persons(filename: str):
    people = read_json(filename)

    for person in people:
        print(f"{person["name"]} {person["age"]} years ({", ".join(person["hobbies"])})")


if __name__ == "__main__":
    print_persons("src/file1.json")