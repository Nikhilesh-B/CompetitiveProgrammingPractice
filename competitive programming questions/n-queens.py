from pprint import pprint
from itertools import permutations

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board_configs = {i:"."*i+"Q"+"."*(n-1-i) for i in range(n)}
        row_orders = [j for j in range(n)]
        pass

if __name__ == "__main__":
    s = Solution()
    ans = s.solveNQueens(n=4)
    pprint(ans)
