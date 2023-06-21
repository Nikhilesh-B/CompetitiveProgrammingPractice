import random
from pprint import pprint

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0],x[1]),reverse=True)
        envelopes_larger_than = {tuple(envelopes[0]):0}
        max_envelopes_larger_than = 0
        for i, (hx, wx) in enumerate(envelopes):
            if i == 0:
                continue
            else:
                for j, (hy, wy) in enumerate(envelopes[0:i]):
                    if hy > hx and wy > wx:
                        new_envelopes_fit_in = envelopes_larger_than[(hy, wy)]+1
                        if (hx, wx) not in envelopes_larger_than:
                            envelopes_larger_than[(hx, wx)] = new_envelopes_fit_in
                            if new_envelopes_fit_in > max_envelopes_larger_than:
                                max_envelopes_larger_than = new_envelopes_fit_in
                        elif envelopes_larger_than[(hx, wx)] < new_envelopes_fit_in:
                            envelopes_larger_than[(hx, wx)] = new_envelopes_fit_in
                            if new_envelopes_fit_in > max_envelopes_larger_than:
                                max_envelopes_larger_than = new_envelopes_fit_in
                    
                    if j==i-1 and (hx, wx) not in envelopes_larger_than:
                        envelopes_larger_than[(hx, wx)] = 0
        
        return max_envelopes_larger_than+1



if __name__ == "__main__":
    s = Solution()
    length = 10000
    envelopes=[[random.randint(a=1, b=int(10**5)), 
                random.randint(a=1, b=int(10**5))] 
                for _ in range(length)]
    print(envelopes)
    answer = s.maxEnvelopes(envelopes=envelopes)
    print("Answer =",answer)