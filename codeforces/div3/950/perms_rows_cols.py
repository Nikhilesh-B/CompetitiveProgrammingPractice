def col_sorted(matrix):
    empty_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    copy_matrix = matrix.copy()
    for i in range(len(copy_matrix)):
        copy_matrix[i].sort()
    
    n = len(copy_matrix)
    first_vals_col1 = []
    idxs1 = [i for i in range(n)]
    for i in range(n):
        first_vals_col1.append(copy_matrix[i][0])
    
    zipped = list(zip(first_vals_col1, idxs1))
    zipped.sort(key=lambda x: x[0])
    idxs1 = [x[1] for x in zipped]

    for i, idx in enumerate(idxs1):
        empty_matrix[i] = copy_matrix[idx]
    
    return empty_matrix

def transpose(matrix):
    empty_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            empty_matrix[j][i] = matrix[i][j]
    return empty_matrix

def pretty_print_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    t = int(input())
    matrix1s = {}
    matrix2s = {}

    for i in range(t):
        n_m = list(map(int, input().split()))
        n = n_m[0]
        m = n_m[1]
        matrix1 = [[0 for _ in range(m)] for _ in range(n)]
        matrix2 = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(n):
            matrix1[j] = list(map(int, input().split()))
        
        for j in range(n):
            matrix2[j] = list(map(int, input().split()))
        
        matrix1s[i] = matrix1
        matrix2s[i] = matrix2

    for i in range(t):
        matrix1 = matrix1s[i]
        matrix2 = matrix2s[i]
        transposed_matrix1 = transpose(matrix1)
        transpose_matrix2 = transpose(matrix2)
        cond1 = (col_sorted(matrix1) == col_sorted(matrix2))   
        cond2 = (col_sorted(transposed_matrix1) == col_sorted(transpose_matrix2))

        if cond1 and cond2:
            print("YES")
        else:
            print("NO") 
