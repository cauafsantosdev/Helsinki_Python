# Write your solution here

n = int(input("Layers: "))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

left = ""    
right = ""    
char = n - 1       
repeat = 2 * n - 1   

while char >= 1:
    left = left + letters[char]
    right = letters[char] + right
    repeat -= 2
    print(left + letters[char] * repeat + right)
    char -= 1

while char <= n - 1:
    print(left + letters[char] * repeat + right)
    left = left[:-1]
    right = right[1:]
    repeat += 2
    char += 1