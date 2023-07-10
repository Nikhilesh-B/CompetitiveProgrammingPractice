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


    def canPartition(self, nums: list[int]) -> bool:
        nums.sort()
        total_sum = self.findSum(nums)
        desired_sum = total_sum/2
        freqs = Counter(nums)
        nums = set(nums)
        explored = set()
        q = [[n] for n in nums]
        while q:
            print(q)
            cand = q.pop(0)
            tup = tuple(cand)
            if sum(tup) == desired_sum: return True
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

if __name__ == "__main__":
    sol = Solution()
    ans = sol.canPartition(nums=[i for i in range(1,15)])
    print("Here the answer is", ans)

    #[1,5,5,11] #the properyy of how the numbers rise in value over time helps tremendously 
    # 1+5+14+2 = 2+10+10 