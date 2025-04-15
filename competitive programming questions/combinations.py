from typing import List, Set, Tuple


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.recursiveCombine(n, k, [])

    def recursiveCombine(self, n: int, k: int, existing: Set[Tuple[int]]) -> List[List[int]]:
        if k == 0:
            lst = []
            for ex in existing:
                lst.append(list(ex))
            return lst
        else:
            new_existing = set()
            if not existing:
                new_existing = set(tuple([i]) for i in range(1, n+1))
                return self.recursiveCombine(n, k-1, new_existing)
            else:
                for ex in existing:
                    for j in range(1, n+1):
                        if j not in list(ex):
                            new_potential = tuple(sorted(list(ex)+[j]))
                            if new_potential not in new_existing:
                                new_existing.add(new_potential)
                return self.recursiveCombine(n, k-1, new_existing)


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(6, 3))
    pass
