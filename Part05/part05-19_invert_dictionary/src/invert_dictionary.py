# Write your solution here

def invert(dictionary: dict):
    t = {}
    
    for k, v in dictionary.items():
        t[v] = k

    dictionary.clear()

    for k, v in t.items():
        dictionary[k] = v

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)