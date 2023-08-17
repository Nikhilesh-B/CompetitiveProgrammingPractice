nums = [100,20,20,102,201,2101,200]


largest_num = -1 
for num in nums:
    if num>largest_num:
        largest_num=num   #<-

print(largest_num)




def findIdxs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

print(findIdxs(nums, 300))




