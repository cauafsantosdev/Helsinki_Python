# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def line(a: int, b: str):
    if b == "":
        b = "*"
    print(b[0] * a)


def shape(s1, c1, s2, c2):
    for i in range(1, s1 + 1):
        line(i, c1)
    for i in range(1, s2 + 1):
        line(s1, c2)


if __name__ == "__main__":
    shape(5, "x", 2, "o")