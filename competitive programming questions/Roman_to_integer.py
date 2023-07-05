class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"M":1000}
        small_to_large =["I","V","X","L","C","M"]

        integer = 0
        for i, numeral in enumerate(s):
            if i<len(s)-1:
                next_numeral = s[i+1]
                curr_idx = small_to_large.index(numeral)
                next_idx = small_to_large.index(next_numeral)
                if curr_idx<next_idx:
                    integer -= values[numeral]
                    
                else:
                    integer += values[numeral]
            else:
                integer += values[numeral]

        return integer



