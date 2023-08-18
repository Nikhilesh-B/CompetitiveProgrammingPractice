class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        saved_sols = [[n-j if i == m else m-i if j == n else None for i in range(m+1)] for j in range(n+1)]

        for j in range(n-1,-1,-1):
            for i in range(m-1, -1, -1):
                real_j, real_i = n-1-j, m-1-i
                if word1[real_i] == word2[real_j]:
                    saved_sols[j][i] = saved_sols[j+1][i+1]

                else:
                    saved_sols[j][i] = 1+min(saved_sols[j+1][i+1],
                                                       saved_sols[j][i+1],
                                                       saved_sols[j+1][i])

        return saved_sols[0][0]



if __name__ ==  "__main__":
    sol = Solution()
    word1 = "horse"
    word2 = "ros"
    print(sol.minDistance(word1=word1, word2=word2))