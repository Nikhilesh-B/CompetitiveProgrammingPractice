from typing import List


class Solution:
    def neighbors(self, maze: List[List[str]], pos: List[int]) -> List[List[int]]:
        r, c = pos[0], pos[1]
        neighs = []
        for vert, hor in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if len(maze) > r+vert > -1 and len(maze[0]) > c+hor > -1 and maze[r+vert][c+hor] == '.':
                neighs.append([r+vert, c+hor])

        return neighs

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        explored = set(tuple(entrance))
        entrance += [0]
        q = [entrance]
        while q:
            node = q.pop(0)
            r, c, d = node[0], node[1], node[2]
            if (r == 0 or c == 0 or r == len(maze)-1 or c == len(maze[0])-1) and (r != entrance[0] or c != entrance[1]):
                return d

            neighs = self.neighbors(maze, node)

            for neigh in neighs:
                coord = tuple(neigh)
                if coord not in explored:
                    explored.add(coord)
                    q.append([neigh[0], neigh[1], d+1])

        return -1


if __name__ == "__main__":
    maze = [[".","+"]]
    entrance = [0, 0]
    print(Solution().nearestExit(maze, entrance))
