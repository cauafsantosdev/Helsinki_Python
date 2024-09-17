# Write your solution here

f = int(input("Please type in a temperature (F): "))
celsius = (f - 32) * 5 / 9

if celsius < 0:
    print(f"{f} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{f} degrees Fahrenheit equals {celsius} degrees Celsius")