class Solution:
    def findMin(self, nums: list[int]) -> int:
        print(nums)
        if nums[0]<nums[-1]:
            return nums[0]
        elif len(nums) <= 2:
            return min(nums)
        else:
            mid = len(nums)//2
            if nums[0]>nums[mid]:
                return self.findMin(nums[0:mid+1])
            else:
                return self.findMin(nums[mid:])

if __name__ == "__main__":
    sol = Solution()
    nums = [2,1]#[11,13,15,17]
    print(sol.findMin(nums))

