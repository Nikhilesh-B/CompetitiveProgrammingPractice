
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        saved_sols = {num:0 for num in sorted_nums}
        ans = 1
        for num in nums:
            idx_of_num = sorted_nums.index(num)
            if idx_of_num!=0:
                saved_sols[num] = max(saved_sols[num],saved_sols[sorted_nums[idx_of_num-1]]+1)
            else:
                saved_sols[num] = 1

            for j in range(idx_of_num,len(sorted_nums)):
                larger_num = sorted_nums[j]
                if saved_sols[num] > saved_sols[larger_num]:
                    saved_sols[larger_num] = saved_sols[num]
            ans = max(saved_sols[num],ans)


        return ans




import random
if __name__ == "__main__":
    sol = Solution()
    #nums =[random.randint(-1000,1000) for _ in range(2500)]
    nums = [7,7,7,7,7]
    #print(nums)
    print(sol.lengthOfLIS(nums=nums))