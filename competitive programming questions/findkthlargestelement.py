from collections import Counter

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        mn, mx = min(nums), max(nums)
        freqs = Counter(nums)

        running_cnt = 0 

        query = mn-1
        while running_cnt<k:
            query += 1
            if query in freqs: 
                running_cnt += freqs[query]
        
        return query

















import random
if __name__ == "__main__":
    s = Solution()
    length = 10
    k = 2
    nums = [random.randint(int(-1*10e4),int(10e4)) for _ in range(length)]  
    print("Numbers analyzing=", nums)
    ans = s.findKthLargest(nums=nums,k=k)
    print(str(k)+"nd/th smallest element= "+str(ans))





