class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        closest_num = 101
        closest_j = None
        if len(nums)==1:
            return

        for i in range(len(nums)-2,0,-1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j] and nums[j]<closest_num:
                    closest_num = nums[j]
                    closest_j = j

            if closest_j != None:
                nums_i = nums[i]
                nums[i] = nums[closest_j]
                nums[closest_j] = nums_i
                new_nums = sorted(nums[i+1:])
                m = 0
                for x in range(i+1, len(nums)):
                    nums[x] = new_nums[m]
                    m+=1
                break
            

        if closest_num == 101:
            nums.sort()

import random            
if __name__ == "__main__":
    sol = Solution()
    nums = [random.randint(0,100) for _ in range(100)]
    print(nums)
    sol.nextPermutation(nums=nums)
    print(nums)
