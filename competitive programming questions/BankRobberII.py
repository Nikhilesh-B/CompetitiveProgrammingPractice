class Solution:
    def rob(self, nums: list[int]) -> int:
        self.nums= nums
        saved_sols_with0, saved_sols_without0 = {}, {}
        mx_loot = 0 
        for i, num in enumerate(nums):
            previous_sols = filter(lambda x:x>=0 ,[i-j for j in range(2,4)])
            if i == 0:
                saved_sols_with0[i] = num
                if num > mx_loot:
                    mx_loot = num
            
            elif i == len(nums)-1:
                saved_sols_without0[i] = num
                if num > mx_loot:
                    mx_loot = num

                for sol in previous_sols:
                    if sol in saved_sols_without0:
                        new_loot = saved_sols_without0[sol]+num
                        if saved_sols_without0[i] < new_loot:
                            saved_sols_without0[i] = new_loot
                        if new_loot>mx_loot:
                            mx_loot = new_loot
            else:
                saved_sols_without0[i] = num
                if num > mx_loot:
                    mx_loot = num
                for sol in previous_sols:
                    if sol in saved_sols_with0:
                        new_loot = saved_sols_with0[sol]+num
                        if i not in saved_sols_with0:
                            saved_sols_with0[i] = new_loot
                        elif saved_sols_with0[i] < new_loot:
                            saved_sols_with0[i] = new_loot

                        if new_loot>mx_loot:
                            mx_loot = new_loot
                    
                    if sol in saved_sols_without0:
                        new_loot = saved_sols_without0[sol]+num
                        if saved_sols_without0[i] < new_loot:
                            saved_sols_without0[i] = new_loot
                        if new_loot>mx_loot:
                            mx_loot = new_loot

        return mx_loot
    

import random
if __name__ == "__main__":
    s = Solution()
    ans = s.rob(nums=[random.randint(0,1000) for _ in range(100)])
    print(s.nums)
    print("Answer=", ans)


