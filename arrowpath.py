t = int(input())

move_dic = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}


def potential_moves(x, y, n):
    moves = []
    if y == 1:
        moves.append("U")
        if x > 1:
            moves.append("L")
        if x < n:
            moves.append("R")
    if y == 2:
        moves.append("D")
        if x > 1:
            moves.append("L")
        if x < n:
            moves.append("R")
    return moves


def new_square(x, y, grid):
    if grid[x-1][y-1] == ">":
        return x+1, y
    else:
        return x-1, y


for _ in range(t):
    top_line = input().split("")
    bottom_line = input().split("")
    grid = [top_line, bottom_line]
    n = len(top_line)
    x0, y0 = 1, 1
    xg, yg = n, 2
    q = []
    explored = set()

    moves = potential_moves(x0, y0, n)
    moves = [(x0+move_dic[m][0], y0+move_dic[m][1]) for m in moves]
    moves = [new_square(m[0], m[1], grid) for m in moves]
    q += moves

    while q:
        explored_node = q.pop(0)
        if explored_node == (xg, yg):
            print("YES")
        x0, y0 = explored_node[0], explored_node[1]
        moves = potential_moves(x0, y0, n)
        moves = [(x0+move_dic[m][0], y0+move_dic[m][1]) for m in moves]
        moves = [new_square(m[0], m[1], grid) for m in moves]
        moves = [m for m in moves if m not in explored]
        q += moves
        explored.add(explored_node)
    print("NO")
