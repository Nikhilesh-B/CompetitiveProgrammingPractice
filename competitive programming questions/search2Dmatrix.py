class Solution:
    def binary_search(self, lst, target):
        print(lst)
        mid = len(lst)//2
        if len(lst) == 1:
            if lst[0]==target: return True 
            else: return False
        if lst[mid] > target:
            return self.binary_search(lst[0:mid], target)
        else:
            return self.binary_search(lst[mid:], target)


    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        sorted_lst = []
        for row in matrix:
            sorted_lst += row
        return self.binary_search(sorted_lst, target)

    def printMatrix(self, matrix):
        print("[")
        for row in matrix: 
            print(','.join(map(str, row)))
        print("]")



if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 99
    sol = Solution()
    sol.printMatrix(matrix=matrix)
    print(sol.searchMatrix(matrix=matrix,target=99))



