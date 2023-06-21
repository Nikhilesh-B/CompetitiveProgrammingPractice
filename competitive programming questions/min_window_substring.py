class incorrect_solution(object):
    def create_leter_dict(self, str):
        rdic = {}
        for letter in str:
            if letter in rdic:
                rdic[letter] += 1
            else:
                rdic[letter] = 0 

        return rdic 
    
    def deletion_ok(self, bdic, sdic, letter):
        if letter not in sdic:
            return True
        elif bdic[letter] <= sdic[letter]:
            return False 
        else:
            return True
        
    def not_matching(self, bdic, sdic):
        for k in sdic:
            if k not in bdic:
                return False
            elif bdic[k] < sdic[k]:
                return False
        return True

    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        bdic, sdic = self.create_leter_dict(s), self.create_leter_dict(t)

        if not self.not_matching(bdic, sdic):
            return ""

        i, j = 0, len(s)-1

        reduce_size = self.deletion_ok(bdic, sdic, s[j]) or self.deletion_ok(bdic, sdic, s[i])
        while reduce_size:
            if self.deletion_ok(bdic, sdic, s[i]) and self.deletion_ok(bdic, sdic, s[j]):
                if s[i] not in sdic:
                    bdic[s[i]] -= 1
                    i += 1
                
                else:
                    bdic[s[j]] -= 1
                    j -= 1
            
            elif self.deletion_ok(bdic, sdic, s[j]):
                bdic[s[j]] -= 1
                j -= 1

            elif self.deletion_ok(bdic, sdic, s[i]):
                bdic[s[i]] -= 1
                i += 1
            
            reduce_size = self.deletion_ok(bdic, sdic, s[j]) or self.deletion_ok(bdic, sdic, s[i])

        return s[i:j+1]



class Solution(object):
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        saved_sols = set()
        for let1 in t:
            if not saved_sols:
                for j, let2 in enumerate(s):
                    if let1 == let2:
                        saved_sols.add((j,j+1))

            else:
                new_sols = set()
                for sol in saved_sols:
                    sidx, eidx = sol[0], sol[1]
                    for j in range(sidx+1, eidx):
                        if s[j] == let1:
                            new_sols.add(sol)
                            break
                    
                    for start in range(sidx, -1, -1):
                        if s[start] == let1:
                            new_sols.add((start, eidx))

                    for end in range(eidx, len(t)):
                        if s[end] == let1:
                            new_sols.add((sidx, end+1))
                
                saved_sols = new_sols

        min_len = len(s)
        solution = s

        for sol in saved_sols:
            length = sol[1]-sol[0]
            if length<min_len:
                solution = s[sol[0]:sol[1]]
                min_len = length
        
        return solution





s = Solution()
import random

string = ''
for _ in range(int(1e5)):
    let = random.sample(list("fdhafdABC"),k=1)[0]
    string += let

a = s.min_window(string, "ABC")

print(a)
        