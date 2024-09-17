# Write your solution here

word = input("Word: ")

start = (28 - len(word)) // 2
if len(word) % 2 == 0:
    end = start
else:
    end = start+1


print('*' * 30)
print(f"*{(start * ' ')}{word}{(end * ' ')}*")
print('*' * 30)