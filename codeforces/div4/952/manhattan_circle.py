def process_case(grids, t_i):
    n, m = dims[t_i]
    grid = grids[t_i]
    ans = 0
    first_row, last_row = n+1, -1
    first_col, last_col = m+1, -1

    for rw in range(n):
        for cl in range(m):
            if grid[rw][cl] == '#':
                first_row = min(first_row, rw)
                last_row = max(last_row, rw)
                first_col = min(first_col, cl)
                last_col = max(last_col, cl)

    center_row = (first_row + last_row) // 2
    center_col = (first_col + last_col) // 2

    print(center_row+1, center_col+1)


if __name__ == "__main__":
    t = int(input())
    dims = {}
    grids = {}

    for t_i in range(t):
        n_m = list(map(int, input().split()))
        n, m = n_m
        grid = []
        for _ in range(n):
            row_str = input()
            row = [row_str[i] for i in range(m)]
            grid.append(row)

        dims[t_i] = (n, m)
        grids[t_i] = grid

    for t_i in range(t):
        process_case(grids, t_i)
