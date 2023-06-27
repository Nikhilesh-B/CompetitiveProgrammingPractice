from collections import Counter 

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        length = len(nums)
        majority_number = int(length//2)
        counts = Counter(nums)
        for key in counts:
            if counts[key]>majority_number:
                return key 



if __name__ == "__main__":
    s = Solution()
    nums = [3]
    maj_element = s.majorityElement(nums=nums)
    print("The majority element =", maj_element)
