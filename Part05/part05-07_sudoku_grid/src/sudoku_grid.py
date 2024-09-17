# Write your solution here

def row_correct(sudoku: list, row_no: int):
    for i, j in enumerate(sudoku[row_no]):
        if sudoku[row_no].count(i+1) > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int):
    column = []
    for i in sudoku:
        if i[column_no] > 0:
            column.append(i[column_no])

    for i in column:
        if column.count(i) > 1:
            return False
    return True


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


def sudoku_grid_correct(sudoku: list):
    for row in range(0, 9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0, 9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if not block_correct(sudoku, row, column):
                return False
            
    return True

if __name__ == "__main__":
 
    sudoku = []
    sudoku_grid_correct()