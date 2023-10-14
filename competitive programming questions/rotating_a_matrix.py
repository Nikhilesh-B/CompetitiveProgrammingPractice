from copy import copy


def rotate_matrix(matrix):
    copy_of_matrix = copy(matrix)
    n = len(matrix)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            new_col = (i+n) % n
            new_row = (j+n) % n
            copy_of_matrix[new_row][new_col] = val

    return copy_of_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    # [13, 9, 5, 1]
    # [14, 10, 6, 2]
    # [15, 11, 7, 3]
    # [16, 12, 8, 4]
    rotated_matrix = rotate_matrix(matrix)
    print(rotated_matrix)
