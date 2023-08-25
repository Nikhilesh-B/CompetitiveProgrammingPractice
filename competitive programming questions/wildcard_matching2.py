class Solution:
        def print_matrix(self, matrix):
            for row in matrix:
                for val in row:
                    print(f"{val:5}", end="")
                print()



        def isMatch(self, s, p):
                while "**" in p:
                    idx = p.index("**")
                    p = p[:idx+1]+p[idx+2:]

                if p == "" and s == "" or p=="" and s=="*":
                    return True 

                n, m = len(s), len(p)
                saved_sols = [[0 for i in range(n+1)] for j in range(m+1)]
                saved_sols[-1][-1] = 1


                for i in range(n-1,-1,-1):
                     if(p[i-1] == '*' ): saved_sols[0][i] = saved_sols[0][i-1]
                
                for i in range(n-1,-1,-1):
                    for j in range(m-1,-1,-1):
                        real_j, real_i = m-1-j, n-1-i
                        if p[real_j] == s[real_i] or p[real_j] == "*":
                            saved_sols[j][i] = saved_sols[j+1][i+1]
                    
                        elif p[real_j] == "*":
                             saved_sols[j][i] = saved_sols[j-1][i] or saved_sols[j][i-1]
                        
                self.print_matrix(saved_sols)
                return bool(saved_sols[0][0])             

                        
        
if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    p = "*"
    print(sol.isMatch(s=s,p=p))