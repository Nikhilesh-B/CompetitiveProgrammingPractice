class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        saved_nums = {}
        for row, lst in enumerate(matrix):
            for col, num in enumerate(lst):
                coords = (row, col)
                if coords in saved_nums:
                    element = saved_nums[coords]
                    saved_nums.pop(coords)
                    saved_nums[(col, n-1-row)] = matrix[col][n-1-row]

                else:
                    element = num
                    saved_nums[(col, n-1-row)] = matrix[col][n-1-row]
                matrix[col][n-1-row] = element

from pprint import pprint
import numpy as np
import random 
if __name__ == "__main__":
    s = Solution()
    n = 20
    matrix = [[random.randint(0,9) for _ in range(n)] for _ in range(n)]
    print(*matrix, sep="\n")
    s.rotate(matrix=matrix)
    print("XXXXXXXXXX")
    print(*matrix, sep="\n")
