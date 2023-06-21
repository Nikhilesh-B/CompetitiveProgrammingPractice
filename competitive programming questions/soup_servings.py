from pprint import pprint
class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        saved_sol =   {(n,n):1}
        q = [(n,n)]
        answer = 0 

        while len(q):
            state = q.pop(0)
            for op_a, op_b in [(-100,0),(-75,-25),(-50,-50),(-25,-75)]:
                new_state = (state[0]+op_a,state[1]+op_b)
                
                if new_state in saved_sol:
                    saved_sol[new_state] += 1/4*saved_sol[state]
                    

                else:
                    saved_sol[new_state] = 1/4*saved_sol[state]
                    if new_state[0]>0 and new_state[1]>0:
                        q.append(new_state)
                
        
        for sol in saved_sol:
            if sol[0] <= 0 and sol[1]>0:
                answer += saved_sol[sol]
            
            elif sol[0] <= 0 and sol[1]<=0:
                answer += 1/2*saved_sol[sol]

        pprint(saved_sol)
        print("Answer = ",answer)
        return answer
                    
if __name__ == "__main__":
    s = Solution()
    answer = s.soupServings(500)
    print(answer)