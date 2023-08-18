def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val}\t", end="")
        print()


def abbreviation(a,b):
    n = len(a)
    m = len(b)  
    saved_sols = [[None for j in range(m)] for i in range(n)]   
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            real_i, real_j = n-1-i, m-1-j
            if a[real_i] == b[real_j]:
                if real_i == 0 or real_j == 0:
                    saved_sols[i][j] = True
                else:
                    saved_sols[i][j] = saved_sols[i+1][j+1]
            
            else:
                if a[real_i].islower():
                    if a[real_i].islower() and a[real_i].upper() == b[real_j]:
                        if real_i == 0 or real_j == 0:
                            saved_sols[i][j] = True
                        else:
                            saved_sols[i][j] = saved_sols[i+1][j] or saved_sols[i+1][j+1] 
                    else:
                        if real_i == 0 or real_j == 0:
                            saved_sols[i][j] = True
                        else:
                            saved_sols[i][j] = saved_sols[i+1][j]
    if saved_sols[0][0]:
        return "YES"
    else:
        return "NO"



a, b = "beFgH", "EFH"



print(abbreviation(a,b))



