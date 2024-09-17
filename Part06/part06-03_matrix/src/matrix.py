# write your solution here

def matrix():
    matrix_list = []
    with open("src/matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split(",")
            for i in range(len(line)):
                line[i] = int(line[i])
            matrix_list.append(line)

    return matrix_list


def matrix_sum():
    matrix_list = matrix()
    s = 0
    for i in matrix_list:
        s += sum(i)
    return s


def matrix_max():
    matrix_list = matrix()
    biggest = 0
    for i in matrix_list:
        line_biggest = max(i)
        if line_biggest > biggest:
            biggest = line_biggest
    return biggest


def row_sums():
    matrix_list = matrix()
    rows = []
    for i in matrix_list:
        rows.append(sum(i))
    return rows


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())