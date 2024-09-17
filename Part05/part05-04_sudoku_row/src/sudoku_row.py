# Write your solution here

def row_correct(sudoku: list, row_no: int):
    for i, j in enumerate(sudoku[row_no]):
        if sudoku[row_no].count(i+1) > 1:
            return False
    return True


if __name__ == "__main__":
    sudoku = []
    row_correct()