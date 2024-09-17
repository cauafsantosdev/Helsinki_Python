# Write your solution here

def longest(a: list):
    longest = a[0]
    for i in a:
        if len(i) > len(longest):
            longest = i
    return longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))