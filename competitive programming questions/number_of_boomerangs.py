from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        saved_distances = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if (i, j) in saved_distances or (j, i) in saved_distances:
                    continue
                distance = self.calculate_distance(points[i], points[j])
                saved_distances[(i, j)] = distance
                saved_distances[(j, i)] = distance

        # build a dictionary of each reference point and the number of points that have a particular distance from t

        points_distance_dict = {}

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = saved_distances[(i, j)]
                if i in points_distance_dict:
                    if distance in points_distance_dict[i]:
                        points_distance_dict[i][distance] += 1
                    else:
                        points_distance_dict[i][distance] = 1
                else:
                    points_distance_dict[i] = {distance: 1}

        result = 0
        for i in points_distance_dict:
            for distance in points_distance_dict[i]:
                count = points_distance_dict[i][distance]
                result += count * (count - 1)

        return result

    def calculate_distance(self, point1: List[int], point2: List[int]) -> int:
        return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
    print(sol.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))
    print(sol.numberOfBoomerangs([[1, 1], [2, 2], [3, 3], [4, 4]]))
    print(sol.numberOfBoomerangs(
        [[1, 1], [2, 2], [3, 3], [4, 4], [-1, 5], [6, 6]]))
    print(sol.numberOfBoomerangs([[1, 1]]))
