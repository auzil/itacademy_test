# №5
# Напишите алгоритм нахождения определителя матрицы размерностью 4Х4.
#
# №9
# Напишите, без использования стандартных библиотек, программу нахождения определителя матрицы любой размерности.


def print_matrix(matrix):
    for matrix_row in matrix:
        print(matrix_row)


def get_new_matrix_index(current_index, exclude_index):
    new_index = current_index

    if exclude_index < current_index:
        new_index = current_index - 1

    return new_index


def get_minor(matrix, row_index, col_index):
    new_matrix = []
    matrix_range = range(len(matrix))

    for i in matrix_range:
        if i != row_index:
            new_matrix_i = get_new_matrix_index(i, row_index)
            new_matrix.append([])

            for j in matrix_range:
                if j != col_index:
                    new_matrix[new_matrix_i].append(matrix[i][j])

    return new_matrix


def determinant(matrix):
    m = len(matrix)
    n = len(matrix[0])

    if m != n:
        return None
    if n == 1:
        return matrix[0][0]

    sig = 1
    det = 0

    for i in range(n):
        det += matrix[0][i] * sig * determinant(get_minor(matrix, 0, i))
        sig *= -1

    return det


matrix = [
    [2, 3, 0, 4, 5],
    [0, 1, 0, -1, 2],
    [3, 2, 1, 0, 1],
    [0, 4, 0, -5, 0],
    [1, 1, 2, -2, 1],
]

print_matrix(matrix)
print(determinant(matrix))

matrix = [
    [2, 3, 0, 4],
    [0, 1, 0, -1],
    [3, 2, 1, 0],
    [0, 4, 0, -5],
]

print_matrix(matrix)
print(determinant(matrix))
