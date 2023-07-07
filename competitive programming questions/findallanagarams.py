class Solution:
    def dics_equal(self, dic1: dict, dic2: dict):
        keys = set(dic1.keys()).union(set(dic2.keys()))
        for key in keys:
            if key not in dic2 or key not in dic1:
                return False
            elif dic1[key] != dic2[key]:
                return False
        return True

    def create_freq_count(self, word):
        d = dict()
        for w in word:
            if w in d: 
                d[w] += 1
            else:
                d[w] = 1
        return d 

    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []

        if len(s) < len(p):
            return ans

        p_len = len(p)
        p_count = self.create_freq_count(p)
        s_count = None

        for i in range(0,len(s)-p_len):
            removed_letter = s[i]
            if not s_count:
                s_count = self.create_freq_count(s[i:i+p_len])
                if self.dics_equal(p_count, s_count):
                    ans.append(i)
            else:
                added_letter = s[i+p_len-1]
                if added_letter in s_count:
                    s_count[added_letter] += 1
                else:
                    s_count[added_letter] = 1

                if self.dics_equal(p_count, s_count):
                    ans.append(i)
            s_count[removed_letter] -= 1
            if s_count[removed_letter] == 0:
                s_count.pop(removed_letter)

        return ans

import random
import string
if __name__ == "__main__":
    sol = Solution()
    lets = list(string.ascii_lowercase)
    print(lets)
    length1, length2 = 10000,1000#random.randint(0,int(3*10**4)), random.randint(0, int(3*10^4))
    print(length1, length2)
    s, p = "".join([random.choice(lets) for _ in range(length1)]), "".join([random.choice(lets) for _ in range(length2)]) 
    print(s)
    print("XXXXXXXXXXXXXXX")
    print(p)
    ans = sol.findAnagrams(s=s, p=p)
    print(ans)
