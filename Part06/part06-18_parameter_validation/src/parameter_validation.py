# Write your solution here

def new_person(name: str, age: int):
    if name == "":
        raise ValueError("Name input is empty")
    elif len(name.split()) < 2:
        raise ValueError("Name contains less than two words")
    elif len(name) > 40:
        raise ValueError("Name was too long")
    elif age < 0:
        raise ValueError("Age can't be negative")
    elif age > 150:
        raise ValueError("Nobody lives that much")
    else:
        data = name, age
        return data
    
if __name__ == "__main__":
    new_person()
