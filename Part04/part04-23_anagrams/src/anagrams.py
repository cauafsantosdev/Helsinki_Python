# Write your solution here

def anagrams(word1 : str, word2 : str):
    sorted1 = sorted(word1)
    sorted2 = sorted(word2)
    if sorted1 == sorted2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams())