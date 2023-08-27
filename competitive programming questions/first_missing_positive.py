class Solution():
    #if you have constant time you have to use the data that you're given to work in constant time for you 
    #find workarounds, it's often through marking or something on those lines 
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            if num<0: 
                nums[i] = 0

        for j, num in enumerate(nums):
            if num!=0:
                nums[num-1]*=-1

        for k, num in enumerate(nums):
            if k>0:
                return k+1
        


if __name__ == "__main__":
    pass


