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
            return len(s) == 0
        
        def generate_perms(n):
            q = ["("]
            perms = []
            while len(q):
                s = q.pop(0)
                if len(s) == 2*n and correct_paren(s):
                    perms.append(s)
                else:   
                    open_brackets = int(len([char for char in s if char=="("])<n)
                    closed_brackets = int(len([char for char in s if char==")"])<n)
                    additions = ["("]*(open_brackets)+[")"]*(closed_brackets)
                    for addition in additions:
                        q.append(s+addition)

            return perms

        perms =  generate_perms(n)
        return perms

if __name__ == "__main__":
    s = Solution()
    n = 8
    ans = s.generateParenthesis(n=n)
    print("Answer=",ans)