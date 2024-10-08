# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height})"
    

class Room:

    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return len(self.people) == 0
    
    def print_contents(self):
        total_height = sum([i.height for i in self.people])

        print(f"There are {len(self.people)} persons in this room, and their combined height is {total_height} cm")
        for person in self.people:
            print(f"{person.name} ({person.height} kg)")

    def shortest(self):
        if not self.is_empty():
            return min(self.people, key=lambda p: p.height)
        
        return None
    
    def remove_shortest(self):
        if not self.is_empty():
            to_remove = self.shortest()
            self.people.remove(to_remove)
            return to_remove
        
        return None
    

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

