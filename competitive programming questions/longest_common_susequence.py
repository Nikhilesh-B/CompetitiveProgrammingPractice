import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        saved_sols = [[0 if (i==len(text1) or j== len(text2)) else -1*np.inf for i in range(len(text1)+1)] 
                  for j in range(len(text2)+1)]
        print(saved_sols)
        
        for j in range(len(text2)-1,-1,-1):
            for i in range(len(text1)-1,-1,-1):
                real_j, real_i = len(text2)-1-j,len(text1)-1-i
                if text1[real_i] == text2[real_j]:
                    saved_sols[j][i] = saved_sols[j+1][i+1]+1 
                else:
                    saved_sols[j][i] = max(saved_sols[j+1][i],saved_sols[j][i+1])

        return saved_sols[0][0]


if __name__ == "__main__":
    sol = Solution()
    text1, text2 = "abcde", "ace"
    print(sol.longestCommonSubsequence(text1=text1,text2=text2))
    


