import numpy as np 
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        triggered = False
        print("ID=",id(nums),nums)


        if nums == sorted(nums, reverse=True):
            nums.sort()
            triggered = True

        if not triggered:
            for i in range(len(nums)-1,1,-1):
                if nums[i]>nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    triggered = True 
                    print(nums)
                    break


        def find_closest_zero(nums):
            inum = nums[0]
            mn = 101
            idx = None
            for i, n in enumerate(nums):
                if abs(n-inum)<mn and abs(n-inum)!=0 and n>inum:
                    mn = abs(n-inum)
                    idx = i
            return idx

        print("ID=",id(nums),nums)
        if not triggered:
            i = find_closest_zero(nums)
            x = sorted(nums[0:i]+nums[i+1:])
            nums[0] = nums[i]

            for i in range(1, len(nums)):
                nums[i] = x[i-1]

            print("ID=",id(nums),nums)


if __name__ == "__main__":
    s = Solution()
    nums = [np.random.choice([0,1,2,3,4,5,6,7,8,9]) for _ in range(2)]
    print(nums)
    s.nextPermutation(nums=nums)
    print(nums)