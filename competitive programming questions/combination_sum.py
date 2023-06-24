class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target < min(candidates):
            return []
        sum_set = {tuple(candidate) for candidate in candidates}
        saved_sums_backward = {candidate:[[candidate]] for candidate in candidates}
        new_sums = {candidate:[[candidate]] for candidate in candidates}

        for num in range(min(candidates), target):
            for sum in saved_sums_backward:
                for 
        
        

if __name__ == "__main__":
    s = Solution()



