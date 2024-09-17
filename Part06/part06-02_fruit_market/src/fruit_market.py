# write your solution here

def read_fruits():
    prices = {}
    with open("src/fruits.csv") as file:
        
        for line in file:
            fruit = line.split(";")
            prices[fruit[0]] = float(fruit[1])

    return prices
    

if __name__ == "__main__":
    print(read_fruits())
