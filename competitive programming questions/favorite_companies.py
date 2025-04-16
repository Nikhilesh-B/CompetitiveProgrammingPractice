from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        indepdent = []
        favCompanies = [(lst, idx) for idx, lst in enumerate(favoriteCompanies)]
        favCompanies.sort(key=lambda x: len(x[0]), reverse=True)

        print(favCompanies)

        running_sets = []

        for j, (lst, idx) in enumerate(favCompanies):
            if j == 0:
                indepdent.append(idx)
                running_sets.append(set(lst))
                continue

            is_independent = True
            for sett in running_sets:
                if set(lst).issubset(sett):
                    is_independent = False
                    break

            if is_independent:
                indepdent.append(idx)
                running_sets.append(set(lst))

        return sorted(indepdent)


if __name__ == "__main__":
    favoriteCompanies = [["leetcode", "google", "facebook"], [
        "google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]
    print(Solution().peopleIndexes(favoriteCompanies))
