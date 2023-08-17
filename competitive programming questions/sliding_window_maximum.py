import numpy as np
import heapq

class Solution:
    def find_idx(self, ordered_lst, val):
        mid = len(ordered_lst)//2
        if not ordered_lst:
            return -1
        if ordered_lst[mid]==val:
            return mid
        elif ordered_lst[mid]<val:
            return mid+1+self.find_idx(ordered_lst[mid+1:],val=val)
        else:
            return self.find_idx(ordered_lst[:mid],val=val)
        

    def insert_val(self, val):
        idx = self.find_idx(ordered_lst=self.ordered_nums, val=val)
        self.ordered_nums = self.ordered_nums[:idx+1]+[val]+self.ordered_nums[idx+1:]
        

    def delete_val(self, val):
        idx = self.find_idx(ordered_lst=self.ordered_nums, val=val)
        self.ordered_nums = self.ordered_nums[:idx]+self.ordered_nums[idx+1:]

    def max_idx(self, nums):
        mx = max(nums)
        ridx = -1
        for j, n in enumerate(nums):
            if n == mx:
                ridx = j
        return ridx
    
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        for i in range(len(nums)-k+1):
            if i==0: 
                self.ordered_nums = sorted(nums[i:i+k].copy())
            ans.append(self.ordered_nums[-1])
            prev_num = nums[i]
            next_num = nums[i+k]
            self.delete_val(prev_num)
            self.insert_val(next_num)

        return ans

import random
if __name__ == "__main__":
    sol = Solution()
    # ordered_lst = [1,2,3,4,9,100]
    # sol.delete_val(val=100)
    # print(sol.ordered_nums)
    lst = [random.randint(-1*int(10**4),int(10**4)) for _ in range(int(10**5))]
    max_sliding_window = sol.maxSlidingWindow(nums=lst, k=50000)
    print("Maximum sliding window =", max_sliding_window)

