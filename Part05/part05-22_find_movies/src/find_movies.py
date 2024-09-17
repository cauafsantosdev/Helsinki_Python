# Write your solution here

def find_movies(database: list, search_term: str):
    films = []
    for film in database:
        if search_term in film["name"].lower():
            films += [film]
    return films

if __name__ == "__main__":
    database = []
    my_films = find_movies()
    print(my_films)