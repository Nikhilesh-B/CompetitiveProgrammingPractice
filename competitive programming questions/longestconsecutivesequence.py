from collections import Counter

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        freqs = Counter(nums)

        sorted_list = []

        for i in range(mn, mx+1):
            if i in freqs:
                sorted_list += [i for _ in range(freqs[i])]

        max_consec = 1
        curr_consec = 1

        for i, num in enumerate(sorted_list):
            if i>0:
                if num-sorted_list[i-1]==1:
                    curr_consec+=1
                    if curr_consec>max_consec:
                        max_consec=curr_consec
                else:
                    curr_consec=1

        return max_consec

import random
if __name__ == "__main__":
    sol = Solution()
    length = 10
    nums = [random.randint(int(-1*10**9),int(10**9)) for _ in range(10)]
    print("Ans=", sol.longestConsecutive(nums=nums))
