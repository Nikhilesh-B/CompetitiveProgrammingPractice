#divide and conquer type of algorithm 
import numpy as np
class Solution:
    def printMatrix(self, matrix):
        print("[")
        for row in matrix: 
            print(','.join(map(str, row)))
        print("]")
    def searchMatrixNaive(self, matrix: list[list[int]], target: int) -> bool:
        possible_rows = []
        possible_cols = []
        t_matrix = list(zip(*matrix))

        for row_no, row in enumerate(matrix):
            if row[0]<=target and target<=row[len(matrix[0])-1]:
                possible_rows.append(row_no)

        for row_no, row in enumerate(t_matrix):
            if row[0]<=target and target<=row[len(t_matrix[0])-1]:
                possible_cols.append(row_no)
        
        for row_no in possible_rows:
            for col_no in possible_cols:
                if matrix[row_no][col_no] == target:
                    return True
                
        return False 

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if type(matrix) != np.array:
            matrix = np.array(matrix)

        m, n = len(matrix)-1, len(matrix[0])-1
        if m<2 and n<2:
            return self.searchMatrixNaive(matrix=matrix, target=target)
        
        booleans = []
        #1
        top_lft_corner = matrix[0][0]
        middle = matrix[int(m//2)][int(n//2)]
        
        if top_lft_corner<=target and target<=middle:
            if top_lft_corner == target or middle == target:
                return True
            else:
                booleans.append(self.searchMatrix(matrix=matrix[:int(m//2)+1,:int(n//2)+1],target=target))
        #2
        top_edge = matrix[0][int(n//2)]
        right_edge = matrix[int(m//2)][n]

        if top_edge<=target and target<=right_edge:
            if top_edge == target or right_edge == target:
                return True
            else:
                booleans.append(self.searchMatrix(matrix=matrix[:int(m//2)+1,int(n//2):],target=target))


        #3
        left_edge = matrix[int(m//2)][0]
        bottom_edge = matrix[m][int(n//2)]

        if left_edge<=target and target<=bottom_edge:
            if left_edge == target or bottom_edge == target:
                return True
            else:
                booleans.append(self.searchMatrix(matrix=matrix[int(m//2):,:int(n//2)+1],target=target))


        #4
        bottom_right_corner = matrix[m][n]
        if middle<=target and target<=bottom_right_corner:
            if middle == target or bottom_right_corner == target:
                return True
            else:
                booleans.append(self.searchMatrix(matrix=matrix[int(m//2):,int(n//2):],target=target))
        return any(booleans)

if __name__ == "__main__":
    sol = Solution()
    length = 200
    nums = [i for i in range(int(length**2))]
    matrix = np.array([[nums[x+y*length] for x in range(length)] for y in range(length)])
    sol.printMatrix(matrix)
    print(sol.searchMatrix(matrix=matrix,target=6))