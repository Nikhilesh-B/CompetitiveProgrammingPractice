from collections import Counter

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        mx = max(nums)
        freqs = Counter(nums)
        running_cnt = 0 

        query = mx+1
        while running_cnt<k:
            query -= 1
            if query in freqs: 
                running_cnt += freqs[query]
        
        return query

import random
if __name__ == "__main__":
    s = Solution()
    length = int(10)
    k = 1
    #nums = [random.randint(int(-1*10e4),int(10e4)) for _ in range(length)]  
    nums = [1]
    #nums = [1,2,2,2,2,2,2,3,4,5,6,7]
    print("Numbers analyzing=", sorted(nums), "kth smallest=", str(sorted(nums)[-k]))
    ans = s.findKthLargest(nums=nums,k=k)
    print(str(k)+"nd/th largest element= "+str(ans))