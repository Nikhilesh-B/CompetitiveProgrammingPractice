from typing import List, Set, Tuple


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.recursiveCombine(n, k, [])

    def recursiveCombine(self, n: int, k: int, existing: Set[Tuple[int]]) -> List[List[int]]:
        if k == 0:
            return existing
        else:
            new_existing = []
            if not existing:
                new_existing = [[i] for i in range(1, n+1)]
                return self.recursiveCombine(n, k-1, new_existing)
            else:
                for ex in existing:
                    last_val = ex[-1]
                    for j in range(last_val+1, n+1):
                        new_potential = ex + [j]
                        new_existing.append(new_potential)
                return self.recursiveCombine(n, k-1, new_existing)


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(10, 5))
    pass
