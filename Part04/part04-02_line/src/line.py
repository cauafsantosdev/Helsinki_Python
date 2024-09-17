# Write your solution here
# You can test your function by calling it within the following block

def line(a: int, b: str):
    if b == "":
        b = "*"
    print(b[0] * a)

if __name__ == "__main__":
    line(3, "")