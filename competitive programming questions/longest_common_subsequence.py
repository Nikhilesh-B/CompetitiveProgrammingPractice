import time
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = time.time()
        if len(text1)>len(text2):
            ref_str = text1
            iter_str = text2
        else:
            ref_str = text2
            iter_str = text1
        s = {}
        for idx, char in enumerate(ref_str):
            if char not in s:
                s[char] = [idx]
            else:
                s[char].append(idx)

        saved_sub_seq = []
        explored = set()
        max_length = 0
        print("first time")
        print(time.time()-t1)
        for m, char in enumerate(iter_str):
            print(str(m)+"th/nd iteration =", str(time.time()-t1))
            if char not in s:
                continue
            else:
                new_seq = []
                for ss, last_idx in saved_sub_seq:
                    if ss+char not in explored:
                        current_idxs = s[char]
                        for curr_idx in current_idxs:
                            if curr_idx > last_idx:
                                new_seq.append((ss+char, curr_idx))
                                explored.add(ss+char)
                                if len(ss)+1 > max_length:
                                    max_length = len(ss)+1
                                break
                saved_sub_seq += new_seq

                if char not in explored:
                    saved_sub_seq.append((char, s[char][0]))
                    explored.add(char)
        return max_length
    




import random
import string

def strigify(lst):
    s = ""
    for char in lst:
        s+=char
    return s

if __name__ == "__main__":
    sol = Solution()
    #a, b = "acbdabcdee", "abcdab"
    letters = list(string.ascii_lowercase)
    print(letters)
    lena, lenb = 60, 60
    a, b = strigify([random.choice(letters) for _ in range(lena)]), strigify([random.choice(letters) for _ in range(lenb)])
    # a, b = "rqshbyhqljxnktikkwvl", "oqttcfsdswkiptvctzdk"
    print('a= "'+a+'"')
    print('b= "'+b+'"')

    #a, b = "abc", "def"
    lcs = sol.longestCommonSubsequence(text1=a, text2=b)
    print("LCS=",lcs)