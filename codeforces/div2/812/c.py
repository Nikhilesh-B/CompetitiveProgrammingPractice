import bisect

t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    perm = [-1 for _ in range(n)]

    squares = []
    i = 0
    while i**2 <= 2*n-2:
        squares.append(i**2)
        i += 1

    fail_flag = False

    for j in range(n-1, -1, -1):
        j_max = j+n-1
        ridx = bisect.bisect_right(squares, j_max)
        lidx = bisect.bisect_left(squares, j)
        if ridx == len(squares):
            possible_squares = squares[lidx:ridx]
        else:
            possible_squares = squares[lidx:ridx]

        for idx in range(len(possible_squares)-1, -1, -1):
            square = possible_squares[idx]
            insert_i = square - j
            # print(possible_squares, j)
            # print("INSERT I ", insert_i)
            if perm[insert_i] == -1:
                perm[insert_i] = j
                break

            # print(perm)
            # print("IDX", idx)
            if idx == 0:
                fail_flag = True
                break

        if fail_flag:
            break

    if fail_flag:
        print(-1)

    else:
        print(" ".join(map(str,perm)))
