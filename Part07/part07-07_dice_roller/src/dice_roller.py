# Write your solution here

def roll(die: str):
    from random import randint

    dice_a = [3, 3, 3, 3, 3, 6]
    dice_b = [2, 2, 2, 5, 5, 5]
    dice_c = [1, 4, 4, 4, 4, 4]

    if die in "Aa":
        side = randint(0, 5)
        return dice_a[side]
    elif die in "Bb":
        side = randint(0, 5)
        return dice_b[side]
    elif die in "Cc":
        side = randint(0, 5)
        return dice_c[side]
    

def play(die1: str, die2: str, times: int):
    results = ()
    one = two = draw = 0

    for i in range(times):
        dice1 = roll(die1)
        dice2 = roll(die2)
        if dice1 > dice2:
            one += 1
        elif dice2 > dice1:
            two += 1
        else:
            draw += 1
    
    results = one, two, draw
    return results
        
    
if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)

