# Write your solution here
# You can test your function by calling it within the following block

def same_chars(string, int1, int2):
    if int1 >= len(string) or int2 >= len(string):
        return False
    return string[int1] == string[int2]


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))