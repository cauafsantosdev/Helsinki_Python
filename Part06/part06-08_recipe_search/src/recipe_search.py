# Write your solution here

def recipes(filename: str):
    
    recipes = []
    temporary = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                recipes.append(temporary[:])
                temporary.clear()
            else:
                temporary.append(line)
        recipes.append(temporary[:])
    return recipes


def search_by_name(filename: str, word: str):
    recipe_list = recipes(filename)
    
    found = []

    for i in recipe_list:
        if word.lower() in i[0].lower():
            found.append(i[0])
    
    return found


def search_by_time(filename: str, prep_time: int):
    recipe_list = recipes(filename)
    
    found = []

    for i in recipe_list:
        if prep_time >= int(i[1]):
            found.append(f"{i[0]}, preparation time {i[1]} min")
    
    return found


def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = recipes(filename)
    
    found = []

    for i in recipe_list:
        if ingredient in i[2:]:
            found.append(f"{i[0]}, preparation time {i[1]} min")
    
    return found


if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)
    
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "milk")
    
    for recipe in found_recipes:
        print(recipe)