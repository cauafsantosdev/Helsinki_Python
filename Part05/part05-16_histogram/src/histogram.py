# Write your solution here

def histogram(string : str):
    d = {}
    for i in string:
        if i not in d:
            d[i] = 0
        d[i] += 1
    
    for key, value in d.items():
        print(f"{key} {value*'*'}")


if __name__ == "__main__":
    histogram()