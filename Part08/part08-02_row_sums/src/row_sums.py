# Write your solution here

def row_sums(my_matrix: list):
    for i in range(0, len(my_matrix)):
        my_matrix[i].append(sum(my_matrix[i]))


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)