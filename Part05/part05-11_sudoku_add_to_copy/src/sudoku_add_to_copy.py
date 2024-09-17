# Write your solution here

def print_sudoku(sudoku: list):
    cr = cc = 0
    for i in sudoku:
        for j in i:
            cr += 1
            if j == 0:
                print("_", end=" ")
            else:
                print(f"{j}", end=" ")
            if cr % 3 == 0:
                print(" ", end="")
        print()
        cc += 1
        if cc % 3 == 0:
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new = []
    for i in sudoku:
        temporary = []
        for j in i:
            temporary.append(j)
        new.append(temporary)
    new[row_no][column_no] = number
    return new


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)