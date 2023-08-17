class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        answer = [-1 for _ in range(length)]
        for j in range(length-1,-1,-1):
            flag = False
            if j == length-1:
                answer[j] = 0
            else:
                i = j+1
                while temperatures[j]>=temperatures[i]:
                    if answer[i] == 0:
                        answer[j] = 0 
                        flag = True
                        break
                    else:
                        i+=answer[i]
                if not flag:
                    answer[j] = i-j

        return answer

import random

if __name__ == "__main__":
    s = Solution()
    temps = [random.randint(30,100) for _ in range(int(20))]
    answer = s.dailyTemperatures(temperatures=temps)
    print(temps)
    print(answer)