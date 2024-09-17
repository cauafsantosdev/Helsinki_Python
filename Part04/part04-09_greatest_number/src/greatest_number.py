# Write your solution here
# You can test your function by calling it within the following block

def greatest_number(n1,n2,n3):
    l = []
    l.append(n1)
    l.append(n2)
    l.append(n3)

    return max(l)


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)