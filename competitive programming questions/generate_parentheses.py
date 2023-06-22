class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def correct_paren(candidate):
            s = []
            for char in candidate:
                if char == "(":
                    s.append(char)
                elif char == ")":
                    if len(s) == 0:
                        return False
                    else:
                        s.pop()
                else:
                    raise Exception("INVALID CANDIDATE")
            
            return True
        
        def generate_perms(n):
            parens = "("*n+")"*n
            q = [char for char in parens]

            perms = set()
            while len(q):
                s = q.pop(0)
                if len(s) == 2*n:
                    perms.add(s)
                
                else:
                    open_brackets = len([char for char in s if s=="("])
                    closed_brackets = len([char for char in s if s==")"])
                    additions = ["("]*(n-open_brackets)+[")"]*(n-closed_brackets)

                    for addition in additions:
                        q.add(s+addition)

            return perms

        perms =  generate_perms(n)
        rlist= [perm for perm in perms if correct_paren(perm)]
        return rlist





if __name__ == "__main__":
    s = Solution()
    n = 3
    ans = s.generateParenthesis(n=n)
    print("Answer=",ans)