# Write your solution here

def column_correct(sudoku: list, column_no: int):
    column = []
    for i in sudoku:
        if i[column_no] > 0:
            column.append(i[column_no])

    for i in column:
        if column.count(i) > 1:
            return False
    return True

if __name__ == "__main__":
    sudoku = []
    column_correct()