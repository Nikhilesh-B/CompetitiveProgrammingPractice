

import numpy as np

class Solution:
    def max_idx(self, nums):
        mx = max(nums)
        ridx = -1
        for j, n in enumerate(nums):
            if n == mx:
                ridx = j
        return ridx
    
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        cmax = -1*np.inf
        for i in range(len(nums)-k+1):
            if i==0: 
                max_idx = self.max_idx(nums[i:i+k])
                ans.append(nums[max_idx])
                cmax = nums[max_idx]
            
            else:
                if nums[i+k-1] > cmax:
                    max_idx = i+k-1
                    cmax = nums[i+k-1]
                    ans.append(nums[max_idx])
                elif max_idx<i:
                    max_idx = i+self.max_idx(nums[i:i+k])
                    cmax = nums[max_idx]
                    ans.append(nums[max_idx])
                else:
                    ans.append(cmax)

                        

        return ans

import random
if __name__ == "__main__":
    sol = Solution()
    lst = [random.randint(-1*int(10**4),int(10**4)) for _ in range(int(10**5))]
    max_sliding_window = sol.maxSlidingWindow(nums=lst, k=50000)
    print("Maximum sliding window =", max_sliding_window)

