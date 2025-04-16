from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)

        # For each point as the center
        for i in range(n):
            # Use a dictionary to count points at each distance
            distance_counts = defaultdict(int)

            # Calculate distances to all other points
            for j in range(n):
                if i != j:
                    distance = self.calculate_distance(points[i], points[j])
                    distance_counts[distance] += 1

            # For each distance, if we have k points at that distance,
            # we can form k * (k-1) boomerangs
            for count in distance_counts.values():
                if count >= 2:
                    result += count * (count - 1)

        return result

    def calculate_distance(self, point1: List[int], point2: List[int]) -> int:
        dx = point1[0] - point2[0]
        dy = point1[1] - point2[1]
        return dx * dx + dy * dy


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
    print(sol.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))
    print(sol.numberOfBoomerangs([[1, 1], [2, 2], [3, 3], [4, 4]]))
    print(sol.numberOfBoomerangs(
        [[1, 1], [2, 2], [3, 3], [4, 4], [-1, 5], [6, 6]]))
    print(sol.numberOfBoomerangs([[1, 1]]))
