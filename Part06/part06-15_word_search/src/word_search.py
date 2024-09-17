# Write your solution here

def dot_wildcard(search_term: str, word: str):
    same = True
    for i in range(len(word)):
        if search_term[i] != '.' and search_term[i] != word[i]:
            same = False
    return same


def find_words(search_term: str):
    search_term = search_term.lower()
    found = []

    with open("src/words.txt") as words:
        word_list = [line.strip() for line in words]

    if search_term.endswith("*"):
        search_term = search_term.rstrip("*")
        for word in word_list:
            if word.startswith(search_term):
                found.append(word)
        
    elif search_term.startswith("*"):
        search_term = search_term.lstrip("*")
        for word in word_list:
            if word.endswith(search_term):
                found.append(word)

    elif "." in search_term:
        for word in word_list:
            if len(search_term) == len(word):
                if dot_wildcard(search_term, word) == True:
                    found.append(word)
    else:
        for word in word_list:
            if search_term == word:
                found.append(word)
        
    return found


if __name__ == "__main__":
    print(find_words(".a.e"))