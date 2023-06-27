from pprint import pprint
from itertools import permutations

class Solution:
    def valid_perm(self, perm):
        length = len(perm)
        for i in range(length):
            for j in range(i+1, length):
                num1, num2 = perm[i], perm[j]
                if j-i == abs(num1-num2):
                    return False
        return True

    def solveNQueens(self, n: int) -> list[list[str]]:
        board_configs = {i:"."*i+"Q"+"."*(n-1-i) for i in range(n)}
        row_orders = [j for j in range(n)]

        perms_row_orders = permutations(row_orders)
        valid_row_orders = []

        for perm in perms_row_orders:
            if self.valid_perm(perm):
                valid_row_orders.append(perm)
        
        valid_board_configs = []

        for valid_row_order in valid_row_orders:
            board_config = []
            for row in valid_row_order:
                board_config.append(board_configs[row])
            valid_board_configs.append(board_config)

        return valid_board_configs

if __name__ == "__main__":
    s = Solution()
    ans = s.solveNQueens(n=8)
    pprint(ans)
