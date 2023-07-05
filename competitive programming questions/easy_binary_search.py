class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)
        while high-low>1:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid 

            else:
                high = mid
                
        
        if nums[low] == target:
            return low
        
        else:
            return -1
        

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    sol = Solution()
    ans = sol.search(nums=nums, target=1)
    print('the answer is =', ans)