from collections import Counter

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        freqs = set(nums)
        for f in freqs.copy():
            if f-1 not in freqs and f+1 not in freqs:
                freqs.discard(f)
        
        if not freqs:
            return 0

        mn = min(freqs)
        mx = max(freqs)

        sorted_list = []
        for i in range(mn, mx+1):
            if i in freqs:
                sorted_list += [i]

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
    length = int(10**5)
    magnitude = 10**9
    nums = [random.randint(int(-1*magnitude),int(magnitude)) for _ in range(length)]
    print("nums=",nums)
    print("Ans=", sol.longestConsecutive(nums=nums))
