from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, 1, [], result)
        return result

    def backtrack(self, n: int, k: int, start: int, current: List[int], result: List[List[int]]) -> None:
        # Base case: if we've collected k elements, add the current combination to result
        if len(current) == k:
            result.append(current[:])
            return

        # Try each number from start to n
        for i in range(start, n + 1):
            # Add the current number to the combination
            current.append(i)
            # Continue with the next number
            self.backtrack(n, k, i + 1, current, result)
            # Backtrack by removing the last number
            current.pop()


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(20, 10))
    pass
