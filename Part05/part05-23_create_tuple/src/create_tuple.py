# Write your solution here

def create_tuple(x: int, y: int, z: int):
    tuple = (min(x, y, z), max(x, y, z), (x + y + z))
    return tuple


if __name__ == "__main__":
    print(create_tuple())