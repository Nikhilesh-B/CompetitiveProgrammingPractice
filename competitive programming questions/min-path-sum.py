class Solution:
    def get_children(self,row,col,m,n):
        neighs = []
        if row < m-1:
            neighs.append((row+1,col))
        if col < n-1:
            neighs.append((row, col+1))

        return neighs
    
    def replace(self, lst, val1, val2):
        idx1 = lst.index(val1)
        lst[idx1] = val2

    def minPathSum(self, grid: list[list[int]]) -> int:
        min_sum = 200**3+1
        m, n = len(grid), len(grid[0])
        q = [((0,0),grid[0][0])]
        sums = {(0,0):grid[0][0]}
        while q:
            (r, c), running_sum = q.pop(0)
            if r == m-1 and c == n-1:
                if running_sum<min_sum:
                    min_sum = running_sum
                    continue
                else:
                    continue
            
            elif running_sum>min_sum:
                continue

            else:      
                neighs = self.get_children(row=r, col=c, m=m, n=n)
                for row, col in neighs:
                    if (row, col) not in sums:
                        q.append(((row,col),running_sum+grid[row][col]))
                        sums[(row, col)] = running_sum+grid[row][col]
                    
                    elif sums[(row, col)] > running_sum+grid[row][col]:
                        self.replace(lst=q,
                                     val1=((row, col),sums[(row, col)]),
                                     val2=((row, col),running_sum+grid[row][col]))
                        sums[(row, col)] = running_sum+grid[row][col]

        return min_sum



import random
if __name__ == "__main__":
    s = Solution()
    grid = [[random.randint(1,200) for _ in range(200)] for _ in range (200)]
    print("Grid=", grid)
    ans = s.minPathSum(grid=grid)
    print('answer=',ans)