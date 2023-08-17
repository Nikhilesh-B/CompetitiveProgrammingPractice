from collections import Counter
import pprint
class Solution:
    def findSum(self, nums):
        total = 0
        for n in nums:
            total += n 
        return total

    def convert_to_tuple(self, freqs):
        a = []
        for f in freqs.keys():
            for _ in range(freqs[f]):
                a.append(f)
        a.sort()
        return tuple(a)
    
    def findNeighs(self, candidate, freqs):
        candidate = Counter(candidate)
        neighs = []
        for f in freqs:
            if f not in candidate or (f in candidate and candidate[f]<freqs[f]):
                neighs.append(f)
        return neighs
    
    def good2go(self, freqs, counts):
        for key in freqs:
            if freqs[key] < counts[key]:
                return False
        return True


    def canPartition(self, nums: list[int]) -> bool:
        nums.sort()
        total_sum = self.findSum(nums)
        desired_sum = total_sum/2
        freqs = Counter(nums)
        nums = set(nums)
        explored = set()
        q = [[n] for n in nums]
        saved_sums = dict()
        while q:
            cand = q.pop(0)
            print("XXXX")
            print(q)
            print("XXXX")
            tup = tuple(cand)
            stup = sum(tup)
            if stup not in saved_sums:
                saved_sums[stup] = [tup]
            else:
                saved_sums[stup].append(tup)
            if stup == desired_sum: return True
            if desired_sum-stup in saved_sums: 
                for ntup in saved_sums[desired_sum-stup]:
                    new_counter = Counter(cand+list(ntup))
                    if self.good2go(freqs=freqs,counts=new_counter): 
                        return True
            if stup < desired_sum: 
                neigs = self.findNeighs(cand, freqs)
                for n in neigs:
                    new_cand = sorted(cand+[n])
                    new_tup = tuple(new_cand)
                    if new_tup not in explored:
                        q.append(new_cand)
                        explored.add(new_tup)
            
        return False

    def canPartition2(self, nums: list[int]) -> bool:
        nums.sort()
        total_sum = self.findSum(nums)
        desired_sum = total_sum/2
        freqs = Counter(nums)
        nums = list(set(nums)) 
        sums = {num:[{num:1}] for num in nums}
        q = [n for n in nums]
        max_sum = nums[-1]
        additions = set()
        while q:
            sum = q.pop(0)
            if total_sum==sum:
                return False
            if desired_sum in sums:
                return True
            for i, dic in enumerate(sums[sum]):
                for num in set(nums):
                    if num not in dic:
                        new_dic = dic.copy()
                        new_dic[num] = 1
                        tup = self.convert_to_tuple(new_dic)
                        if sum+num not in sums:
                            additions.add(tup)
                            sums[sum+num] = [new_dic]
                            if sum+num not in q:
                                if sum+num>max_sum:
                                    max_sum = sum+num
                                q.append(sum+num)
                        elif tup not in additions:
                                additions.add(tup)
                                sums[sum+num].append(new_dic)
                                if sum+num not in q:
                                    if sum+num>max_sum:
                                        max_sum = sum+num
                                    q.append(sum+num)
                        
                        
                    elif dic[num]<freqs[num]:
                        new_dic = dic.copy()
                        new_dic[num] += 1
                        tup = self.convert_to_tuple(new_dic)

                        if sum+num not in sums:
                            additions.add(tup)
                            sums[sum+num] = [new_dic]
                            if sum+num not in q:
                                if sum+num>max_sum:
                                    max_sum = sum+num
                                q.append(sum+num)
                        elif tup not in additions:
                            additions.add(tup)
                            sums[sum+num].append(new_dic)
                            if sum+num not in q:
                                if sum+num>max_sum:
                                    max_sum = sum+num
                                q.append(sum+num)

        return desired_sum in sums
    


    def canPartition3(self, nums):
        
        freqs = Counter(nums)
        
        q = [[]]




        pass

import random

if __name__ == "__main__":
    sol = Solution()
    nums = [random.randint(1,100) for _ in range(15)]
    print("the length is", len(nums), nums)
    ans = sol.canPartition(nums=nums)
    print("Here the answer is", ans)
    print("Nums is ", nums)
    #[1,5,5,11] #the properyy of how the numbers rise in value over time helps tremendously 
    # 1+5+14+2 = 2+10+10 