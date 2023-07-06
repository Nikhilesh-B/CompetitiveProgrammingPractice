from operator import xor 
class Solution:
    def print_mat(self, matrix):
        print('[')
        for row in matrix:
            print('  [' + ', '.join(map(str, row)) + ']')
        print(']')
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        self.modify_zeros(matrix=matrix)

        for r, row in enumerate(matrix):
            for c, element in enumerate(row):
                if element == 'A':
                    self.modfiy_cols_rows(matrix, r, c)
                    self.print_mat(matrix)

    def modfiy_cols_rows(self, matrix, x, y):
        for r, row in enumerate(matrix):
            for c, element in enumerate(row):
                if r == x or c == y:
                    if xor(r==x, c==y) and element=='A':
                        continue
                    else:
                        matrix[r][c] =0



    def modify_zeros(self, matrix):
        for r, row in enumerate(matrix):
            for c, element in enumerate(row):
                if element == 0:
                    matrix[r][c] = 'A'


import random

if __name__ == "__main__":
    sol = Solution()
    m=10
    n=11
    matrix = [[random.randint(0,9) for _ in range(m)] for _ in range(n)]
    print("Original matrix")
    print(str(matrix))
    sol.setZeroes(matrix=matrix)
    print("New matrix")
    print(str(matrix))