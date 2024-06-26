import sys
def neighbors(r, c, m, n):
    row_neighbors = []
    col_neighbors = []
    if r != 0:
        row_neighbors.append((r-1, c))
    if c != 0:
        col_neighbors.append((r, c-1))
    if r != m-1:
        row_neighbors.append((r+1, c))
    if c != n-1:
        col_neighbors.append((r, c+1))
    return row_neighbors, col_neighbors



def transpose(matrix, m, n):
    new_matrix = []
    for c in range(n):
        new_row = []
        for r in range(m):
            new_row.append(matrix[r][c])
        new_matrix.append(new_row)
    return new_matrix


def matrix_has_at_least_row_all_ones(matrix):
    rval = False
    for row in matrix:
        rval = rval or (sum(row) == len(row))
    return rval


if __name__ == "__main__":
    m_n = list(map(int, input().split(" ")))
    m = m_n[0]
    n = m_n[1]
    matrix = []

    for r in range(m):
        row = list(map(int, input().split(" ")))
        matrix.append(row)

    ones = False
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 1:
                ones = True
                row_neighs, col_neighs = neighbors(r, c, m, n)
                row_bool = False
                for rn in row_neighs:
                    row_bool = row_bool or (matrix[rn[0]][rn[1]] == 1)
                col_bool = False
                for cn in col_neighs:
                    col_bool = col_bool or (matrix[cn[0]][cn[1]] == 1)
                if not (row_bool or col_bool) and not (m == 1 and n == 1):
                    print("NO")
                    sys.exit(0)

    if ones:
        if not (matrix_has_at_least_row_all_ones(matrix) and matrix_has_at_least_row_all_ones(transpose(matrix, m, n))):
            print("NO")
            sys.exit(0)

    print("YES")

    r_matrix = [[0 for _ in range(n)] for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 1:
                mark_value = True
                row_neighs, col_neighs = neighbors(r, c, m, n)
                for rn in row_neighs:
                    mark_value = mark_value and (matrix[rn[0]][rn[1]] == 1)
                for cn in col_neighs:
                    mark_value = mark_value and (matrix[cn[0]][cn[1]] == 1)
                r_matrix[r][c] = 1 if mark_value else 0

    for r in range(m):
        for c in range(n):
            if c != n-1:
                print(r_matrix[r][c], end=" ")
            else:
                print(r_matrix[r][c])
