from collections import Counter 
import random


class Solution: 
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum%2==1: return False
        desired_sum = total_sum//2
        sums = self.findSums(nums=nums)
        return desired_sum in sums

    
    def findSums(self, nums):
        if len(nums)==1 or len(nums)==0:
            return nums
        else:
            mid = len(nums)//2
            l1, l2 = nums[:mid], nums[mid:]
            set1 = set(self.findSums(l1))
            set2 = set(self.findSums(l2))
            return set1 | set2 | {s1+s2 for s1 in set1 for s2 in set2}


from random import randint

if __name__ == "__main__":
    length = 100 
    #nums = [randint(1,100) for _ in range(200)]
    nums = [43,87,61,26,73,64,23,9,54,100,14,47,75,49,90,50,62,96,18,86,95,27,87,67,67,92,82,19,53,86,15,37,83,81,59,84,47,11,80,6,14,58,72,13,78,31,56,72,94,79,67,86,25,85,19,54,50,11,52,95,100,37,96,88,71,45,77,58,13,12,49,83,50,20,2,54,84,51,3,25,42,30,92,35,91,68,57,19,4,87,15,17,6,94,84,85,91,31,47,33]
    print(nums)
    sol = Solution()
    ans = sol.canPartition(nums=nums)
    print("The answer is", ans)