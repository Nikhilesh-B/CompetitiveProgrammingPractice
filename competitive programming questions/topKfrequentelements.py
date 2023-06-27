from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        counts_elements = [(counts[element],element) for element in counts]


        counts_elements.sort(reverse=True, key= lambda x: x[0])
        k_highest_totals = counts_elements[0:k]

        elements = [count_element[1] for count_element in k_highest_totals]
        return elements


from random import randint
if __name__ == "__main__":
    s = Solution()
    #nums = [randint(-100,100) for _ in range(200)]
    nums = [1,2]
    k = 2
    ans = s.topKFrequent(nums=nums,k=k)
    print(nums)
    print(ans)