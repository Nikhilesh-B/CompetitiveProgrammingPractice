import numpy as np

class Solution:
    def print_matrix(self, matrix):
        print("[")
        for row in matrix: 
            print(','.join(map(str, row)))
        print("]")

    def recompute_tuple(self, curr_tuple, order_zero):
        if order_zero=='R':
             return (curr_tuple[0],curr_tuple[1]+1)
            
        elif order_zero=='D':
             return (curr_tuple[0]+1,curr_tuple[1])
        
        elif order_zero=='L':
            return (curr_tuple[0],curr_tuple[1]-1)
        
        else:
            return (curr_tuple[0]-1,curr_tuple[1])

    def get_back_in_bounds(self, curr_tuple, order_zero):
        if order_zero=='R':
             return (curr_tuple[0],curr_tuple[1]-1)
            
        elif order_zero=='D':
             return (curr_tuple[0]-1,curr_tuple[1])
        
        elif order_zero=='L':
            return (curr_tuple[0],curr_tuple[1]+1)
        
        else:
            return (curr_tuple[0]+1,curr_tuple[1])

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        matrix = np.array(matrix)
        m = len(matrix)
        n = len(matrix[0])
        total_length = m*n
        spiral_order = []
        curr_tuple = (0,0) 
        accounted_tuples = set()
        order = ["R","D","L","U"]
        while len(spiral_order)!=total_length:
            if curr_tuple in accounted_tuples or curr_tuple[0]<0 or curr_tuple[0]>m-1 or curr_tuple[1]<0 or curr_tuple[1]>n-1:
                curr_tuple = self.get_back_in_bounds(curr_tuple,order_zero=order[0])
                order = order[1:]+[order[0]]
                curr_tuple = self.recompute_tuple(curr_tuple, order_zero=order[0])

            spiral_order.append(matrix[curr_tuple])
            accounted_tuples.add(curr_tuple)

            print(order)
            curr_tuple = self.recompute_tuple(curr_tuple, order_zero=order[0])

        return spiral_order

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.print_matrix(matrix=matrix)
    print(sol.spiralOrder(matrix=matrix))
