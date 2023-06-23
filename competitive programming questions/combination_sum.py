class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target < min(candidates):
            return []
        sum_set = {tuple(candidate) for candidate in candidates}
        saved_sums_backward = {candidate:[[candidate]] for candidate in candidates}

        for num in candidates:
            for sum in saved_sums_backward:
                new_sum = num+sum
                if sum ==  target:
                    return saved_sums_backward[target]
                if sum>target:
                    return []
                for pattern in saved_sums_backward[sum]:
                    new_pattern = pattern.append(num).sort()
                    if new_sum in saved_sums_backward and new_pattern not in sum_set:
                        saved_sums_backward.append(new_pattern)
                        sum_set.add(new_pattern)
                    else:
                        saved_sums_backward[num] = [pattern.append(num).sort()]
                        sum_set.add(new_pattern)


if __name__ == "__main__":
    s = Solution()



