class NaiveSolution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        print(nums)
        #you store this as a heap so log(n) retrieval and only check the max
        saved_lengths = {}
        mx = 1
        for i, num in enumerate(nums):
            saved_lengths[num] = 1
            for j in range(0, i): 
                nlength = saved_lengths[nums[j]]+1
                if num > nums[j] and nlength>saved_lengths[num]:
                    saved_lengths[num] = nlength
                    if nlength > mx:
                        mx = nlength

        return mx

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        pass

import random

if __name__ == "__main__":
    ns = NaiveSolution()
    s = Solution()
    length = 5
    mn, mx = 0, 1000
    answer = ns.lengthOfLIS(nums=[random.randint(mn,mx) for _ in range(length)])
    print("The answer is", answer)