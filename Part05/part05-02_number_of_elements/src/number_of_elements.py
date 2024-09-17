# Write your solution here

def count_matching_elements(matrix: list, character: int):
    i = 0
    for j in matrix:
        for k in j:
            if k == character:
                i += 1
    return i

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))