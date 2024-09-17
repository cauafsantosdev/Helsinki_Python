# Write your solution here

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    film = {"name": name, "director": director, "year": year, "runtime": runtime}
    database += [film]

if __name__ == "__main__":
    database = []
    add_movie(database, "Close-Up", "Abbas Kiarostami", 1990, 90)
    print(database)