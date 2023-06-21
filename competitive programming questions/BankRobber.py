class Solution:
    def rob(self, nums: list[int]) -> int:
        print(nums)
        saved_robberies = {}
        mx = 0
        for i, num in enumerate(nums):
            saved_robberies[i] = num
            if i == 0:
                mx = num
                continue

            elif i == 1:
                if num > mx:
                    mx = num
                continue 

            neigbors = [i-j for j in range(2,4)]
            neigbors = filter(lambda x: x>=0, neigbors)

            highest_val = max([saved_robberies[n] for n in neigbors])

            if saved_robberies[i] < num+highest_val:
                saved_robberies[i] = num+highest_val
                if saved_robberies[i] > mx:
                    mx = saved_robberies


        return mx


import random
if __name__ == "__main__":
    s = Solution()
    nums = [10,2]
    # nums = [1,2,3,1]
    ans = s.rob(nums=nums)
    print("Answer=",ans)