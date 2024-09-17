# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            n = sudoku[i][j]
            if n > 0 and n in numbers:
                return False
            else:
                numbers.append(n)
    return True

if __name__ == "__main__":
 
    sudoku = []
    block_correct()