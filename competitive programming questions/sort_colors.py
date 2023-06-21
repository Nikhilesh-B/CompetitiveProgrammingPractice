import random
class Solution(object):
    def sort_colors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        basic counting sort implementation
        """
        zeros, ones, twos = 0, 0, 0
        for num in nums: 
            if num == 0:
                zeros += 1 
            elif num == 1:
                ones += 1
            else: 
                twos += 1

        length = zeros+ones+twos

        for i in range(length):
            if i < zeros:
                nums[i] = 0
            elif i < ones+zeros: 
                nums[i] = 1
            else:
                nums[i] = 2
s = Solution()
nums = [1, 2, 0, 0, 1, 2]
n_copy = sorted(nums)
print(n_copy, nums)
s.sort_colors(nums)
print(nums)
print(nums==n_copy)

